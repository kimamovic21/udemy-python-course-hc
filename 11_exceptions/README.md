# 11 — Exceptions

This section introduces runtime exceptions, input validation, and custom exception classes. The examples use `try`, `except`, `else`, `finally`, and `raise` to handle errors, process chai bills, and close a file after writing. Early examples also show unhandled exceptions and how to read their tracebacks.

**Status: in progress.** This checkpoint covers numbered examples 01–08.

## Learning order

1. Start with [01_basic.py](01_basic.py) to observe an unhandled exception and understand why it occurs.
2. Continue with [02_try_except.py](02_try_except.py) to catch a missing dictionary key and let execution continue.
3. Continue with [03_complex_try.py](03_complex_try.py) to compare successful and failed calls using `raise`, `except`, `else`, and `finally`.
4. Continue with [04_multiple_exception.py](04_multiple_exception.py) to handle different exception types separately and observe how multiplying a string by an integer behaves.
5. Continue with [05_custom_exceptions.py](05_custom_exceptions.py) to validate a flavour and explicitly raise `ValueError` with a custom message.
6. Continue with [06_custom_except_two.py](06_custom_except_two.py) to define an exception class derived from `Exception` and raise it when an ingredient is missing.
7. Continue with [07_complete_order.py](07_complete_order.py) to validate orders, calculate bills, handle errors, and run a final message for each call.
8. Continue with [08_file_handling.py](08_file_handling.py) to write an order beside the script and close the file using `try`/`finally`.

The numbered examples will follow the course order as this section grows.

## Files covered so far

| File | Purpose |
| --- | --- |
| [01_basic.py](01_basic.py) | Accessing an out-of-range list index and inspecting the resulting `IndexError`. |
| [02_try_except.py](02_try_except.py) | Catching `KeyError` when a chai flavour is missing from a dictionary. |
| [03_complex_try.py](03_complex_try.py) | Raising and handling `ValueError`, running `else` on success, and running `finally` for both demonstrated outcomes. |
| [04_multiple_exception.py](04_multiple_exception.py) | Handling `KeyError` and `TypeError` separately, with examples of a missing item and string repetition. |
| [05_custom_exceptions.py](05_custom_exceptions.py) | Rejecting an unsupported flavour using Python's built-in `ValueError` and an application-specific message. |
| [06_custom_except_two.py](06_custom_except_two.py) | Defining `OutOfIngredientsError` and raising it when milk or sugar equals zero. |
| [07_complete_order.py](07_complete_order.py) | Combining `InvalidChaiError`, integer checks, billing, `except Exception`, and `finally` in one order-processing function. |
| [08_file_handling.py](08_file_handling.py) | Building a path with `pathlib`, writing `order.txt`, and closing the file in `finally`. |

## Example 01: An Out-of-Range List Index

Read [01_basic.py](01_basic.py). The script creates this list:

```python
orders = ["masala", "ginger"]
```

Python list indexes start at zero. `orders[0]` refers to `"masala"`, and `orders[1]` refers to `"ginger"`.

The next line tries to access index `2`, which would refer to a third item:

```python
print(orders[2])
```

The list contains only two items, so evaluating `orders[2]` raises `IndexError` before `print()` can display a value. Because the exception is unhandled, execution stops and Python displays a traceback.

The traceback identifies the file, line, and operation where the error occurred. Its final line is:

```text
IndexError: list index out of range
```

This error is the expected behaviour of the current example. Reading an existing item with `orders[0]` or `orders[1]` would return its value successfully.

## Example 02: Catching a Missing Dictionary Key

Read [02_try_except.py](02_try_except.py). `chai_menu` contains the keys `"masala"` and `"ginger"`. The `try` block attempts to access `chai_menu["elaichi"]`, which raises `KeyError` because that key is absent.

`except KeyError:` catches that exception and prints a message. Execution then continues after the handler, so the final `print("Hello chai code")` also runs.

Expected output, matching the current script's wording:

```text
The key that you are tying to access does not exists
Hello chai code
```

## Example 03: `try`, `except`, `else`, and `finally`

Read [03_complex_try.py](03_complex_try.py). `serve_chai(flavor)` demonstrates two paths: serving a known flavour and reporting an unknown one.

| Part | Role in this example |
| --- | --- |
| `try` | Print the preparation message, then check whether the flavour equals `"unknown"`. |
| `raise ValueError(...)` | Explicitly raise an exception for `"unknown"`, with the message `We don't know that flavor`. |
| `except ValueError as e` | Catch the exception and print its message through `e`. |
| `else` | Print the served message when the `try` block completes without an exception. |
| `finally` | Print `Next customer please` after either demonstrated outcome. |

For `serve_chai("masala")`, preparation succeeds and `else` runs. For `serve_chai("unknown")`, the raised exception is handled by `except`, and `else` is skipped. Both calls reach `finally`.

Expected output:

```text
Preparing masala chai...
masala chai is served
Next customer please
Preparing unknown chai...
Error:  We don't know that flavor
Next customer please
```

## Example 04: Multiple Exception Handlers

Read [04_multiple_exception.py](04_multiple_exception.py). `process_order(item, quantity)` looks up a price in `{"masala": 20}`, multiplies it by the supplied quantity, and prints the result.

Separate handlers provide different messages depending on the exception:

- `except KeyError` handles a missing menu item.
- `except TypeError` handles an operation that does not support the supplied type, such as multiplying the price by `None`.

For `process_order("ginger", 2)`, the dictionary lookup fails because `"ginger"` is absent. Python runs the `KeyError` handler and skips the remaining statements in `try`.

