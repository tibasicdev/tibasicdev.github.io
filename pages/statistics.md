# Statistics Commands
The TI-83 series calculators include a wide range of commands for statistical analysis. In addition to some wide-purpose statistical commands, the commands available include regression models, probability distributions, and tools for calculating confidence intervals and significance tests.

Virtually all statistical calculations that take actual data as an argument will accept both an actual list of data (each element occurs in the list the number of times it occurred in the data), and data split up by frequency (two lists, the first giving each distinct element that occurred in the data, and the second giving the number of times it occurred).


## General Statistical Commands

These commands are meant to determine sample statistics of data. Further commands which are not generally used in statistics but may be helpful are located in the [2nd][LIST] menu.

- [1-Var Stats](1-var-stats.html)
- [2-Var Stats](2-var-stats.html)
- [mean(](mean.html)
- [median(](median.html)
- [stdDev(](stddev.html)
- [variance(](variance.html)

Plots are also a useful statistical tool, allowing you to analyze data graphically. The following commands exist for dealing with plots:
- [Plot1(, Plot2(, Plot3(](plotn.html)
- [PlotsOn](plotson.html)
- [PlotsOff](plotsoff.html)
- [Select(](select.html)

## [Regression Models](regression-models.html)

These commands are used to fit a line or curve to approximate a set of data. If you're running the commands outside a program, the result will be displayed on-screen ([DiagnosticOn](diagnosticon.html) and [DiagnosticOff](diagnosticoff.html) control whether you'll see the correlation statistics). Regardless, you can access the result in variables that can be accessed from the [VARS] > Statistics... > EQ submenu. Optionally, the regression model can also be stored to an equation variable.

(for more information, see [Regression Models](regression-models.html))

## [Probability Distributions](probability-distributions.html)

These commands are used to calculate or to graph probability values for various distribution types. For the continuous distributions, ...pdf( gives the probability density function (mainly useful for graphing), and ...cdf( gives the actual probability of a result occurring in an interval. For the discrete distributions, ...pdf( gives the probability for a single value, and ...cdf( gives the probability for all values up to some limit. 

(for more information, see [Probability Distributions](probability-distributions.html))

## [Confidence Intervals](confidence-intervals.html)

These commands are used to calculate a confidence interval. Given a specific distribution type, and a confidence value 0 to 1 (common values are 0.95 and 0.99), one of these commands will give you an interval such that you can say, with the given confidence value, that the true population parameter we're interested in (usually the mean) will lie in the interval.

(for more information, see [Confidence Intervals](confidence-intervals.html))

## [Significance Tests](significance-tests.html)

These commands are used to test if experimental data supports some model we have. To do a significance test, we first assume the null hypothesis - that any deviation from that model occurred by chance alone. Then we calculate the probability of such data occurring if the null hypothesis is correct. If this probability is sufficiently low (usually less than 0.05, or less than 0.01), then because it's so unlikely that the data occurred by chance, we conclude that some external factor did affect the data, rejecting the null hypothesis.

(for more information, see [Significance Tests](significance-tests.html))

## External References

Chapters 12 and 13 of the [TI-83 Plus Manual](http://education.ti.com/educationportal/sites/us/productdetail/us_ti83p.html?bid-6) describe the various statistics commands in detail.
