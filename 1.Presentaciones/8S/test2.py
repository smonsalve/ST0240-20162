def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

archivo = str(input("ingrese Archivo: "))

elarchivo = open(archivo,'r')
for line in elarchivo:
	if is_palindrome(line):
	    print("Si, es un palindromo")
	else:
	    print("No, no es palindromo")