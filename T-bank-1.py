#1
'''
# Чтение входных данных
s = input().strip()

# Проверка количества каждого символа в строке
if len(s) != 3 or \
   s.count('R') != 1 or \
   s.count('S') != 1 or \
   s.count('M') != 1:
    print("No")  # Строка некорректна
else:
    # Теперь проверим положение символов 'R' и 'M'
    pos_R = s.find('R')
    pos_M = s.find('M')
    
    if pos_R < pos_M:
        print("Yes")
    else:
        print("No")
'''
#2
'''
import sys
from bisect import bisect_right

def max_bouquet_cost(a):
    # Генерируем список степеней двойки от 2^0 до 2^60,
    # поскольку максимальное ограничение на a_i составляет 10^18 (~2^60)
    powers_of_two = [2**i for i in range(61)]
    
    # Функция нахождения максимального возможного результата
    def find_max_sum(budget):
        idx = bisect_right(powers_of_two, budget)-1
        
        # Перебираем возможные значения первой степени двойки
        while idx >= 2:
            p1 = powers_of_two[idx]
            
            # Остаточная сумма после выбора первой степени
            remaining_budget = budget - p1
            
            # Ищем следующую возможную степень двойки
            jdx = bisect_right(powers_of_two, remaining_budget)-1
            
            # Перебираем возможные значения второй степени двойки
            while jdx > 0 and jdx < idx:
                p2 = powers_of_two[jdx]
                
                # Оставшаяся сумма после выбора первых двух цветов
                second_remaining = remaining_budget - p2
                
                # Третья степень двойки должна быть меньше обеих выбранных
                kdx = bisect_right(powers_of_two, second_remaining)-1
                
                # Если третья степень возможна и отличается от первых двух
                if kdx >= 0 and kdx < jdx:
                    return p1 + p2 + powers_of_two[kdx]
                    
                jdx -= 1
            
            idx -= 1
        
        return -1
    
    result = []
    for amount in a:
        result.append(find_max_sum(amount))
    
    return result

# Чтение ввода
n = int(input())
budgets = [int(input()) for _ in range(n)]

# Расчет результатов
results = max_bouquet_cost(budgets)

# Вывод результатов
for res in results:
    print(res)
'''
#3
'''
def min_corrections_to_satisfy_schedule(n, m, arr):
    first = arr[0]
    second = arr[1]
    good_days_count = 0
    corrections_needed = 0
    
    # Проходим по каждому дню начиная с третьего
    for i in range(2, n):
        current_value = arr[i]
        
        # Определяем, является ли день хорошим
        if first <= current_value <= second:
            good_days_count += 1
        else:
            # Рассчитываем требуемые корректировки
            # Нижняя граница
            lower_bound_diff = abs(first - current_value)
            # Верхняя граница
            upper_bound_diff = abs(second - current_value)
            
            # Минимальное количество коррекций, чтобы сделать день хорошим
            diff = min(lower_bound_diff, upper_bound_diff)
            corrections_needed += diff
            good_days_count += 1
        
        # Если уже набрали достаточно хороших дней, прекращаем процесс
        if good_days_count >= m:
            break
    
    # Если хорошие дни достигнуты, возвращаем результат
    if good_days_count >= m:
        return corrections_needed
    else:
        # Если нельзя достичь нужных дней без нарушений ограничений
        return -1

# Чтение входных данных
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Вывод результата
print(min_corrections_to_satisfy_schedule(n, m, arr))
'''
#4
'''
from typing import List


def solve(n: int, x: int, y: int, z: int, seq: List[int]) -> int:
    def steps_to_make_divisible(a: int, divisor: int) -> int:
        remainder = a % divisor
        if remainder == 0:
            return 0
        else:
            return divisor - remainder

    best_costs = []
    for a in seq:
        # Определяем минимальное количество шагов для каждого числа x, y, z
        dx = steps_to_make_divisible(a, x)
        dy = steps_to_make_divisible(a, y)
        dz = steps_to_make_divisible(a, z)
        
        # Рассматриваем комбинирование элементов
        # Возможны случаи, когда один элемент покрывает сразу два числа
        best_costs.extend([
            dx,
            dy,
            dz,
            max(dx, dy),     # Покрытие сразу x и y
            max(dy, dz),     # Покрытие сразу y и z
            max(dx, dz)      # Покрытие сразу x и z
        ])
    
    # Сортируем затраты и выбираем три лучших варианта
    best_costs.sort()
    return sum(best_costs[:3])

# Чтение данных
n, x, y, z = map(int, input().split())
seq = list(map(int, input().split()))

result = solve(n, x, y, z, seq)
print(result)
'''
#5

#6
'''
from itertools import combinations

def is_collinear(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return ((y2 - y1)*(x3 - x1) - (y3 - y1)*(x2 - x1)) == 0

def max_happy_triples(points):
    n = len(points)
    happy_triples = []
    
    # Генерация всех возможных троек и проверка на коллинеарность
    for triple in combinations(range(n), 3):
        p1, p2, p3 = points[triple[0]], points[triple[1]], points[triple[2]]
        if not is_collinear(p1, p2, p3):
            happy_triples.append(set(triple))
    
    # Максимальное покрытие вершин (найти наибольшее количество несвязанных троек)
    used = set()  # Использованные точки
    result = 0
    
    while True:
        found = False
        for triple in happy_triples:
            if all(i not in used for i in triple):
                result += 1
                used.update(triple)
                found = True
                break
        if not found:
            break
    
    return result

if __name__ == "__main__":
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    print(max_happy_triples(points))
'''
#7
