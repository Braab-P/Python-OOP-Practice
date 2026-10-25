class Character:
    def __init__(self, name, damage):
        self.name = name
        self._health = 100
        self._damage = damage
    
    def attack(self, target):
        if hasattr(target, 'take_damage'):
            target.take_damage(self._damage)
    
    def take_damage(self, amount):
        self._health -= amount
    
    def get_status(self):
        return f"Имя: {self.name}, Здоровье: {self._health}"


class Warrior(Character):
    def __init__(self, name, damage, armor):
        super().__init__(name, damage)
        self.armor = armor
    
    def take_damage(self, amount):
        actual_damage = max(0, amount - self.armor)
        self._health -= actual_damage


class Mage(Character):
    def __init__(self, name, damage, mana):
        super().__init__(name, damage)
        self.mana = mana
    
    def attack(self, target):
        if self.mana >= 10:
            self.mana -= 10
            super().attack(target)
        else:
            print(f"{self.name} не хватает маны для атаки!")

if __name__ == '__main__':
    # Пример использования
    warrior = Warrior("Рыцарь", damage=20, armor=5)
    mage = Mage("Маг", damage=30, mana=20)
    
    print(warrior.get_status())
    print(mage.get_status())
    
    mage.attack(warrior)
    print("После атаки мага:", warrior.get_status())