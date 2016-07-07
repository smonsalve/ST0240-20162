def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

#archivo = raw_input("ingrese Archivo: ")
miarchivo = "pali.ttt"

elarchivo = open(miarchivo,'r')
for line in elarchivo:
	line = line.rstrip('\n')
	if is_palindrome(line):
	    print(line + " -> Si, es un palindromo")
	else:
	    print(line + " -> No, no es palindromo")