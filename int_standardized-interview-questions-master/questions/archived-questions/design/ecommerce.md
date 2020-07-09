# Design an Ecommerce platform

- Maintainer: @douglas.jones

## Overview

Design the systems needed for an ecommerce platform. The intention is to have a conversation to get an understanding of the candidate's architectural knowledge. Different opinions are not bad. Well thought out reasoning that reaches a different conclusion benefits us all.

The questions below are questions I've asked previously given this prompt. I have never asked ALL of these questions of a single candidate. You will not get through all of these questions. The intent is to have a discussion around designing systems (AKA architecture). Please feel free to add questions and let me know your thoughts around this exercise.

## Prompt
We have decided to build a business to compete with Amazon since they only have 49% of the ecommerce market (51% for us!). 

We want a web application built for scale where users can view products with associated descriptions, see the current inventory count of in stock items, and purchase products via checkout. We'll have this MVP (Minimum Viable Product) and iterate from here.

Assume we can identify users (authentication assumed for now, but have a couple questions around it toward end) and that the user can successfully search and find a product they want. We want the user to be able to 

* add an item to their cart and click checkout on product page
* enter shipping information and payment information and click "Pay Now"

## Questions and *Possible* Answers

### 1. What systems are needed to accomplish this? What architecture did you choose and why?
We NEED 1 web server and 1 database. If we have a significant amount of code and a need for significant scale, I'd want:

* an MVVM framework on the front end
  * React or Angular, or Vue js
  * Allows app to appear like a native app, responding instantly to user interaction
* an API gateway (like graphQL)
* multiple microservices such as 
  * PaymentProcessor
  * Product Service
  * Order Service
  * Fulfillment Service
  * etc...
* A db associated with each microservice.
  * Given constraints so far it could be a NoSQL option with primary and 2 secondaries per shard, but would want sharded.
  * Could be a sharded relational db without read replicas.


### 2. What would be the benefit of doing it another way?
If they chose microservice route, then cons for microservices:

* Separate code into different repos making it harder to find
* Add significant complexity in getting changes made because changes are now needed in multiple repos
  * Needed in both microservice and client
* Failures must be accounted for
  * Retry mechanisms and fallbacks for transient network errors 

If they chose a single app, then cons for monolith:

* No clear DDD bounded context allowing concerns to blur together
* Very difficult to pull apart later because of blurred concerns
* A lot of developers in the single repo leading to a lot of time spent on merge conflicts
* Deployments slow because entire app needs to be regression tested
  * or risk a change in area x affecting area y inadvertently
  * When issue found, deployment with all changes postponed
* Doesn't scale well. Parts of app need much more cpu/memory than others yet must scale entire app.

### 3. If we hit a limit on the IO of the web server, how can we alleviate the problem? Why shouldn't we just use a bigger machine?

Candidate should speak to a way to scale out the load onto multiple machines, which could be multiple physical machines using f5 hardware load balancer, cloud virtual machines, or kubernetes pods on nodes. These are scaling out solutions. There's no machine big enough to vertically scale up.

### 4. What db did you decide on and why? How can we prevent heavy load on our dbs?
A lot to this. We want to ensure our dbs can handle the load, but we also want caching.

**DB**

If 1 db instance per db, explain that won't hold up for millions of requests.

* NoSQL
  * use the replication sets to read from
  * Traditional primary / 2 secondary approach means the writes aren't scaling and that we now have eventual consistency to contend with on the secondaries.
* Sharding - Regardless of SQL or NoSQL
  * Especially needed for SQL scaling

**Caching**

What's the fastest cache we could use? Which cache would you use?

* in memory cache is fastest
* what are the tradeoffs there?
  * Fastest, no network hops
  * Biggest pain, as no easy way to invalidate cache, not easily scalable

I'd use a distributed cache because easy to scale, easy to invalidate cache.

*  Redis or Memcache most popular, but just ensure candidate names a distributed cache.

