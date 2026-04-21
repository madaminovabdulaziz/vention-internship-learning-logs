# Day 2 — Closures & Decorators

## Topics covered

1. Closures & `nonlocal`
2. Decorator basics (`@decorator` syntax)
3. Preserving metadata with `@wraps`
4. Decorators with arguments (three-layer pattern)

## What I built

- `@timer` — measures execution time of any function
- `@log_calls` — prints function name, args, and return value
- `@retry(max_attempts=N, delay=S)` — retries a function on exceptions

## Key takeaways (in my own words)

- First of all, I have learned what are the closures, and that they are the foundation for decorators,
- and that if we do not write nonlocal, the code will crash, coz it always saves for reference, even parent funcion is executed and finshed, the inner function (closure) save varible data
- Also, I have learned to use decorators, that they are solving repetition behaviour in functions 
- Learned that @wraps doing very important work, it helps us to trace bugs, testing etc
- I have learned what actually works under the hood of @retry(max_attempts=3, delay=1)


## Files

- `01-closures/` — concepts + 7 exercises
- `02-basics/` — decorator basics + 5 exercises
- `03-preserving-metadata/` — `@wraps` + 3 exercises
- `04-with-arguments/` — three-layer pattern + 4 exercises (including `@retry`)