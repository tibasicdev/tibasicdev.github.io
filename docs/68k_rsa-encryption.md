# RSA Encryption
[RSA](https://en.wikipedia.org/wiki/rsa) is a popular encryption algorithm. It is a public-key algorithm — this means that anyone can encrypt messages using the "public key", but only the person who knows the "private key" can decrypt them.

The security of RSA relies on factoring large numbers being difficult. Unfortunately, numbers that would be large enough to be secure are also too large for the calculator to handle. Any key you could generate on a calculator could be broken on a computer in a matter of minutes or hours, depending on the length.

This program is a good example of a number-theoretic algorithm implemented on 68k calculators.


## The Code

```
rprime(a,b)
:Func
:Local p
:a+rand()(a-b)→p
:p+mod(p,2)+1→p
:Loop
:  If isPrime(p)
:    Return p
:  p+2→p
:EndLoop
:EndFunc
```

```
extgcd(a,b)
:Func
:Local q,r
:{1,0,a}→a
:{0,1,b}→b
:While b[3]>0
:  intDiv(a[3],b[3])→q
:  a-q*b→r
:  b→a
:  r→b
:EndWhile
:a
:EndFunc
```

```
rsakey(nbits)
:Func
:Local m,p,q,d,e
:intDiv(nbits,2)→nbits
:rprime(2^nbits,2^(nbits+1))→p
:rprime(2^nbits,2^(nbits+1))→q
:(p-1)(q-1)→m
:1+rand(m-2)→e
:While gcd(e,m)>1
:  1+rand(m-2)→e
:EndWhile
:extgcd(m,e)[2]→d
:{e,d,p*q}
:EndFunc
```

```
rsa(txt,e,n)
:Func
:txt/txt→result
:While e>0
:  If mod(e,2)=1
:    mod(result*txt,n)→result
:  mod(txt^2,n)→txt
:  intDiv(e,2)→e
:EndWhile
:result
:EndFunc
```

## An Explanation

The code for this program is divided into four parts. Two of them are necessarily independent: rsakey() is used to generate a public and private key, and rsa() is used to encrypt or decrypt. The other two functions could easily be part of rsakey(); they're isolated here for clarity, and because they're somewhat useful on their own; rprime() generates a random prime, and extgcd() is the extended Euclidean Algorithm.

First, here is a description of how RSA works.

To generate the key:
1. We find two large primes P and Q, and find N=PQ which will be used as a modulus. Let M=(P-1)(Q-1).
2. Take a random integer E, 1<E<M, which has no divisors in common with M.
3. Find E's inverse mod M: an integer D such that DE ≡ 1 mod M.
4. The pair (E,N) is the public key, and (D,N) is the private key.

To encrypt text:
1. Divide it into blocks which are encoded as integers A, 1<A<N.
2. Compute A^E mod N for each block, giving the encrypted version of that block.

To decrypt text, encrypt it using D instead of E.

It's a basic result in number theory that if N and M are defined as above, then A<sup>M</sup>≡ 1 mod N. This means that (A<sup>E</sup>)<sup>D</sup> = A<sup>DE</sup> ≡A<sup>M+1</sup>≡A mod N. Therefore the decryption actually does reverse the encryption.

We could find D from E easily because we know M, which depends on knowing P and Q. However, someone who knows just the public key only knows N=PQ; to get P and Q from there, he'd need to factor N, which is hard. This means that someone who doesn't know D can't easily find it, and the encryption is secure. 

### The rprime() function

This is by far the most time-consuming part of the entire algorithm. Fortunately, it only has to be done to generate a key, and keys are reusable. Still, the key generation could easily take a minute or two as a consequence.

The purpose of rprime() is to generate a prime number between its two arguments (i.e. rprime(1,100) generates a random prime between 1 and 100). In practice, it can end up overflowing past the upper bound, but this is very unlikely, especially for the ranges RSA deals with.

The idea is simple: a+rand(a-b)→p generates a random number between a and b to start at. The next line makes sure this starting point is odd. From there, we keep testing the number to see if it's prime; if it's not, we increase it by 2 and try again.

### The extgcd() function

The extended Euclidean Algorithm not only computes the GCD of a and b, but finds two constants M and N such that M*a+N*b=GCD(a,b) — this has lots of applications, only one of which is RSA.

The idea is similar to the standard Euclidean Algorithm to compute GCD. Initially, we can express a as 1*a+0*b, and b as 0*a+1*b. After that, each time we take a remainder, we can express it as a sum of a and b. The final remainder is the GCD, giving us the M and N above.

### The rsakey() function

The first part of the code is easy: we generate the random primes P and Q. Each of them has half the bits that N should, since multiplying them will approximately add the number of bits. 

The next few lines just follow the algorithm outlined earlier. Note that to get a random number relatively prime to M, we just keep picking numbers until the GCD is 1. This shouldn't take a long time, since most numbers are relatively prime to M (if factoring is hard, *accidentally* factoring should be even harder). 

The only tricky part is that we use extgcd() to find D. The reason this works is the following: If DE≡1 mod M, then D*E=k*M+1 for some k, so D*E-k*M=1. This is just the equation that the extended Euclidean Algorithm solves! (note that GCD(E,M)=1).

### The rsa() function

This function should work equally well for encrypting lists and single numbers. We'll assume that txt is a single number for simplicity, but every operation used distributes over lists, so a list would work the same way.

The exponentiation routine is not the For loop you'd expect. This would be terribly slow, since E is, on average, around 2<sup>127</sup> for a 128-bit modulus. Instead, we use the following logic:

- If E is even, then computing A<sup>E</sup> is the same as computing (A<sup>2</sup>)<sup>E/2</sup>.
- If E is odd, then A<sup>E</sup>=A*A<sup>E-1</sup>, for which the first bullet applies.

Therefore, every loop, we do the following:
- If E is odd, then we multiply A into the result, and we're left with the task of computing A<sup>E-1</sup>.
- Now E is even no matter what, so we square A and divide E by 2.

To prevent the numbers from getting too large, we take mod() ahead of time with every product.
