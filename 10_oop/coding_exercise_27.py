class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower = horsepower

    def get_engine_info(self) -> str:
        return f"{self.horsepower} HP Engine"


class Vehicle:
    total_vehicles = 0

    def __init__(self, brand: str, model: str, engine: Engine) -> None:
        self.brand = brand
        self.model = model
        self.engine = engine
        self._rental_price = 0.0
        Vehicle.total_vehicles += 1

    def get_details(self) -> str:
        return f"{self.brand} {self.model} with {self.engine.get_engine_info()}"

    @staticmethod
    def get_vehicle_type() -> str:
        return "Generic Vehicle"

    @classmethod
    def get_total_vehicles(cls) -> int:
        return cls.total_vehicles

    @property
    def rental_price(self) -> float:
        return self._rental_price

    @rental_price.setter
    def rental_price(self, price: float) -> None:
        if price < 0:
            raise ValueError("Rental price cannot be negative")
        self._rental_price = price


class Car(Vehicle):
    def __init__(self, brand: str, model: str, engine: Engine, seats: int) -> None:
        super().__init__(brand, model, engine)
        self.seats = seats

    def get_details(self) -> str:
        return f"{super().get_details()}, Seats: {self.seats}"
