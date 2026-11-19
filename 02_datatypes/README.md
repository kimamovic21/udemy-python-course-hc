# 02 — Data Types

This section introduces Python data types and their behaviour through small examples about tea, weather, temperatures, shopping, store inventory, and customer profiles.

Chapter 11 also introduces imports, date and time handling, and named tuples.

**Status: in progress.** This checkpoint covers chapters 1–11 and six coding exercises. More lessons will be added as I continue the course.

## Files covered so far

| File | What it demonstrates |
| --- | --- |
| [chapter_1.py](chapter_1.py) | Integer values, variable reassignment, and object identity with `id()`. |
| [chapter_2.py](chapter_2.py) | Creating and changing a set with `set()` and `.add()`. |
| [chapter_3.py](chapter_3.py) | Arithmetic operators and readable large numbers. |
| [chapter_4.py](chapter_4.py) | Booleans, conversion with `bool()`, and the `and` operator. |
| [chapter_5.py](chapter_5.py) | Floating-point numbers, precision, and `sys.float_info`. |
| [chapter_6.py](chapter_6.py) | Strings, f-strings, slicing, reversing text, and UTF-8 encoding and decoding. |
| [chapter_7.py](chapter_7.py) | Tuples, unpacking values, swapping variables, and membership testing with `in`. |
| [chapter_8.py](chapter_8.py) | List operations, `max()` and `min()`, concatenation, repetition, and `bytearray`. |
| [chapter_9.py](chapter_9.py) | Set union, intersection, difference, and membership testing. |
| [chapter_10.py](chapter_10.py) | Dictionaries: creating, accessing, updating, and removing key-value pairs. |
| [chapter_11.py](chapter_11.py) | Importing packages and modules, UTC and time zones with `arrow`, and named tuples with `collections.namedtuple`. |

## Coding exercise files

Each exercise has a Markdown file containing the original challenge and a separate Python file containing the solution. Read the challenge first, then compare it with the solution.

| Exercise | Challenge description | Python solution |
| --- | --- | --- |
| 01 — Playing with Numbers | [CODING_EXERCISE_01.md](CODING_EXERCISE_01.md) | [coding_exercise_01.py](coding_exercise_01.py) |
| 02 — Should You Go for a Walk? | [CODING_EXERCISE_02.md](CODING_EXERCISE_02.md) | [coding_exercise_02.py](coding_exercise_02.py) |
| 03 — Swapping Temperature | [CODING_EXERCISE_03.md](CODING_EXERCISE_03.md) | [coding_exercise_03.py](coding_exercise_03.py) |
| 04 — Shopping List | [CODING_EXERCISE_04.md](CODING_EXERCISE_04.md) | [coding_exercise_04.py](coding_exercise_04.py) |
| 05 — Managing Store Inventory | [CODING_EXERCISE_05.md](CODING_EXERCISE_05.md) | [coding_exercise_05.py](coding_exercise_05.py) |
| 06 — Customer Profile Management | [CODING_EXERCISE_06.md](CODING_EXERCISE_06.md) | [coding_exercise_06.py](coding_exercise_06.py) |

## Chapter 1: integers and object identity

`sugar_amount` first refers to the integer `2`, then is reassigned to `12`.

- An integer (`int`) represents a whole number.
- Integers are **immutable**: their value cannot be changed in place. Reassigning the variable makes it refer to another object.
- `id()` returns a number identifying an object during its lifetime. The calls to `id(2)` and `id(12)` inspect the identities of those two integer objects.

The sugar values printed are `2` and `12`. Object IDs can differ between program runs, so the exact ID numbers are not expected output to memorise.

## Chapter 2: mutable sets

`spice_mix = set()` creates an empty **set**. The program adds `"Ginger"`, `"cardamom"`, and `"lemon"` with `.add()`.

- A set stores unique values. Adding the same value again does not create a duplicate.
- A set does not guarantee the order in which its contents are displayed.
- Sets are **mutable**: `.add()` changes the existing object, so its ID stays the same before and after these additions.

In the output, the lines containing `id(spice_mix)` show the object's identity; the lines containing `spice_mix` show its contents.

