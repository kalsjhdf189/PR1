class Monster:  # Объявление класса "Монстр"
    def __init__(self, health, power): # Конструктор
        self.set_health(health) # Здоровье монстра
        self.set_power(power) # Сила монстра
        self.ogr() # Ограничение, чтобы сумма здоровье и силы у монстра не было больше 150

    def set_health(self, health): # Определение здоровья
        if health < 1: # Если здоровье меньше 1
            self.health = 1 # Значит оно будет равняться 1
        elif health > 100: # Иначе если здоровье больше 100
            self.health = 100 # Значит оно будет равняться 100
        else:
            self.health = health # Здоровье будет равняться здоровью

    def set_power(self, power): # Определение силы
        if power < 1:  # Если сила меньше 1
            self.power = 1  # Значит она будет равняться 1
        elif power > 100:  # Иначе если сила больше 100
            self.power = 100  # Значит она будет равняться 100
        else:  # Иначе
            self.power = power  # Сила будет равняться силе
    def ogr(self): # Определение ограничения
        if self.power + self.health < 2:  # Если сумма силы и здоровья будет меньше 2
            self.health = 1  # Значит здоровье будет равно 1
            self.power = 1  # Значит сила будет равна 1
        elif self.power + self.health > 150:  # Иначе если сумма силы и здоровья будет больше 150
            sr = self.power + self.health - 150  # Значит присваивамем переменной "sr" разность суммы здоровья и силы и 150
            if self.health > self.power:  # Если здоровье больше силы
                self.health -= sr  # Значит здоровье отнимаем от переменной "sr"
            else:  # Иначе
                self.power -= sr  # Силу отнимаем от переменной "sr"

    def show(self):
        print(f"Здоровье монстра: {monster.health}, Сила монстра: {monster.power}")

class Demon:  #Объявление класса "Демон"
    def __init__(self, intellect): # Конструктор
        self.set_intellect(intellect) # Разум монстра

    def set_intellect(self, intellect): # Определение разума
        if intellect < 1: #Если разум меньше 1
            self.intellect = 1 #Значит разум будет равен 1
        elif intellect > 100: #Если разум больше 100
            self.intellect = 100 #Значит разум будет равен 100
        else: #Иначе
            self.intellect = intellect #Разум будет равен разуму

    def show(self):
        print(f"Разум демона: {demon.intellect}")

monster = Monster(
    health=int(input("Введите здоровье монстра: ")), # Запрос на ввод здоровья Монстра
    power=int(input("Введите силу монстра: ")) # Запрос на ввод силы Монстра
)
demon = Demon(
    intellect = int(input("Разум демона: ")) # Запрос на ввод разума Демона
)

sum = monster.health + monster.power + demon.intellect # Сумма здоровья, силы Монстра и разума Демона

if sum > 200: # Если суммарное значение всех свойств больше 200
    sr = sum - 200 # Значит присваиваем переменной "sr" разность суммарного значиня всех свойств от 200
    if monster.power >= sr: # Если сила монстра больше или равно переменной "sr"
        monster.power -= sr # Значит силу монстра отнимаем от переменной "sr"
    elif monster.health >= sr: # Иначе если здоровье монтсра больше или равно переменной "sr"
        monster.health -= sr # Значит здорье монстра отнимаем от переменной "sr"
    else:
        demon.intellect -= sr # Иначе разум демона отнимаем от переменной "sr"

demon.show()
monster.show()
print(f"Суммарное значение всех свойств: {sum}")
