# Threads, Processes, and Concurrency

This folder corresponds to **Udemy section 17** and follows the projects in [challenges](../challenges/README.md), ending with the Flask URL Shortener. The local folder number is `12`; the course section number is `17`.

**Status: in progress — current course section.** Examples 01–02 use threads and separate processes to overlap simulated chai-shop tasks.

[Main project overview](../README.md#folder-overview)

## Files covered so far

| File | What it demonstrates |
| --- | --- |
| [01_threading.py](01_threading.py) | Creating two `Thread` objects, starting them with `start()`, pausing with `time.sleep()`, and waiting for completion with `join()`. |
| [02_multiprocessing.py](02_multiprocessing.py) | Creating three separate `Process` workers, passing arguments, starting all workers before joining, and protecting startup with `if __name__ == "__main__":`. |

Video **131: What is Concurrency and Parallelism ?** includes both examples above. `01` and `02` identify the local Python files, not two different videos. The video-progress record remains in `documentation.txt`, maintained by the repository owner.

Keep future numbered examples in course order and add their explanations here as the section grows.

## Running the examples

From the repository root:

```powershell
python "12_threads_concurrency/01_threading.py"
python "12_threads_concurrency/02_multiprocessing.py"
```

Run the commands one at a time to observe each example. You can also open either file in VS Code and press **Ctrl + S** with the existing Run on Save configuration. Output appears in the terminal; there is no browser page or input prompt.

`threading`, `multiprocessing`, and `time` are part of Python's standard library. No additional packages need to be installed. Neither script creates output files.

## 01: How the threading example works

1. `take_orders()` loops over `range(1, 4)`, prints an order number from 1 to 3, and sleeps for two seconds after each message.
2. `brew_chai()` also loops three times, prints the chai number, and sleeps for three seconds after each message.
3. `threading.Thread(target=take_orders)` creates a thread assigned to the order-taking function. The other `Thread` is assigned to `brew_chai`. Passing the function without parentheses lets the thread call it when started.
4. Calling `start()` on both objects begins their execution. While one thread sleeps, the other can make progress.
5. Calling `join()` makes the main thread wait for that worker thread to finish. Both workers keep running while the main thread waits.
6. After both joins return, the main thread prints `All orders taken and chai brewed`.

`time.sleep()` pauses the calling thread. It does not pause every thread in the process.

### Output and timing

Each run prints three order messages, three brewing messages, and the final completion message. The two groups of messages can be interleaved, and their exact order can change between runs. The completion message appears after both workers finish.

| Task | Waiting time in the current code |
| --- | --- |
| Taking three orders | About 6 seconds: `3 × 2`. |
| Brewing three cups | About 9 seconds: `3 × 3`. |
| Both tasks with overlapping waits | About 9 seconds overall, plus scheduling overhead. |

Running the same functions one after the other would take about 15 seconds. Both functions sleep after their final message too, so the program can remain active after all six task messages have appeared.

The sleeps simulate waiting. This example demonstrates concurrency by overlapping those waits; it does not benchmark calculation speed.

## 02: How the multiprocessing example works

1. `brew_chai(name)` prints a start message, sleeps for three seconds, and prints an end message for that worker.
2. Inside `if __name__ == "__main__":`, a list comprehension creates three `Process` objects named through their arguments: `Chai Maker #1`, `Chai Maker #2`, and `Chai Maker #3`.
3. `target=brew_chai` selects the function each worker will run. `args=(f"Chai Maker #{i+1}",)` passes its name as a one-element tuple; the trailing comma makes it a tuple.
4. The first loop calls `start()` on every worker. Each process runs independently with its own Python interpreter and memory space.
5. The second loop calls `join()` on every worker. The parent process waits for all workers to finish before printing `All chai served`.

The main guard is essential when using the Windows `spawn` start method: a child imports the script to obtain its function definitions, and the guard keeps it from creating another set of workers. Keep process creation and startup inside that block.

### Output and timing

The terminal displays three start messages and three end messages, then `All chai served`. The exact order of worker messages can vary. All workers are started before the parent begins joining them, so their three-second waits overlap. Total runtime is roughly three seconds plus process startup and scheduling overhead; calling the function three times sequentially would spend about nine seconds sleeping.

Starting all workers first matters. Starting one process and immediately joining it inside the same loop would make the parent wait before starting the next worker.

### Threads and processes in these examples

| Threads in example 01 | Processes in example 02 |
| --- | --- |
| Worker threads share one process and its memory. | Each worker has a separate process and memory space. |
| Created with `threading.Thread`. | Created with `multiprocessing.Process`. |
| The two functions simulate order taking and brewing. | Three workers run the same brewing function with different arguments. |

Both examples use `start()` and `join()`. Separate processes can execute work on different CPU cores, but these examples primarily simulate waiting with `sleep()`. Their runtimes are not a comparison of CPU performance because they perform different tasks.

## Concurrency and parallelism

- **Concurrency:** multiple tasks make progress during the same period, including taking turns while another task waits.
- **Parallelism:** multiple tasks execute at the same instant, for example on different CPU cores.

The distinction helps explain why this example can finish sooner even though most of its time is spent waiting.

## Useful links and source code

- [Python threading documentation](https://docs.python.org/3/library/threading.html): thread objects, `start()`, and `join()`.
- [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html): processes, argument passing, and safe startup with the main guard.
- [time.sleep reference](https://docs.python.org/3/library/time.html#time.sleep): suspending the calling thread.
- [CPython — GitHub](https://github.com/python/cpython): Python's reference implementation and standard-library source, including these modules. They are not separate pip packages.
