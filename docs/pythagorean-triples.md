# Pythagorean Triples
|Routine Summary|Inputs|Outputs|Variables Used|Author|Download|
|--- |--- |--- |--- |--- |--- |
|Displays the Pythagorean triples.|*C* - how many triples you want to display|None|A, B, C|Weregoose|[file pythagoreantriples.zip]|

```
:For(A,2,C
:For(B,1,A-1
:Disp {A²-B²,2AB,A²+B²
:If getKey:Pause
:End:End
```

A [Pythagorean triple](https://en.wikipedia.org/wiki/pythagorean_triple) occurs when, while using the [Pythagorean Theorem](https://en.wikipedia.org/wiki/pythagorean_theorem) a<sup>2</sup>+b<sup>2</sup>=c<sup>2</sup> to find the three sides of a right triangle, all three values are whole integers. For example, a common triple is 3,4,5 — in this case, 9 (3<sup>2</sup>) + 16 (4<sup>2</sup>) = 25 (5<sup>2</sup>). The general formula that can be derived to figure out when a triple occurs is: a=(A<sup>2</sup>-B<sup>2</sup>) b=(2AB) c=(A<sup>2</sup>+B<sup>2</sup>).

Now that you know what a Pythagorean triple is, the routine should be pretty clear. We are essentially looping over the range of values that we want to find triples in, and then displaying the triples as a three element [list](lists.html) using the above mentioned formula. Because there can be many triples found, and displaying all of them would just be like a blur on the screen, the [Pause](pause.html) command allows you to temporarily halt the program so you can see the triples that are currently displayed.
