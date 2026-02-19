![The bal( Command](bal/BAL.GIF "The bal( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the remaining balance after *n* payments in an [amortization schedule](https://en.wikipedia.org/wiki/amortization_schedule).|bal(*n*,[*roundvalue*]|TI-83/84/+/SE|2 bytes|

### Menu Location
On the TI-83, press:
1. 2nd FINANCE to access the finance menu.
1. 9 to select bal(, or use arrows and ENTER.

On the TI-83+ or higher, press:
1. APPS to access the applications menu.
1. 1 or ENTER to select Finance...
1. 9 to select bal(, or use arrows and ENTER.
       
# The bal( Command

The `bal(` command calculates the remaining balance after *n* payments in an [amortization schedule](https://en.wikipedia.org/wiki/amortization_schedule). It has only one required argument: *n*, the payment number. However, it also uses the values of the finance variables PV, PMT, and I% in its calculations.

The optional argument, *roundvalue*, is the number of digits to which the calculator will round all internal calculations. Since this rounding affects further steps, this isn't the same as using [`round(`](round.html) to round the result of `bal(` to the same number of digits.

Usually, you will know the values of **N**, PV, and I%, but not PMT. This means you'll have to use the finance solver to solve for PMT before calculating `bal()`; virtually always, FV will equal 0.

## Sample Problem

*Imagine that you have taken out a 30-year fixed-rate mortgage. The loan amount is $100000, and the annual interest rate (APR) is 8%. Payments will be made monthly. After 15 years, what amount is still left to pay?*

We know the values of **N**, I%, and PV, though we still need to convert them to monthly values (since payments are made monthly). **N** is 30*12, and I% is 8/12. PV is just 100000.

Now, we use the finance solver to solve for PMT. Since you intend to pay out the entire loan, FV is 0. Using either the interactive TVM solver, or the [`tvm_Pmt`](tvm.html) command, we get a value of about -$733.76 for PMT.

We are ready to use `bal(`. We are interested in the payment made after 15 years; this is the 15*12=180<sup>th</sup> payment. `bal(180)` gives us the result $76781.55 — as you can see, most of the loan amount is still left to pay after 15 years.

## Formulas

The calculator uses a recursive formula to calculate `bal()`:

$$
\operatorname{bal}(0)=\operatorname{PV}$$
$$
\operatorname{bal}(m)=\left(1-\frac{I\%}{100}\right)\operatorname{bal}(m-1)+\operatorname{PMT}$$

In the case that *roundvalue* is given as an argument, the rounding is done at each step of the recurrence (which virtually forces us to use this formula). Otherwise, if no rounding is done (and assuming I% is not 0), we can solve the recurrence relation to get:

$$
\operatorname{bal}(m)=\frac{1-\left(1-\frac{I\%}{100}\right)^m}{\frac{I\%}{100}}\operatorname{PMT}+\left(1-\frac{I\%}{100}\right)^m\operatorname{PV}$$

## Error Conditions

- **[ERR:DOMAIN](errors.html#domain)** is thrown if the payment number is negative or a decimal.

## Related Commands

- [`ΣPrn(`](sigmaprn.html)
- [`ΣInt(`](sigmaint.html)
- [`tvm_Pmt`](tvm.html)
