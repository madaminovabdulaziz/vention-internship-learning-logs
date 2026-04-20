# Comprehensions & Generators — my notes

## What it is

A short way to build a collection from an iterable in one line, with optional filtering.

Instead of:
```python
out = []
for x in range(5):
    out.append(x*x)
```

Just write:
```python
[x*x for x in range(5)]
```

Same thing. Reads as: "x*x for each x in range 5."

## Four flavors — the brackets decide

```python
[x*x for x in range(5)]     # list      [0, 1, 4, 9, 16]
{x*x for x in range(5)}     # set       {0, 1, 4, 9, 16}
{x: x*x for x in range(5)}  # dict      {0:0, 1:1, 2:4, 3:9, 4:16}
(x*x for x in range(5))     # generator — NOT a tuple! lazy
```

> Watch: `(...)` is a generator expression, not a tuple comprehension. Tuple comprehensions don't exist.

## Anatomy

```
[ expression    for var in iterable    if condition ]
      ↑                  ↑                    ↑
   what to yield     what to loop        filter (optional)
```

## `if` at the end vs `if/else` in the middle — different things

These two look similar but do very different jobs. I confused them at first.

**`if` at the end = FILTER** (drops items):
```python
[x for x in range(10) if x % 2 == 0]   # [0, 2, 4, 6, 8]  ← odds are GONE
```

**`if/else` at the start = TRANSFORM** (keeps all, changes values):
```python
[x if x % 2 == 0 else 0 for x in range(10)]
# [0, 0, 2, 0, 4, 0, 6, 0, 8, 0]  ← same length, odds turned to 0
```

Rule I use:
- "keep some, drop some" → `if` at end
- "keep all, transform differently" → `if/else` at start

## Generators — the whole point is memory

A list comprehension builds the **whole list right now** and stores it.
A generator expression builds **a recipe**. Values come out only when you ask.

```python
lst = [x*x for x in range(1_000_000)]   # ~8 MB in memory
gen = (x*x for x in range(1_000_000))   # ~200 bytes
```

Same logic, 40,000× memory difference. Crazy.

### When I use which

**List** — when I need to:
- iterate more than once
- check `len()` or index into it
- keep the result around

**Generator** — when I:
- only loop once (e.g., feeding it to `sum`, `max`, `any`, `for`)
- might stop early (like `any()` short-circuiting)
- don't need to store the result

### Gotchas I hit

**Generators are one-shot.** After you iterate, it's empty.
```python
g = (x for x in range(3))
list(g)   # [0, 1, 2]
list(g)   # []  ← gone!
```

**No indexing, no len.**
```python
g[0]     # TypeError
len(g)   # TypeError
```

If I need these, use a list.

### Parens-dropping trick

When a generator is the ONLY argument to a function, the outer parens go away:
```python
sum(x*x for x in range(10))        # clean
sum((x*x for x in range(10)))      # also works, but redundant
```

Pretty, idiomatic, use it.

## Dict comprehension — my go-to tricks

**Invert a dict:**
```python
{v: k for k, v in d.items()}
```

**Build from two lists:**
```python
{k: v for k, v in zip(keys, values)}
# or just: dict(zip(keys, values))
```

**Filter while building:**
```python
{k: v for k, v in d.items() if v > 0}
```

> Duplicate keys: later one wins, silently.

## When NOT to use a comprehension

Sometimes a loop is just clearer. I switch back to a loop when:

- I need side effects (print, log, mutate something external)
- There's complex branching / try-except
- It wouldn't fit on one ~80-char line
- I need to **accumulate** into something (like appending to existing lists under dict keys) — this is awkward in a comprehension, clean with `setdefault` in a loop

Example where a loop wins:
```python
# Group users by city
by_city = {}
for u in users:
    by_city.setdefault(u["city"], []).append(u["name"])
```
Trying to do this in one comprehension ends up O(n²) or ugly. Just loop.

## What I learned the hard way

- `{}` is an **empty dict**, not an empty set. For empty set: `set()`.
- `(x for x in ...)` is a **generator**, not a tuple. Tuple comprehensions don't exist — use `tuple(...)` if you really want a tuple.
- Generators look cheap but remember they're one-shot. If in doubt, use a list.
- Readability > cleverness. A 3-line loop beats a 1-line unreadable comprehension.

## Quick self-check (I should know these cold)

- `[x*x for x in range(5)]` → `[0,1,4,9,16]`
- `{x%3 for x in range(10)}` → `{0,1,2}`
- `{x: x*x for x in range(3)}` → `{0:0, 1:1, 2:4}`
- `(x for x in range(3))` → generator object, not a tuple
- List vs generator memory: list scales with N; generator stays tiny
- Filter (`if` at end) vs transform (`if/else` at start) — different jobs
- Generator is one-shot: after `list(g)`, `list(g)` again is `[]`