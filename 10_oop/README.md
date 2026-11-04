# 10 — Object-Oriented Programming

This section introduces object-oriented programming (OOP): classes, objects, attributes, instance, static, and class methods, inheritance, and composition. The examples cover initialisation with `__init__`, reusing a base class through `super()`, method resolution order (MRO), and properties with validation. Exercises 26–27 apply these concepts to a device tracker and a vehicle rental system.

**Status: in progress.** This checkpoint covers numbered examples 01–11 and coding exercises 26–27.

## Learning order

1. Start with [01_simple_class.py](01_simple_class.py) to define classes, create an object, and inspect its type.
2. Continue with [02_namespace.py](02_namespace.py) to explore namespaces and the difference between class and instance attributes.
3. Continue with [03_attribute_shadowing.py](03_attribute_shadowing.py) to override an attribute on one instance and observe what happens when it is deleted.
4. Continue with [04_self_args.py](04_self_args.py) to define an instance method and understand how `self` receives the object.
5. Continue with [05_init_objects.py](05_init_objects.py) to initialise each object with its own order details using `__init__`.
6. Read the [original challenge 26](CODING_EXERCISE_26.md), then explore [coding_exercise_26.py](coding_exercise_26.py) to track device status and practise attribute shadowing.
7. Continue with [06_inheritance_composition.py](06_inheritance_composition.py) to combine inherited behaviour with a shop that contains a separate chai object.
8. Continue with [07_base_class.py](07_base_class.py) to reuse base class initialisation with `super()` and add an attribute in a subclass.
9. Continue with [08_mro.py](08_mro.py) to inspect the class lookup order when a class inherits from two parents.
10. Continue with [09_static_methods.py](09_static_methods.py) to group a text-cleaning helper in a class and call it with `@staticmethod`.
11. Continue with [10_classmethod.py](10_classmethod.py) to create orders from dictionaries and strings using `@classmethod`.
12. Continue with [11_property_decorators.py](11_property_decorators.py) to read an attribute through a property and validate assignments through its setter.
13. Read the [original challenge 27](CODING_EXERCISE_27.md), then explore [coding_exercise_27.py](coding_exercise_27.py) to combine composition, inheritance, methods, and properties in a vehicle rental system.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_simple_class.py](01_simple_class.py) | Defining empty classes, creating an instance, and comparing its type with two classes. |
| [02_namespace.py](02_namespace.py) | Reading class attributes through an object, adding attributes, and giving an instance its own value. |
| [03_attribute_shadowing.py](03_attribute_shadowing.py) | Shadowing a class attribute on an instance, then deleting instance attributes with `del`. |
| [04_self_args.py](04_self_args.py) | Calling an instance method through an object or its class and reading attributes with `self`. |
| [05_init_objects.py](05_init_objects.py) | Initialising separate orders with `__init__` and returning their descriptions through `summary()`. |
| [06_inheritance_composition.py](06_inheritance_composition.py) | Inheriting chai and shop behaviour, and selecting the class used to create a shop's chai object. |
| [07_base_class.py](07_base_class.py) | Comparing repeated assignments, a direct base class call, and `super().__init__()` when initialising a subclass. |
| [08_mro.py](08_mro.py) | Resolving an inherited attribute through multiple inheritance and inspecting the class order with `__mro__`. |
| [09_static_methods.py](09_static_methods.py) | Using a static method, `split()`, `strip()`, and a list comprehension to clean a list of ingredients. |
| [10_classmethod.py](10_classmethod.py) | Creating orders through alternative constructors and inspecting instance attributes with `__dict__`. |
| [11_property_decorators.py](11_property_decorators.py) | Reading a calculated property and validating an assigned value with a setter. |
| [CODING_EXERCISE_26.md](CODING_EXERCISE_26.md) | The original Smart Home Device Tracker challenge, maintained manually. |
| [coding_exercise_26.py](coding_exercise_26.py) | Initialising devices, shadowing the default brand, and returning their power status. |
| [CODING_EXERCISE_27.md](CODING_EXERCISE_27.md) | The original Vehicle Rental System challenge, maintained manually. |
| [coding_exercise_27.py](coding_exercise_27.py) | Combining engines, vehicles, and cars with a shared counter and a validated rental price. |

