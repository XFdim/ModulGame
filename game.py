import random


if __name__ == "__main__":
    while True:
        def fight(attack, defence):
            if attack == defence:
                return 0
            if attack == 1 and defence == 2:
                return 1
            if attack == 1 and defence == 3:
                return -1
            if attack == 2 and defence == 3:
                return 1
            if attack == 2 and defence == 1:
                return -1
            if attack == 3 and defence == 1:
                return 1
            if attack == 3 and defence == 2:
                return -1

        def attack(attack_choise: int, enemy: Enemy):
            defence = enemy.select_defence
            return fight(attack_choise, defence)

#Warrior = 1
#Rogue = 2
#Mage = 3








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
