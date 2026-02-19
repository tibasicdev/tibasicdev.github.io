![The ShowStat Command](68k_showstat/showstat.png "The ShowStat Command")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Displays the results of an earlier statistics command.|ShowStat|This command works on all calculators.|2 bytes|
       
### Menu Location
- Press 2nd MATH to enter the MATH popup menu.
- Press 6 to enter the Statistics submenu.
- Press 9 to select ShowStat.
       
# The ShowStat Command

The ShowStat command displays the results of the last regression or summary statistics command in a dialog box. The full list of such commands is: [68k:CubicReg](68k:cubicreg.html), [68k:ExpReg](68k:expreg.html), [68k:LinReg](68k:linreg.html), [68k:LnReg](68k:lnreg.html), [68k:Logistic](68k:logistic.html), [68k:MedMed](68k:medmed.html), [68k:OneVar](68k:onevar.html), [68k:PowerReg](68k:powerreg.html), [68k:QuadReg](68k:quadreg.html), [68k:QuartReg](68k:quartreg.html), [68k:SinReg](68k:sinreg.html), and [68k:TwoVar](68k:twovar.html). 

For regressions, ShowStat first displays the general form of the regression (for instance, y=a*x+b), then the values of the parameters (a and b, in this case); LinReg also outputs the value of corr, and all of them but MedMed display the value of R<sup>2</sup>. For OneVar and TwoVar, ShowStat merely displays the list of [68k:system variables](68k:system-variables.html) modified, along with their values.

If there are no statistics to display (for instance, if none of these commands have been used since the calculator was last reset), ShowStat will display "No stat variables" in the dialog box. The calculator also automatically deletes the statistics if the variables they were calculated from are modified or deleted.

ShowStat might not always be the best choice to display these results. For instance, when doing a regression, looking at regeq(x) (assuming x is undefined) will give you the entire equation at once. In a program especially, you might want to display the output in a different way than with ShowStat.

## Related Commands

- [68k:LinReg](68k:linreg.html)
- [68k:OneVar](68k:onevar.html)
- ...