## Chapter 3: arithmetic and large numbers

The examples practise calculations with tea, milk, and cardamom:

| Operator | Meaning | Example from the lesson | Result |
| --- | --- | --- | --- |
| `+` | Addition | `14 + 3` | `17` |
| `-` | Subtraction | `14 - 3` | `11` |
| `/` | Division | `7 / 4` | `1.75` |
| `//` | Floor division | `7 // 4` | `1` |
| `%` | Remainder | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

Each calculation uses the variables in its expression. Calculating `total_grams` does not change `black_tea_grams`, which still contains `14` when the subtraction runs.

For these integer inputs, `/` returns a `float`, while `//` returns an `int` by rounding the quotient down. The `%` operator gives the remainder. `2 ** 3` means `2 * 2 * 2`.

The literal `1_000_000_000` is one billion. Underscores make the number easier to read without changing its value; the program prints it as `1000000000`.

## Chapter 4: booleans and conditions

A **boolean** (`bool`) has one of two values: `True` or `False`.

- In arithmetic, `True` acts as `1` and `False` as `0`. Therefore, `5 + True` produces `6`.
- `bool(0)` produces `False`, which represents the absence of milk in this example.
- With the two boolean values used here, `water_hot and tea_added` is `True` when both are `True`.

Expected output:

```text
Total actions: 6
Is there milk? False
Can we serve chai? True
```

## Chapter 5: floats and precision

`ideal_temp = 95.5` and `current_temp = 95.49` are **floating-point numbers** (`float`). The program prints both temperatures, subtracts them, and displays `sys.float_info`.

Many decimal values are stored approximately as binary floating-point numbers. As a result, the subtraction can display a value very close to `0.01` with extra decimal digits. This is normal floating-point behaviour.

`sys.float_info` describes the precision and range of Python's floating-point numbers. There is no need to memorise all of its fields at this stage.

`Fraction` and `Decimal` are also imported in the current file, but are not used in its calculations yet.

## Chapter 6: strings, slicing, and UTF-8

A **string** (`str`) stores text. `chai_type`, `customer_name`, `chai_description`, and `label_text` all contain strings in this example.

An **f-string** starts with `f` before the quotation marks. Expressions inside `{}` are replaced with their values, allowing the order message to include the customer's name and type of chai.

String slicing extracts part of a string or changes the direction in which it is read. For `chai_description = "Aromatic and Bold"`:

| Expression | Result | Explanation |
| --- | --- | --- |
| `chai_description[:8]` | `"Aromatic"` | Characters from the start up to, but not including, index `8`. |
| `chai_description[12:]` | `" Bold"` | Characters from index `12` to the end, including the space before `Bold`. |
| `chai_description[::-1]` | `"dloB dna citamorA"` | The entire description in reverse order. |

String indexes start at `0`. The reverse slice produces the whole reversed description, even though the current program labels that output as `Last word`.

The final part of the lesson converts `"Chai Spécial"` between text and bytes:

- `.encode("utf-8")` converts the string into a `bytes` object stored in `encoded_label`.
- The encoded value is displayed as `b'Chai Sp\xc3\xa9cial'`. The `b` prefix identifies bytes; the accented `é` is represented by two bytes in UTF-8.
- `.decode("utf-8")` converts those bytes back into the original string, stored in `decoded_label`.

Encoding and decoding with the same encoding restores the text, including its accented character.

## Chapter 7: tuples, unpacking, and swapping

`masala_spices = ("cardamom", "cloves", "cinnamon")` creates a **tuple**, an ordered collection whose items cannot be replaced, added, or removed in place.

The lesson demonstrates three operations:

- **Unpacking:** `spice1, spice2, spice3 = masala_spices` assigns each tuple item to a separate variable in order.
- **Swapping:** `ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio` exchanges the values `2` and `1`. Python evaluates the right-hand side before assigning the values on the left.
- **Membership testing:** `"cinnamon" in masala_spices` returns `True` because the tuple contains that value.

Swapping changes which values the variables refer to; it does not modify the original `masala_spices` tuple.

## Chapter 8: lists and byte arrays

