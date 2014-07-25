import random

def gen_small(len = 6):
	assert len <= 6

	password = ""
	for i in range(len):
		password += chr(random.randint(0,9))
	return password


def gen(len = 16):
	assert len >= 12

	password = ""
	for i in range(3):
		password += chr(random.randint(48, 57))
	for i in range(3):
		password += chr(random.randint(65, 90))
	for i in range(3):
		password += chr(random.randint(97,122))
	password += chr(random.randint(35, 46))
	password += chr(random.randint(58, 64))
	password += chr(random.randint(93, 95))
	for i in range(len - 12):
		v = random.randint(35, 122)
		while v == 47 or v == 92 or v == 96:
			v = random.randint(35, 122)
		password += chr(v)

	tmp_list = list(password)
	random.shuffle(tmp_list)
	password = ""
	for ch in tmp_list:
		password += ch
	return password
