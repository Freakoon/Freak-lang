def tokens(code:str):
	result = {}
	line_number = 0
	word = ""
	for line in code.splitlines():
		line_number += 1
		if not line_number in result:
			result[line_number] = []
		for token in line:
			if token == " ":
				if word == "":
					pass
				else:
					result[line_number].append(word)
				word = ""
			else:
				word += token
	return result



code = "let a = 5 \nlet b = 5 \n echo a + b "
print(tokens(code))