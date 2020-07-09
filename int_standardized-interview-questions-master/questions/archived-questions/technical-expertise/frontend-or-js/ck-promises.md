# Implement Promises

- Maintainer: @tbd

## Overview

## Prompts

Implement JS Promise API. The Promise object is used for asynchronous computations.
A Promise represents a value which may be available now, or in the future, or never.
Syntax
```
new Promise( function(resolve, reject) { ... } );
```
Parameters
A function that is passed with the arguments resolve and reject. The executor function is
executed immediately by the Promise implementation, passing resolve and reject functions
(the executor is called before the Promise constructor even returns the created object).
The resolve and reject functions, when called, resolve or reject the promise respectively.
The executor normally initiates some asynchronous work and then, once that completes, calls
either the resolve or reject function to resolve the promise or else reject it if an error occurred.
If an error is thrown in the executor function, the promise is rejected. The return value of the executor is ignored.
You'll develop this in a stepwise manner based on the following requirements:
1. Promise should have instance methods .then() and .catch() that are called based on the result
of the executor function.  .then signature should include fullfilled and rejected handlers. .catch
should include a rejected handler only.
2. .then() and .catch() should be callable multiple times and their associated handlers should
be queued.
3. The executor method should be called before the constructor returns
4. Insure that if the promise has already been fullfilled or rejected when a corresponding
handler is attached, the handler will be called, so there is no race condition between an
asynchronous operation completing and its handlers being attached
5. If .then() or .catch() methods return promises they should be chainable
6. Implement .all(iterable) which returns a promise that either fulfills when all of the
promises in the iterable argument have fulfilled or rejects as soon as one of the promises
in the iterable argument rejects. If the returned promise fulfills, it is fulfilled with an
array of the values from the fulfilled promises in same order as defined in the iterable.
If the returned promise rejects, it is rejected with the reason from the first promise in
the iterable that rejected. This method can be useful for aggregating results of multiple promises.

```
function CKPromise() {

}

new CKPromise(function(fulfill, reject) {

  setTimeout(function() {
    if (Math.random() >= 0.5) {
      reject(new Error('Promise Rejected'))
    } else {
      fulfill('Hello World')
    }
  }, 100)

}).then(function(data) {
  console.log(data)
}).catch(function(err) {
  console.log(err)
})
```

----

#### What do we want to see/hear?

----

## Example Solutions

- [Language](#Language)

# Language

```
Some code
```

