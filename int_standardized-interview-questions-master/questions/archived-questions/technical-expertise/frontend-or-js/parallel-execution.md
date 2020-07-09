# Parallel Execution

- Maintainer: @tim.scanlin

## Overview

This task helps to check the knowledge of core JS plus evaluate the knowledge of common eng problems (race conditions, etc). The solution is to create a queue of arguments in memory


## Prompts

Assume that `a`, `b`, `c`, `d` and `e`are asynchronous functions with one argument. The only argument of each of the function is `callback`. Each time when they finish their execution, they call the `callback` argument. These functions may make some server interactions, animations, etc.

**Example**

```js
const a = function (callback) {
    setTimeout(function () {
        callback();
    }, 1000)
}

const b = function (callback) {
    fetch('http://example.com/').then(function() {
        doSomething();
        callback();
    })
}
```

Please write a function `$do`, which follows the following rules:

- The function accepts an arbitrary number of arguments and all the arguments passed to `$do` are _functions_.
- Each _function_ passed to do has a single argument and it is a _callback_ (see examples above).
- If `$do` is executed with several arguments, it _waits_ till the end of the execution and then runs the functions from the next call of do.

**Test spec**

```js

const a = function (callback) {
    setTimeout(function () {
        console.log('a')
        callback();
    }, 1000)
}

const b = function (callback) {
    setTimeout(function () {
        console.log('b')
        callback();
    }, 500)
}

const c = function (callback) {
    setTimeout(function () {
        console.log('c')
        callback();
    }, 700)
}

const d = function (callback) {
    setTimeout(function () {
        console.log('d')
        callback();
    }, 1200)
}

const e = function (callback) {
    setTimeout(function () {
        console.log('e')
        callback();
    }, 100)
}

$do(a, b, c, d);
$do(e);

// Logs "b, c, a, d, e" in the console
```

----

#### What do we want to see/hear?

----

## Example Solutions

- [Javascript](#Javascript)

# Javascript

```javascript
const queue = [];
let isRunning = false;
const $do = function (...args) {
    if (!args.length) {
        return
    }
    queue.push(args);

    function runNext() {
        if (!queue.length) {
            return;
        }
        isRunning = true;
        const fns = queue.pop();
        let totalCallbacks = 0;
        for (let i = 0; i < fns.length; i++) {
            fns[i](function() {
                totalCallbacks ++;
                if (totalCallbacks === fns.length) {
                    isRunning = false;
                    runNext();
                }
            })
        }
    }

    if (!isRunning) {
        runNext();
    }
}
```
