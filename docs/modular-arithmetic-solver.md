# Modular Arithmetic Solver
|Routine Summary|Inputs|Variables Used|
|--- |--- |--- |
|Finds the remainder of a division between two numbers.|A,M|A,M|

```
:A-Mint(A/M
```

This program takes modular equations of the form X ≡ A (mod M) and solves them for the common residue, which is equal to the remainder after A has been divided by M. Among other things, it can be useful for finding the day of the week (with Sunday–Saturday matching up with 0–6) after M number of days has passed, or the time on a clock after a number of hours has passed.

For example, if we were on a Saturday (which is day 6, given that Sunday is day 0), and we wanted to figure out what it will be in 18 days, we would store 6+18→A, then 7→M as the appropriate number of days in a week, and finally we would calculate MfPart(A/M to get 3, which translates to a Wednesday.

This simpler version can be used if A is guaranteed to be positive:
```
:MfPart(A/M
```
It may fail due to rounding precision errors.
