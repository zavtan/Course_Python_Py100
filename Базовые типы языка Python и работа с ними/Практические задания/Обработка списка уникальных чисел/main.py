list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
numbers = set(list_)
unique_numbers = numbers
sum_of_numbers = sum(unique_numbers)
count_of_numbers = len(unique_numbers)
average_of_numbers = float(sum_of_numbers / count_of_numbers)
average_of_numbers = round(average_of_numbers, 5)
# TODO найти сумму, количество и среднее арифметическое уникальных чисел

print("Сумма уникальных чисел:", sum_of_numbers, end=" ")
print("Количество уникальных чисел:", count_of_numbers,end=" ")
print("Среднее арифметическое уникальных чисел:", average_of_numbers)
describe = {1: 'Сумма уникальных чисел:, -6', 2: 'Количество уникальных чисел:, 14',
            3: 'Среднее арифметическое уникальных чисел: -0.42857'}

print(describe)
