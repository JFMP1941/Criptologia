import random

def generar_claves_diffie_hellman(q, alpha):
    # Generar claves privadas aleatorias
    clave_privada_ana = random.randint(2, q - 2)  # 1 < clave_privada < q-1
    clave_privada_bob = random.randint(2, q - 2)

    # clave_publica = alpha^clave_privada mod q
    clave_publica_ana = pow(alpha, clave_privada_ana, q)
    clave_publica_bob = pow(alpha, clave_privada_bob, q)

    # clave compartida
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
print(resultado)