So as far as I understood, decorator with arguments is a decorator I can configure when I use it, by passing some settings in parentheses


```
@timer
def foo(): ... # no args, always behaves the same


@retry(max_attempts=3)  # with args - you told it "try 3 times"
def bar(): ... 


How do they work:

@retry(max_attempts=3) runs first as function call, it returns a decorator with 3 inside it as settings

The next step is, the returned decorator wras function just regular @

Why three layers

Because you have three different jobs, each needing its own scope:

Capture the arguments (max_attempts=3) → outer function
Capture the function being wrapped → middle function
Actually do the work when the function is called → inner function (the wrapper)

Each layer is a closure that remembers the stuff from the layers outside it. That's how the innermost wrapper has access to both max_attempts AND the original func.