For `process_order("masala", "two")`, the price is found and Python evaluates `20 * "two"`. Multiplying a string by an integer repeats that string, so this call prints `"two"` twenty times after the cost label. It completes without triggering the `TypeError` handler.

Expected output from the two calls currently in the script:

```text
Sorry that chai is not on menu
total cost is twotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwo
```

An exception handler responds to operations Python rejects. Enforcing numeric-only quantities would require an explicit check.

## Example 05: Validating Input with `raise`

Read [05_custom_exceptions.py](05_custom_exceptions.py). `brew_chai(flavor)` checks whether the supplied flavour belongs to `["masala", "ginger", "elaichai"]`, matching the values currently in the script.

If the flavour is absent, `raise ValueError("Unsupported chai flavor...")` explicitly raises an exception. This uses Python's built-in `ValueError` with a custom message.

The script calls `brew_chai("mint")`. Because `"mint"` is unsupported, the exception is raised before the brewing message can print. There is no handler for this call, so execution stops and Python displays a traceback ending with:

```text
ValueError: Unsupported chai flavor...
```

For a supported flavour, the function reaches its `print()` statement. For example, calling it with `"masala"` would display `brewing masala chai...`.

## Example 06: Defining a Custom Exception Class

Read [06_custom_except_two.py](06_custom_except_two.py). The script defines an application-specific exception type:

```python
class OutOfIngredientsError(Exception):
    pass
```

Inheriting from `Exception` gives the class the standard exception behaviour. `pass` provides a valid class body while leaving that inherited behaviour in place. The class name identifies the particular problem: missing ingredients.

`make_chai(milk, sugar)` checks `milk == 0 or sugar == 0`. If either value is zero, it raises `OutOfIngredientsError("Missing milk or sugar")` before the brewing success message can print.

The active call is `make_chai(1, 0)`, so the zero sugar value triggers the exception. It is unhandled in this script, and execution stops with a traceback ending with:

```text
OutOfIngredientsError: Missing milk or sugar
```

The other two calls are commented out. Considered individually, `make_chai(0, 0)` would also raise the exception, while `make_chai(1, 1)` would print `chai is ready...`.

## Example 07: Chai Billing with Validation and Error Handling

Read [07_complete_order.py](07_complete_order.py). `InvalidChaiError` inherits from `Exception` and represents a request for a flavour that is absent from the menu.

`bill(flavor, cups)` uses `{"masala": 20, "ginger": 40}` as its menu. Inside `try`, it checks the flavour first, then checks `isinstance(cups, int)`. A valid order reaches the multiplication and prints its bill.

| Call | Behaviour |
| --- | --- |
| `bill("mint", 2)` | Raise `InvalidChaiError("that chai is not available")` because the flavour is missing. |
| `bill("masala", "three")` | Raise `TypeError("Number of cups must be an integer")` because the quantity is a string. |
| `bill("ginger", 3)` | Calculate `40 * 3` and print a bill for `120` rupees. |

`except Exception as e` catches both demonstrated exception types and prints their messages. The errors are handled inside the function, so the script continues to the next order.

`finally` prints `Thank you for visiting chaicode!` after each call, whether that call reports an error or prints a bill.

Expected output:

```text
Error:  that chai is not available
Thank you for visiting chaicode!
Error:  Number of cups must be an integer
Thank you for visiting chaicode!
Your bill for 3 cups of ginger chai: rupees 120
Thank you for visiting chaicode!
```

## Example 08: Writing a File and Closing It with `finally`

Read [08_file_handling.py](08_file_handling.py). The script builds its output path with:

```python
order_path = Path(__file__).resolve().parent / "order.txt"
```

`__file__` identifies the Python script, `resolve()` produces its resolved absolute path, and `parent` gives its containing folder. Joining that folder with `"order.txt"` places the output at `11_exceptions/order.txt`, regardless of the working directory used to run the script.

`open(order_path, "w", encoding="utf-8")` opens the file for writing. It creates the file if absent or replaces its existing contents when opened again.

The `try` block writes the order, and `finally` calls `file.close()`. After the file is opened successfully, this closes it even if writing raises an exception. A writing exception would continue to propagate after the cleanup.

The generated file contains:

```text
ginger tea - 4 cups
```

A successful run writes the file without printing a message in the terminal.

## Practice Role Play 2: Error-Handling Strategy

**Completed: all role play goals met.**

The discussion covered locating failures in file reading and record processing, handling specific expected exceptions, allowing unexpected errors to propagate, and choosing meaningful custom exceptions. It also covered preserving debugging context through tracebacks, exception chaining, and logs, while giving users clear messages and keeping customer data out of logs.

Recovery decisions included choosing whether an invalid record can be skipped or should stop processing that file. These were design topics discussed in the role play.

## How to run these examples

Open the repository root in VS Code, select your Python interpreter, and open a numbered example. Press **Ctrl + S** to format and run it using the project's editor settings.

Alternatively, run the examples from the repository root:

```powershell
python 11_exceptions/01_basic.py
python 11_exceptions/02_try_except.py
python 11_exceptions/03_complex_try.py
python 11_exceptions/04_multiple_exception.py
python 11_exceptions/05_custom_exceptions.py
python 11_exceptions/06_custom_except_two.py
python 11_exceptions/07_complete_order.py
python 11_exceptions/08_file_handling.py
```

Examples 01, 05, and 06 stop with the unhandled exceptions shown above. These are the expected results of their current calls; the file paths and traceback formatting can vary with the environment. Examples 02–04 and 07 handle their demonstrated exceptions and display the output shown above.

Example 08 writes `11_exceptions/order.txt` and closes it without terminal output on success.

See the [main README](../README.md#quick-start) for editor setup and its [useful links](../README.md#useful-links-for-beginners) for beginner references on exceptions and file handling.
