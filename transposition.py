class Trans(object):
	"""docstring for Trans"""
	key=6
	def encrypt(self,message):
		key=self.key
		ciphertext = [''] * key
		# print ciphertext
		for col in range(key):
			pointer=col
			while pointer<len(message):
				ciphertext[col]+=message[pointer]
				# print message[pointer]
				# print ciphertext
				pointer+=key
		return''.join(ciphertext)
	def decrypt(self,message):
		
		finalMsg = ""
		dl = message.split(' ')[:-1]
		for i in range(len(dl[0])):
			for dls in dl:
				finalMsg += dls[i]

		print finalMsg
		
a= Trans()
print "Encrypted Data: "+ a.encrypt("zurez tuba awesome good")
print a.decrypt("ztw uuegrbsoeaooz md ae")

