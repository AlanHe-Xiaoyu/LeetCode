# Memcache Implementation
- Maintainer: @mason.jones

## Overview
This interview question asks the candidate to implement basic Memcache server functionality. The core of the question focuses on the internal functionality, not the server part, since asking someone to write code to receive and parse commands in a TCP request isn't particularly interesting. However, you could have them build simple API endpoints if you wanted to proceed into some sort of user interface question.

If you are curious to dig deeper into the actual Memcache protocol specification, you can find it here: [https://github.com/memcached/memcached/blob/master/doc/protocol.txt](https://github.com/memcached/memcached/blob/master/doc/protocol.txt)

## Prompts
These are the prompts to share with the candidate to describe the stages of the question. Start with Part 1, then move on to the following parts if there's still time remaining. For each part, there's the initial text that you can copy/paste to share, followed by details to help you answer some of the questions the candidate is likely to ask.

If you're interviewing a particularly senior candidate, you could quickly sketch out the first two parts together and quickly move on to Part 3, which is the more complicated and advanced part of the question.

----

### PART 1

The goal of this exercise is to code the internals of a simple Memcache server (without the server part). As background, Memcache stores key-value pairs in memory, and supports commands to SET and GET the keys. So, let's start with those:

`SET <key> <value>` to set the key to the given value, and returns a code indicating success or failure.

`GET <key>` to retrieve the value that was stored for the key, and returns the value or a null if the key wasn't found.

Implement functions that a server component could call if it received either of those commands. Keep in mind that this code will be running within a server being called by things like web applications and back-end systems.

#### Expected questions from the candidate

* Types: both the key and value parameters are strings. Assume they'll be parsed by the server and passed in as normal strings.
* Existing key: if SET is called for a key that already exists, it should update the key with the new value.
* Scale: the functions and data structures should be chosen to provide good scaling, so the system could be run on a server with a lot of memory and it will still set/get with good performance.
* Limits: if the system runs out of memory, it should not crash. GET operations should continue to work but SET would return an error.
* Errors: besides the return values described above, it would be nice to return an error code and message if something goes wrong.

#### What do we want to see/hear?

* Questions about expecting scalability and performance.
* Questions and/or thinking out loud about valid values (example: max length of a key or value?).
* Questions and/or thinking out loud about error/exception handling (example: what if the value passed in is null?) including how to return detailed error information in addition to the basic return values.
* Tests (of course) to prove that the functions are doing what's expected.
* The most important question is about the data structure used to hold the keys/values. Usually people will opt for a hash/map in whatever language they choose. They should talk out loud about the performance characteristics, but this is a fine option for this first part.
* The most experienced engineers might start out early thinking about the fact that this needs to be multi-threaded and concurrent. Bonus points if they talk about that and point out that SET needs to be atomic, and extra bonus points if they either put a lock around it or even just talk about doing so.

----

### PART 2

With the initial SET and GET implemented, let's enable our users to delete old keys as well, by implementing another command function:

`DELETE <key>` to remove the key and value specified, and return true (deleted) or false (key not found)

#### Expected questions from the candidate

* Probably not much to ask on this one; it's straight-forward

#### What do we want to see/hear?

* Performance of the deletion would be nice to think about, although if they used their language's hashmap then they might only be able to guess.
* Tests (of course) added to prove that deletion works. The expectation would likely be a test that does a SET, then a GET, then a DELETE, then another GET.
* As above, the more experienced engineers will mention that DELETE needs to be atomic and would need a lock or other synchronization mechanism to prevent weird behavior (to simultaneous DELETEs, for example, or DELETE/SET leaving things in a bad state).

----

### PART 3

One of the best Memcache features is key expiration, so let's implement that. The SET command should now have a parameter with the expiration time of the key, so it looks like:

`SET <key> <exptime> <value>` where exptime is an integer for the number of seconds before the key expires; a value of zero means no expiration

As an example, if you call `SET foo 10 bar` then that should set the key 'foo' to the value 'bar', and if you call `GET foo` 11 seconds later it should not find the key. If you call `SET foo 0 bar` means the key won't expire.

#### Expected questions from the candidate

* The most likely help they'll need is around whether to write a concurrent function that wakes up every second to check things. This could be a time-killer so it's fine for them to first write the code to expire keys, and if there's time write the actual timer to do it.
* One good initial approach is to first write the expiration code; and write a test that does a SET with a 1-second expiration, then a GET, then a sleep for 1 second, and then calls the expire function followed by another GET. That expire function should result in the key being deleted so the last GET won't find the key.

#### What do we want to see/hear?

* The candidate should first think about what this means for their data structure. Probably they used a hashmap with string key and string value. Now they need to add a timestamp of some sort to each key. The value will most likely now become an object with a string value and a timestamp. Hopefully they add that and re-run their tests to make sure nothing broke.
* Since they're likely using a hashmap, for the first pass they might use the brute force approach, which is to iterate all of the keys, check the expirations, and delete a key if it's expired. That's fine to verify things but is not nearly performant enough, and hopefully they talk about that. Ask them to imagine this running on a server with 16GB of RAM and millions of keys.
* Adding a secondary data structure works well for this: for example an ordered list, ordered by timestamp. They don't need to store the keys with a zero expiration time, since they don't need to be expired. If they store not the expiration in seconds, but the actual expiration time (current time + expiration), the list can hold the oldest keys first, and each time the expire function is run it can process the list in order until it reaches a key with the expiration time greater than current time, and then stop.
* In that case the deletion code needs to be updated to not just delete the key from the hashmap, but also from the list.
* Hopefully the candidate calls the delete function to do the expiration, and doesn't re-code it.

----

## Options and Additions

If you're interviewing someone for a particular, specific area of expertise, this question can be varied in a few ways.

### API Implementation

You could have the candidate do the first two parts and then build a server component with API endpoints for SET, GET, and DELETE.

### Statistics (easy, could use instead of expiration)

Have the candidate implement the STATS command, which should return a set of statistics:

* curr_items: number of keys being stored
* total_items: total number of keys stored since the server was started
* bytes: total number of bytes being stored (size of values in bytes)
* get_hits: number of GET requests that returned values
* get_misses: number of items requested that were not found

Ideally the candidate will create a data structure to hold the stats, and a centralized function or set of functions to update it, called by the other functions. This is another area where locking and synchronization is critical so concurrency doesn't cause broken statistics.

### Eviction (high difficulty)

Have the candidate implement key eviction:

* Specify the maximum memory size in bytes (hard-coding it is fine to start)
* Track the total size, in bytes, of all values in storage (ignore size of keys)
* When a SET will cause the total size to exceed the maximum, evict some of the least-recently-used keys

This is probably a "talk through this problem" and not actual implementation because it's complicated. If there's time, though, talking about it is very useful and interesting for senior candidates.

Questions are likely to include asking about how much to evict, which is an interesting conversation. In the real world, it's good to dynamically evict more or less based on usage (high growth leads to larger/faster evictions), but that's complex. Setting a config value to something like 10% of the maximum memory size is perfectly fine to start.

Implementing this will require updating the data structure to store the time at which each key was last touched, and modifying the existing code to update it when a key is fetched via GET or updated via SET. In addition, another data structure will be needed to store the keys ordered by the keys' last-touched timestamp, likely another list.

Invoking the eviction when a SET is called (as described above) works, but it's a bonus if the candidate suggests having a concurrent process running that performs eviction in the background when the memory usage exceeds a threshold (e.g. 95% of maximum).

