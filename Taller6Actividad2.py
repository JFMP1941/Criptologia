import random

def generar_claves_diffie_hellman(q, alpha):
    # Generar claves privadas aleatorias
    clave_privada_ana = random.randint(2, q - 2)  # 1 < clave_privada < q-1
    clave_privada_bob = random.randint(2, q - 2)

    #clave_publica = alpha^clave_privada mod q
    clave_publica_ana = pow(alpha, clave_privada_ana, q)
    clave_publica_bob = pow(alpha, clave_privada_bob, q)

    # Calcular la clave compartida
    clave_compartida_ana = pow(clave_publica_bob, clave_privada_ana, q)
    clave_compartida_bob = pow(clave_publica_ana, clave_privada_bob, q)

    # Verificacion de claves
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

q = 65537  
alpha = 3  
resultado = generar_claves_diffie_hellman(q, alpha)
print(f"Parámetros públicos: q = {q}, a = {alpha}")
print(f"Clave privada de Ana: {resultado['Clave privada de Ana']}")
print(f"Clave pública de Ana: {resultado['Clave pública de Ana']}")
print(f"Clave privada de Bob: {resultado['Clave privada de Bob']}")
print(f"Clave pública de Bob: {resultado['Clave pública de Bob']}")
print(f"Clave compartida calculada por Ana: {resultado['Clave compartida']}")
print(f"Clave compartida calculada por Bob: {resultado['Clave compartida']}")