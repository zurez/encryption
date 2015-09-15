class Viginere(object):
	"""docstring for Viginere"""
	alph="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	def __init__(self):
		pass


	def encrypt(self,text,key):


		cipheredText = []
		l = len(key)
		j = 0
		for i in range(len(text)):
			if text[i].isupper():
				c = chr( ord('A') + (ord(text[i]) + ord(key[j%l].uppper()) - 2*ord('A'))%26 )
				j += 1 
			elif text[i].islower():
				c = chr( ord('a') + (ord(text[i]) + ord(key[j%l].lower()) - 2*ord('a'))%26  ) 
				j += 1
			else:	
				c =text[i]
			#print(i%l)
			cipheredText.append(c)

		cipheredText = ''.join(cipheredText)

		print("Your ciphered Text is", cipheredText , )
		return (cipheredText, key)

	def decrypt(self,ct,key):

		msgText = []
		l = len(key)
		j = 0
		for i in range(len(ct)):
			if ct[i].isupper():
				c = chr( ord('A') + (ord(ct[i]) - ord(key[j%l].uppper()) )%26 )
				j += 1 
			elif ct[i].islower():
				c = chr( ord('a') + (ord(ct[i]) - ord(key[j%l].lower()) )%26  ) 
				j += 1
			else:	
				c = ct[i]
			#print(i%l)
			msgText.append(c)
			#print(c)

		msgText = ''.join(msgText)
		return msgText
a=Viginere()
print a.encrypt("zurez","lol")
print a.decrypt("kicpn","lol")