import random

q = 4294967311  # Número primo
g = 142           # Raíz usada
M = 837976    # Palabra SOL de verificación en ascii

def generar_claves(q, g):
    clave_privada = random.randint(2, q - 2)  
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

clave_privada_ana, clave_publica_ana = generar_claves(q, g)
clave_privada_bob, clave_publica_bob = generar_claves(q, g)
clave_privada_anon, clave_publica_anon = generar_claves(q, g)

# Anonymous envía su clave pública a Ana y Bob, haciéndose pasar por el otro
clave_publica_ana_falsa = clave_publica_anon  # Anonymous envía su clave a Ana, haciéndose pasar por Bob
clave_publica_bob_falsa = clave_publica_anon  # Anonymous envía su clave a Bob, haciéndose pasar por Ana

# Cifrado de la clave K por Ana y Bob usando las claves públicas falsas
K = M  # Usamos la palabra de verificación como clave
c1_ana, c2_ana = cifrar_elgamal(q, g, clave_publica_bob_falsa, K)  # Ana cifra con la clave falsa de Bob
c1_bob, c2_bob = cifrar_elgamal(q, g, clave_publica_ana_falsa, K)  # Bob cifra con la clave falsa de Ana

# Descifrado de la clave K por Anonymous
K_descifrada_ana = descifrar_elgamal(q, clave_privada_anon, c1_ana, c2_ana)  # Anonymous descifra el mensaje de Ana
K_descifrada_bob = descifrar_elgamal(q, clave_privada_anon, c1_bob, c2_bob)  # Anonymous descifra el mensaje de Bob

# Mostrar resultados
print("=== Ataque de intermediario (Man-in-the-Middle) en ElGamal ===")
print(f"Parámetros públicos: q = {q}, g = {g}")
print(f"Clave privada de Ana: {clave_privada_ana}")
print(f"Clave pública de Ana: {clave_publica_ana}")
print(f"Clave privada de Bob: {clave_privada_bob}")
print(f"Clave pública de Bob: {clave_publica_bob}")
print(f"Clave privada de Anonymous: {clave_privada_anon}")
print(f"Clave pública de Anonymous: {clave_publica_anon}")
print(f"Clave K (palabra de verificación): {K}")
print(f"Cifrado de Ana (c1, c2): ({c1_ana}, {c2_ana})")
print(f"Cifrado de Bob (c1, c2): ({c1_bob}, {c2_bob})")
print(f"Clave K descifrada por Anonymous (desde Ana): {K_descifrada_ana}")
print(f"Clave K descifrada por Anonymous (desde Bob): {K_descifrada_bob}")