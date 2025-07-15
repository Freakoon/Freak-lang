import tokenizer,json
from keywords import Keyword

def parse(codeTokens):
	keyword = Keyword()
	result = {}
	for k,v in codeTokens.items():
		if keyword.check(v[0]):
			if v[0] == "let":
				result[k] = {"type":v[0],"name":v[1],"values":v[3:]}
			elif v[0] == "echo":
				result[k] = {"type":v[0],"values":v[1:]}
	return result
