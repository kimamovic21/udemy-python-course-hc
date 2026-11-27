# Threads, Processes, and Concurrency

This folder corresponds to **Udemy section 17** and follows the projects in [challenges](../challenges/README.md), ending with the Flask URL Shortener. The local folder number is `12`; the course section number is `17`.

**Status: in progress — current course section.** Examples 01–08 cover threads, processes, the GIL, function arguments, concurrent HTTP downloads, and protecting a shared counter with a lock.

[Main project overview](../README.md#folder-overview)

## Files covered so far

| File | What it demonstrates |
| --- | --- |
| [01_threading.py](01_threading.py) | Creating two `Thread` objects, starting them with `start()`, pausing with `time.sleep()`, and waiting for completion with `join()`. |
| [02_multiprocessing.py](02_multiprocessing.py) | Creating three separate `Process` workers, passing arguments, starting all workers before joining, and protecting startup with `if __name__ == "__main__":`. |
| [03_gil_threading.py](03_gil_threading.py) | Named threads, `current_thread()`, CPU-bound counting loops, elapsed time, and the effect of the GIL on Python thread execution. |
| [04_gil_multiprocessing.py](04_gil_multiprocessing.py) | Running CPU-bound counting in two separate processes, protecting startup with the main guard, joining both workers, and measuring total elapsed time. |
| [05_thread_one.py](05_thread_one.py) | Running two different breakfast functions in threads and measuring their overlapping waits. |
| [06_thread_two.py](06_thread_two.py) | Reusing one function in two threads with different positional arguments supplied through `args`. |
| [07_thread_download.py](07_thread_download.py) | Starting one thread per image URL, downloading response bytes with Requests, and joining workers stored in a list. |
| [08_thread_lock.py](08_thread_lock.py) | Ten threads updating one global counter inside a `with lock:` block. |

Video **131: What is Concurrency and Parallelism ?** includes `01_threading.py` and `02_multiprocessing.py`. `01` and `02` identify the local Python files, not two different videos. Examples 03–04 introduce CPU-bound work and the GIL. The video-progress record remains in `documentation.txt`, maintained by the repository owner.

Keep future numbered examples in course order and add their explanations here as the section grows.

## Running the examples

From the repository root:

```powershell
python "12_threads_concurrency/01_threading.py"
python "12_threads_concurrency/02_multiprocessing.py"
python "12_threads_concurrency/03_gil_threading.py"
python "12_threads_concurrency/04_gil_multiprocessing.py"
python "12_threads_concurrency/05_thread_one.py"
python "12_threads_concurrency/06_thread_two.py"
python "12_threads_concurrency/07_thread_download.py"
python "12_threads_concurrency/08_thread_lock.py"
```

Run the commands one at a time to observe each example. You can also open any of these files in VS Code and press **Ctrl + S** with the existing Run on Save configuration. Output appears in the terminal; there is no browser page or input prompt.

`threading`, `multiprocessing`, and `time` are part of Python's standard library. Example 07 also needs the third-party Requests package and an internet connection. Install it in the Python environment used by VS Code if needed:

```powershell
python -m pip install requests
```

These scripts create no output files. In particular, example 07 downloads image data into memory without saving images to disk.

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

## 03: CPU-bound threading and the GIL

Unlike the waiting examples, `03_gil_threading.py` spends its working time repeatedly incrementing a number. It contains no `sleep()` call.

1. `brew_chai()` prints the current thread's name using `threading.current_thread().name`.
2. Each call initializes its own local `count` and runs `count += 1` for `100_000_000` iterations. The two threads therefore perform 200 million increments in total, with independent local counters.
3. Two `Thread` objects run that function, named `Barista-1` and `Barista-2`.
4. `time.time()` records the start before the workers are started. After both `join()` calls return, a second reading records the end.
5. `end - start` is the elapsed wall-clock time for starting and completing both workers. `:.2f` formats it to two decimal places.

### Observed output

The repository owner reported this successful run:

```text
Barista-1 started brewing...
Barista-2 started brewing...
Barista-1 finished brewing...
Barista-2 finished brewing...
total time taken: 5.51 seconds
```

Message order and runtime can vary with the interpreter, computer, and other running tasks. `5.51` seconds is an observed result, not an expected fixed duration or a pass/fail threshold. The final time is printed after both workers finish. The script does not print the final counter values.

### What the GIL means here

In **GIL-enabled CPython**, the Global Interpreter Lock permits only one thread at a time to execute Python bytecode in an interpreter. These counting loops can take turns making progress, but two threads do not automatically make the pure-Python CPU work twice as fast. Seeing both start messages before either finish message does not establish simultaneous execution on two CPU cores.

This differs from example 01, where the workers spend most of their time sleeping and can overlap their waits. For the counting example, a meaningful speed comparison would require running the same total workload sequentially and comparing timings in the same environment. The current script measures only the threaded run, so its output alone does not demonstrate a speedup or determine whether the GIL is enabled.

Modern Python also has **free-threaded CPython builds**, available from Python 3.13, which can run with the GIL disabled. The explanation above applies when the GIL is enabled; check the current [threading performance notes](https://docs.python.org/3/library/threading.html#gil-and-performance-considerations) when comparing interpreter builds.

## 04: CPU-bound work with multiprocessing

`04_gil_multiprocessing.py` runs the counting workload in two separate processes. Unlike example 02's simulated brewing delay, the workers spend their time incrementing a number.

1. `crunch_number()` prints a start message, initializes a local `count`, increments it 100 million times, and prints an end message.
2. Inside the main guard, `start = time.time()` records the beginning before the worker objects are created.
3. `Process(target=crunch_number)` creates each of the two workers. They receive the same function, but each has a separate interpreter and memory space.
4. Both `start()` calls run before either `join()`, allowing the workers to make progress independently while the parent waits.
5. After both joins return, `end = time.time()` records completion. The final message displays `end - start` to two decimal places.

Keep process creation inside `if __name__ == "__main__":` so Windows child-process imports do not start more workers.

The terminal prints `Started the count process...` twice and `Ended the count process...` twice, followed by `Total time with multi-processing is ... seconds`. Worker-message order can vary. Both start messages use the same text, so this version does not identify workers by name. Final counter values are not printed, and no output files are created.

### Comparing examples 03 and 04

| Example 03 | Example 04 |
| --- | --- |
| Two threads in one process. | Two separate worker processes. |
| Each thread performs 100 million increments. | Each process performs 100 million increments. |
| In GIL-enabled CPython, workers take turns executing Python bytecode. | Workers have independent interpreters and can execute on different CPU cores. |

Each script performs 200 million increments overall. On a multicore computer, separate processes can make this CPU-bound Python work faster, but process startup and scheduling add overhead. A twofold speedup is not guaranteed, and the `5.51` seconds reported for example 03 is not a target for example 04.

Compare the scripts in the same Python environment, running them separately under similar system load. Their timed regions also differ slightly: example 04 includes process-object creation, while example 03 creates its thread objects before starting the timer. These are learning examples rather than a controlled benchmark. The GIL-enabled versus free-threaded distinction described above still matters when interpreting the results.

## 05: Two different tasks with overlapping waits

`05_thread_one.py` prepares a simulated breakfast. `boil_milk()` waits for two seconds, while `toast_bun()` waits for three seconds. A separate thread runs each function.

Both workers start before the main thread joins them, so their waits overlap. After both finish, the script prints `Breakfast is ready in ... seconds`. Total runtime is roughly three seconds plus overhead, compared with about five seconds if the functions were called sequentially. Message order can vary.

The elapsed time is measured with `time.time()`. These functions simulate waiting with `sleep()`; they do not perform CPU-intensive cooking calculations.

## 06: One function with different arguments

`06_thread_two.py` reuses `prepare_chai(type_, wait_time)` for two workers:

| Thread | Arguments | Effective function call |
| --- | --- | --- |
| `t1` | `args=("Masala", 2)` | `prepare_chai("Masala", 2)` |
| `t2` | `args=("Ginger", 3)` | `prepare_chai("Ginger", 3)` |

`target` selects the function, while `args` supplies its positional arguments as a tuple. Each call prints its tea type, waits for its own duration, and prints a ready message. Unlike example 05's two different functions, both threads here run the same function with different inputs.

The waits overlap, so the script takes roughly three seconds plus overhead. It joins both workers but does not measure or print total elapsed time.

## 07: Concurrent image downloads

`07_thread_download.py` requests the JPEG, PNG, and SVG image endpoints from [httpbin](https://httpbin.org/), a service for testing HTTP clients.

1. `download(url)` prints the URL and calls `requests.get(url)`.
2. The response body is available as `resp.content`; `len(resp.content)` gives its size in bytes.
3. A loop creates and starts one thread per URL. `args=(url,)` is a one-element tuple; its comma makes it a tuple rather than a parenthesized string.
4. Each worker is added to the `threads` list. A second loop joins all workers after they have been started.
5. The final line reports the overall elapsed time as `All downloads done in ... seconds`.

Network waits can overlap, so downloads can make progress concurrently. Completion order and total time depend on the network and server. The owner's observed `1.22` seconds is an example, not a fixed expected runtime. Output from different threads can appear together on one terminal line.

**The downloaded images are not saved as files.** Their bytes are held in memory while each function runs, and only the URL, byte count, and elapsed time are printed. There is no generated image folder or CSV.

The current function does not set a request timeout or check the response with `raise_for_status()`. It reports the size of the returned body; the final timing message does not validate that every response was a successful image download.

## 08: Protecting a shared counter with a lock

`08_thread_lock.py` creates a single global `counter`, initially zero, and a `threading.Lock()`. Ten threads call `increment()`, each performing 100,000 increments.

- `global counter` lets the function update the variable defined outside the function.
- `with lock:` acquires the same lock for each update. One thread at a time can execute the protected `counter += 1` block; other threads attempting that block wait.
- Leaving the block releases the lock automatically, including when an exception exits the block.
- The script starts all ten workers, joins them, and then prints the shared result.

Expected output after all increments finish:

```text
Final counter: 1000000
```

The total is `10 × 100,000`. Unlike example 03's independent local counters, all workers here modify the same variable. The lock demonstrates synchronization of shared updates; the GIL should not be treated as a general replacement for application-level locking. This example does not measure elapsed time.

## Concurrency and parallelism

- **Concurrency:** multiple tasks make progress during the same period, including taking turns while another task waits.
- **Parallelism:** multiple tasks execute at the same instant, for example on different CPU cores.

Examples 01–02 and 05–06 simulate overlapping waits, 03–04 compare CPU-bound workers, 07 uses real network requests, and 08 introduces synchronization of shared data.

## Useful links and source code

- [Python threading documentation](https://docs.python.org/3/library/threading.html): thread objects, `start()`, and `join()`.
- [Lock objects](https://docs.python.org/3/library/threading.html#lock-objects): protecting shared updates in example 08.
- [GIL and threading performance](https://docs.python.org/3/library/threading.html#gil-and-performance-considerations): official CPython guidance, including free-threaded builds.
- [What Is the Python Global Interpreter Lock (GIL)? — Real Python](https://realpython.com/python-gil/): supplementary background reading for examples 03–04. Use the official Python notes above for current interpreter-specific behavior.
- [Python multiprocessing documentation](https://docs.python.org/3/library/multiprocessing.html): processes, argument passing, and safe startup with the main guard.
- [time.sleep reference](https://docs.python.org/3/library/time.html#time.sleep): suspending the calling thread.
- [Requests quickstart: binary response content](https://requests.readthedocs.io/en/latest/user/quickstart/#binary-response-content): the response bytes used in example 07.
- [Requests — GitHub](https://github.com/psf/requests): official source repository for the third-party HTTP client.
- [httpbin](https://httpbin.org/): the source of example 07's JPEG, PNG, and SVG responses.
- [CPython — GitHub](https://github.com/python/cpython): Python's reference implementation and standard-library source, including these modules. They are not separate pip packages.
