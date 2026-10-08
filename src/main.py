from arte_cesaro import logo

print(logo)
print('¡Bienvenido al Descifrador Cesaro')

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cesar(texto_original, cantidad_shift, cifrado_descifrado):
    texto_modificado = ''

    if cifrado_descifrado == 'descifrar':
        cantidad_shift *= -1
    
    for letra in texto_original:
        if letra not in abecedario:
            texto_modificado += letra
        else:
            posición_shifteo = abecedario.index(letra) + cantidad_shift
            posición_shifteo %= len(abecedario)
            texto_modificado += abecedario[posición_shifteo]
    print(f'Aquí está tu mensaje {cifrado_descifrado}: {texto_modificado}')

de_nuevo = True

while de_nuevo:
    opcion = input('Escriba "cifrar" para encriptar, escriba "descifrar" para desencriptar. ').lower()
    text = input('Escriba su mensaje: ').lower()
    shift = int(input('Escriba cuántos espacios quiere recorrer: '))

    cesar(texto_original=text, cantidad_shift=shift, cifrado_descifrado=opcion)

    reinicio = input('Escriba "si" si quiere volver a ejecutar el programa. Caso contrario, escriba "no". ')

    if reinicio == 'no':
        de_nuevo = False
        print('¡¡Adiós!!')
