# Implement Google Sheets

## Requirements

Implement a Google Sheet like product with the following features:

* Cell Entry
* Cell Formatting
* Save/Load (Auto-Save)
* Undo/Restore
* Collaboration
* Formulas (time permitting)

## Overview

This problem will test how a candidate separates front-end and back-end concerns. The features are ordered by difficulty.

## Notes

### Cell Entry

* The candidate should design their data structure at this stage. How is the spreadsheet represent in-memory on the client and how should it be represented in the server?
* The solution should account for a sparse table. One value in A1 and one value in ZZZZ9999 should not require an exorbitant amount of memory.
* How are the cells indexed? Can they accessed or traversed in an efficient manner?

### Cell Formatting

* The candidate should recognize the need for a “raw value” and a “display value”. Mutating the original value in this problem will lead to an incorrect design. Can they format the value twice without implementing crazy string parsing logic?
* Nudge the candidates with the formulas requirement if they are stuck here.

### Save/Load (Auto-Save) & Undo/Restore

* I would bundle these under the same “feature”. How will the candidate send updates to the server without transmitting the entire state back and forth? Does it scale on larger spreadsheets?
* What is the scope of the undo/restore feature, how long should the list be maintained?
* What happens if someone refreshes the browser?
* How should the undo/restore work differently than the native browser undo/restore
* When should the auto-save be triggered?
* What happens if the network latency is high?
* How would you implement “off-line” mode. (Bonus)

### Collaboration

* Ideally, the candidate should build upon their previous features.
* How will the two users connect to each other?
* How are changes from both users merged? How are conflicts handled?
* How will you handle high network latency?
* Connection management, how do users join a session, leave a session or timeout?
* How will the undo and restore feature work in a collaborative environment? Do you roll back the collision handling as well?

### Formulas (time permitting)

* How would you detect self-referential formulas?
* Incompatible types
* Should you perform the computation on the client, server or both? What are the trade offs.

## Rubric

### Unfamiliar

An unfamiliar candidate will struggle to design a working system. They may design a system that is unacceptably inefficient. Candidate may not know how to solve the problem even if the scaling and performance problems are brought up to them. Candidate may not understand how to separate concerns between the frontend and backend.

### Familiar

A familiar candidate should be able to design the first four features with efficient state management on the front-end. They should be knowledgeable in API design and produce a system that minimizes network traffic. The solution may not be optimal and there might be UX issues, but the candidate should at least recognize the problems and corner cases without solving it.

### Proficient

A proficient candidate should have a good grasp of the user experience requirements of the product. Their design will allow Google Sheets to behave like a desktop application with network latency hidden to the user.

Collaboration should be implemented between at least two users. The candidate should design a system that will reflect user A’s updates to user B’s browser automatically while resolving any conflicts (modifying the same cell).

Candidates should ensure their previously implemented features work with their collaboration design.

### Master

A master candidate should be able to design a system with all of the features at scale while handling certain corner cases and errors. The collaboration system should work with more than 2 users. Finally, the candidate should be able to walk through some formula use cases, including handling user errors (cycles, invalid cells…)
