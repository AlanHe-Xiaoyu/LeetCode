# Data Formatting UI

- Maintainer: @shane.rogers

> Note: Suitable for onsites as requires company interview laptop. Most suitable for react skill set evaluation but can process the data and build vanilla html if needed.

## Overview
* To test the product building skills of the candidate, the ask is for them to work with a dirty blob of JSON data which represents CK offers and convert it into a trimmed down payload to power a standard CK offer component.
* The hope is that the candidate can derive from the UI mock what data they will need to pick out from the JSON and then format it in a clean and concise way for the FE.
* The candidate should then build the Offer UI represented in the mock.

## Prompts
* Clone the following [repo](https://code.corp.creditkarma.com/ck-private/fett_interview)
* Install the project dependencies with `npm i` from the root of the directory
* Start the app with `yarn start`

----

#### What do we want to see/hear?
* Quickly identify and note types of data from the mock which they need to pull from the JSON (title, reviews, approval odds, image)
* They should ask clarifying questions around their assumptions of what data is not needed, and what certain types of visual elements are such as approval odds.
* Identify various categories (Cards, Personal Loans, Auto) of data within the JSON, spotting which data is common and which is not (e.g. image url keys are different between categories)
* Solution should gracefully handle missing data / values.
* Build responsive UI which aligns with the mock layout and styles. Candidate should be competent at scaffolding and styling UI.

----

## Example Solutions

- [UI example](https://code.corp.creditkarma.com/ck-private/fett_interview/blob/master/src/offerTiles.png)

