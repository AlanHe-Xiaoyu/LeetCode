# Link-Shortening Service

- Maintainer: @benjamin.reese

## Overview

This is a whiteboard design problem that seeks to explore a candidate's ability to hierarchically
plan a system with an initially simple specification with the option of expanding in complexity.

## Prompt

> Let's design a website that acts as a link-shortening service.
>
> Our users will provide us a valid URL, possibly with many
> request parameters, and we will give them a short link.
>
> When anyone requests that short link, we'll redirect them to the original URL.
>
> Let's start designing such a system on the whiteboard, starting at the highest level of architecture and working our
> way down. Keep in mind that I may add system requirements as we go.

### Common pitfalls

* Using a reversible "hashing function" to generate short links - no storage
  * Conflict resolution is required
  * Some hashing functions produce long output
* Random creation
  * how do we know when to increase our URL length?
  * Birthday paradox - "does the birthday paradox have an effect here? If so, how do we mitigate it?"
  * How many times do we expect to have to regenerate as the number of links grow? What about when we have 100k links? A million? A billion?
* Sequential generation - to me this feels optimal, but there are still questions to pose
  * Generating a unique sequence when scaling becomes a non-trivial problem. How do you guarantee uniqueness across many instances of the service?
  * What about enumeration? does it matter? how would we mitigate that? (maybe a substitution cypher)

### Possible sub-questions
* > How do we scale this system?
  * This sub-question significantly increases the difficulty of the problem, and unless your candidate has experience in large
  distributed systems it may not be appropriate
  * If we shard our database, how do we ensure uniqueness? (each shard has a prefix, etc)
* > Business has requested that we de-duplicate our results. If a different user requests a short-link to an equivalent URL
that someone else already has, we return the first short link. What's your response?
  * The best engineers will pose some questions back to business
    * Why? What's the value?
    * The cost to de-duping is greater than the cost of just generating another link
    * You lose the ability to do metrics per-link creation
  * Define an equivalent URL - a URL with the request parameters reordered is equivalent. So is the same URL with a `#` at the end
  * Many candidates will go down the rabbit-hole of breaking the URL into parts
    * permute the params to find all possible equivalent links
      * What if there are 10 parameters? How many possibilities is that? (10!)
    * storing the component parts for later look-up
      * I let them attempt for a while, because it shows db/sql skills. So far, no one has gotten close
  * Clever candidates will think to sort the request parameters - O(n log n) sort is much better than these other options
* > We're moving to an ad-supported model, the `adf.ly` model if you're familiar with that
  * When the user makes a request with a short-link, we first show them an ad and then redirect them
  * We'd like to share some of the ad revenue with the link creator
  * This problem adds many system components and considerations
    * user creation and authentication
    * associating a link with a user
    * client vs server redirection
      * if they use client-side redirection, I pose this sub-problem: "A malicious user creates a browser add-on that reads
      your JS and redirects the user immediately. How do you mitigate this?"
    * ad-blocking mitigation
    * integrating with a third-party - the ad-service
* What about site administration?

### Possible learnings
* It could reveal certain expertise
  * Some candidates intuitively plan for scaling the system
  * Some candidates intuitively solve the typical "gotchas"
  * Some candidates have a better "big-picture" perspective - They'll ask probing questions ahead of time
    * "how long should the link be valid?"
    * "what if someone requests a short-link for a url we already have generated for?" - before asking the de-dupe section
    * "Should I segment by region, etc"
    * "Should I provide a preview page before redirection?"
  * Some candidates are more security-conscious, pointing out potential security flaws
    * "Sequential link generation is enumerable"
    * "Client-side redirection could be exploited"
    * "We should security-scan the link or otherwise compare it against a blacklist of domains"
* It could reveal holes in knowledge
  * modern web and client-server architecture
  * HTTP protocol
  * database design, usage, and caveats
  * scaling strategies
  * how hashing works
