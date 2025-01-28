import random

def generar_claves_diffie_hellman(q, alpha, clave_privada):
    # Calcular clave pública usando la fórmula: clave_publica = alpha^clave_privada mod q
    clave_publica = pow(alpha, clave_privada, q)
    return clave_publica

def calcular_clave_compartida(clave_publica_otro, clave_privada, q):
    # Calcular clave compartida usando la fórmula: clave_compartida = clave_publica_otro^clave_privada mod q
    clave_compartida = pow(clave_publica_otro, clave_privada, q)
    return clave_compartida

# Parámetros
q = 65537  # Número primo
alpha = 3  # Raíz primitiva

# Generar claves privadas
clave_privada_ana = random.randint(2, q - 2)
clave_privada_bob = random.randint(2, q - 2)
clave_privada_anonymous = random.randint(2, q - 2)

# Calcular claves públicas
clave_publica_ana = generar_claves_diffie_hellman(q, alpha, clave_privada_ana)
clave_publica_bob = generar_claves_diffie_hellman(q, alpha, clave_privada_bob)
clave_publica_anonymous = generar_claves_diffie_hellman(q, alpha, clave_privada_anonymous)

# Interceptación de claves públicas por Anonymous
# Anonymous envía su clave pública a Ana y Bob, haciéndose pasar por el otro
clave_publica_ana_falsa = clave_publica_anonymous  # Anonymous envía su clave a Ana, haciéndose pasar por Bob
clave_publica_bob_falsa = clave_publica_anonymous  # Anonymous envía su clave a Bob, haciéndose pasar por Ana

# Cálculo de claves compartidas
# Ana cree que está compartiendo una clave con Bob, pero en realidad es con Anonymous
clave_compartida_ana = calcular_clave_compartida(clave_publica_ana_falsa, clave_privada_ana, q)

# Bob cree que está compartiendo una clave con Ana, pero en realidad es con Anonymous
clave_compartida_bob = calcular_clave_compartida(clave_publica_bob_falsa, clave_privada_bob, q)

# Anonymous calcula las claves compartidas con Ana y Bob
clave_compartida_anonymous_ana = calcular_clave_compartida(clave_publica_ana, clave_privada_anonymous, q)
clave_compartida_anonymous_bob = calcular_clave_compartida(clave_publica_bob, clave_privada_anonymous, q)

# Mostrar resultados
print("=== Ataque de intermediario (Man-in-the-Middle) ===")
print(f"Parámetros públicos: q = {q}, α = {alpha}")
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