import heapq
import random


def heap_sort(iterable, descending=False):
    # Визначаємо, який знак використовувати залежно від порядку сортування
    sign = -1 if descending else 1

    # Створюємо купу, використовуючи заданий порядок сортування
    h = [sign * el for el in iterable]
    heapq.heapify(h)
    # Витягуємо елементи, відновлюємо їхні оригінальні значення (якщо потрібно) і формуємо відсортований масив
    return [sign * heapq.heappop(h) for _ in range(len(h))]


def main():
    total_cost= 0
    sorted_cables = heap_sort(cables, descending=True)
    print(f"Відсортований список мережевих кабелів:\n {sorted_cables}\n")
    for i in range(len(sorted_cables) - 1):
        print(f"Крок {i + 1}: ")
        print(f"З'єднання: {' та '.join(str(el) for el in heapq.nsmallest(2, sorted_cables))}")

        sorted_cables = heap_sort(sorted_cables, descending=False)
        min_two_cables = heapq.heappop(sorted_cables) + heapq.heappop(sorted_cables)
        print(f"Поточні витрати на з'єднання: {min_two_cables}\n")
        total_cost += min_two_cables
        heapq.heappush(sorted_cables, min_two_cables)

    print(f"Загальні витрати на з'єднання: {total_cost}")


if __name__ == "__main__":
    cables = [random.randint(1, 100) for _ in range(10)]
    print(f"Список мережевих кабелів, які потрібно з'єднати:\n {cables}\n")
    main()
