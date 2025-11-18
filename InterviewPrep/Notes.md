# Python Interview Preparation Guide

## Section 1: 100 Python Interview Questions with Detailed Explanations

### 1. What is Python?

Python is a high-level, interpreted programming language known for readable syntax and extensive libraries. It supports multiple paradigms (procedural, OOP, functional) and is widely used in web development, data science, AI, scripting, and automation. Python's design philosophy emphasizes code readability, making it easy for beginners and powerful for professionals.

### 2. Key features of Python?

Key features include:

* **Interpreted**: No compilation step; Python executes line by line.
* **Dynamically typed**: No need to declare variable types.
* **Object-oriented**: Everything is an object.
* **Extensive standard library**: Modules for file handling, networking, math, etc.
* **Cross-platform**: Runs on Windows, macOS, Linux.
* **Large ecosystem**: Django, Flask, NumPy, pandas, TensorFlow.

### 3. What is PEP8?

PEP8 is the official Python style guide that provides rules for naming conventions, indentation, spacing, imports, and programming best practices, making Python code clean and consistent.

### 4. Differences between list and tuple?

* **Mutability**: Lists are mutable; tuples are immutable.
* **Performance**: Tuples are faster due to immutability.
* **Use case**: Lists for dynamic data; tuples for fixed collections.

### 5. Explain dictionary in Python.

A dictionary is a hash-based key-value store. Keys must be immutable and unique. Lookup, insertion, and deletion are extremely fast (O(1) average).

### 6. What is garbage collection?

Python uses:

* **Reference counting**: Object deleted when count becomes zero.
* **Cyclic garbage collector**: Detects and cleans reference cycles.

### 7. Shallow vs Deep Copy?

* **Shallow copy**: Copies references; inner objects remain shared.
* **Deep copy**: Recursively copies all nested structures, creating independent copies.

### 8. What are decorators?

Decorators wrap a function and modify its behavior without changing its code. Widely used for authentication, logging, caching, and validation.

### 9. What are lambda functions?

Anonymous one-line functions created using `lambda`. Good for short operations.

### 10. What are generators?

Functions using `yield` to return one value at a time. Efficient for large datasets because they do not store all results in memory.

### 11. Define iterators.

An iterator is any object implementing `__iter__()` and `__next__()`, enabling sequential access.

### 12. range() vs xrange().

`xrange()` existed in Python 2 only. In Python 3, `range()` behaves like lazy `xrange()`.

### 13. Explain GIL.

The Global Interpreter Lock ensures only one thread executes Python bytecode at a time in CPython. This limits multithreading for CPU-bound tasks.

### 14. Overcoming GIL limitations?

Use multiprocessing, C/C++ extensions, or interpreters like Jython.

### 15. What is monkey patching?

Modifying classes or modules at runtime. Useful in testing but risky.

### 16. **init** vs **new**.

* `__new__`: Creates object.
* `__init__`: Initializes object attributes.

### 17. What is a metaclass?

A class responsible for creating classes. Used for frameworks, enforcing rules, logging, or auto-generating attributes.

### 18. '==' vs 'is'.

* `==` compares values.
* `is` compares memory addresses.

### 19. What are virtual environments?

Isolated Python environments to manage project-specific dependencies.

### 20. Exception handling flow.

Flow: try → except → else → finally. Ensures robust error handling.

### 21. Modules vs Packages.

* **Module**: A single `.py` file.
* **Package**: A directory containing multiple modules.

### 22. if **name** == "**main**".

Ensures code runs only when file is executed, not imported.

### 23. List comprehension.

Compact syntax for creating lists using expressions inside brackets.

### 24. Context manager.

Manages resources like files using `with`, ensuring cleanup.

### 25. Pickling.

Serializing Python objects for storage or transfer.

### 26. Magic methods.

Special methods enabling custom behavior like addition, printing, iteration.

### 27. pass vs continue vs break.

* **pass**: Placeholder.
* **continue**: Skip current loop.
* **break**: Exit loop.

### 28. Memory management in Python.

Python uses a private heap, garbage collector, and memory managers.

### 29. Data types.

Includes numeric, sequence, mapping, set, and custom objects.

### 30. *args and **kwargs.

Used to accept variable numbers of arguments.

### 31. Static vs class methods.

* **Static methods**: No access to class/object.
* **Class methods**: Access class via `cls`.

### 32. Named tuples.

Tuple subclass with named fields, improving readability.

### 33. Sets in Python.

Unordered unique collections, good for fast membership checking.

### 34. Closures.

Functions retaining access to outer scope variables even after scope ends.

### 35. map(), filter(), reduce().

Functional utilities for transforming, filtering, and reducing data.

### 36. Multithreading.

Useful for I/O-bound tasks but limited by GIL.

### 37. Multiprocessing.

Uses multiple CPUs, avoiding GIL limitations.

### 38. Dependency management.

pip, virtualenv, and requirements.txt are used.

### 39. async/await.

Used for writing non-blocking asynchronous code.

### 40. Sync vs async.

Synchronous is blocking; asynchronous allows concurrency.

### 41. SQLAlchemy.

An ORM for interacting with SQL databases.

### 42. Flask.

A lightweight framework for APIs.

### 43. Django.

A full-stack web framework with ORM and admin.

### 44. Unit testing.

Testing small units of code using unittest or pytest.

### 45. assert statement.

Used to check assumptions during development.

### 46. Caching.

Storing function results using lru_cache to increase performance.

### 47. Typing module.

Provides support for type hints.

### 48. Code optimization.

Use optimized libraries, caching, vectorization, and profiling.

### 49. REST APIs.

APIs using HTTP verbs such as GET, POST, PUT, DELETE.

### 50. Design patterns.

Common solutions like Singleton, Factory, and Decorator.


