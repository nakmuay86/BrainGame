import random

def generate_geometric_progression(length):
    # Генератор чисел
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    progression = [start * (ratio ** i) for i in range(length)]
    return progression

def play_game():
    print("Добро пожаловать в Brain Games!")
    name = input("Укажите свой nickname! ->   ")
    print(f"Hello, {name}!")

    length = random.randint(5, 10)  # Length of the progression
    progression = generate_geometric_progression(length)

    # Для того, чтобы спрятать определённый индекс для разгадки
    hidden_index = random.randint(0, length - 1)
    hidden_value = progression[hidden_index]
    progression[hidden_index] = '..'  # .. - Каким символом мы прячем индекс

    # Display the question
    print("Какое число было спрятано?")
    print("Вопрос:", ' '.join(map(str, progression)))

    # Get the user's answer
    user_answer = input("Твой ответ: ")

    # Проверка на корректность ответа
    if user_answer.isdigit() and int(user_answer) == hidden_value:
        print("Правильно!")
    else:
        print(f"'{user_answer}' это не правильный ответ  ;(. Правильный ответ: '{hidden_value}'.")
        print(f"Попробуй снова, {name}!")

if __name__ == "__main__":
    play_game()
