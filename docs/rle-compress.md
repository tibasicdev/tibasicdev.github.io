# Run-Length Encoding (RLE) Compression
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Compresses a list of numbers using RLE compression.|*L₁* - The list of numbers you want to compress|*L₁* - The list of compressed numbers|L₁, I, J|[file rlecompress.zip]|

```
:1→J
:For(I,2,dim(L₁
:If L₁(I)=L₁(J:Then
:.002+L₁(J→L₁(J
:Else
:If L₁(I)=int(L₁(J:Then
:.001+L₁(J→L₁(J
:Else
:J+1→J
:L₁(I→L₁(J
:End:End:End
:J→dim(L₁
```

[Run-length encoding (RLE)](https://en.wikipedia.org/wiki/run-length_encoding) is a very easy compression algorithm that you can use for compressing a list of numbers. The way it works is that you remove all of the consecutive repeated numbers from the list, and modify the first instance of the numbers with how many repeated numbers there were.

For example, say you have a list of numbers 1,2,2,3,3,3,4. You start with the 1, and since there is only one 1, it wouldn't be modified. There are two 2's, however, so you would remove the second two, and add a decimal part (using [fPart(](fpart.html)) of how many 2's there were (in this case, just two, which we represent as .002). You would do this for the rest of the list, and the final list would be 1,2.002,3.003,4.

To save memory (which is of course the reason we're compressing) we will store the result to L₁, the same list the uncompressed data is in. Throughout the loop, J is the index of the last element of the compressed part of the list, and I is the index in the uncompressed part. We don't have to worry about the indices colliding, since I is always bigger than J.

We loop over the list with I, and check if the current element has the same value as the last element of the compressed list. If it is, then it's the beginning of a run, so we add .002 to that last element. 

If it isn't there's another possibility — the last element could represent an existing run of the same element. We check for this with the code If L₁(I)=int(L₁(J)). If this turns out to be the case, we add .001 to increase the length of the run. Otherwise, the element really is different, and we increase J and add a new element.

At the end, we store J to the size of L₁. This gets rid of all the unnecessary data, leaving us only with the compressed portion of the list.

Note that we never store anything to L₁ itself, only to its elements. This is a useful technique to avoid using too much memory while the program is running: if we stored to L₁, a copy of the list would be stored to Ans, which could easily give a [ERR:MEMORY](errors.html#memory) if the list is too large. As the program is now, the only additional memory used is contained in three real variables (I, J, and Ans).

## Related Routines

- [RLE Decompression](rle-decompress.html)
- [RLE Decompression for Strings](rle-compress-string.html)
