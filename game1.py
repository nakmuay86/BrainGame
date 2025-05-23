import math
import random

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def main():
    print("Добро пожаловать Brain Games!")
    name = input("Укажите свой nickname! ->   ")
    print(f"Hello, {name}!")
    print("Найдите наименьшее общее кратное заданных чисел. ")
    while True:
        num1, num2 = generate_question()
        print(f"Вопрос: {num1} {num2}")
        attempts = 3  # количество попыток
        for attempt in range(1, attempts + 1):
            answer = input("Ваш ответ: ").strip()
            if not answer.isdigit():
                print(f"'{answer}' не правильный ответ! ;(. Правильный ответ: '{lcm(num1, num2)}'.")
                print(f"Давай по новой {name}!\n")
                return  # завершение игры после неправильного ввода
            user_answer = int(answer)
            correct_answer = lcm(num1, num2)
            if user_answer == correct_answer:
                print("Правильно!\n")
                break  
            else:
                remaining_attempts = attempts - attempt
                if remaining_attempts > 0: # Фильтр на цифру 0
                    print(f"'{user_answer}' Не правильный ответ ;(. Попробуй снова.")
                else:
                    print(f"'{user_answer}' Не правильный ответ ;(. Правильный ответ  '{correct_answer}'.")
                    print(f"Попробуй снова, {name}!\n")
                    return  # завершение игры после исчерпания попыток

if __name__ == "__main__":
    main()