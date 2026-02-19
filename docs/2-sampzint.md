![The 2-SampZInt( Command](2-sampzint/2-SAMPZINT.GIF "The 2-SampZInt( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Using either already-calculated statistics, or two data sets, computes a Z confidence interval for the difference between two sample means.|2-SampZInt(*σ<sub>1</sub>*, *σ<sub>2</sub>*, [*list1*, *list2*, [*frequency1*], [*frequency2*], [*confidence level*]<br>(data list input)<br><br>2-SampZInt(*σ<sub>1</sub>*, *σ<sub>2</sub>*, *x<sub>1</sub>*, *n<sub>1</sub>*, *x<sub>2</sub>*, *n<sub>2</sub>*, [*confidence level*]<br>(summary stats input)|TI-83/84/+/SE|2 bytes|

### Menu Location
When editing a program, press:
1. STAT to access the statistics menu
1. LEFT to access the TESTS submenu
1. 9 to select 2-SampZInt(, or use arrows
(this key sequence will give you the 2-SampZInt... screen outside a program)
       
# The 2-SampZInt( Command

The 2-SampZInt( command uses the techniques of Z Intervals to compute an interval for the **difference** between the means of two independent populations, at a specified confidence level. Use 2-SampZInt( when you have two independent variables to compare, and you already know their standard deviations. The 2-SampZInt( command assumes that both variables are distributed normally, but it will work for other distributions if the sample size is large enough.

There are two ways to call this command: by supplying it with needed sample statistics (mean and sample size, for both data sets), or by entering two lists and letting the calculator work the statistics out. In either case, you will need to enter the standard deviation and desired confidence level as well. 

In the data list syntax, *σ<sub>1</sub>* and *σ<sub>2</sub>* are the two standard deviations. 
In the summary stats syntax, *σ<sub>1</sub>* and *σ<sub>2</sub>* are the two standard deviations, *x<sub>1</sub>* and *x<sub>2</sub>* the two sample means, and *n<sub>1</sub>* and *n<sub>2</sub>* the two sample sizes.

The output will contain an open interval (a, b) that is your answer: the difference between the two means will lie in this interval. Specifically, it is the second mean subtracted from the first - μ<sub>1</sub>-μ<sub>2</sub>. If you're interested in the reverse difference, just flip the signs on the interval.

Tip: don't use this command in a matched-pairs setting when you can match the two samples up by units or subjects. Instead, take the difference between the two samples in each matched pair, and use a regular [ZInterval](zinterval.html).

## Sample Problem

You want to compare the average height of a freshman and a senior at your school. You haven't asked everyone, but you took a random sample of 40 people from each class and found out their heights (and stored them to L<sub>1</sub> and L<sub>2</sub>). You've read in your textbook that the standard deviation of teenagers' heights is usually 6 inches. You've decided to use a 95% confidence interval.

Based on the data list syntax for a 2-SampZInt(, here is your code:
```
:2-SampZInt(6,6,L1,L2,95
you can also use
:2-SampZInt(6,6,L1,L2,.95
```

Alternatively, you could calculate the mean and sample size and enter those instead. The sample size in this case is 40 for both data sets; let's say the means were 57 inches and 67 inches. You now have all the needed statistics:
- *σ<sub>1</sub>* is the standard deviation for freshmen: 6 inches
- *σ<sub>2</sub>* is the standard deviation for seniors: also 6 inches 
- *x<sub>1</sub>* is the mean height of freshmen: 57 inches
- *n<sub>1</sub>* is the number of freshmen in the sample: 40
- *x<sub>2</sub>* is the mean height of seniors: 67 inches
- *n<sub>2</sub>* is the number of seniors in the sample: 40
This means that the code is:
```
:2-SampZInt(6,6,57,40,67,40,95
you can also use
:2-SampZInt(6,6,57,40,67,40,.95
```

Of course, the main use of the 2-SampZInt( command is in a program. While you can enter the command on the home screen as well (just look in the catalog for it), it would probably be easier to select 2-SampZInt... from the STAT>TEST menu (see the sidebar), since you don't have to remember the syntax.

## Advanced Uses

As with most other statistical commands, you can add frequencies to the lists (only with the data list syntax, of course); if you do, both lists must have frequencies, and the arguments go in the order *first data list*, *second data list*, *first freq. list*, *second freq. list*. Each frequency list must contain non-negative real numbers, which can't be all 0.
## Optimization

Using the data list syntax, all items but the standard deviations are optional: the calculator will assume you want to use L1 and L2 for your data unless other lists are supplied, and that the confidence level you want is 95% unless you give another one. Using the summary stats syntax, the confidence level is also optional - again, the calculator will assume 95%. This means we can rewrite our code above in a simpler manner:

```
:2-SampZInt(6,6,L1,L2,95
can be
:2-SampZInt(6,6
```
```
:2-SampZInt(6,6,57,40,67,40,95
can be
:2-SampZInt(6,6,57,40,67,40
```

## Related Commands

- [ZInterval](zinterval.html)
- [TInterval](tinterval.html)
- [2-SampTInt](2-samptint.html)
