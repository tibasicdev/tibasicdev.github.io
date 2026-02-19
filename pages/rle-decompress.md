# Run-Length Encoding (RLE) Decompression
|Routine Summary|Inputs|Outputs|Variables Used|Download|
|--- |--- |--- |--- |--- |
|Decompresses a run length-encoded list.|*L₁* - The compressed list|*L₁* - The decompressed list|L₁, I, J|http://tibasicdev.github.io/local—files/rle-decompress/rledecompress.zip rledecompress.zip|

```
:dim(L₁→J
:sum(E3fPart(L₁)+not(fPart(L₁→dim(L₁
:For(I,Ans,1,-1
:int(L₁(J→L₁(I
:If .001<fPart(L₁(J:Then
:L₁(J)-.001→L₁(J
:Else
:J-1→J
:End:End
```

[Run-length encoding (RLE)](https://en.wikipedia.org/wiki/run-length_encoding) is a very easy compression algorithm that you can use for compressing a list of numbers. The way it works is that you remove all of the consecutive repeated numbers from the list, and modify the first instance of the numbers with how many repeated numbers there were.

For example, say you have a list of numbers 1,2,2,3,3,3,4. You start with the 1, and since there is only one 1, it wouldn't be modified. There are two 2's, however, so you would remove the second two, and add a decimal part (using [fPart(](fpart.html)) of how many 2's there were (in this case, just two, which we represent as .002). You would do this for the rest of the list, and the final list would be 1,2.002,3.003,4.

This routine could loosely be described as the [RLE compression](rle-compress.html) routine, but backwards. We start by calculating the length of the decompressed list. This is the sum of the length of the runs — E3fPart(L₁) — plus the number of elements with no runs — not(fPart(L₁)). Here E represents the [scientific E](e-ten.html).

Then, the decompression begins. The routine keeps the following loop invariants (things that stay true after each iteration of the loop):

- Every element after the Ith element is the correct decompressed element in that spot.
- The portion of the list up to and including the Jth element is the compressed version of the list elements that will be 1 through I.

We "unpack" one element from the end of the compressed portion: int(L₁(J→L₁(I. Then we test if this compressed portion is a run that still contains more elements. If it is, we subtract .001, reducing the number of elements in the run by 1. If it's not, we decrease J by 1 to move on to the previous compressed element. As you can see, the conditions listed above are still true.

Once the loop ends, the first condition of the ones above ensures that all elements have been correctly decompressed.

Note that we never store anything to L₁ itself, only to its elements. This is done to avoid using any more memory than necessary: if we stored to L₁, a copy of the list would get temporarily stored to Ans, and we would be using twice the memory we need. This way, the routine will work even for large lists. As a bonus, the only time we change the size of the list is the very beginning. So if the decompressed list wouldn't fit in memory, the routine crashes immediately and keeps the list intact.

## Error Conditions

- **[ERR:MEMORY](errors.html#memory)** is thrown if there is not enough space to store the decompressed list. 
- **[ERR:INVALID DIM](errors.html#invaliddim)** is thrown if the decompressed list would be longer than 999 elements.

## Related Routines

- [RLE Compression](rle-compress.html)
- [RLE Decompression for Strings](rle-compress-string.html)
