"""
Both Tuple and NamedTuple are containers for data.
The standard tuple uses numerical indexes to access its members
A namedtuple assigns names, as well as the numerical index, to each member.
Each kind of namedtuple is represented by its own class, created by using the namedtuple() factory function. The arguments are the name of the new class and a string containing the names of the elements.
"""


## Example of Tuple
bob1 = ('Bob', '30', 'male')
print('Representation:', bob1)

## Example of NamedTuple
import collections

Person = collections.namedtuple("Person", 'name, age, gender')
print("Type of Person", type(Person))

bob2 = Person(name = 'Bob', age = 30, gender = "male")
print('Representation:', bob2)

# it is possible to access the fields of the namedtuple 
# by name using dotted notation (obj.attr) 
# as well as using the positional indexes of standard tuples
print(bob2.name)
print(bob2.age)
