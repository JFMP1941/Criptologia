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
       return (
        "Clave privada de Ana: " + str(clave_privada_ana) + "\n"
        "Clave pública de Ana: " + str(clave_publica_ana) + "\n"
        "Clave privada de Bob: " + str(clave_privada_bob) + "\n"
        "Clave pública de Bob: " + str(clave_publica_bob) + "\n"
        "Clave compartida: " + str(clave_compartida_ana)
)
        
    else:
        return "Error: Las claves compartidas no coinciden."

q = 65537  
a = 3   #raiz usada
resultado = generar_claves_diffie_hellman(q, a)
print(resultado)