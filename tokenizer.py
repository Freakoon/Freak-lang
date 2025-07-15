def tokens(code:str):
	result = {}
	line_number = 0
	word = ''
	for line in code.splitlines():
		if line.strip() == "":
			continue
		line_number += 1
		if not line_number in result:
			result[line_number] = []
		for token in line:
			if token == " " or token == "":
				result[line_number].append(word)
				word = ''
			else:
				word += token
		if word:
			result[line_number].append(word)
			word = ''
	return result