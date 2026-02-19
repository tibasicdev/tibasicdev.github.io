# UPC
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Returns the check digit for a UPC.|None|None|N|DarkerLine|[file upc.zip]|

```
:Repeat E10≤N and N<E11
:Input "UPC? ",N
:End
:sum(3int(10fPart(Nseq(10^(I),I,-11,-1
:10fPart(.1Ans+.1)-1
```

A [UPC](https://en.wikipedia.org/wiki/universal_product_code) is a barcode system that is used for different items in stores. It works by encoding numbers in bars, with different length and width bars representing different digits. When the UPC machine scans in a barcode, it reads the bars and returns if it is a valid barcode or not.

Although all of the digits are important, the last digit is especially important because it is used to detect any variance. It is commonly known as the check digit, and it is actually calculated based on the values of the other 10 digits:

- Add all of the odd-numbered position digits and multiply the value by three
- Add all of the even-numbered position digits to the previous odd-numbered value
- If the last digit of the result is zero, then the check digit is itself zero.
- If the last digit is not zero, then subtract the last digit from 10, and that is the check digit.

In order to ensure that we have a value UPC, we check to make sure that it has a value within the appropriate range. Since our UPC is an 11-digit number, it should be between 10 and 100 billion.

We now loop through all of the digits, both even and odd, and get the resultant value stored in [Ans](ans.html). The reason this works is because the first two steps in calculating the check digit can be combined, since you are simply adding their values together. We then return the appropriate check digit, based on whether Ans is zero or not zero.
