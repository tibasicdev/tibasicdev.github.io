![Binomcdf](nspire_binomcdf/sample.png "Binomcdf")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|
|--- |--- |--- |
|Calculates the binomial cumulative probability, either at a single value or for all values|for a single value:<br>binomcdf(trials, probability, [lower_bound,] upper_bound)<br><br>for a list of all values (0 to trials)<br>binomcdf(trials, probability)|If this is only available on certain versions of the nspire|

### Menu Location
From inside a document:<br>Press Menu, then scroll to probability.<br>Press the right arrow, then scroll to Distributions.<br>Press the right arrow, then scroll to Binomial Cdf (B)

# Binomcdf

This command is used to calculate the binomial cumulative probability function. In plainer language, it solves a specific type of often-encountered probability problem, that occurs under the following conditions:
1. A specific event has only two outcomes, which we will call "success" and "failure"
1. This event is going to repeat a specific number of times, or "trials"
1. Success or failure is determined randomly with the same probability of success each time the event occurs
1. We're interested in the probability that there are **at most** N successes

For example, consider a couple that intends to have 4 children. What is the probability that at most 2 are girls?

1. The event here is a child being born. It has two outcomes "boy" or "girl". In this case, since the question is about girls, it's easier to call "girl" a success.
1. The event is going to repeat 4 times, so we have 4 trials
1. The probability of a girl being born is 50% or 1/2 each time
1. We're interested in the probability that there are at most 2 successes (2 girls)

The syntax here is `binomcdf(*trials*, *probability*, *value*)`. In this case:
```
binomcdf(4,.5,2)
```
This will give .6875 when you run it, so there's a .6875 probability out of 4 children, at most 2 will be girls.

If you wanted the probability that at least 1 and at most 2 will be girls, the syntax would be:
```
binomcdf(4,.5,1,2)
```

Another alternate syntax for `binomcdf(` leaves off the last argument, *value*. This tells the calculator to compute a list of the results for all values. For example:
```
:binomcdf(4,.5
```

This will come to {.0625 .3125 .6875 .9375 1} when you run it. These are all the probabilities we get when you replace "at most 2 girls" with "at most 0", "at most 1", etc. Here, .0625 is the probability of "at most 0" girls (or just 0 girls), .3125 is the probability of at most 1 girl (1 or 0 girls), etc.

Several other probability problems actually are the same as this one. For example, "less than N" girls, just means "at most N-1" girls. "At least N" girls means "at most (total-N)" boys (here we switch our definition of what a success is). "No more than", of course, means the same as "at most".




## Related Commands

- [`nspire:binompdf`](nspire:binompdf.html)
- [`nspire:geometpdf`](nspire:geometpdf.html)
- [`nspire:geometcdf`](nspire:geometcdf.html)
