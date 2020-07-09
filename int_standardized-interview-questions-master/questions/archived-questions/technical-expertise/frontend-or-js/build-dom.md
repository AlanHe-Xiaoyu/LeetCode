# DOM Building

- Maintainer: @tim.scanlin

## Overview

This task test the knowledge of core JS plus evaluates the knowledge of the common engineering problems, recursion and validation.

## Prompts

Based on this json structure representing the DOM, build out a function to generate the proper HTML.

Each array item has the signature:
`[nodeName, attributes, children]`

Be sure to handle:
- children as null, a string, or an array
- self closing elements

```javascript
let validDomInput = [
    'html', { lang: 'en' }, [
        ['head', null, [
            ['title', null, 'Credit Karma']
        ]],
        ['body', { class: 'app' }, [
            ['div', null, [
                ['h1', null, 'Hello world!'],
                ['input', { type: 'number' }, null]
            ]]
        ]]
    ]
]

console.assert(
    standardDom(validDomInput) === '<html lang="en"><head><title>Credit Karma</title></head><body class="app"><div><h1>Hello world!</h1><input type="number"></div></body></html>',
    'Should build proper DOM structure.'
)
```

**Additional**

To add more complexity to this problem various types of validation can be added.

- Validate to make sure there are no nested links (no `<a>` tags are allowed in other `<a>` tags).

----

#### What do we want to see/hear?

----

## Example Solutions

- [Javascript](#Javascript)

# Javascript

```js
function standardDom (data) {
    if (!data) return ''

    const attrs = data[1] ? Object.keys(data[1]).reduce((p, c) => {
        return `${p} ${c}="${data[1][c]}"`
    }, '') : ''

    const firstTag = `<${data[0]}${attrs}>`
    if (data[0] === 'input') {
        return firstTag
    }

    return `${firstTag}${
        (data[2] && typeof data[2] !== 'string')
            ? data[2].map(el => standardDom(el)).join('')
            : data[2]
    }</${data[0]}>`
}

let additionalTags = [
    'html', { lang: 'en' }, [
        ['head', null, [
            ['title', null, 'Credit Karma']
        ]],
        ['body', { class: 'app' }, [
            ['a', { href: '#' }, [
                ['div', null, [
                    ['a', { href: 'www.creditkarma.com' }, 'creditkarma.com']
                ]]
            ]]
        ]]
    ]
]

function additionalValidation (data, isa = false) {
    if (!data) return ''
    const attrs = data[1] ? Object.keys(data[1]).reduce((p, c) => {
        return `${p} ${c}="${data[1][c]}"`
    }, '') : ''
    const firstTag = `<${data[0]}${attrs}>`
    if (data[0] === 'input') {
        return firstTag
    }
    if (data[0] === 'a') {
        if (isa) {
            console.log(data[0])
            throw new Error('No nested a tags allowed')
        }
        isa = true
    }
    return `${firstTag}${
        (data[2] && typeof data[2] !== 'string')
            ? data[2].map(el => additionalValidation(el, isa)).join('')
            : data[2]
    }</${data[0]}>`
}
```
