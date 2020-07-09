# Implement an MMO

![Fortnite](/images/fortnite.jpg?raw=true "Fortnite")

## Overview

Pick a game the user is familiar with, and stretch it into a realtime MMO version. The candidate will draw and talk through the architecture. It's designed to be an unfamiliar, nearly unsolvable problem for most folks. No two candidates will have the same skills and experience here, so administering the question will require some tuning.

The interviewer's job is to let the candidate show their experience while architecting a functional system design from scratch. They should see, with help if need be, the common traps, and come up with viable workarounds.

They should talk extensively about tradeoffs, the capabilities of chosen technologies, and be able to make choices and guide the conversation toward a solution.

## The Setup

"Pretend you're a consultant and I'm the customer. I want you to architect a massively multiplayer version of _________. There are no right or wrong answers, I just want to see how we can work through an unfamiliar problem together."

### Constraints

* One World
* 100,000 simultaneous players _(it's a ludicrous amount, and would break down if everyone were to interact with each other at the same time. This is primarily what makes this hard.)_
* Real-time
* pick a game in which the players can see each other move, preferably many at once. If they aren't familiar with anything, choose Fortnite, as they're likely to have at least heard about it.

### Focus

* Only on gameplay
* Communications _(how do clients talk to the server, and potentially each other? What is the pattern, frequency, and content of the messages?)_
* How do we handle latency?
* **What is the role of the server?**
* Where does information live? _(**What is the source of truth?**)_
* What kind of storage will we use?
* What technologies will we use on the Server?

### Skip

* Don’t worry about Authentication, Registration, Login, etc.
* Don't focus on datacenters - imagine all players are in the Bay Area
* Don't worry about the 3D rendering; imagine we're using Unity and just focus on the information flowing.
* Don't worry about Voice Chat (this sometimes comes up)

### Ready?

![The Setup](/images/interviewprompt2.png?raw=true "The Setup")

After the setup I usually draw three boxes - two clients and a serverland. I ask the candidate to talk about how they're connected, and what they say to each other.

If they get stuck on this, or propose using HTTP, I'll follow up with:

*"You and I are players in the game and we can see each other. If you jump, I need to see it in real time. How do we do this?"*

### Expectations

They should be able to talk about the various parts of a system fluently and creatively. They should be forthright and self-aware about where their knowledge ends. Even if they don't know details about a technology, being able to talk about its reputation or what it *should* do is a plus.

They should be able to follow directions, communicate back and forth well. They should be able to explain what they know well, ask questions about what they're unclear about, and push back against things they're sure are wrong or bad ideas.

They should also engage with the problem once it's set up and clear. If the entire time you have to interrogate them to pull information out, perhaps they'll have problems connecting with other unfamiliar or uncomfortable problems. (It's your job to direct the conversation to *"find a vein"* they can engage with.)

I also like to see people be able to think outside of their career *"box". If they're one of the *"JDBC crew"* who has only done that for 20 years, can they leave that experience a bit and talk about how one might build a system for which a DB is second-fiddle or an afterthought? (like maybe this one?)

## Realms

### Communications

Lots of leeway, as in all parts of this. The candidate should, at minimum, propose a long-lived connection between clients and servers. If they say *"HTTP"* and stick to it, try to show them, with questions, how that won't work. If they say *"long-polling", I'll count that but also focus more on their technology chops, since that's an older technique obviated by Websockets and the like.

I generally expect to hear *"Websocket", or something they describe as such. I don't need a ton of familiarity, just the idea. I'll talk through UDP if they're up to it.

P2P is a risky move and can derail the whole conversation. I try to steer people away from it, BUT I will let them talk about it to see if they can see how complex it will get. I generally ask questions to see if, in the answering, they see the complexity.

If their mind is made up, then P2P can stand, but the *"source of truth"* has to be explored, and the concept of elections and leaders can come into play. It can get interesting, but we're also foregoing talk of server technology, which is more relevant. Your discretion.

They should be able to describe the contents of a message, which should lead them to sending the user's location (the most salient piece of information), which should lead them to see the major problem : telling everyone else what you just did.

This leads to the question, which is more pointed in a P2P situation, *"How does X know whom to tell about what you just did?"*

Bonus points for candidates who mention Bittorrent or blockchain protocols and who can defend their thinking when applied to this problem.

### Alerting others

If the candidate doesn't see this immediately, I'll ask the question, *"If player A jumps, do we tell everyone?"* and see if they see the problem.

This is where the *"server vs P2P"* question is perhaps settled. If they are still on the P2P track, you can ask them, *"How does a client know whom to tell?"* and *"does the client open connections to all 99,999 other players?"*

(There's an advanced answer involving VPCs and broadcast or multicast but it's not expected.)

The more straightforward approach is a hub-and-spoke model where the server acts as message broker.

![Hub and Spoke](/images/hub_spoke.jpg?raw=true "Hub and Spoke")

Assuming they land on this eventually, then the server needs to keep track of where everyone is. And then the challenge is : *"you just jumped - how do we find people around you?"

The answer should be : **only tell people who care about what i just did.** (i.e., people that can see or hear me.)

#### The problem with telling everyone

The candidate should be able to see that telling everyone when anyone does anything is an O(N^2) proposition. Besides being a lot of work, the network may itself become a bottleneck.

I prefer to lead the candidate to this conclusion, and like it when they quickly see the need to divide and conquer. If they don't get there, you can ask questions like, *"So 100,000 people reporting their location every 100ms means 1m RPS incoming to the server, which each then generates 100,000 outgoing requests, so 10 **billion** RPS outgoing."*

If they don't see the need to lower the work nor to make it less chatty, dig into that. if they can't see how, you can provide a toy problem to shine a light on the most relevant question - *"how do we divide and conquer"*?

My toy problem is a simple particle simulator:

![Particles](/images/particles.png?raw=true "particles")

I was writing this and when I tried to detect collisions, it got slow with more than a few particles. Because of the naive algorithm:

```
for each particle A:
  for each particle B:
    if (does_touch(A, B)):
      bounce()
```
This is clearly quadratic and the candidate should be able to talk about that. Then they should have some ideas of how to **only check particles around the one in question**. (They should also see the analog to the problem in question.)

#### Divide and conquer strategies

* **simple grid** : divide the world into static chunks - ask them how they decide the chunk size
* **geohashing** : a geocoding system which divides up a space - probably overkill but it's interesting to hear they know about it.
* **quadtree** : this is my preferred implementation, and it's simple to talk about. (it's just like a binary tree but four leaves instead of two) This brings the search complexity to something logarithmic.

This handles the problem of _"how do i find people around me?"_ but the candidate may still act like this is happening all in one machine's memory. See if you can get them to think about breaking things up. (One million requests per second into a thing that holds the tree is a lot.)

### Splitting up State

1. a process for each region (sharding the world)

![How to Break Up State](/images/statebreak.png?raw=true "breaking up state")

Now we've solved one problem - each process / server is responsible for one region, and thus load is lightened. But now the candidate has unlocked another set of problems.

* "What happens if Player A and Player B are shooting at each other across a boundary?" (answer: the processes responsible for each region need to share events with each other, either directly, or via a queueing mechanism)
![boundaries are a problem](/images/map.png?raw=true "boundaries")
* "What happens if everyone goes to the same place?" (answer: you can dynamically shard again, like in a quadtree or voronoi diagram, **but** at some point it just doesn't work. Bonus points for coming up with ideas like Fog of War [to limit visibility] and Slowing Time [as in EVE Online])
![everyone in one place](/images/mapalloneplace.png?raw=true "all in one place")

2. Consistent Hashing - hash the users into one server/process and all of their state goes to that server. The server figures out who needs to hear that. This is chatty, complex, and slow, but may be viable if they can mitigate some of those things.

![Consistent Hashing](/images/splitting_up_state.png?raw=true "Consistent Hashing")

Once the state is split up, how is the state actually shared?

Candidate should imagine a system wherein servers that are connected to people and getting their events update the Source of Truth, and they (or another system) tells everyone that needs to know. Interposes communication is considered here. And queues are a good fit, if they candidate can reasons about that well.

### Latency

"If Player A and Player B shoot each other at the same time, but Player A has fiber and Player B has public WiFi, how does the server know what happens first?"

The candidate should mention or consider:

* **using timestamps** - clients send the time they think things happened.
* server should process things in a **window**, and **reconcile** events therein
* bonus points for talking about **synching clocks**
* bonus points for talking about **_how fast, maximum_** they need to be (rendering frame rate provides a potential boundary, usually 60, 30, or even 24 Hz)
* attempts at **cheating** by messing with timestamps
* at some point, it's **not fair** for the people with fast connections to wait for those with super slow connections

### Storage

For this question, relying on a DB as the source of truth means they might not have a real instinct for DB usage under load. It's important to dive into that and see if it's just the only way they know how to make things. (This is also OK, but they should then be able to see the problem.)

DB is appropriate for slow facts - analytics, backups, etc., but not as the source of truth. One million writes to the DB per second and one million `SELECT STATE AROUND PLAYER \<X\>` queries per second is a lot. They should realize this and rely on an in-memory store. There may be modern systems that could handle this, but the candidate had better be an expert before positing those.

If they break things up a different way, then a fast in-memory cache like Memcache or Redis may also work in parts, but the big question with Storage is "what is the source of truth?"

For processing, I favor doing things in memory to avoid the roundtrip and competition for a shared resource.

### Technologies

Things I want to hear about in the course of this interview:

* message queues
* a web or microservice framework
* a communication protocol (Thrift, gRPC, REST, etc) - they should at least be quite familiar with ONE, and depending on level, more.
* database systems (noSQL and SQL)
* caches

## End State

Here's one possible final diagram achieved over the course of an hour on this problem: (some details missing and would depend on candidate's choices)

![Possible End State](/images/possibleendstate.png?raw=true "One Possible End State")

Note:

* The complete flow of information is visible. Updates come in, are handled, and the relevant info is sent out to the users. This should NOT be "send everything to everyone" but "everyone gets exactly what they need and not much more."
* If Message Queues are used, try to get an idea of how : what kinds of topics, how does the information flow? Will there be 100k topics? or one per region?
* a system like this will need a system to leave and join regions, subscribe to region-specific topics, etc. This needs to be elucidated if time permits.
* In this design, the region-servers need to hear updates from adjacent regions, and this is accomplished using the message queue. Then the region-servers collect the recent deltas and tell everyone they're responsible for, using a QuadTree or the same to limit bandwidth out.
* Bonus for sending updates on a cadence to everyone, instead of reacting to every event.

### Scoring Rubric:

* **Unfamiliar** - Requirements: Communication, Server, Questions
* **Familiar** - Requirements: Communication, Server, Questions, State
* **Proficient** - Requirements: Communication, Server, Questions, State, Database, Planning, Storage
* **Master** - Requirements: Communication, Server, Questions, State, Database, Planning, Hubris, Storage, Practical

| Level          | Comm | Server | Scale | Location | State | DB | Queue | Latency | Order | Qs | planning | hubris | practical | storage |
|----------------|------|--------|-------|----------|-------|----|-------|---------|-------|----|----------|--------|-----------|---------|
| Unfamiliar     | ✅    | ✅      |       |          |       |    |       |         |       | ✅  |          |        |           |         |
| Familiar       | ✅    | ✅      |       |          | ✅     |    |       |         |       | ✅  |          |        |           |         |
| Proficient     | ✅    | ✅      |       |          | ✅     | ✅  |       |         |       | ✅  | ✅        |        |           | ✅       |
| Master         | ✅    | ✅      | +1    | +1       | ✅     | ✅  | +1    | +1      | +1    | ✅  | ✅        | ✅      | ✅         | ✅       |
