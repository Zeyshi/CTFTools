import binascii

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

input_file = 'EDA4A23F.bmp'
lef = open(input_file, 'rb')
lefile = lef.read()
LSBs = ''
for i in range(0, len(lefile)):
	LSBs += text_to_bits(lefile[i])[7]
i = 0
message = ''
while i < len(LSBs):
	try:
		message += chr(int(LSBs[i:i+8], 2))
	except:
		pass
	i += 8
with open('output.txt', 'w') as output_file:
	output_file.write(message)
print message
