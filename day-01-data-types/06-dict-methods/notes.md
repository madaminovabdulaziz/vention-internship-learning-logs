# Dictionaries — my notes

## What it is

Key → value mapping. Keys must be **hashable** (can't be list/dict/set). Values can be anything.
Ordered by insertion

## Creating

```python
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d = dict(zip(keys, values))
d = {k: 0 for k in keys}           # comprehension
d = dict.fromkeys(keys, 0)
```

> Trap: `dict.fromkeys(keys, [])` — all keys share the SAME list. Same bug as `[[]]*3`.
> For independent lists: `{k: [] for k in keys}`.

## Access

```python
d[key]              # KeyError if missing
d.get(key)          # None if missing
d.get(key, default) # default if missing
key in d            # O(1)
```

Rule I use: **`d[key]` if missing is a bug, `d.get(key)` if missing is OK.**

## Modify

```python
d[k] = v               # add or overwrite
d.pop(k)               # remove + return value (KeyError if missing)
d.pop(k, None)         # safe pop
del d[k]               # remove, no return
d.clear()              # empty
d.update(other)        # merge in place
a | b                  # new merged dict (3.9+)
a |= b                 # merge in place (3.9+)
```

## `setdefault` — the grouping hack

```python
d.setdefault(k, default)
```

If `k` exists → returns its value.
If `k` missing → inserts `k: default`, returns `default`.

Perfect for grouping:
```python
groups = {}
for word in words:
    groups.setdefault(word[0], []).append(word)
```

One line per item. No "if k in groups" check needed.

## Views — keys, values, items

These are NOT lists. They're **live windows** into the dict.

```python
k = d.keys()
d["new"] = 1
print(k)    # already includes "new"
```

If you need a real list: `list(d.keys())`.

### Set ops work on keys and items

```python
d1.keys() & d2.keys()    # common keys
d1.keys() - d2.keys()    # keys only in d1
d1.items() & d2.items()  # identical pairs
```

**Not on values** — values might not be hashable.

## Iteration — the patterns I use

```python
for k in d:                  # keys (default)
    ...

for v in d.values():         # values
    ...

for k, v in d.items():       # pairs ← most common
    ...

for k in sorted(d):          # sorted keys
    ...

for k, v in sorted(d.items(), key=lambda kv: kv[1]):   # by value
    ...
```

**95% of my dict loops are `for k, v in d.items():`.** Memorize this one.

## THE trap — mutating while iterating

```python
for k in d:
    if d[k] == 2:
        del d[k]   # RuntimeError
```

Fix — iterate a snapshot:
```python
for k in list(d):
    if d[k] == 2:
        del d[k]
```

Or build a filtered copy (cleaner):
```python
d = {k: v for k, v in d.items() if v != 2}
```

## Patterns I'll use constantly

**Counting:**
```python
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
```

**Grouping:**
```python
groups = {}
for item in items:
    groups.setdefault(item.category, []).append(item)
```

**Inverting:**
```python
inv = {v: k for k, v in d.items()}
```

**Filtering:**
```python
filtered = {k: v for k, v in d.items() if cond(v)}
```

**Merging (3.9+):**
```python
merged = d1 | d2
```

## Pitfalls I already hit

- `{}` is dict, not set. (burned me in topic 4)
- `d.keys()` is not a list. Wrap in `list()` to index.
- `.pop()` returns the value, `del` doesn't — pick based on whether I need it.
- `fromkeys` + mutable default = shared reference trap.
- Don't mutate while iterating. Use `list(d)` or a comprehension.

## Self-check

- `d.get("x")` vs `d["x"]` — `None` vs `KeyError`.
- Iterate both keys + values → `.items()`.
- Group words by first letter → `setdefault(letter, []).append(word)`.
- Merge two dicts → `a | b` (3.9+) or `{**a, **b}`.
- Views are live — they reflect changes in the dict.