## Example 01: Classes and Objects

Read [01_simple_class.py](01_simple_class.py). A **class** defines a type of object. An **instance** is an individual object created from that class.

- `class Chai:` and `class ChaiTime:` define two separate classes. Each uses `pass` as a placeholder for an otherwise empty body.
- `type(Chai)` returns `type`: the class itself is also an object in Python.
- `ginger_tea = Chai()` creates an instance of `Chai` and stores it in `ginger_tea`.
- `type(ginger_tea)` returns the class `Chai`.
- `type(ginger_tea) is Chai` is `True`, while the comparison with `ChaiTime` is `False`.

Expected output when running the file directly:

```text
<class 'type'>
<class '__main__.Chai'>
True
False
```

`__main__` identifies the module running as the program's entry point. The displayed class name can have a different module prefix if the file is imported instead.

## Example 02: Namespaces and Attributes

Read [02_namespace.py](02_namespace.py). A **namespace** associates names with values. A class and its instances can each have their own attributes, accessed using dot notation such as `Chai.origin` or `masala.origin`.

The example builds up these attributes step by step:

1. `origin = "India"` inside the class creates a class attribute.
2. `Chai.is_hot = True` adds another attribute to the class after its definition.
3. `masala = Chai()` creates an instance. Initially, `masala.origin` and `masala.is_hot` read the values defined on the class.
4. `masala.is_hot = False` creates an instance attribute. Reading `masala.is_hot` now returns its own value, while `Chai.is_hot` remains `True`.
5. `masala.flavor = "Masala"` adds an attribute to that instance.

For the attributes in this example, Python checks the instance for a value first, then looks on the class if it is absent. This is why assigning `masala.is_hot` changes the value read through that object without changing `Chai.is_hot`.

Expected output:

```text
India
True
Masala India
Masala True
Class:  True
Masala False
Masala
```

## Example 03: Attribute Shadowing and Deletion

Read [03_attribute_shadowing.py](03_attribute_shadowing.py). **Attribute shadowing** happens when an instance has an attribute with the same name as a class attribute. For this example, reading the attribute through the instance uses its own value.

1. `Chai.temperature` starts as `"hot"`. The new `cutting` object initially reads that class value.
2. `cutting.temperature = "Mild"` gives this instance its own value. `Chai.temperature` remains `"hot"`.
3. `cutting.cup = "small"` adds an attribute to the instance.
4. `del cutting.temperature` removes the instance's value. Reading `cutting.temperature` now finds `"hot"` on the class again.
5. `del cutting.cup` removes that instance attribute. The class has no `cup` attribute, so uncommenting the final `print(cutting.cup)` would raise `AttributeError`.

Deleting an instance attribute does not delete the class attribute with the same name.

Expected output with the final line left commented:

```text
hot
After changing  Mild
cup size is   small
Direct look into the class  hot
hot
```

## Example 04: Instance Methods and `self`

Read [04_self_args.py](04_self_args.py). A **method** is a function defined inside a class. Here, `describe(self)` uses `self.size` to return a description of a particular cup.

`self` refers to the instance receiving the method call. It is a conventional parameter name, rather than a Python keyword.

These two calls pass the same object to `describe`:

```python
cup.describe()             # Python passes cup as self automatically.
Chaicup.describe(cup)       # The object is passed explicitly.
```

Both return `"A 150ml chai cup"`, which `print()` displays. Initially, `self.size` finds the class attribute `size = 150`.

The example then creates a separate object, `cup_two`, and assigns `cup_two.size = 100`. Calling `Chaicup.describe(cup_two)` makes `self` refer to that object, so the description uses `100`. The class value and the size read through the first cup remain `150`.

Expected output:

