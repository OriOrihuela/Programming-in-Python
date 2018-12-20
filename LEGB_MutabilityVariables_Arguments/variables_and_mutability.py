# OBJETOS INMUTABLES #
a = 3
b = a

# B es 3 #

a = 3
b = a
a = "spam"

# B es 3 #

# Los objetos integer no son mutables #

a = 3
b = a
a = a + 2

# B es 3 #

# OBJETOS MUTABLES #

L = [2, 3, 4]           # A mutable object
M = L                   # Make a reference to the same object
L[0] = 24               # A in-place change

L
[24, 3, 4]
M 
[24, 3, 4]

# Copia de objetos en referencia #

L = [2, 3, 4]
M = L[:]                # Make a copy of L (or list (L), copy.copy(L), etc.)
L[0] = 24
L
[24, 3, 4]
M 
[2, 3, 4]               # M is not changed


# Shared references and Equality #

L = [1, 2, 3]           
M = L                   # M and L reference the same object
L == M                  # Same values ---> operador igualdad de valores 
True
L is M                  # operador identidad de objetos: compra las referencias (los punteros)
True


L = [1, 2, 3]
M = [1, 2, 3]          # L and M reference the same object
L == M                  # Same values -> operador igualdad de valores
True
L is M                  # operador identidad de objetos: compara las referencias (los punteros)
False



# CACHE #

X = 42
Y = 42                    # Should be two different objects
X == Y
True
X is Y                  # Same object anyhow: caching at work!!!!
True

