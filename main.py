import math
import random

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def generate_question():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    return num1, num2

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")
    while True:
        num1, num2 = generate_question()
        print(f"Question: {num1} {num2}")
        attempts = 3  # количество попыток
        for attempt in range(1, attempts + 1):
            answer = input("Your answer: ").strip()
            if not answer.isdigit():
                print(f"'{answer}' is wrong answer ;(. Correct answer was '{lcm(num1, num2)}'.")
                print(f"Let's try again, {name}!\n")
                return  # завершение игры после неправильного ввода
            user_answer = int(answer)
            correct_answer = lcm(num1, num2)
            if user_answer == correct_answer:
                print("Correct!\n")
                break  
            else:
                remaining_attempts = attempts - attempt
                if remaining_attempts > 0:
                    print(f"'{user_answer}' is wrong answer ;(. Try again.")
                else:
                    print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
                    print(f"Let's try again, {name}!\n")
                    return  # завершение игры после исчерпания попыток

if __name__ == "__main__":
    main()