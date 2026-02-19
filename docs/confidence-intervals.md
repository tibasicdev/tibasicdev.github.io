# Confidence Intervals
These commands are used to calculate a confidence interval. Given a specific distribution type, and a confidence value 0 to 1 (common values are 0.95 and 0.99), one of these commands will give you an interval such that you can say, with the given confidence value, that the true population parameter we're interested in (usually the mean) will lie in the interval.

Although it's very easy to say "there's a 95% (or 99%) probability that the population parameter lies in the interval," some picky people feel that it's incorrect to talk about probabilities of the parameter, when it has a fixed value - we just don't know it. According to this school of thought, the correct way of phrasing a conclusion is "if we were to conduct this experiment (or study) multiple times, we would capture the correct value of the parameter in our interval 99% (for example) of the time." 

All tests can be performed either on actual data, or on statistics such as mean and standard deviation. The following tests are available:

- [ZInterval](zinterval.html)
- [TInterval](tinterval.html)
- [2-SampZInt(](2-sampzint.html)
- [2-SampTInt](2-samptint.html)
- [1-PropZInt(](1-propzint.html)
- [2-PropZInt(](2-propzint.html)
- [LinRegTInt](linregtint.html) — TI-84+/SE only

Here's how you decide which test to use:

1. If you have two unrelated samples, use the commands with a 2- in them.
1. If you're interested in a proportion, use one of the PropZ intervals.
1. If you know the standard deviation already, use a Z interval.
1. If you want to approximate the standard deviation from your data, use a T interval.
1. Use LinRegTInt for calculating an interval for the slope of a regression.
