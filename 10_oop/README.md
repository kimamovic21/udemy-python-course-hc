# 10 — Object-Oriented Programming

This section introduces object-oriented programming (OOP), starting with classes, objects, attributes, instance methods, and initialisation with `__init__`. The examples use chai to explore how a class relates to the objects created from it. Exercise 26 applies these basics to a smart home device tracker.

**Status: in progress.** This checkpoint covers numbered examples 01–05 and coding exercise 26.

## Learning order

1. Start with [01_simple_class.py](01_simple_class.py) to define classes, create an object, and inspect its type.
2. Continue with [02_namespace.py](02_namespace.py) to explore namespaces and the difference between class and instance attributes.
3. Continue with [03_attribute_shadowing.py](03_attribute_shadowing.py) to override an attribute on one instance and observe what happens when it is deleted.
4. Continue with [04_self_args.py](04_self_args.py) to define an instance method and understand how `self` receives the object.
5. Continue with [05_init_objects.py](05_init_objects.py) to initialise each object with its own order details using `__init__`.
6. Read the [original challenge 26](CODING_EXERCISE_26.md), then explore [coding_exercise_26.py](coding_exercise_26.py) to track device status and practise attribute shadowing.

Follow this order even if your editor sorts the files differently. The numbered examples are explained below.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_simple_class.py](01_simple_class.py) | Defining empty classes, creating an instance, and comparing its type with two classes. |
| [02_namespace.py](02_namespace.py) | Reading class attributes through an object, adding attributes, and giving an instance its own value. |
| [03_attribute_shadowing.py](03_attribute_shadowing.py) | Shadowing a class attribute on an instance, then deleting instance attributes with `del`. |
| [04_self_args.py](04_self_args.py) | Calling an instance method through an object or its class and reading attributes with `self`. |
| [05_init_objects.py](05_init_objects.py) | Initialising separate orders with `__init__` and returning their descriptions through `summary()`. |
| [CODING_EXERCISE_26.md](CODING_EXERCISE_26.md) | The original Smart Home Device Tracker challenge, maintained manually. |
| [coding_exercise_26.py](coding_exercise_26.py) | Initialising devices, shadowing the default brand, and returning their power status. |

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

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open a numbered example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run each example from the repository root:

```powershell
python 10_oop/01_simple_class.py
python 10_oop/02_namespace.py
python 10_oop/03_attribute_shadowing.py
python 10_oop/04_self_args.py
python 10_oop/05_init_objects.py
```

All five scripts include calls that produce the output shown above.

`coding_exercise_26.py` defines the class for automatic testing. Running that file alone does not display output. To try the exercise example, start an interactive session from the repository root:

```powershell
python -i 10_oop/coding_exercise_26.py
```

Then enter the calls shown in the exercise example. Use `exit()` to leave the interactive session.

See the [main README](../README.md#quick-start) for editor setup.
