import models

class GameOver(Exception):
    def __init__(self, obj):
        self.obj = obj


class EnemyDown(Exception):
    def __init__(self, obj):
        self.obj = obj


#Содержит класс GameOver - унаследованный от Exception. В классе должен быть реализован механизм сохранения финального счета игрока по завершению игры в файл scores.txt
#Содержить класс EnemyDown - унаследованный от Exception. Функционал не обязателен.
#Создать механизм сохранения только 10 лучших счетов игроков. Можно реализовать через класс Score.