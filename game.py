import random


if __name__ == "__main__":
    while True:
        user_action = input("Choose 1 - Mage, 2 - Warrior, 3 - Rogue: ")
        possible_actions = ["Mage", "Warrior", "Rogue"]
        computer_action = random.choice(possible_actions)
        print(f"\nВы выбрали {user_action}, компьютер выбрал {computer_action}.\n")
        if user_action == computer_action:
            print(f"Оба пользователя выбрали {user_action}. Ничья!!")
        elif user_action == "Mage":
            if computer_action == "Warrior":
                print("Камень бьет ножницы! Вы победили!")
            else:
                print("Бумага оборачивает камень! Вы проиграли.")
        elif user_action == "Rogue":
            if computer_action == "Mage":
                print("Бумага оборачивает камень! Вы победили!")
            else:
                print("Ножницы режут бумагу! Вы проиграли.")
        elif user_action == "Warrior":
            if computer_action == "Rogue":
                print("Ножницы режут бумагу! Вы победили!")
            else:
                print("Камень бьет ножницы! Вы проиграли.")
        play_again = ""
        play_again = input("Сыграем еще? (д/н): ")
        if play_again.lower() != "д":
            print ()
            print ("Good Luck ")
            break







# Содержит блок на проверку имени модуля (main)
# внутри if блок try/except.
# try запускает функцию play()
# except обрабатывает два исключения: GameOver - выводит сообщение об ошибке, записывает результат в таблицу рекордов. KeyboardInterrupt - pass
# finally печатает "Good bye!"
# game.py - play():
#
# Ввод имени игрока
# Создание объекта player
# level = 1
# Создание объекта enemy
# в бесконечном цикле вызывает методы attack и defense объекта player
# при возникновении исключения EnemyDown повышает уровень игры, создает новый объект Enemy с новым уровнем, добавляет игроку +5 очков.
