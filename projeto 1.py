import numpy as np

def simulate_dice_roll():
    dice1 = np.random.randint(1, 7)
    dice2 = np.random.randint(1, 7)
    return dice1 + dice2

num_simulations = 1000
results = np.array([simulate_dice_roll() for _ in range(num_simulations)])

average_result = np.mean(results)
min_result = np.min(results)
max_result = np.max(results)

occurrences = np.bincount(results)[2:]

print("média dos resultados:", average_result)
print("lançamento máximo:", max_result)
print("lançamento mínimo:", min_result)

for i, count in enumerate(occurrences, start=2):
    print("número de vezes que", i, "ocorreu:", count)

expected_occurrences = num_simulations / 11

print("\nTeste de Hipótese:")
if np.allclose(occurrences, expected_occurrences, atol=50):
    print("os resultados coincidem com a suposição de um jogo justo.")
else:
    print("os resultados não coincidem com a suposição de um jogo justo.")