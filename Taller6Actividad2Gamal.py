from sympy import primitive_root
import random
from hashlib import sha256

q = 4294967311  
g = 142    #raiz usada       
M = 837976    #palabra SOL en ascii


def generar_claves(q, g):
    clave_privada = random.randint(2, q - 2)  # 1 < clave_privada < q-1
    clave_publica = pow(g, clave_privada, q)
    return clave_privada, clave_publica


def cifrar_elgamal(q, g, clave_publica, K):
    k = random.randint(2, q - 2)  
    c1 = pow(g, k, q)
    c2 = (K * pow(clave_publica, k, q)) % q
    return c1, c2


def descifrar_elgamal(q, clave_privada, c1, c2):
    K = (c2 * pow(c1, -clave_privada, q)) % q
    return K


def firmar(mensaje, clave_privada, q):
    hash_mensaje = int(sha256(str(mensaje).encode()).hexdigest(), 16)
    firma = pow(hash_mensaje, clave_privada, q)
    return firma


def verificar_firma(mensaje, firma, clave_publica, q):
    hash_mensaje = int(sha256(str(mensaje).encode()).hexdigest(), 16)
    return pow(firma, clave_publica, q) == hash_mensaje


clave_privada_ana, clave_publica_ana = generar_claves(q, g)
clave_privada_bob, clave_publica_bob = generar_claves(q, g)


K = M  
c1, c2 = cifrar_elgamal(q, g, clave_publica_bob, K)


firma_ana = firmar((c1, c2), clave_privada_ana, q)


if verificar_firma((c1, c2), firma_ana, clave_publica_ana, q):
    print("Firma válida. El mensaje es auténtico.")
    # Descifrar la clave K usando la clave privada de Bob
    K_descifrada = descifrar_elgamal(q, clave_privada_bob, c1, c2)
    print(f"Clave K descifrada por Bob: {K_descifrada}")
else:
    print("Firma inválida. Posible ataque de intermediario.")