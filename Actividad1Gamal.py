import random

q = 4294967311  
g = 142    #raiz usada       
M = 837976    #palabra SOL en ascii


def generar_claves(q, g, nombre ):
    clave_privada = random.randint(2, q - 2)  
    
    clave_publica = pow(g, clave_privada, q)
    
    
    return clave_privada, clave_publica

def cifrar_elgamal(q, g, clave_publica, K):
    k = random.randint(2, q - 2)  
    print(f" valor de k: {k}")
    c1 = pow(g, k, q)
    print(f" valor de c1: {c1}")
    c2 = (K * pow(clave_publica, k, q)) % q
    print(f" valor de c2: {c2}")
    return c1, c2

def descifrar_elgamal(q, clave_privada, c1, c2):
    K = (c2 * pow(c1, -clave_privada, q)) % q
    return K
clave_privada_ana, clave_publica_ana = generar_claves(q, g, "ana")
clave_privada_bob, clave_publica_bob = generar_claves(q, g, "bob")
K = M  
c1, c2 = cifrar_elgamal(q, g, clave_publica_bob, K)
K_descifrada = descifrar_elgamal(q, clave_privada_bob, c1, c2)

print("-- Resultados finales----")
print(f"Parámetros públicos: q = {q}, g = {g}")
print(f"Clave privada de Ana: {clave_privada_ana}")
print(f"Clave pública de Ana: {clave_publica_ana}")
print(f"Clave privada de Bob: {clave_privada_bob}")
print(f"Clave pública de Bob: {clave_publica_bob}")
print(f"Clave K (palabra de verificación): {K}")
print(f"Cifrado (c1, c2): ({c1}, {c2})")
print(f"Clave K descifrada por Bob: {K_descifrada}")