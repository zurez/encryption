class Ceaser(object):
	"""docstring for Ceaser"""
	
	alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
	def encrypt(self,text,shift):
		alph=self.alpha
		cipher=""
		for i in text:
			if i==" ":
				cipher+=" "
			else:
				shifted = alph.index(i)+shift
				if shifted<26:

					cipher= cipher+ alph[shifted]
				else:
					cipher= cipher+ alph[shifted-26]
		return cipher
	def decrypt(self, text,shift):
		alph=self.alpha
		cipher=""
		for i in text:

			if i not in alph:
				cipher+=" "
			else:
				shifted = alph.index(i)-shift
				if shifted<26:

					cipher= cipher+ alph[shifted]
				else:
					cipher= cipher+ alph[shifted+26]
		return cipher

a= Ceaser()
b= "et, tu brute????? nruqjrjsyx hfjxfw hnumjw fzymtw- mnrfsxmz xfnsn\n"
for i in range(1,25):
	print a.decrypt(b,i)