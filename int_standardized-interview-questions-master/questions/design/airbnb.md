# Implement AirBnB

## Overview

Design the relational database schema and high-level backend strategy for AirBnB.

## Step 1: Basic Functionality

### Requirements

* Search for listings
* Book a listing
* Don’t worry about logging in, payments, the state machine, etc

Prompt this as just “searching” and “booking” and let them derive the word “listing”. Naming concepts is a crucial skill.

Ask them if they’re familiar with AirBnB and give them an overview if they aren’t. You can open the AirBnB app or website on your phone to show them the product experience, even if they say they’re familiar with AirBnB. This is a good way to tie product to engineering design, an important skill.

### Expectations

They should draw some table schemas with table names and columns. It’s OK to omit column types. The key part is to see whether or not they correctly identify the right tables, the relationships between the tables, and the right columns for each table.

### Solution

A correct solution might look like this:

```
Users
  Name
  Email

Listing
  Host User ID
  Name
  Price
  Description

Booking
  Listing ID
  Guest User ID
  From Date
  To Date
```

Red flags include:

* Denormalizing any of these tables without a good justification.
* Omitting key foreign keys.
* Needlessly using JSON or non-structured data.

## Step 2: Reviews

### Requirements

Handle and store reviews of listings (prompt this as just “reviews” and let them figure out what that means)

Then ask them to provide aggregated (averaged, or any other aggregation mechanism) of reviews. Show them the part in the app that has stars, like `**** (4.5)`.

### Expectations

They need to make a new table for reviews. It’s up to them to decide whether or not a review is attached to a listing or a booking. However, they should motivate which one makes more sense and how that relates to the product.

They need to figure out a way to make the aggregation fast. Joining a bunch of tables is not acceptable.

### Solution

The key difference between attaching a review to a listing or booking is that attaching a review to a booking means that a user staying multiple times in the same place can review multiple times.

```
Reviews
  Listing or Booking ID
  Guest User ID
  Content
  Stars
```

As for aggregation, a solution is to add a `avg_stars` column to the listing and keep it updated. This leads us to step 3…

## Step 3: Denormalization

### Requirements

Keep the `avg_stars` column up to date.

### Expectations

They design a way to keep the `avg_stars` column up to date, since you now have a derived field that can become stale.

### Solutions

Good signs include asking about the needed scale of the system: it should scale to AirBnB scale. Another good sign is making a case for aggregated reviews not needing to be real-time up to date. 24 hours or more between review and aggregated stars update is acceptable. We want to see unified product and engineering thinking.

#### Bad Solutions

Database triggers

* DB triggers are generally bad

Application logic that recomputes it every time a review is left

* Expensive and monolithic-style

Cron job that recomputes it for all listings every 24 hours

* Super expensive, won’t scale to millions of listings

#### Decent Solutions

* Application logic that uses math to avoid full recomputation: `((old_avg * num_reviews) + new_stars) / (num_reviews + 1)`
* Cron job that recomputes for only listings with new reviews

#### Best Solution

Leaving a review should put an event on an event bus, which another service should consume and use as a signal to update reviews.

## Step 4: Availability

### Requirements

Implement listing availability. How do you make sure that people only book dates that are available?

### Expectations

They may add a new table that represents host availability, or they can assume that every day is bookable. Either is OK.

When a user wants to book, they need to detect if any of the dates (range inclusive) they’re attempting to book are disallowed, either because the host is not available on that date, or because the listing is already booked for that date.

### Solution

There is a subproblem in here which is deciding if two intervals overlap. This is by itself a surprisingly tricky interview question. If they figure this out, good for them; if not, you might need to rescue them after awhile.

#### Bad solutions

* Iterate through every booking for the listing and check `forAll(booking, !overlap(attemptingBookingInterval, booking))`
* The above, but in a monstrous SQL join statement

#### Good solutions

* Denormalize booking dates into a datastore indexed by `(listing ID, date)` and stores availability. With this, deciding if a listing is available on a date is trivial and fast.
* As for how to keep this datastore up to date, refer to Step 3 solutions for best practices for keeping derived data up to date.

## Step 5: Search

### Requirements

Implement search! A user can search by:

* Location (not just a city, but “search within map area” type functionality)
* Availability dates
* Price
* Number of Guests

This has to be fast. Emphasize how critical accurate, fast searching is to AirBnB’s business.

### Expectations

They need to figure out some way to do search. Many people have little experience with search and might assume that the DB is magically able to do fast joins with no effort. This is false.

Price and number of guests are trivial to search because they’re static scalar attributes of the listing. Location and availability dates are hard.

If they made a slow solution in step 4 for checking availability, it will certainly fall over in this step and they need to reevaluate how to search availability for millions of listings quickly.

### Solutions

#### Bad solutions

* Attempting to shard by city, zip code, or state.
    * Extremely uneven shards.
    * Remind them that this has to work internationally, where zip codes and states don’t exist.
* Naively thinking you can cheaply do `a < lat < b AND c < long < d` on a relational database.
    * This will make your SQL DB fall over. Range queries on multiple columns is simply not possible because SQL can only index by one column. A contact book is fast because it’s sorted by first name. How would you sort a contact book such that you can do a range query on both first and last name? It’s impossible.

#### Good solutions

* Geospatial indexing using Elasticsearch, another capable datastore, or self-implemented.
* Recognizing that specialized search tools are necessary, especially for combining location and availability date searches.
    * More bonus points for using event buses to keep the specialized search datastore up to date with the source of truth.
* Talking about sharding or parallelization of searches, such as the dangers of uneven sharding, virtual shards, shard splitting, etc.

## Rubric (Design)

See the steps for examples of positive and negative signs.

### Unfamiliar

Makes their way through Step 1 and 2 with some difficulty.

### Familiar

Does Step 1 and 2, handles Step 3 with some difficulty, and struggles on Step 4.

### Proficient

Does Steps 1, 2, 3, handles 4 with some difficulty, and starts or tackles Step 5.

### Master

Does steps 1, 2, 3, 4, 5 with all best-in-class solutions and deep discussions on every topic.
