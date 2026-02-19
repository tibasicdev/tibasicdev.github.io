# Significance Tests
These commands are used to test if experimental data supports some model we have. To do a significance test, we first assume the the null hypothesis - that any deviation from that model occurred by chance alone. Then we calculate the probability of such data occurring if the null hypothesis is correct. If this probability is sufficiently low (usually less than 0.05, or less than 0.01), then because it's so unlikely that the data occurred by chance, we conclude that some external factor did affect the data, rejecting the null hypothesis.

The following commands are avalable for significance testing:

- [Z-Test(](z-test.html)
- [T-Test](t-test.html)
- [2-SampZTest(](2-sampztest.html)
- [2-SampTTest](2-sampttest.html)
- [1-PropZTest(](1-propztest.html)
- [2-PropZTest(](2-propztest.html)
- [χ²-Test(](chisquare-test.html)
- [2-SampFTest](2-sampftest.html)
- [LinRegTTest](linregttest.html)
- [ANOVA(](anova.html)
- [χ²GOF-Test(](chisquaregof-test.html) (84+/SE only)

How to decide which test to use:

Five of the tests are for fairly specific purposes:
1. If you have many categories, such as days of week, to compare against an expected value, use one of the χ² tests:
 - The χ²-Test( command is for comparing frequencies of two different categorical variables (e.g. weather vs. month).
 - The χ²GOF-Test( is for testing a distribution of a single categorical variable.
1. If you want to see the effects of many categories on one variable, use ANOVA.
1. If you're comparing the variance of two variables, use the *F* test.
1. Use LinRegTTest for testing the hypothesis of a linear relation between two variables.

For the remaining six tests:
1. If you're testing for significant difference betwen two data sets, use a command with 2- in it (for obvious reasons).
1. If your variable is a proportion, use 1-PropZTest or 2-PropZTest: proportion tests ALWAYS use z- rather than t-distributions.
1. If you already know the standard deviation, use a ZTest.
1. If you want to determine the standard deviation from the data, use a TTest.