```text
A 150ml chai cup
A 150ml chai cup
A 100ml chai cup
```

## Example 05: Initialising Objects with `__init__`

Read [05_init_objects.py](05_init_objects.py). `ChaiOrder` represents an order with a tea type and a size. Python automatically calls its `__init__(self, type_, size)` method to initialise a newly created instance.

For `order = ChaiOrder("Masala", 200)`:

1. Python creates a new object and passes it to `__init__` as `self`, along with `type_="Masala"` and `size=200`.
2. `self.type = type_` stores `"Masala"` as an instance attribute.
3. `self.size = size` stores `200` as another instance attribute.

The trailing underscore in `type_` avoids using the name of Python's built-in `type()` function as a parameter name.

Calling `order.summary()` makes `self` refer to that order. The method reads `self.size` and `self.type`, returns the formatted description, and `print()` displays it.

`order_two = ChaiOrder("Ginger", 220)` creates a separate object and initialises its own attributes. The two orders therefore keep different values:

| Object | `type` | `size` |
| --- | --- | --- |
| `order` | `"Masala"` | `200` |
| `order_two` | `"Ginger"` | `220` |

Expected output:

```text
200ml of Masala chai
220ml of Ginger chai
```

## Coding exercise 26: Smart Home Device Tracker

**Implemented and checked locally.**

Read the [original challenge](CODING_EXERCISE_26.md) and the [Python solution](coding_exercise_26.py).

The task is to represent smart home devices with a name, a power status, and a brand, then return a description of each device's current state.

- `SmartDevice.brand = "HomeTech"` defines the default brand on the class.
- `__init__(self, device_name, power_status)` stores the device name and Boolean power status as instance attributes.
- `self.brand = "CustomBrand"` gives each instance its own brand, shadowing the class attribute. `SmartDevice.brand` remains `"HomeTech"`.
- `get_status()` uses `"ON"` when `self.power_status` is `True` and `"OFF"` when it is `False`. It returns a string containing the device name, status, and instance brand.

After loading the solution, these calls:

```python
ac = SmartDevice("AC", True)
fan = SmartDevice("Fan", False)

print(ac.get_status())
print(fan.get_status())
print(SmartDevice.brand)
```

display:

```text
AC is ON - CustomBrand
Fan is OFF - CustomBrand
HomeTech
```

The devices keep their own attributes, so changing one device's power status does not change the other. `get_status()` returns its description; the caller decides whether to print it.

## Example 06: Inheritance and Composition

Read [06_inheritance_composition.py](06_inheritance_composition.py). This example combines two relationships:

- **Inheritance:** `MasalaChai` inherits `__init__()` and `prepare()` from `BaseChai`, then adds `add_spices()`. `FancyChaiShop` inherits `__init__()` and `serve()` from `ChaiShop`.
- **Composition:** each shop stores a separate chai object in `self.chai` and calls that object's `prepare()` method when serving it.

The class attribute `chai_cls` holds the class used to create the chai. Inside the shop's `__init__()`, `self.chai_cls("Regular")` creates an instance of that selected class:

| Shop object | Selected `chai_cls` | Class of `self.chai` | `self.chai.type` |
| --- | --- | --- | --- |
| `shop = ChaiShop()` | `BaseChai` | `BaseChai` | `"Regular"` |
| `fancy = FancyChaiShop()` | `MasalaChai` | `MasalaChai` | `"Regular"` |

`FancyChaiShop` sets its own `chai_cls = MasalaChai`, so the inherited initialisation creates a different kind of chai object for that shop. Both chai objects receive the name `"Regular"` from the shop's `__init__()`.

Both calls to `serve()` print the order and call `self.chai.prepare()`. The final call, `fancy.chai.add_spices()`, separately invokes the extra method available on the `MasalaChai` instance.

Expected output:

```text
Serving Regular chai in the shop
Preparing Regular chai....
Serving Regular chai in the shop
Preparing Regular chai....
Adding cardamom, ginger, cloves.
```