If candidate went with NoSQL, recognize that timing would be good enough for each individual query without cache, but what if you really need to "join" data from multiple tables? (Could be in memory join after multiple nosql calls then stored to memcache).

Remember to ask cache questions in this list.

### 5. What's a good shard key to use?
Make sure it's thought out and that it won't cause obvious hotspots. Could use userid, which also allows for joining in our db, since we'd have access to that user's associated data in a relational db.

### 6. How is this data being persisted and what do the data structures look like? 
Normalized solution using only 1 db below. Only want candidate to list out what they are working with right now (Order, PaymentInfo) and allow them to hand wave away the rest.

* Product - ProductNo, Description, Price, Count
* Inventory - ProductNo, Count
* Order - UserId, AddressId, PaymentId, Product, OrderPrice, IsCompleted
* OrderLineItem - OrderId, ProductId, Count, LineItemPrice
* User - UserId, FirstName, LastName, etc...
* Address - UserId, Street1, Street2, City, State, Zip
* PaymentInfo - PaymentId, PaymentType, AccountNumber, CardCode (CVC) 
* UserCart - UserId, OrderId, IsActive

### 7. What's the risk to storing this data?
A bad actor could gain access to the db and steal all payment information for all members, as has been happening a lot in the news recently, such as Target's data breach.

### 8. How can we keep it secure? Who will be able to decrypt the data? If the answer is "the system", what if a bad actor gained control of the system? 
I won't do this justice, but looking for basic understanding here.

* Don't store what we don't have to. 
* Encrypt what we have to and keep secure. This likely means constantly rotating keys that can never be retrieved, such as with AWS KMS, forcing the encryption/decryption to go through the service. A bad actor now needs access to the service, the encrypted data from the db, an understanding of what else it was encrypted with ('iv', 'salt', 'context' - for KMS), access to that data, and needs to get it all before it's discovered by org and the credentials to KMS are changed, which should also be getting rotated.

### 9. We could use a 3rd party like Stripe for payment processing. Does that lower our risk?
Yes, if we have confidence in 3rd party. We no longer store the payment information. In order to get it the bad actor would need to gain access to our encrypted stripe identifiers in our db, decrypt, gain access to our stripe account and make proper call to get CC # for each account.

### 10. Walk me through the flow to get the payment processed. 
User clicks "Pay Now". Synchronously:

* Inventory is deducted. 
* Payment is processed.
* Successful return from API call and "Your order has been placed" displayed on page. 

### 11. What should happen to that item in inventory? What if we're out of stock? What if an error occurs, what should happen? What happens if another user tried to purchase that same item right afterwards?
Inventory item gets deducted. User gets an error after entering all of their cc info and shipping address because the item is out of stock. Any other error would cause the same problem, user sees error message. Another user clicking "Pay Now" right after last item sold would get same out of stock error.

### 12. I want the users on the product page to be updated in real time with our current inventory count. I want to reduce the item from the inventory the user sees when a user adds it to their cart. How do I accomplish this programmatically? Walk me throught the process when user1 adds item to cart how user2 sees updated inventory count.
When a user clicks 'add to cart' a call will be made to an endpoint that adds to cart and removes cached inventory count. Inventory count now needs to be considered `inventoryCount - activeCartCount` for each product. We could use websockets and maintain an open connection on the product pages to allow a server side push to update the count or have a polling mechanism from the client side to check or a combination of the 2 via socket.io/signalr style long polling. 

### 13. What could go wrong? What if the user never checks out?
After some time limit, consider the product inventory in cart inactive and don't count against inventory #. We only subtract cart inventory from product inventory while cart is active. Could add a job that runs every minute deleting carts that have been inactive or transfer to a different db to analyze.

### 14. How can we speed up the page loads, giving a better experience to the users?
Use an edge server (WAF or reverse proxy) as a cache at the edge for html, css, js.

