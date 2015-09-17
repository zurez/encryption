class Xor(object):
	
	"""
	Logic: Convert Text and pad to binary and get their xor. Simple!
	"""
	pad="zurez"
	def encrypt(self,text):
		return bytearray(a^b for a, b in zip(*map(bytearray, [text, self.pad]))) 
	def decrypt(self,text):
		return bytearray(a^b for a, b in zip(*map(bytearray, [text, self.pad]))) 


a= Xor()
b=a.encrypt("delhi")
print b
print a.decrypt(b)