# Day 3 — Object-Oriented Programming

## Topics covered

1. Classes & `__init__`
2. Methods (instance, class, static)
3. Encapsulation & properties (merged — access levels, `_protected`, name mangling, `@property` / setter / deleter)
4. Inheritance
5. MRO (Method Resolution Order)
6. Abstract classes
7. Polymorphism

## What I built

- `SecretBox` — three access levels (public, `_protected`, `__private`) to see what Python actually enforces
- `Logger` — protected `_messages` buffer, showing `_` is a contract, not a lock
- `Circle` — `@property` with getter + validating setter + computed properties (area, diameter, circumference)
- `BankAccount` — property-based balance with validation funneling every write through one place
- `Rectangle` — read-only computed `area` / `perimeter` that stay in sync when width/height change
- `User` (with `@name.deleter`) — full getter/setter/deleter triple
- `HumanUser` — email normalization via setter (strip + lowercase + `@` check)

## Key takeaways (in my own words)

- "Private" in Python is a convention, not enforcement. `__x` gets name-mangled to `_ClassName__x` — you can still reach it, just uglier.
- The `_` prefix is a handshake with other developers: "internal, don't touch." Python will still let you touch it.
- The three pieces of a property: storage (`self._x`), getter (`@property` with public name), setter (`@x.setter` same name). Storage name MUST differ from property name or you get infinite recursion.
- Properties let you add validation later without changing calling code. `self.email = email` in `__init__` works the same whether `email` is a plain attribute or a property with a setter — that's the killer feature.
- `r.area()` (method) vs `r.area` (property) signals intent: action vs. value. Computed properties stay in sync automatically.

## When to reach for what

1. Just stored, no rules → public attribute (`self.x`)
2. Needs validation / type-checking / logging on read/write → property with getter + setter
3. Derived from other attributes → read-only property (getter only)
4. Expensive to compute, should be cached → property (with caching inside)

## Files

- `01-classes-and-init/` — class basics, constructors
- `02-methods/` — instance / class / static methods
- `03-encapsulation-properties/` — access levels + `@property` (merged, since they're the same idea)
- `04-inheritance/` — (in progress)
- `05-mro/` — (in progress)
- `06-abstract-classes/` — (in progress)
- `07-polymorphism/` — (in progress)
