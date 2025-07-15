import tokenizer
import parser

def parse_to_str(dic):
	word = ""
	for i in dic:
		word += i
	return word

def run(parseCode:dict):
	vars = {}
	for key in parseCode.keys():
		p = parseCode[key]
		vartype = p["type"]
		if vartype == "let":
			if parse_to_str(p["bool"]) == "true":
							vars[p["name"]] = eval("True", {}, vars)
					
			elif parse_to_str(p["bool"]) == "false":
							vars[p["name"]] = eval("False", {}, vars)
			else:
				vars[p["name"]] = eval(parse_to_str(p["values"]), {}, vars)
		elif vartype == "echo":
			text = parse_to_str(p["values"])
			result = eval(text, {}, vars)
			print(result)

code = """
let a = 5 + 1
echo a
let b = true
echo b
"""

while True:
	a = tokenizer.tokens(code)
	b = parser.parse(a)
	run(b)
	break
	stdin = input(">>> ")
	if stdin.startswith("freak"):
		words = tokenizer.tokens(stdin)
		try:
			with open(words[1][1],"r") as f:
				tokenizer_code = tokenizer.tokens(f.read())
				parse = parser.parse(tokenizer_code)
				run(parse)
		except (FileNotFoundError,IndexError):
			print("File not found")
	elif stdin == "":
		continue
	else:
		tokenizer_code = tokenizer.tokens(stdin)
		parse = parser.parse(tokenizer_code)
		run(parse)