![The 2-SampFTest Command](2-sampftest/2-SAMPFTEST.GIF "The 2-SampFTest Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Performs a *F*-test to compare the standard deviations of two populations.|2-SampFTest [*list1*, *list2*, *frequency1*, *frequency2*, *alternative*,*draw?*]<br>(data list input)<br><br>2-SampFTest *s<sub>1</sub>*, *n<sub>1</sub>*, *s<sub>2</sub>*, *n<sub>2</sub>*, [*alternative*,*draw?*]<br>(summary stats input)|TI-83/84/+/SE|2 bytes|

### Menu Location
While editing a program, press:
1. STAT to access the statistics menu
1. LEFT to access the TESTS submenu
1. ALPHA D to select 2-SampFTest, or use arrows
Outside the program editor, this will select the 2-SampFTest... interactive solver.

Change the last keypress to ALPHA E on a TI-84+/SE with OS 2.30 or higher.
       
# The 2-SampFTest Command

2-SampFTest performs an *F*-test to compare the standard deviations of two populations. This test is valid for two normally distributed populations, but is extremely sensitive to non-normality, so it should not be used unless you are certain that the populations are normal.


The logic behind the test is as follows: we want to test the hypothesis that the standard deviations of the two populations are equal (the null hypothesis). The letter σ is used for a standard deviation, so this is usually written as σ<sub>1</sub>=σ<sub>2</sub>. To do this, we assume that this "null hypothesis" is true, and calculate the probability that the difference between the two standard deviations occurred, under this assumption. If this probability is sufficiently low (usually, 5% is the cutoff point), we conclude that since it's so unlikely that the data could have occurred under the null hypothesis, the null hypothesis must be false, and therefore the deviations are not equal. If, on the other hand, the probability is not too low, we conclude that the data may well have occurred under the null hypothesis, and therefore there's no reason to reject it.

In addition to the null hypothesis, we must have an alternative hypothesis as well - usually this is simply that the two standard deviations are not equal. However, in certain cases when we have reason to suspect that one deviation is greater than the other (such as when we are trying to verify a claim that one standard deviation is greater), our alternative hypothesis may be that the first standard deviation is greater than the second (σ<sub>1</sub>>σ<sub>2</sub>) or less (σ<sub>1</sub><σ<sub>2</sub>).

As for the 2-SampFTest command itself, there are two ways of calling it: you may give it a list of all the sample data, or the necessary statistics about the list (*s<sub>1</sub>* and *s<sub>2</sub>* the sample standard deviations,  and *n<sub>1</sub>* and *n<sub>2</sub>* the sample sizes). In either case, you can indicate what the alternate hypothesis is, by a value of 0, -1, or 1 for the *alternative* argument. 0 indicates a two-sided hypothesis of *σ<sub>1</sub>*≠*σ<sub>2</sub>*, -1 indicates *σ<sub>1</sub>*<*σ<sub>2</sub>*, and 1 indicates *μ<sub>1</sub>*>*μ<sub>2</sub>*. (In fact, the calculator will treat any negative value as -1, and any positive value as 1).

Although you can access the 2-SampFTest command on the home screen, via the catalog, there's no need: the 2-SampFTest... interactive solver, found in the statistics menu, is much more intuitive to use - you don't have to memorize the syntax.

In either case, it's important to understand the output of 2-SampFTest. Here are the meanings of each line:

- The first line, involving σ<sub>1</sub> and σ<sub>2</sub>, is the alternative hypothesis.
- F is the test statistic, the ratio of the standard deviations. If the null hypothesis is true, it should be close to 1.
- p is the probability that the difference between σ<sub>1</sub> and σ<sub>2</sub> (the two standard deviations) would occur if the null hypothesis is true. When the value is sufficiently small, we reject the null hypothesis and conclude that the alternative hypothesis is true. You should have a cutoff value ready, such as 5% or 1%. If p is lower, you "reject the null hypothesis on a 5% (or 1%) level" in technical terms.
- Sx<sub>1</sub> and Sx<sub>2</sub> are the two sample standard deviations.
- x-bar<sub>1</sub> and x-bar<sub>2</sub> are the two sample means. They aren't used in the calculation, and will only be shown with the data list syntax.
- n<sub>1</sub> and n<sub>2</sub> are the sample sizes.

## Advanced Uses

The final optional argument of 2-SampFTest, *draw?*, will display the results in a graphical manner if you put in "1" for it. The calculator will draw the distribution, and shade the area of the graph that corresponds to the probability p. In addition, the value of F and the value of p will be displayed. You would make your conclusions in the same way as for the regular output.

As with most other statistical commands, you may use frequency lists in your input (when using the data list syntax). If you do, then both lists must have frequencies, and the order of the arguments would be *list1*, *list2*, *frequency1*, *frequency2*.

## Optimization

Some of the arguments of the 2-SampFTest command have default values, and the argument can be omitted if this value is accepted.

- The *draw?* argument can be omitted if you don't want graphical output, although you could put "0" in as well.
- If the above argument is omitted, and you're doing a two sided test, you may omit the *alternative* argument.
- With data list input, you can always omit the frequency lists if you won't be using them.
- With data list input, if the flags that go at the end are omitted, and you're using the default lists L1 and L2, you may omit those as well.

Example:
```
:2-SampFTest L1,L2,0
can be
:2-SampFTest
```

## Related Commands

- [Z-Test(](z-test.html)
- [T-Test](t-test.html)
