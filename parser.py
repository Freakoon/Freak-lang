import tokenizer,json
from keywords import Keyword

#parser 
def parse(codeTokens):
	keyword = Keyword()
	result = {}
	for k,v in codeTokens.items():
		if keyword.check(v[0]):
			if v[0] == "let":
				#boolean parse type
				if v[3] == "true":
					result[k] = {"type":v[0],"name":v[1],"bool":v[3]}
				elif v[3] == "false":
					result[k] = {"type":v[0],"name":v[1],"bool":v[3]}
				#ohter
				else:
					result[k] = {"type":v[0],"name":v[1],"values":v[3:],"bool":""}
			elif v[0] == "echo":
				result[k] = {"type":v[0],"values":v[1:]}
			elif v[0] == "if":
				pass
	return result
