#1
'''
def is_palindrome(s):
    return s == s[::-1]

def almost_palindrome(s):
    n = len(s)
    for i in range(n):
        # Формируем новую строку, удаляя i-й символ
        new_str = s[:i] + s[i+1:]
        if is_palindrome(new_str):
            return "YES"
    return "NO"

# Входные данные
string = input().strip()

# Запускаем проверку
print(almost_palindrome(string))
'''
#2
'''
import math

# Чтение количества веток
n = int(input())

# Запись расписания для каждой ветки
schedule = []
for _ in range(n):
    ti, di = map(int, input().split()) # первое прибытие и интервал между поездами
    schedule.append((ti, di))

# Количество запросов
m = int(input())

# Обработка запросов
for _ in range(m):
    i, qj = map(int, input().split()) # индекс ветки и момент времени
    ti, di = schedule[i-1]
    
    # Вычисление минимального k
    k = math.ceil((qj - ti) / di)
    
    # Время прибытия ближайшего поезда
    next_train_time = ti + k * di
    
    print(next_train_time)
'''
#3
'''
def max_unique_elements(arr):
    unique_numbers = set()
    
    for num in arr:
        while True:
            unique_numbers.add(num)
            if num == 1:
                break
            num = num // 2
            
    return len(unique_numbers)

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Получение максимального количества уникальных элементов
result = max_unique_elements(arr)
print(result)
'''
#4
'''
def count_arithmetic_subarrays(n, arr):
    result = 0
    
    # Проходим по каждому индексу как первому элементу потенциальной тройки
    for first in range(n - 2):
        second = first + 1
        third = first + 2
        
        while third < n:
            # Проверяем, является ли данная последовательность арифметической прогрессией
            if arr[second] - arr[first] == arr[third] - arr[second]:
                # Найден нужный подотрезок, считаем количество покрываемых подотрезков
                # Все подотрезки от текущего положения 'first' до конца массива включительно будут подходить
                result += (n - third)
            
            # Продолжаем движение вперед по массиву
            second += 1
            third += 1
    
    return result

# Чтение входных данных
n = int(input())
arr = list(map(int, input().split()))

# Поиск и вывод результата
print(count_arithmetic_subarrays(n, arr))
'''
#5
'''
from hea
pq import heappush, heappop

INF = int(1e18)

def minCostToBPS(n, a, b, s):
    s = list(s)
    n = len(s)
    
    # Массивы для подсчета необходимого количества перемещений и замещения
    extra_close = []  # Избыточные закрывающие скобки
    open_needed = []  # Необходимые дополнительные открывающие скобки
    
    ans = 0
    balance = 0
    for i in range(len(s)):
        if s[i] == '(':
            balance += 1
        elif s[i] == ')':
            balance -= 1
        
        # Если баланс становится отрицательным, фиксируем позицию,
        # которая нуждается в замене на '(', иначе запись закрывающей скобки позже станет дорогой
        if balance < 0:
            extra_close.append(i)
            balance += 1
            ans += b  # Прямая замена на '('
    
    # Сохраняем избыточные закрывающие скобки для возможного дальнейшего перераспределения
    balance = 0
    for i in reversed(range(len(s))):
        if s[i] == ')':
            balance += 1
        elif s[i] == '(':
            balance -= 1
        
        # Если баланс положителен, фиксируем позицию,
        # которая потенциально полезна для размещения дополнительной открывающей скобки
        if balance > 0:
            open_needed.append(i)
            balance -= 1
    
    # Оптимизация через обмены (используя очередь с приоритетом)
    exchange_heap = []
    while extra_close and open_needed:
        pos_close = extra_close.pop()  # Позиция избыточной закрывающей скобки
        pos_open = open_needed.pop()   # Позиция необходимой открывающей скобки
        
        # Проверяем эффективность обмена
        if pos_close < pos_open:
            # Возможность произвести обмен, так как индекс позиции закрытия меньше индекса открытия
            ans -= b  # Уменьшаем общую стоимость на сумму предыдущей замены
            ans += a  # Добавляем стоимость обмена
    
    # Все оставшиеся замены выполняются напрямую
    ans += len(extra_close) * b
    ans += len(open_needed) * b
    
    return ans

# Чтение входных данных
n, a, b = map(int, input().split())
s = input()

print(minCostToBPS(n, a, b, s))
'''
#6
'''
def max_difference_sum(n, heights):
    # Сортируем массив высот
    heights.sort()
    
    # Общая сумма различий
    total_diff = 0
    
    # Берём первую и последнюю точку массива, формируя пары
    left = 0
    right = n - 1
    
    while left < right:
        diff = abs(heights[left] - heights[right])
        total_diff += diff
        left += 1
        right -= 1
    
    return total_diff

# Чтение входных данных
n = int(input())
heights = list(map(int, input().split()))

# Получение оптимального результата
result = max_difference_sum(n, heights)

# Вывод результата
print(result)
'''
#7
'''
from fractions import Fraction
from math import gcd
from functools import reduce
MOD = 998244353

def extended_gcd(a, b):
    """Расширенный алгоритм Евклида"""
    if a == 0:
        return b, 0, 1
    g, y, x = extended_gcd(b%a,a)
    return g, x - (b//a) * y, y

def modinv(a, m):
    """Модульное обратное по модулю"""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError('modular inverse does not exist')
    else:
        return x % m

def find_all_sequences(n, a):
    """Ищем все прекрасные последовательности и возвращаем сумму интересностей."""
    sequences = set()
    
    # Генерация последовательности
    def generate_sequence(index, seq):
        if index == n:
            # Все элементы сформированы, проверяем НОД
            common_gcd = reduce(gcd, seq)
            if common_gcd == 1:
                interest = 1
                for el in seq:
                    interest = (interest * el) % MOD
                sequences.add(interest)
            return
        
        # Генерируем следующий элемент, используя предыдущий
        prev_element = seq[index-1]
        next_elements = []
        # Пробуем разные способы поделить текущее число
        target_product = a[index-1]
        for numerator in range(1, target_product+1):
            denominator = target_product // numerator
            if numerator * denominator == target_product:
                next_elements.append(denominator)
        
        for next_el in next_elements:
            new_seq = seq[:index]+[next_el]
            generate_sequence(index+1, new_seq)
    
    # Начало генерации
    start_elements = [1]
    generate_sequence(1, start_elements)
    
    total_interest = sum(sequences) % MOD
    return total_interest

# Основной блок программы
if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    result = find_all_sequences(n, a)
    print(result)
'''
