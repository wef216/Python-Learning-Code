# Data Model in Python

## The Python Data Model
The python interpreter invokes special methods to perform basic object operations, triggered by special syntax.

*i.e* `__getitem__` supports the syntax `obj[key]`

The special method allow your **object** to implement, support, and interact with basic language constructs such as:
- **Iteration**
- **Collections**
- **Attribute access**
- **Operator overloading**
- **Function and method invocation**
- **Object creation and destruction**
- **String representation and formatting**
- **Managed context**


### How Special Methods Are Used
The special methods are called by the **Python Interpreter**, not by used. For example

> `len(my_object)` rather than `my_object__len__()`

Sometimes, the special method call is **IMPLICIT**, for example
> `for i in x` actually calls `x.__iter__()` first.

It is usually better to call a related built-in function (*i.e* len, iter, str, etc) than invoking a special method.


----
## Array of Sequences


- **Container sequences:**
*list, tuple, collections.deque*: hold items of different types
    - hold reference to the objects contained
- **Flat sequence:** *str, byte, bytearray, array* hold items of one type.
    - compact, not as distinct objects
    - hold prime values only, *i.e* char, byte, and num

Or grouping by the **Mutability**
- **Mutable Sequences**: *list, bytearray, array, collections.deque*
- **Immutable Sequences**: *tuple, string, byte*



