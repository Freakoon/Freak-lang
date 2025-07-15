import tokenizer
import parser
import inpter
import json

code = """
let a = "Hello"
let b = 111
let c = true
echo a
echo b
echo c
"""

def jsonshow(x):
	return json.dumps(x,indent=4)

token = tokenizer.tokens(code)
parse = parser.parse(token)
print(jsonshow(parse))
print(inpter.run(parse))