class Keyword:
	def __init__(self):
		self.keyword = []
		self._setting()
	def _setting(self):
		with open("keywords","r") as f:
			for line in str(f.read()).splitlines():
				self.keyword.append(line.strip())
			return True
	def check(self,word):
		if word in self.keyword:
			return True
		else:
			False