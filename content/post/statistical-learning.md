---
title: "Statistical Learning"
date: 2017-11-02
tags: ["statistical-learning"]
categories: ["python"]
menu:
  main:
    parent: Python
---

## Definition

1.  A closure is a function that makes use of variables defined in outer
    functions that have previously returned
2.  We have to "return" the inner function for this to work
3.  We can either call the inner function right away by using an extra () or we
    can store the result of the function in a variable
4.  Closure only exists when an inner function makes use of variables defined
    from an outer function that has returned. If the inner function does not
    make use of any of the external variables all we have is a nested function

## Example
```javascript
function outer() {
    var start = "Closures are"
    return function inner(){
        return start + " here";
    }
}
```
```javascript
var outer = (a) => inner = (b) => a + b
```
```javascript
var outerFn = () => innerFn = () => "Just returned from the inner function"
```
