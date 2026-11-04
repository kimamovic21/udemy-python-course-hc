Vehicle Rental System

You are designing a Vehicle Rental System that tracks different types of vehicles and their components.


Tasks:

Create a class Engine with an attribute horsepower and a method get_engine_info() that returns "150 HP Engine".

Create class Vehicle

Attributes: brand, model, and an Engine object.

Class attribute: total_vehicles (increased by 1 each time a new vehicle is created).

Add a method get_details() returning brand, model, and engine info.

Add @staticmethod get_vehicle_type() → returns "Generic Vehicle".

Add @classmethod get_total_vehicles() → returns total number of vehicles.

Add a @property rental_price and corresponding setter that ensures the value is non-negative.-

Create a Car class that inherits from Vehicle.

Add an attribute seats.

Override the get_details() method and use super() to include base details and append "Seats: X".