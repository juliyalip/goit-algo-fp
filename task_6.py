items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
   total_cost=0
   total_calories = 0
   chosen_items =[]
   ratios = [(name, info["calories"] / info["cost"]) for name, info in items.items()]

   sorted_ratios = sorted(ratios, key=lambda x: x[1], reverse=True)

   for name, ratio in sorted_ratios:
      cost = items[name]["cost"]
      calories = items[name]["calories"]
      
      if total_cost + cost <=budget:
         chosen_items.append(name)
         total_cost +=cost
         total_calories += calories
   return chosen_items, total_calories, total_cost


def dynamic_programming(items, budget):
   item_list = list(items.items())
   n = len(item_list)

   dp = [[0] * (budget + 1) for _ in range(n+1)]

   for i in range(1, n+1):
      name, info = item_list[i-1]
      cost = info["cost"]
      calories = info["calories"]

      for w in range(budget +1):
         if cost <=w:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w-cost]+ calories)
         else:
            dp[i][w]=dp[i-1][w]

   w=budget
   chosen_items = []
   total_cost = 0
   for i in range(n, 0, -1):
      if dp[i][w] != dp[i-1][w]:
         name, info =item_list[i-1]
         chosen_items.append(name)
         total_cost += info["cost"]
         w -= info["cost"]
   total_calories = dp[n][budget]
   chosen_items.reverse()
   return chosen_items, total_calories, total_cost

if __name__=="__main__":
    items_list, all_calories, all_cost = greedy_algorithm(items, 150)
    items, calories, cost = dynamic_programming(items, 150)
    print("Жадібний алгоритм:")
    print(f"Вибрані продукти: {items_list}. Всього калорій {all_calories}. Сумма {all_cost}")
    print("Динамічний алгоритм: ")
    print(f"Вибрані продукти: {items}. Всього калорій {calories}. Сумма {cost}")