A **list** is an ordered, mutable collection. This lesson starts with ingredients such as `"water"`, `"milk"`, and `"black tea"`, then changes the lists with these methods:

| Method | What it does |
| --- | --- |
| `.append(value)` | Adds one item at the end. |
| `.remove(value)` | Removes the first matching item. |
| `.extend(other_list)` | Adds the items from another list at the end. |
| `.insert(index, value)` | Adds an item at a position; indexes start at `0`. |
| `.pop()` | Removes and returns the last item. |
| `.reverse()` | Reverses the current order in place. |
| `.sort()` | Sorts the list in place; the strings in this lesson are sorted alphabetically. |

For `sugar_levels = [1, 2, 3, 4, 5]`, `max(sugar_levels)` returns `5` and `min(sugar_levels)` returns `1`.

The `+` operator creates a new list by joining two lists. The `*` operator creates a new list by repeating the items: `["black tea", "water"] * 3` contains six items. These expressions leave the original lists unchanged.

The final example creates a **bytearray**, a mutable sequence of bytes. Each byte has a value from `0` to `255`:

```python
raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
```

The `b` prefix marks a bytes literal. Replacing `CINNA` with `CARD` leaves the ending `MON`, producing `CARDMON`. The `.replace()` method returns a new `bytearray`, which is assigned back to `raw_spice_data`.

The final line prints:

```text
Bytes: bytearray(b'CARDMON')
```

## Chapter 9: comparing sets

The lesson creates two sets: `essential_spices` contains cardamom, ginger, and cinnamon; `optional_spices` contains cloves, ginger, and black pepper.

| Operator | Operation | Result in this lesson |
| --- | --- | --- |
| `\|` | Union: all unique values from both sets. | Cardamom, ginger, cinnamon, cloves, and black pepper. |
| `&` | Intersection: values present in both sets. | Ginger. |
| `-` | Difference: values in the first set but not the second. | Cardamom and cinnamon. |
| `in` | Membership: check whether a value is present. | `"cloves" in optional_spices` returns `True`. |

The union, intersection, and difference expressions create new sets, leaving the original sets unchanged. Difference is directional: `essential_spices - optional_spices` asks specifically which essential spices are missing from the optional set.

Sets do not guarantee a display order. Focus on which values are included when reading the printed results.

## Chapter 10: dictionaries and key-value pairs

A **dictionary** (`dict`) stores values under keys. In `{"size": "Medium"}`, `"size"` is the key and `"Medium"` is its value. Dictionaries are mutable and preserve insertion order.

The lesson uses tea orders and recipes to practise:

- Creating dictionaries with `dict(type="Masala Chai", size="Large", sugar=2)` and `{...}`, or starting with an empty `{}`.
- Adding entries with `chai_recipe["base"] = "black tea"` and reading values with `chai_recipe["base"]`.
- Deleting an entry with `del chai_recipe["liquid"]`.
- Checking whether a key exists with `"sugar" in chai_order`, which returns `True`.
- Inspecting keys, values, and key-value pairs with `.keys()`, `.values()`, and `.items()`.
- Removing and returning the last inserted pair with `.popitem()`. For the second order, this returns `('sugar', 1)`.
- Adding cardamom and ginger to the recipe with `.update(extra_spices)`.

The second order contains `"size": "Medium"`, so this line assigns `"Medium"` to `customer_note`:

```python
customer_note = chai_order.get("size", "NO Note")
```

`.get(key, default)` returns the value when the key exists, or the default when it is missing. Here, `"NO Note"` is used only if `"size"` is missing. The variable name `customer_note` does not change which key is read.

## Chapter 11: imports, time zones, and named tuples

This lesson uses two imports: the external package `arrow` for dates and times, and `namedtuple` from Python's standard-library module `collections`.

Before running this file, install `arrow` using the same Python interpreter that runs your examples:

```powershell
python -m pip install arrow
```

If Python reports `ModuleNotFoundError: No module named 'arrow'`, the package is missing from the interpreter running the file. `collections` is included with Python and needs no separate installation.

The first part of the program:

