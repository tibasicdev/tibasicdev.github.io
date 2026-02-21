![The ►Eff( Command](eff/EFF.GIF "The ►Eff( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Converts a nominal interest rate to an effective interest rate.|►Eff(*interest rate*,*compounding periods*)|TI-83/84/+/SE|2 bytes|

### Menu Location
On the TI-83, press:
1. 2nd FINANCE to access the finance menu.
2. ALPHA C to select ►Eff(.

On the TI-83+ or higher, press:
1. APPS to access the applications menu.
2. ENTER or 1 to select Finance...
3. ALPHA C to select ►Eff(.
       
# The ►Eff( Command

The `►Eff(` command converts from a nominal interest rate to an effective interest rate. In other words, it converts an interest rate that does not take into account compounding periods into one that does. The two arguments are 1) the interest rate and 2) the number of compounding periods.

For example, take an interest rate of 7.5% per year, compounded monthly. You can use `►Eff(` to find out the actual percent of interest per year:
```
►Eff(7.5,12)
	7.663259886
```

## Formulas

The formula for converting from a nominal rate to an effective rate is:

$$\operatorname{Eff}=100\left(\left(1+\frac{\operatorname{Nom}}{100 \operatorname{CP}}\right)^{\operatorname{CP}}-1\right)$$

Here, Eff is the effective rate, Nom is the nominal rate, and CP is the number of compounding periods.

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if the number of compounding periods is not positive, or if the nominal rate is -100% or lower (an exception's made for the nominal rate if there is only one compounding period, since `►Eff(`X,1`)`=X)

## Related Commands

- [`►Nom(`](-nom.html)
