def roll(text):
	return text[::-1]

def swoop(text):
	text = list(text)
	for i in range(len(text)):
		text[i] = chr(ord(text[i]) - (i % 5))
	return ''.join(text)

password = input("Enter the password: ")
if swoop(roll(password)) == "}12u7#dvl{$`fos_4jwchb}jelg":
	print("Welcome in!")
else:
	print("Sorry, wrong password.")
	
	

password="}12u7#dvl{$`fos_4jwchb}jelg"

#I add following lines 

def swoopI(text):
	text = list(text)
	for i in range(len(text)):
		text[i] = chr(ord(text[i]) - (i % 5))
	return ''.join(text)

print(roll(swoopI(password)))
