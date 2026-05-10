import random
import string

def generar_contrasena(longitud, mayusculas=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase

    if mayusculas:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def main():
    print("=== Generador de Contraseñas Seguras ===")

    try:
        longitud = int(input("Longitud de la contraseña: "))
    except ValueError:
        print("Por favor ingresa un número válido.")
        return

    incluir_mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    incluir_nums = input("¿Incluir números? (s/n): ").lower() == "s"
    incluir_simb = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    contrasena = generar_contrasena(longitud, incluir_mayus, incluir_nums, incluir_simb)
    print("\nTu contraseña generada es:")
    print(contrasena)

if __name__ == "__main__":
    main()
