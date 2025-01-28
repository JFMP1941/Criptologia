import random

def generar_claves_diffie_hellman(q, alpha):
    # Generar claves privadas aleatorias para Ana y Bob
    clave_privada_ana = random.randint(2, q - 2)  # 1 < clave_privada < q-1
    clave_privada_bob = random.randint(2, q - 2)

    # Calcular claves públicas usando la fórmula: clave_publica = alpha^clave_privada mod q
    clave_publica_ana = pow(alpha, clave_privada_ana, q)
    clave_publica_bob = pow(alpha, clave_privada_bob, q)

    # Calcular la clave compartida
    clave_compartida_ana = pow(clave_publica_bob, clave_privada_ana, q)
    clave_compartida_bob = pow(clave_publica_ana, clave_privada_bob, q)

    # Verificar que ambas claves compartidas son iguales
    if clave_compartida_ana == clave_compartida_bob:
        return {
            "Clave privada de Ana": clave_privada_ana,
            "Clave pública de Ana": clave_publica_ana,
            "Clave privada de Bob": clave_privada_bob,
            "Clave pública de Bob": clave_publica_bob,
            "Clave compartida": clave_compartida_ana
        }
    else:
        return "Error: Las claves compartidas no coinciden."

# Parámetros
q = 65537  # Número primo
alpha = 3  # Raíz primitiva (puedes usar cualquiera de las 10 mencionadas)

# Ejecutar la función
resultado = generar_claves_diffie_hellman(q, alpha)
print(resultado)