class Vehicle:
    vehicles_created = 0
    
    def __init__(self, brand, max_speed):
        self.brand = brand
        self._max_speed = max_speed
        self._mileage = 0
        Vehicle.vehicles_created += 1
        
    def get_max_speed(self):
        return self._max_speed
    
    def get_mileage(self):
        return self._mileage
    
    def drive(self, distance):
        self._mileage += distance
        
    def display_info(self):
        print(f"Марка: {self.brand}")
        print(f"Макс. скорость: {self._max_speed} км/ч")
        print(f"Пробег: {self._mileage} км")
        

class Car(Vehicle):
    def __init__(self, brand, max_speed, engine_type):
        super().__init__(brand, max_speed)
        self.engine_type = engine_type
        
    def display_info(self):
        super().display_info()
        print(f'Тип двигателя: {self.engine_type}')
        

class Bicycle(Vehicle):
    def __init__(self, brand, max_speed, frame_material):
        super().__init__(brand, max_speed)
        self.frame_material = frame_material
        
    def display_info(self):
        super().display_info()
        print(f'Материал рамы: {self.frame_material}')


if __name__ == '__main__':
    # Пример использования
    car = Car("Toyota", 180, "Бензиновый")
    bike = Bicycle("Stels", 30, "Алюминий")
    
    print(f"Всего создано транспортных средств: {Vehicle.vehicles_created}\n")
    
    car.drive(150)
    car.display_info()
    
    print("\n" + "-"*20 + "\n")
    
    bike.drive(10)
    bike.display_info()