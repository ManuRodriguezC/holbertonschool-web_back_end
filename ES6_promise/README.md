# ES6 Promise

This project seeks to know and use different javaScript methods and functions necessary to carry out asynchronous processes or to handle expected responses and control their errors.

## Promise

Is a proxy for a value not necessarily known when the promise is created. It allows you to associate handlers with an asynchronous action's eventual success value or failure reason. This lets asynchronous methods return values like synchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise to supply the value at some point in the future.

Promises can handle two responses:

* resolve: Returns the expected or correct response, because sometimes you don't know what the promise may return.

* reject: Return the promise error, in turn this can be handled when a promise is created.

```
function signUpUser(firstName, lastName) {
  return new Promise((resolve, reject) => {
    resolve({ firstName, lastName });
    reject(Error);
  });
}
```

The returns also can, .then(): this return the successfull resposne and catch(): this give the error and can to modify re response errro.

## Multiple promises.

### Promise.all()
Takes an iterable of promises as input and returns a single Promise. This returned promise fulfills when all of the input's promises fulfill (including when an empty iterable is passed), with an array of the fulfillment values. It rejects when any of the input's promises reject, with this first rejection reason.

### Promise.allSettled()
Takes an iterable of promises as input and returns a single Promise. This returned promise fulfills when all of the input's promises settle (including when an empty iterable is passed), with an array of objects that describe the outcome of each promise.

### Promise.any()
Takes an iterable of promises as input and returns a single Promise. This returned promise fulfills when any of the input's promises fulfill, with this first fulfillment value. It rejects when all of the input's promises reject (including when an empty iterable is passed), with an AggregateError containing an array of rejection reasons.