## Example 07: Base Class Initialisation with `super()`

Read [07_base_class.py](07_base_class.py). `Chai.__init__()` stores `type` and `strength`. Its subclass, `GingerChai`, defines its own `__init__()` to accept those values plus `spice_level`.

The active implementation performs these steps:

1. `super().__init__(type_, strength)` calls `Chai.__init__()` in this single-inheritance example. Python supplies the current instance as `self`, and the base class sets its `type` and `strength` attributes.
2. `self.spice_level = spice_level` adds the subclass's extra attribute to the same object.

The two commented alternatives show the progression:

- Repeating the assignments to `self.type` and `self.strength` duplicates the base class's initialisation code.
- Calling `Chai.__init__(self, type_, strength)` reuses it but explicitly names the base class and passes `self`.

The active version uses `super()` to reuse the base class's initialisation while extending it with the extra attribute.

This file only defines classes, so running it alone produces no output. After loading it, try:

```python
tea = GingerChai("Ginger", "Strong", "High")
print(tea.type)
print(tea.strength)
print(tea.spice_level)
```

Expected output from these calls:

```text
Ginger
Strong
High
```

## Example 08: Method Resolution Order (MRO)

Read [08_mro.py](08_mro.py). **Multiple inheritance** allows a class to inherit from more than one parent. Python uses a **method resolution order (MRO)** to decide which classes to search for inherited methods and attributes.

`A` defines a `label`. Both `B(A)` and `C(A)` provide their own `label`, while `D(C, B)` inherits from both classes and uses `pass` for its body.

`D.__mro__` returns a tuple of classes in this lookup order:

```text
D -> C -> B -> A -> object
```

When reading `cup.label`, the instance has no own `label`, and `D` does not define one. The class search reaches `C` first, so the result is `"C: Herbal blend"`.

The shared base `A` appears once, after both `C` and `B`. `object` is Python's ultimate base class. The same MRO also guides `super()` when looking up the next implementation.

Expected output when running the file directly:

