# Balanced Brackets

- Maintainer: @shane.rogers

## Overview
This question requires that the candidate keep track of a series of brackets within an input string and determine whether they are balanced. For example `{}[]()` is balanced, each character has a corrsponding closing bracket and importantly is in order.
A different configuration of brackets like `{[()]}` would also be balanced. This series however is unbalanced `{[}](`. This question lends itself to the use of a Stack to keep track of additions and removals from the data structure.

## Prompts

* Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
* For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

----

#### What do we want to see/hear?

Want to see the candidate reach for a single stack data structure to track brackets.

----

## Example Solutions

- [Javascript](#Javascript)

# Javascript

```javascript
const BRACKET_MAP = {
    "(": ")",
    "[": "]",
    "{": "}"
};

export const balanced = brackets => {
    const stack = [];

    for (let bracket of brackets) {
        const isOpenBracket = Boolean(BRACKET_MAP[bracket])

        if (isOpenBracket) {
            stack.push(bracket);
        } else {
            const lastBracket = stack.pop();

            if (BRACKET_MAP[lastBracket] !== bracket) {
                return false;
            }
        }
    }
    return true;
};
```