- Uses `import arrow` to make the package available.
- Calls `arrow.utcnow()` to get the current date and time in UTC and stores it in `brewing_time`.
- Calls `brewing_time.to("Europe/Rome")` to represent the same instant in Rome's time zone and stores the new object in `rome_time`. The original `brewing_time` remains in UTC.
- Prints both values with descriptive f-strings. Their dates, times, and Rome's UTC offset depend on when the program runs.

The second part imports `namedtuple` and defines `chaiProfile`, a tuple type with fields named `flavor` and `aroma`:

```python
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])
profile = chaiProfile(flavor="spicy", aroma="ginger")
```

The first line defines the type; the second creates a profile. Read its fields with `profile.flavor` and `profile.aroma`. Like ordinary tuples, named tuples are immutable: their fields cannot be reassigned.

After the two time values, the program prints:

```text
Chai profile: chaiProfile(flavor='spicy', aroma='ginger')
Flavor: spicy
Aroma: ginger
```

A script needs `print()` calls to display these results in the terminal. Assigning values to variables or defining a named tuple type does not display them automatically.

## Coding exercise 01: Playing with Numbers

**Completed: all Udemy tests passed.**

Read the [challenge description](CODING_EXERCISE_01.md) and the [Python solution](coding_exercise_01.py).

The program uses `first_number = 10` and `second_number = 5`. It prints the results of addition (`+`), subtraction (`-`), multiplication (`*`), division (`/`), floor division (`//`), and modulus (`%`), in that order.

Expected output:

```text
15
5
50
2.0
2
0
```

The exercise prints **only the results**, one per line. Labels such as `Addition:` or `Division:` made the Udemy tests fail because the tests expected an exact output match.

Notice that `/` produces `2.0`, a `float`, even though the division has no remainder. With these integer inputs, `//` produces `2`, an `int`.

## Coding exercise 02: Should You Go for a Walk?

Read the [challenge description](CODING_EXERCISE_02.md) and the [Python solution](coding_exercise_02.py).

The starting conditions are `is_sunny = True` and `have_umbrella = False`. The exercise combines these boolean values with three logical operators:

- `not` reverses a boolean value: `True` becomes `False`, and `False` becomes `True`.
- `and` returns `True` when both boolean conditions are `True`.
- `or` returns `True` when at least one boolean condition is `True`.

| Expression | Evaluation | Result |
| --- | --- | --- |
| `not is_sunny` | `not True` | `False` |
| `not have_umbrella` | `not False` | `True` |
| `is_sunny and not have_umbrella` | `True and True` | `True` |
| `is_sunny or have_umbrella` | `True or False` | `True` |

Expected output, in the order requested by the challenge:

```text
False
True
True
True
```

The solution prints only these four boolean values, one per line, without extra labels.

## Coding exercise 03: Swapping Temperature

Read the [challenge description](CODING_EXERCISE_03.md) and the [Python solution](coding_exercise_03.py).

The initial values are `min_temp = 40` and `max_temp = 25`. Tuple packing and unpacking swap them without an extra variable:

```python
min_temp, max_temp = max_temp, min_temp
```

The old values on the right form `(25, 40)`, then are assigned to the variables on the left. The program prints the corrected minimum first, followed by the maximum:

```text
25
40
```

## Coding exercise 04: Shopping List

Read the [challenge description](CODING_EXERCISE_04.md) and the [Python solution](coding_exercise_04.py).

The program starts with `my_cart = ["apples", "bananas", "milk"]` and applies the requested list operations in order. It prints the list after each requested change.

- `.append()` adds bread, `.insert()` adds ketchup at the beginning, and `.remove()` removes bananas.
- `.pop()` removes bread, the last item at that point, and stores it in `removed_item`. The program prints that item separately.
- `.extend()` adds rice and butter; `.sort()` orders the list alphabetically, and `.reverse()` reverses that order.
- `combined_cart = my_cart + ["juice", "jam"]` creates a new combined list without changing `my_cart`.
- `duplicated_cart = my_cart * 2` repeats the current five-item cart twice. Juice and jam appear only in `combined_cart`.
- `.split()` converts `"tomato cucumber spinach"` into a list of three words by splitting at whitespace.

