from textwrap import wrap

def encode(text, strip, bits_per_char, offset):
	# text: input to encode
	# strip: number of bits to use from each character of input
	# bits_per_char: bits encoded per character of output
	# offset: character offset for each character of output
	bytes = []
	for char in text:
		#For each character, convert it to binary, left pad it to 8 zeroes, and then take the last 'strip' characters
		bytes.append("{0:b}".format(ord(char)).zfill(8)[-strip:])
	#Combine all the bits of output to one string
	total = "".join(bytes)
	#Split it by the number of bits per character
	output_bytes = wrap(total, bits_per_char)
	output = ""
	for byte in output_bytes:
		#Go over each split set of bits and fold them into the character, adding the output
		output += chr(int(byte, 2)+offset)
	return output