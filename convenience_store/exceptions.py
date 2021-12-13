class NotProductCart(Exception):
    def __init__(self, obj):
        self.obj = obj

    def __str__(self):
        return f"{self.obj} is not an instance of ProductCart class"