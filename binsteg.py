from textwrap import wrap

def encode(text, strip, bits_per_char, offset):
	bytes = ["{0:b}".format(ord(char)).zfill(8)[-strip:] for char in text]
	#Combine all the bits of output to one string
	total = "".join(bytes)
	#Split it by the number of bits per character
	output_bytes = wrap(total, bits_per_char)
	return "".join(chr(int(byte, 2)+offset) for byte in output_bytes)