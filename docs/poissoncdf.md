![The poissoncdf( Command](poissoncdf/POISSONCDF.GIF "The poissoncdf( Command")
           
|Command Summary|Command Syntax|[Calculator Compatibility](compatibility.html)|[Token Size](tokens.html)|
|--- |--- |--- |--- |
|Calculates the Poisson cumulative probability for a single value|poissoncdf(*mean*, *value*)|TI-83/84/+/SE|2 bytes|

### Menu Location
Press:
1. 2ND DISTR to access the distribution menu
1. ALPHA C to select poissoncdf(, or use arrows.
Press ALPHA D instead of ALPHA C on a TI-84+/SE with OS 2.30 or higher.
       
# The poissoncdf( Command

This command is used to calculate Poisson distribution cumulative probability. In plainer language, it solves a specific type of often-encountered probability problem, that occurs under the following conditions:
1. A specific event happens at a known average rate (X occurrences per time interval)
1. Each occurrence is independent of the time since the last occurrence
1. We're interested in the probability that the event occurs at most a specific number of times in a given time interval.

The `poissoncdf(` command takes two arguments: The *mean* is the average number of times the event will happen during the time interval we're interested in. The *value* is the number of times we're interested in the event happening (so the output is the probability that the event happens at most *value* times in the interval). Note that you may need to convert the mean so that the time intervals in both cases match up. This is done by a simple proportion: if the event happens 10 times per minute, it happens 20 times per two minutes.

For example, consider point on a city street where an average of 5 cars pass by each minute. What is the probability that in a given minute, no more than 3 cars will drive by?

1. The event is a car passing by, which happens at an average rate of 5 occurences per time interval (a minute)
1. Each occurrence is independent of the time since the last occurrence (we'll assume this is true, though traffic might imply a correlation here)
1. We're interested in the probability that the event occurs at most 3 times in the time interval.

The syntax in this case is:
```
:poissoncdf(5,3
```
This will give about .265 when you run it, so there's a .265 probability that in a given minute, no more than 3 cars will drive by.

## Formulas

The `poissoncdf(` command can be seen as a sum of [`poissonpdf(`](poissonpdf.html) commands:

$$
\operatorname{poissoncdf}(\lambda,k)=\sum_{i=0}^k \operatorname{poissonpdf}(\lambda,i) = \sum_{i=0}^k \frac {e^{-\lambda} \lambda^i}{i!}$$

We can also write the `poissoncdf(` command in terms of the [incomplete gamma function](https://en.wikipedia.org/wiki/incomplete_gamma_function):

$$
\operatorname{poissoncdf}(\lambda,k)=\frac{\Gamma(k+1,\lambda)}{k!}$$

## Related Commands

- [`binompdf(`](binompdf.html)
- [`binomcdf(`](binomcdf.html)
- [`poissonpdf(`](poissonpdf.html)