```text
C: Herbal blend
(<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

## Example 09: Static Methods and Ingredient Cleaning

Read [09_static_methods.py](09_static_methods.py). `ChaiUtils` groups a helper for converting comma-separated ingredient text into a list of cleaned names.

The `@staticmethod` decorator lets `clean_ingredients(text)` receive the supplied text without an automatic `self` argument. The method works with that input and can be called directly through the class:

```python
cleaned = ChaiUtils.clean_ingredients(raw)
```

For `raw = " water , milk , ginger , honey "`, the expression `[item.strip() for item in text.split(",")]` performs these steps:

1. `text.split(",")` splits the string at each comma, producing ingredient strings that still contain surrounding spaces.
2. The list comprehension visits each ingredient as `item`.
3. `item.strip()` removes whitespace from the beginning and end of each ingredient, and the resulting strings form a new list.

`clean_ingredients()` returns that list. The script stores it in `cleaned` and prints it.

Expected output:

```text
['water', 'milk', 'ginger', 'honey']
```

## Example 10: Class Methods and Alternative Constructors

Read [10_classmethod.py](10_classmethod.py). `ChaiOrder.__init__()` stores the tea type, sweetness, and size on each order. Two methods decorated with `@classmethod` provide alternative ways to create an order:

- `from_dict(cls, order_data)` reads the three named entries from a dictionary.
- `from_string(cls, order_string)` splits a string such as `"Ginger-Low-Small"` at each hyphen and unpacks the three parts.

Python supplies the class as `cls`. Both methods call `cls(...)` to create and return an instance, using that class's `__init__()` to store the supplied values.

The separate static helper, `ChaiUtils.is_valid_size(size)`, checks membership in `["Small", "Medium", "Large"]`. The script calls it with `"Medium"`, which returns `True`. Order construction stores the supplied values without calling this helper.

The example creates `order1` from a dictionary, `order2` from a string, and `order3` directly through `ChaiOrder(...)`. As written, the first argument of `order3` is `"Large"`, so that value becomes its `tea_type`.

Printing each order's `__dict__` displays its instance attributes as a dictionary.

Expected output:

```text
True
{'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}
{'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}
{'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}
```

## Example 11: Properties and Validated Setters

Read [11_property_decorators.py](11_property_decorators.py). `TeaLeaf` stores an internal `_age` attribute. The leading underscore marks it as internal by convention.

- The `@property` getter makes `leaf.age` return `self._age + 2`.
- The `@age.setter` method runs when assigning `leaf.age = value`. It accepts values from `1` to `5`, inclusive, and raises `ValueError("Tea leaf age must be between 1 and 5 years")` for values outside that range.

The constructor directly stores its argument in `_age`. The setter's validation applies when assigning through the `age` property.

The script first creates `TeaLeaf(2)`, so reading `leaf.age` returns `4`. Assigning `leaf.age = 5` stores `5`, and the next read returns `7`. The getter adds `2` when reading; it does not change the stored value.

Expected output:

```text
4
7
```

## Coding exercise 27: Vehicle Rental System

**Implemented and checked locally.**

Read the [original challenge](CODING_EXERCISE_27.md) and the [Python solution](coding_exercise_27.py).

The task combines the section's concepts to describe vehicles and their engines, count created vehicles, and validate rental prices:

| Class | Responsibility |
| --- | --- |
| `Engine` | Store `horsepower` and return a description such as `"150 HP Engine"`. |
| `Vehicle` | Store the brand, model, and an `Engine` object; return vehicle details and manage the shared counter and rental price. |
| `Car(Vehicle)` | Reuse base initialisation with `super()`, add `seats`, and extend `get_details()` with `", Seats: X"`. |

Keeping an engine in `self.engine` is composition. Inheriting from `Vehicle` lets `Car` reuse the base behaviour while extending its description.

`Vehicle.total_vehicles` increases once for each new `Vehicle` or `Car`. Creating an `Engine` does not increase this counter. `get_total_vehicles()` is a class method that reads the counter, and the static method `get_vehicle_type()` returns `"Generic Vehicle"`.

The `rental_price` property starts at `0.0`. Its getter returns the stored value, and its setter accepts zero or positive prices. A negative assignment raises `ValueError("Rental price cannot be negative")` and preserves the previous price.

With a fresh solution loaded and the counter initially at zero, try:

```python
engine = Engine(150)
vehicle = Vehicle("Ford", "Focus", engine)
car = Car("Toyota", "Corolla", Engine(180), 5)
car.rental_price = 59.99

print(vehicle.get_details())
print(car.get_details())
print(car.rental_price)
print(Vehicle.get_vehicle_type())
print(Vehicle.get_total_vehicles())
```

Expected output:

```text
Ford Focus with 150 HP Engine
Toyota Corolla with 180 HP Engine, Seats: 5
59.99
Generic Vehicle
2
```

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open a numbered example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run each example from the repository root:

```powershell
python 10_oop/01_simple_class.py
python 10_oop/02_namespace.py
python 10_oop/03_attribute_shadowing.py
python 10_oop/04_self_args.py
python 10_oop/05_init_objects.py
python 10_oop/06_inheritance_composition.py
python 10_oop/07_base_class.py
python 10_oop/08_mro.py
python 10_oop/09_static_methods.py
python 10_oop/10_classmethod.py
python 10_oop/11_property_decorators.py
```

Examples 01–06 and 08–11 include calls that produce the output shown above. Example 07 defines classes and produces no output when run alone.

Both coding exercise files also define classes without displaying output when run alone. To try a demonstration for example 07, exercise 26, or exercise 27, choose one of these commands to load the corresponding file in an interactive session from the repository root:

```powershell
python -i 10_oop/07_base_class.py
python -i 10_oop/coding_exercise_26.py
python -i 10_oop/coding_exercise_27.py
```

Then enter the calls shown in that file's README example. Use `exit()` to leave the interactive session.

See the [main README](../README.md#quick-start) for editor setup.
