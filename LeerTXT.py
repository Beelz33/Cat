with open('Gato.txt', 'r') as archivo:
    contenido = archivo.read()
print(contenido)

num_letras = sum(c.isalpha() for c in contenido)  #Cuenta las letras
num_espacios = sum(c.isspace() for c in contenido)  #Cuenta los espacios
resumen_contenido = f"Cantidad de letras: {num_letras}\nCantidad de espacios: {num_espacios}" #Crea el contenido resumen

with open('Resumen.txt', 'w') as resumen_archivo: #Escribe el resumen en TXT
    resumen_archivo.write(resumen_contenido)