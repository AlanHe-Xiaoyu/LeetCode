# Fuzzy Search

- Maintainer: @shane.rogers

## Overview
* Candidate should write a function which fuzzy matches a input against a collection of strings. A match occurs when all the characters of the input string can be found within the string being checked.
* These characters have to be matched sequentially but not consecutively.
* For example, a pattern of `row` would be a fuzzy match for `brown` but not a fuzzy match for `worn`, even though all the pattern characters are present within the string being checked.


## Prompts

Implement the findColor function which produces the logged output below

```javascript
const colors = ["aliceblue","antiquewhite","aqua","aquamarine","azure","beige","bisque","black","blanchedalmond","blue","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkgrey","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkslategrey","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dimgrey","dodgerblue","firebrick","floralwhite","forestgreen","fuchsia","gainsboro","ghostwhite","gold","gold","goldenrod","gray","green","greenyellow","grey","honeydew","hotpink","indianred","indigo","ivory","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgray","lightgreen","lightgrey","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightslategrey","lightsteelblue","lightyellow","lime","limegreen","linen","magenta","maroon","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","navy","oldlace","olive","olivedrab","orange","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","purple","red","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen","seashell","sienna","silver","skyblue","slateblue","slategray","slategrey","snow","springgreen","steelblue","tan","teal","thistle","tomato","turquoise","violet","wheat","white","whitesmoke","yellow","yellowgreen"]

function findColor() {

}

console.log(findColor('uqi'))
// [ 'darkturquoise', 'mediumaquamarine', 'mediumturquoise', 'paleturquoise', 'turquoise' ]

console.log(findColor('zre'))
// [ 'azure' ]

console.log(findColor('gold'))
// [ 'darkgoldenrod', 'gold', 'goldenrod', 'lightgoldenrodyellow', 'palegoldenrod' ]
```

----

#### What do we want to see/hear?

* Solution should short-circuit where appropriate and avoid unnecessary loops.
* Candidate should have a strategy for logging and debugging their output while working across the various loops.
* Variables should have sensible names and avoid the use of single char reference variable names like `i || j || k` across the various loops.
* Good to hear clarifying questions around the sequential / consecutive requirements for fuzzy matches.

----

## Example Solutions

- [Javascript](#Javascript)

# Javascript

```javascript
export const findColors = (pattern) => {
    let matches = [];
    for (const color of colors) {
        if (checkMatch(color, pattern)) {
            matches.push(color);
        }
    }

    return matches;
}

const checkMatch = (color, pattern) => {
    const charCount = color.length
    const patternCount = pattern.length
    if (charCount < patternCount) {
        return false;
    }

    for (let charIx = 0; charIx < charCount; charIx++) {
        let currentCharIx = charIx;
        let counter = 0;

        while (currentCharIx < charCount) {
            if (color[currentCharIx] === pattern[counter]) {
                counter++;
            }
            currentCharIx++;
        }
        if (counter === patternCount) {
            return true;
        }
    }


    return false;
}
```
