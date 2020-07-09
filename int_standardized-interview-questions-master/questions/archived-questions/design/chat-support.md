# Design Chat System for Member Support

- Maintainer: Markus Braasch

## Task Description

We ask the candidate to design a simple chat system for our member support team. We want the candidate to come up with 
a data model and basic API endpoints which cover all requirements we shared with him. We invite the candidate to share 
his own ideas for this application which would improve the user experience. In case the candidate goes too deep into this 
kind of brainstorming we can reign in the conversation and ask them to focus more on the technical aspects of the design.

## Requirements for the Candidate

- A support agent should be able to select standard responses from a list displayed to him, based on the context of the 
chat conversation
- We want to be able to measure how many conversations each agent had in a day
- It should be possible to measure how many messages it took on average per agent to satisfy the user  

## Expected Outcome

Candidate asks good questions to clarify the requirements of the system and they design a data model that covers all 
the requirements in an efficient manner. A senior-level candidate should suggest web sockets or a similar approach for 
real-time chat communication. They should also have good thoughts on how to scale the system as the usage increases, 
proposing a sharded database for example.

## Follow-up questions

1. Write a SQL query which tells me how many conversations agent X had yesterday, along with the average number of 
messages / responses per conversation. 
2. Users might enter PII during the chat session. How should we protect these data points from being compromised 
(during the session and at rest)?
3. How would you break this application down into services and/or service endpoints?
4. How would you separate the UI for the users from the UI for the agents from a security perspective?
5. What approaches can you think of to suggest the most suitable standard responses to questions / statements from the user?
