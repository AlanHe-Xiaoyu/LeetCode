# Spiral Matrix Implementation
- Maintainer: @david.trejo

## Overview
This question asks the interviewer to iterate over a matrix in a spiral pattern.
It challenges their ability to create an empty n x n matrix, write for loops,
while loops, recursion (if they choose that route), their off-by-one and index
reasoning, and their visualization skills.

## Prompt (share with candidate)
>Write a function to fill an n x n matrix in a spiral pattern

>Example output:

```js
// n = 2
[
    [1,2],
    [4,3],
]
```

```js
// n = 3
[
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
```

>Two other good ones to consider:
```js
// n = 4

// n = 5
```

Speaker's notes:
>Questions? Stuck? Ask me for help. Typos? No problem. It's okay to google for APIs.

>It can be good to run the code often so we can feel confident about our progress.

>Think of this like a pairing session

**[See here for for a full set of my interview speaker's notes](https://dtrejo.com/engineer-interview-script).**

## Parts
If I really need to lead the candidate along, here're the basic steps we take. A more advanced candidate breezes past them and doesn't need me to say much.

## Dead ends
If you notice the candidate going down one of these...
- I don't recommend trying to come up with a fancy algorithm to compute the contents of the matrix based on the array coordinates. To my knowledge, there isn't one.

## Part 0
Create an empty matrix

## Iterative approach
## Part 1
Fill just the first row of the matrix with e.g. `1, 2, 3`

## Part 2
Try and fill the right column. Notice how you can fill the outer layer of the matrix and then repeat that until it's full?

## Part 3 [bonus-ish]
Notice how if you group the elements into groups of n-1, your `for` loops can have almost the same start and end conditions? (Rather than filling the whole first row with one loop).

## Part 4
The candidate write a wrapping for loop or while loop with a conditional something like "iterate this until counter === n * n". There are other valid conditionals.

## Part 4.5
Candidate abstracts the code which fills a layer of the matrix into a function, which usually accepts the boundaries it should iterate on and returns the incremented counter.

## Part 5
The candidate modifies their for loops so they can start and end on inner layers of the matrix.

## Part 6
Candidate tries n=2,3,4,5 to verify that all are working. I typically don't care much about the edge cases. It is nice when the candidate asks whether they should care about them (I usually say no).

Done!

### Bonus questions if they finish before the 50 minute mark
- What's the time complexity? n*n where n is the height of the matrix
- What's the space complexity? n*n where n is the height of the matrix
- What would you do to improve your code if you had more time?

### Expected questions from candidate
- Do you care about edge cases?
- Want me to write tests?

## Physical / Turtle appoach
Imagine you're a turtle, and you start by walking right, then turn right whenever you hit the edge of the matrix, or a matrix index which has already been filled out.

## Part A
Creates a list of directions, or a set of if statements.

## Part B
Creates a way to advance from one direction to the proper next one.

## Part C
Checks the next matrix index to see if it is undefined or already filled, and decides to turn right

## Part D
Creates condition to stop when either
- `counter === n * n`
- immediately after a turn, it was still full, so the matrix must be full

Either one are good; the first is simpler.

# Evaluation
If the candidate gets to part 5, but keeps experiencing off by one errors, I will give them a 3 if they seem close, and follow up over email with their solution in the same day. I suggest this on the phone, but make it clear that it is optional.

If they finish part 6 with time to spare, I give them a 4.

Otherwise, I give them a 1.

### Other notes
- I don't say anything if they have inconsistent or ugly spacing, although it is unpleasant. I figure maybe they're used to coding with format on save. I don't usually let this affect my rating.
- I notice some candidates talk a TON. Usually this means it won't go too well, BUT I did have one awesome candidate who explained a ton of what they were going to do, and their approach, and finished it all in one pass with their code running perfectly the first time they ran it. So, don't judge for this.
- When a candidate copy and pastes a for loop, it is an opportunity to make a mistake. Because they may not fully think through the loop again, or miss something. So, this is something to watch for.
- It's nicer when the candidate names their variables with coordinate words, like y and x, rather than row / column. It's much harder to get confused when indexing into a 2d matrix like `matrix[y][x]`.
- This problem is available on google, so if they seem really fast, you can ask them if they've done it before, and you won't dock them points even if they have.