Expected output, without extra labels:

```text
['apples', 'bananas', 'milk']
['apples', 'bananas', 'milk', 'bread']
['ketchup', 'apples', 'bananas', 'milk', 'bread']
['ketchup', 'apples', 'milk', 'bread']
bread
['ketchup', 'apples', 'milk', 'rice', 'butter']
['apples', 'butter', 'ketchup', 'milk', 'rice']
['rice', 'milk', 'ketchup', 'butter', 'apples']
['rice', 'milk', 'ketchup', 'butter', 'apples', 'juice', 'jam']
['rice', 'milk', 'ketchup', 'butter', 'apples', 'rice', 'milk', 'ketchup', 'butter', 'apples']
['tomato', 'cucumber', 'spinach']
```

## Coding exercise 05: Managing Store Inventory

Read the [challenge description](CODING_EXERCISE_05.md) and the [Python solution](coding_exercise_05.py).

The program compares the products available in two branches:

- Branch A: bread, milk, butter, and jam.
- Branch B: bread, cheese, butter, and ketchup.

The union contains all six unique products. The intersection contains bread and butter. The difference `branch_a_products - branch_b_products` contains milk and jam. Checking for ketchup in branch A returns `False`.

`essential_items = frozenset({"milk", "bread", "ketchup"})` creates an **immutable set**. Its elements cannot be added or removed after creation. Membership checks and set comparisons are still supported.

The solution uses **f-strings** to label each result, making it clear which branch or operation is being displayed.

Example output; the order of elements inside each set or frozenset may vary:

```text
Branch A products: {'bread', 'milk', 'butter', 'jam'}
Branch B products: {'bread', 'cheese', 'butter', 'ketchup'}
Union of both branches: {'bread', 'milk', 'butter', 'jam', 'cheese', 'ketchup'}
Intersection of both branches: {'bread', 'butter'}
Products only in branch A: {'milk', 'jam'}
Is ketchup available in branch A? False
Essential items (frozenset): frozenset({'milk', 'bread', 'ketchup'})
```

## Coding exercise 06: Customer Profile Management

Read the [challenge description](CODING_EXERCISE_06.md) and the [Python solution](coding_exercise_06.py).

The program manages a customer profile using a dictionary:

1. Create `customer` with the name `"John Doe"`, age `32`, and city `"New York"`.
2. Add email and phone entries, then read the customer's name and city.
3. Check whether `"email"` is a key and delete the `"age"` entry.
4. Display the keys, values, and key-value pairs.
5. Remove and print the last inserted pair with `.popitem()`.
6. Read the missing `"membership"` key with `.get()`.
7. Add `"address": "221B Baker Street"` with `.update()` and print the final profile.

Key results:

| Operation | Result |
| --- | --- |
| `customer["name"]` | `John Doe` |
| `customer["city"]` | `New York` |
| `"email" in customer` | `True` |
| `customer.popitem()` | `('phone', '123-456-7890')` |
| `customer.get("membership")` | `None` |

The phone entry is removed because it was inserted last. `.get("membership")` returns `None` because the key is missing and no default value was supplied.

The final dictionary contains the name, city, email, and address. The current solution prints it twice:

```text
{'name': 'John Doe', 'city': 'New York', 'email': 'john.doe@example.com', 'address': '221B Baker Street'}
```

## How to run these examples

1. Open the repository root in VS Code and select your Python interpreter with **Python: Select Interpreter**.
2. Open the Python file you want to practise with.
3. Edit the file and press **Ctrl + S**. Black formats the code, then Run on Save runs it in the terminal.

To run a file manually, use **Python: Run Python File in Terminal** from the Command Palette (**Ctrl + Shift + P**). To format without saving, use **Shift + Alt + F**.

The [main README](../README.md#quick-start) lists the required extensions. Each file is a separate example and can be run independently.

## Package source repositories

- [Arrow — GitHub](https://github.com/arrow-py/arrow): dates and time zones (`arrow`).

See the [complete package index](../README.md#package-source-repositories) for import-name mappings and projects you can support with a GitHub star.
