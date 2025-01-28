import random

def generar_claves_diffie_hellman(q, alpha, clave_privada):
    clave_publica = pow(alpha, clave_privada, q)
    return clave_publica

def calcular_clave_compartida(clave_publica_otro, clave_privada, q):
    clave_compartida = pow(clave_publica_otro, clave_privada, q)
    return clave_compartida

q = 65537  
alpha = 3 
clave_privada_ana = random.randint(2, q - 2)
clave_privada_bob = random.randint(2, q - 2)
clave_privada_anonymous = random.randint(2, q - 2)
clave_publica_ana = generar_claves_diffie_hellman(q, alpha, clave_privada_ana)
clave_publica_bob = generar_claves_diffie_hellman(q, alpha, clave_privada_bob)
clave_publica_anonymous = generar_claves_diffie_hellman(q, alpha, clave_privada_anonymous)
clave_publica_ana_falsa = clave_publica_anonymous 
clave_publica_bob_falsa = clave_publica_anonymous 
clave_compartida_ana = calcular_clave_compartida(clave_publica_ana_falsa, clave_privada_ana, q)
clave_compartida_bob = calcular_clave_compartida(clave_publica_bob_falsa, clave_privada_bob, q)
clave_compartida_anonymous_ana = calcular_clave_compartida(clave_publica_ana, clave_privada_anonymous, q)
clave_compartida_anonymous_bob = calcular_clave_compartida(clave_publica_bob, clave_privada_anonymous, q)


print("-----------------Ataque Man-in-the-Middle--------------------------------")
print(f"Parámetros públicos: q = {q}, a = {alpha}")
print(f"Clave privada de Ana: {clave_privada_ana}")
print(f"Clave pública de Ana: {clave_publica_ana}")
print(f"Clave privada de Bob: {clave_privada_bob}")
print(f"Clave pública de Bob: {clave_publica_bob}")
print(f"Clave privada de Anonymous: {clave_privada_anonymous}")
print(f"Clave pública de Anonymous: {clave_publica_anonymous}")
print(f"Clave compartida de Ana con Anonymous: {clave_compartida_ana}")
print(f"Clave compartida de Bob con Anonymous: {clave_compartida_bob}")
print(f"Clave compartida de Anonymous con Ana: {clave_compartida_anonymous_ana}")
print(f"Clave compartida de Anonymous con Bob: {clave_compartida_anonymous_bob}")