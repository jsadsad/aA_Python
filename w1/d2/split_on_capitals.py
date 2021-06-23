def cap_space(string):
  res = ""
  i = 0
  while i < len(string):
    char = string[i]
    if char.isupper():
    	res += " "
    res += char
    i += 1
  return res.lower()

print(cap_space("helloWorld"))     #> "hello world"
print(cap_space("iLoveMyTeapot"))  #> "i love my teapot"
print(cap_space("stayIndoors"))    #> "stay indoors"