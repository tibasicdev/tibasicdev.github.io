# Regression Models
These commands are used to fit a line or curve to approximate a set of data (known as a regression model). If you're running the commands outside a program, the result will be displayed on-screen ([DiagnosticOn](diagnosticon.html) and [DiagnosticOff](diagnosticoff.html) control whether you'll see the correlation statistics). Regardless, you can access the result in variables that can be accessed from the [VARS] > Statistics… > EQ submenu.

If you execute one of these commands with no arguments at all, the calculator will attempt to perform the regression on the data found in L₁ and L₂ with the former being the independent variable (x) and the latter being the dependent variable (y), but you can use any two lists you want by typing them after the command. You can also use a frequency list to assign weight to the data points. Finally, supplying an equation (such as Y₁) to the command will cause the regression model to be stored to that equation - it will also be stored to RegEQ, but you can't use that variable in programs.

The following regression models are available:


- [Med-Med](med-med.html)
- [LinReg(ax+b)](linreg(ax-b.html)
- [LinReg(a+bx)](linreg(a-bx.html)
- [QuadReg](quadreg.html)


- [CubicReg](cubicreg.html)
- [QuartReg](quartreg.html)
- [LnReg](lnreg.html)
- [ExpReg](expreg.html)


- [PwrReg](pwrreg.html)
- [Logistic](logistic.html)
- [SinReg](sinreg.html)
- [Manual-Fit](manual-fit.html)
