import tokenizer,json,copy
from keywords import Keyword

JsonBytecode = {
	"type":"",
	"name":"",
	"in":0,
	"integer":0,
	"floating":0,
	"bool":"",
	"string":"", 
	"values":[]
}

numbers = ["0","1","2","3","4","5","6","7","8","9","10"]
numbersfloat = []

#parser 
def parse(codeTokens):
	keyword = Keyword()
	result = {}
	for k,v in codeTokens.items():
		if keyword.check(v[0]):
			if v[0] == "let":
				#boolean parse type
				if v[3] == "true":
					bytecode = copy.deepcopy(JsonBytecode)
					bytecode["type"] = v[0]
					bytecode["name"] = v[1]
					bytecode["bool"] = "true"
					result[k] = bytecode
				elif v[3] == "false":
					bytecode = copy.deepcopy(JsonBytecode)
					bytecode["type"] = v[0]
					bytecode["name"] = v[1]
					bytecode["bool"] = "false"
					result[k] = bytecode
				#ohter
				else:
					bytecode = copy.deepcopy(JsonBytecode)
					bytecode["type"] = v[0]
					bytecode["name"] = v[1]
					bytecode["values"] = v[3:]
					if str(v[3]).startswith('"') and str(v[3]).endswith('"'):
						bytecode["string"] = v[3:]
					elif "input" in v[3]:
						bytecode["in"] = 1
					result[k] = bytecode
			elif v[0] == "echo":
				result[k] = {"type":v[0],"values":v[1:]}
			elif v[0] == "if":
				pass
	return result
