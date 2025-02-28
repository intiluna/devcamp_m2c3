# Exercise 1
## Create a string, number, list, and boolean, each stored in their own variable.
print("Ejercicio 1: ")
string_var = "Aprendiendo a programar con python"
number_var = 100
list_var = [1, 2, "text1", 4, ["lista2_elemento1", "lista2_elemento2"]]
boolean_var = True

print("Ejemplos de Variables:")
print(f"variable tipo string: {string_var}")
print(f"variable tipo numero:{number_var}")
print(f"variable tipo lista:{list_var}")
print(f"variable tipo boolean:{boolean_var}")
print("-----------------")

# Exercise 2
## Use an index to grab the first 3 letters in your string, store that in a variable.
print("Ejercicio 2: ")
first_three_letters = string_var[:3]
print(f"Primeras 3 letras de string:{first_three_letters}")
print("-----------------")

# Exercise 3
## Use an index to grab the first element from your list.
print("Ejercicio 3:")
list_first_element = list_var[0]
print(f"Primer elemento de lista: {list_first_element}")
print("-----------------")

# Exercise 4
## Create a new number variable that adds 10 to your original number.
print("Ejercicio 4:")
new_number = number_var + 10
print(f"Nuevo numero: {new_number}")
print("-----------------")

# Exercise 5
## Use an index to get the last element in your list.
print("Ejercicio 5:")
mi_ultimo_elemento = list_var[-1]
print(f"Ultimo elemento de lista: {mi_ultimo_elemento}")
print("-----------------")

# Exercise 6
## Use split to transform the following string into a list.
print("Ejercicio 6:")
names = 'harry,alex,susie,jared,gail,conner'
names_list = names.split(",")
print(f"Lista de nombres: {names_list}")
print("-----------------")

# Exercise 7
""" Exercise 7: Get the first word from your string using indexes. Use the upper function to
transform the letters into uppercase. Create a new string that takes the uppercase word and the
rest of the original string.
"""
print("Ejercicio 7:")
mi_indice = 11
first_word = string_var[:mi_indice]
print(first_word)
uppercase_first_word = first_word.upper()
print(uppercase_first_word)
new_string = uppercase_first_word + string_var[mi_indice:]
print(new_string)