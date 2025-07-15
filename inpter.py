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
			vars[p["name"]] = parse_to_str(p["values"])
		elif vartype == "echo":
			text = parse_to_str(p["values"])
			eval(f"print({text})",{},vars)

while True:
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