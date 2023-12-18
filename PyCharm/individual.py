def reverse_print_sequence():
    number = int(input("Введите число (для завершения введите 0): "))

    if number != 0:
        # Рекурсивный вызов функции для ввода следующего числа
        reverse_print_sequence()

        # Печать числа в обратном порядке
        print(number)

# Вызов функции для старта программы
reverse_print_sequence()
