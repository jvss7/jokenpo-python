#--- 1. Apresentação e Regras ---
print("------------------------------------------------------")
print("--- Jogo Pedra, Papel e Tesoura (2 Jogadores) ---")
print("------------------------------------------------------")
print("Bem-vindos! Cada jogador deve escolher uma das opções.")

opcoes_validas = ("pedra", "papel", "tesoura")
print(f"Opções válidas: {opcoes_validas}")
print("-" * 25) 

#--- 2. Coleta dos Dados de Entrada ---
jogada_jogador1_inicial = input("Jogador 1, digite sua jogada: ")
jogada_jogador2_inicial = input("Jogador 2, digite sua jogada: ")

#--- 3. Tratamento dos Dados de Entrada ---
jogada_jogador1 = jogada_jogador1_inicial.lower().strip()
jogada_jogador2 = jogada_jogador2_inicial.lower().strip()

print("-" * 25)
print(f"Jogador 1 escolheu: {jogada_jogador1}")
print(f"Jogador 2 escolheu: {jogada_jogador2}")
print("-" * 25)

#--- 4. Lógica do Jogo e Resultado ---
if jogada_jogador1 not in opcoes_validas or jogada_jogador2 not in opcoes_validas:
    print("DSA: Uma ou ambas as jogadas são inválidas! Por favor, use apenas 'pedra', 'papel' ou 'tesoura'.")

# Caso 1: Empate
elif jogada_jogador1 == jogada_jogador2:
    print("Resultado: É um empate!")

# Caso 2: Jogador 1 vence
elif (jogada_jogador1 == "pedra" and jogada_jogador2 == "tesoura") or \
     (jogada_jogador1 == "tesoura" and jogada_jogador2 == "papel") or \
     (jogada_jogador1 == "papel" and jogada_jogador2 == "pedra"):
    print("Resultado: Jogador 1 venceu! Parabéns!")

# Caso 3: Se não empatou e o Jogador 1 não venceu, então o Jogador 2 venceu.
else:
    print("Resultado: Jogador 2 venceu! Parabéns!")

print("\n--- Fim de Jogo ---")