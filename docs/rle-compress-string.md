# Rle Compress String
```
:"_OO3_OO_O3_O_2O_2O->Str1
:"_->Str2
:For(F,1,length(Str1
:sub(Str1,F,1->Str3
:If inString("123456789",Str3
:Then
:For(G,1,expr(Str3
:Str2+sub(Str1,F+1,1->Str2
:End
:Else
:Str2+Str3->Str2
:End
:End
```

You can use a technique known as [Run-length encoding (RLE)](https://en.wikipedia.org/wiki/run-length_encoding) to compress a string. In the example above, this is done by placing a number in front of the consecutive repeated tokens. Str1 is the compressed string, and Str2 is the decompressed string. In Str2, the "2O" in Str1 becomes "OOO", and "3_" becomes "____".

## Related Routines

- [RLE Compression](rle-compress.html)
- [RLE Decompression](rle-decompress.html)
