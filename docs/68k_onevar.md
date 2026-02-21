![The OneVar Command](68k_onevar/onevar.png "The OneVar Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Calculates several summary statistics for a list.|OneVar *list*[,*freq*,*arg3*,*arg4*]|This command works on all calculators.|3 bytes|
       
### Menu Location
1. Press 2nd MATH to enter the MATH popup menu.
2. Press 6 to enter the Statistics submenu.
3. Press 1 to select OneVar.
       
# The OneVar Command

The OneVar command generates some summary statistics for a list. In its simplest form, it takes one argument — a list variable to analyze (it won't work with a list expression). It will store results to the following [68k:system variables](68k:system-variables.html):

- $\bar{x}$ — the average, as given by [68k:mean()](68k:mean.html)
- Σx — the sum, as given by [68k:sum()](68k:sum.html)
- Σx<sup>2</sup> — the sum of squares
- Sx — the sample standard deviation, as given by [68k:stdDev()](68k:stddev.html)
- σx — the population standard deviation, as given by [68k:stDevPop()](68k:stdevpop.html)
- nStat — the length of the list, as given by [68k:dim()](68k:dim.html)
- minX — the smallest element, as given by [68k:min()](68k:min.html)
- q1 — the first quartile
- medStat — the median, as given by [68k:median()](68k:median.html)
- q3 — the third quartile
- maxX — the largest element, as given by [68k:max()](68k:max.html)

It won't actually display any of these results without prompting (although you could check the variables to find out their values). To display all of these statistics, use the [68k:ShowStat](68k:showstat.html) command.

## Advanced Uses

The OneVar command takes up to 4 list arguments. The second argument, if present, is a list of frequencies. This must be the same length as the first list, and if it's there, its N<sup>th</sup> element indicates how many times the N<sup>th</sup> element of the first list should be counted. The calculator has no problems accepting zero or fractional numbers as frequencies.

The third and fourth arguments don't actually have an application. Their intention is to divide the elements into several categories: the third list would indicate which category each element of the data list falls under, and the fourth list would be a list of categories. However, this was apparently never implemented, and adding these lists doesn't affect the output.

## Error Conditions





## Related Commands

- [68k:TwoVar](68k:twovar.html)
- [68k:ShowStat](68k:showstat.html)

## See Also

- [68k:system-variables](68k:system-variables.html)
