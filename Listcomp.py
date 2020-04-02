
### List Comprehensions
## List comprehensions build lists from sequences or any other
## iterable types.

# Example
strings = "Hello World"
print(strings)

### Loop
letters = []
for i in strings:
    letters.append(i)
    print(i)
print(letters)


### Listcomp
letters2 = [i for i in strings]
print(letters2)




## Cartesian Products
colors = ['black', 'white']
sizes = ['S','M','L']

t_shirt = [(color, size) 
                for color in colors 
                for size in sizes]
print(t_shirt)
