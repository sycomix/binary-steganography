# binary-steganography
Encode binary into text, with Python.

Usage:
```python
from binsteg import encode
encode(text, strip, bits_per_char, offset)
```
Where
`text` is the text or characters to encode
`strip` is the number of characters to take from the end of each  input byte (For  most ascii you could get away with 7, for example)
`bits_per_char` is the number of bits to use for each character of output
`offset` is the offset to add to each character of output.
