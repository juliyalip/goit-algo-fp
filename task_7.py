import random
import pandas as pd
import matplotlib.pyplot as plt

num_simulations = 1000000

# мінімально можлива сума 1 + 1, максимально можлива сума 6 + 6
sums_count = {i: 0 for i in range(2, 13)}

for _ in range(num_simulations):
    roll_sum = random.randint(1,6) + random.randint(1,6)
    sums_count[roll_sum] += 1

simulated_probabilities = {
    s: (count / num_simulations) * 100 for s, count in sums_count.items()
}

analytical_probabilities = {
    2: 2.78, 3: 5.56, 4:8.33, 5: 11.11, 6: 13.89, 7: 16.67, 
    8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

plt.bar(simulated_probabilities.keys(), simulated_probabilities.values())
plt.title("Ймовірність сум - Метод Монте-Карло")
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність %")
plt.xticks(range(2,13))
plt.grid(axis="y")
plt.tight_layout()
plt.show()

# Висновок у файлі README