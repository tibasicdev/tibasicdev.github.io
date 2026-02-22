# User Variable Tokens
These two-byte tokens are used for the more complicated user-defined [variables](variables.html). All token values here (and elsewhere in this guide) are in hexadecimal.

Note that although these are the only tokens that are accessible from menus, adding any byte after the first (variable-type) byte will give a valid variable name (e.g. the token 5C 0A is a valid matrix, and AA 0A is a valid string). Since this is unintended behavior on the part of the OS developers, these extra tokens will usually appear as a ? symbol. Such tokens can be used if you run out of regular variable names for matrices or strings. It's possible to do the same for pictures, but harder: since [StorePic](storepic.html) and [RecallPic](recallpic.html) check whether the argument is 0..9, an assembly utility program is required to store and recall them (otherwise, all you need is some assembly program to actually paste the token somewhere).

## First Byte 0x5C ([Matrices](matrices.html))

- **5C 00** — [A]
- **5C 01** — [B]
- **5C 02** — [C]
- **5C 03** — [D]
- **5C 04** — [E]
- **5C 05** — [F]
- **5C 06** — [G]
- **5C 07** — [H]
- **5C 08** — [I]
- **5C 09** — [J]

## First Byte 0x5D ([Lists](lists.html))

- **5D 00** — L<sub>1</sub> 
- **5D 01** — L<sub>2</sub>
- **5D 02** — L<sub>3</sub>
- **5D 03** — L<sub>4</sub>
- **5D 04** — L<sub>5</sub>
- **5D 05** — L<sub>6</sub>

## First Byte 0x5E ([Equations](system-variables.html#equation))


- **5E 10** — Y<sub>1</sub>
- **5E 11** — Y<sub>2</sub>
- **5E 12** — Y<sub>3</sub>
- **5E 13** — Y<sub>4</sub>
- **5E 14** — Y<sub>5</sub>
- **5E 15** — Y<sub>6</sub>
- **5E 16** — Y<sub>7</sub>
- **5E 17** — Y<sub>8</sub>
- **5E 18** — Y<sub>9</sub>
- **5E 19** — Y<sub>0</sub>


- **5E 20** — X<sub>1T</sub>
- **5E 21** — Y<sub>1T</sub>
- **5E 22** — X<sub>2T</sub>
- **5E 23** — Y<sub>2T</sub>
- **5E 24** — X<sub>3T</sub>
- **5E 25** — Y<sub>3T</sub>
- **5E 26** — X<sub>4T</sub>
- **5E 27** — Y<sub>4T</sub>
- **5E 28** — X<sub>5T</sub>
- **5E 29** — Y<sub>5T</sub>
- **5E 2A** — X<sub>6T</sub>
- **5E 2B** — Y<sub>6T</sub>


- **5E 40** — r<sub>1</sub>
- **5E 41** — r<sub>2</sub>
- **5E 42** — r<sub>3</sub>
- **5E 43** — r<sub>4</sub>
- **5E 44** — r<sub>5</sub>
- **5E 45** — r<sub>6</sub>


- **5E 80** — u
- **5E 81** — v
- **5E 82** — w


## First Byte 0x60 ([Pictures](pictures.html))

- **60 00** — Pic1
- **60 01** — Pic2
- **60 02** — Pic3
- **60 03** — Pic4
- **60 04** — Pic5
- **60 05** — Pic6
- **60 06** — Pic7
- **60 07** — Pic8
- **60 08** — Pic9
- **60 09** — Pic0

## First Byte 0x61 ([GDBs](pictures.html))

- **61 00** — GDB1
- **61 01** — GDB2
- **61 02** — GDB3
- **61 03** — GDB4
- **61 04** — GDB5
- **61 05** — GDB6
- **61 06** — GDB7
- **61 07** — GDB8
- **61 08** — GDB9
- **61 09** — GDB0

## First Byte 0xAA ([Strings](strings.html))

- **AA 00** — Str1
- **AA 01** — Str2
- **AA 02** — Str3
- **AA 03** — Str4
- **AA 04** — Str5
- **AA 05** — Str6
- **AA 06** — Str7
- **AA 07** — Str8
- **AA 08** — Str9
- **AA 09** — Str0
