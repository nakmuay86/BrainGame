import os
import sys
import importlib

def main():
    games_dir = os.path.join(os.path.dirname(__file__), 'games')
    sys.path.insert(0, games_dir)

    while True:
        command = input('Введите команду ("braingame" для запуска игр, "exit" для выхода): ').strip().lower()
        
        if command == 'exit':
            print("Выход из программы. До свидания!")
            break
        elif command == 'braingame':
            print("Выберите игру:\n1) nok-nod\n2) find hidden number")
            choice = input("Введите номер игры (1 или 2): ").strip()
            if choice == '1':
                try:
                    nok_nod = importlib.import_module('nok_nod')
                    if hasattr(nok_nod, 'main'):
                        nok_nod.main()
                    else:
                        print("Модуль 'nok_nod' не содержит функцию main().")
                except ModuleNotFoundError:
                    print("Модуль 'nok_nod.py' не найден в папке 'games'.")
            elif choice == '2':
                try:
                    hidden_number = importlib.import_module('hidden_number')
                    if hasattr(hidden_number, 'play_game'):
                        hidden_number.play_game()
                    else:
                        print("Модуль 'hidden_number' не содержит функцию play_game().")
                except ModuleNotFoundError:
                    print("Модуль 'hidden_number.py' не найден в папке 'games'.")
            else:
                print("Некорректный выбор. Пожалуйста, введите 1 или 2.")
        else:
            print("Команда не распознана. Попробуйте снова.")

if __name__ == "__main__":
    main()