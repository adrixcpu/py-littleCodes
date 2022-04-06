print("Harry Potter!")  # Double quotation marks

got = 'Game of Thrones...'  # Single quotation marks
print(got)
print("$")  # Single character

empty = ""
print(empty)  # Just prints an empty line

multiple_lines = '''Triple quotes allows
multi-line string.'''
print(multiple_lines)

#####Cantidad de Caracteres
print("---Cant Caracteres---")
random_string = "I am Batman"  # 11 characters
print(len(random_string))

#####Indices de los strings
print("---Indices---")
batman = "Bruce Wayne"

first = batman[0]  # Accessing the first character
print(first)

space = batman[5]  # Accessing the empty space in the string
print(space)

last = batman[len(batman) - 1]
print(last)
# The following will produce an error since the index is out of bounds
# err = batman[len(batman)]

##### Indice inverso
print("---Indice Inverso---")
girl = "Adriana Perez"
print(girl[-1])  # Corresponds to batman[10]
print(girl[-5])  # Corresponds to batman[6]