* Bundle all common js, css - so user has cached in browser on subsequent page loads
* Make ajax calls for data that changes
* Have the ajax calls hit caching layer like memcache instead of hitting db when retrieving state.

### 15. How do we ensure we have current information in our cache? What's our cache invalidation strategy?

Determine ask and if we can allow short expiry that would be preferable to cache invalidation on change. If cache invalidation needed, then whenever the db changes, our cache must change. If using microservices and the Product Service has the cache yet the Order Service deducts the cache, the db update can be particularly problematic and where events amongst the services can come in.

### 16. Are we guaranteeing up to date info in cache?
No. If we're using replicas like Mongo uses, we're not even guaranteeing up to date on read from the db because we could hit a replica db for read that doesn't have latest write yet. Regardless there's a gap between write to db and invalidation of cache where old data lingers.

### 17. We have a backend fulfillment application that must be aware that the item needs to be shipped. How does that app become aware so that someone in the warehouse can pick the item and ship it?
We publish a message/event/notification to a queue via a service bus of some kind, ex:

* AWS SNS/SQS
* RabbitMQ
* Kafka
* Google Pub/Sub
* etc...

### 18. The Fulfillment Service could poll the web app db or via an api. Why would that be bad?
We wouldn't want the Fulfillment Service to get access to the internal db of our Order Service because this would be an unrecognized dependency and it could be changed at any time, breaking the Fulfillment Service. If it polled via API it is much more tightly coupled to the service and there's added load to network, app (both client and server), and db.

### 19. Let's say we have 'At least once' delivery. How do we ensure we process it only once?
Ensure the subscriber is idempotent. Regardless of how many times it's called, it should only change state the first time. We also need to set up a failure mechanism. This could be a "dead letter queue" so that after retrieval was attempted 3 times, it gets put in the DLQ and an alert goes out.

### 20. What if we decide we want to split off a microservice from one of our current services? What would be a way to add in the microservice without forcing all consumers to be changed at the same time?
We could use a reverse proxy as an intermediary and use the strangler pattern to re-route some calls to new services.

### 21. How are we authenticating the user?
Everyone so far has mentioned oauth, which leads to the next question

### 22. How does our authentication mechanism work?
OAuth has an auth server that authenticates user when user enters username/password, returning a token. For all subsequent requests, the token is sent on the http header to our services. Each service that gets called authenticates the token. The services at the edge must actually call the auth server to validate the token, but services not on edge may not. It's a tradeoff with services further in for greatly increased load on auth server and decreased performance vs likelihood of bad actor getting past edge service(s) and what bad actor could accomplish with those permissions. If user can wipe data from db, auth server will need to validate every time.

## Expectations

### SWE III / IV

The candidate should be able to come up with an architecture that would function with the help of leading questions. They wouldn't necessarily know all the pros/cons, but should be familiar with most of the architecture. They wouldn't necessarily come up with the best fitting architecture.

### Senior I / II

A senior candidate should have a good grasp of all of the architectural pieces and be able to explain pros/cons to the approaches discussed. They should be able to give details that enable their solutions to function (such as explaining how to update UI after order processed with new inventory count).

### Staff

A staff candidate should have deep understanding of everything discussed and provide additional insight into the discussion.

## Additional Discussion Topics
### Web Application Firewall (WAF)
We started getting Distributed Denial Of Service (DDOS) attacks from people in a 3rd world country demanding payment. What system could we add for security to prevent these attacks from happening?
* Imperva Incapsula
* Cloudflare
* Akamai
* Google Cloud Armor
* etc...

### Programming language

What language and runtime would you use and why? What's the benefit to that kind of language? Statically typed or dynamic? Declarative or imperative? Compiled or interpreted? If compiled, compiled to intermediary language (and different JIT/runtime used) or directly to assembly? Dynamically linked vs statically linked? No right answer, but ensure that there is an understanding of which type and an explanation of pros/cons.
