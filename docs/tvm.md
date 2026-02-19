![The tvm_Pmt, tvm_I%, tvm_PV, tvm_N, and tvm_FV Commands](tvm/TVM.GIF "The tvm_Pmt, tvm_I%, tvm_PV, tvm_N, and tvm_FV Commands")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Solves for the specified finance variable.|tvm_Pmt(**N**,I%,PV,FV,P/Y,C/Y)<br><br>tvm_I%(**N**,PV,PMT,FV,P/Y,C/Y)<br><br>tvm_PV(**N**,I%,PMT,FV,P/Y,C/Y)<br><br>tvm_**N**(I%,PV,PMT,FV,P/Y,C/Y)<br><br>tvm_FV(**N**,I%,PV,PMT,P/Y,C/Y)<br><br>All arguments are optional.|TI-83/84/+/SE|2 bytes|

### Menu Location
On the TI-83, press:<br># 2nd FINANCE to access the finance menu.<br># 2 through 6 to select tvm_Pmt through tvm_FV respectively.<br>On the TI-83+ and higher, press:<br># APPS to access the applications menu.<br># 1 or ENTER to select Finance...<br># 2 through 6 to select tvm_Pmt through tvm_FV respectively.
# The tvm_Pmt, tvm_I%, tvm_PV, tvm_N, and tvm_FV Commands

The tvm_*VAR* commands use the TVM (Time Value of Money) solver to solve for the variable *VAR*. They're usually used in programs, since outside a program it's easier to use the interactive solver (the first option in the finance menu).

All five commands can be used by themselves, with no arguments. In that case, they will return the value of *VAR* solved from the current values of the other finance variables. 

If you give them arguments, the values you give will replace the values of the finance variables. You can supply as many or as few arguments as needed, and the finance variables will be replaced in the order: **N**, I%, PV, PMT, FV, P/Y, C/Y (skipping the one you're solving for).

## Error Conditions

- **[ERR:ITERATIONS](errors.html#iterations)** is thrown if the maximum amount of iterations was exceeded in computing I% (this usually means there is no solution)
- **[ERR:NO SIGN CHG](errors.html#nosignchg)** is thrown if calculating I% when FV, (N*PMT), and PV all have the same sign.


## Related Commands

- [Pmt_End](pmt_end.html)
- [Pmt_Bgn](pmt_bgn.html)
