def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open("lsb.pnm") as f:
	dots = f.read().split("\n")

pixels = chunks(dots, 3)
data = ""

for pix in list(pixels)[:-1]:
	pix = map(int, pix)
	r, g, b = pix
	data += str(r&1)

data = map(lambda x:chr(int(x,2)), chunks(data, 8))
print(''.join(data))
