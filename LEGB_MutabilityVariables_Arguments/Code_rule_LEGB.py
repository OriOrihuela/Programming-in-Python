

X = 88

def func():
    X = 99 # Local X: hides global, but we want this here.

func()
print(X) # Prints 88: unchanged

X = 88 # Global X

def func():
    global X 
    X = 99 # Global X: outside def 

func()
print(X)

# Global names may be referenced within a function without being declared 

y, z = 1, 2

def all_global():
    global X
    x = y + z

# X existe ahora en el ambito global con el valor 3 


# NESTED SCOPES #

x = 99
def f1():
    X = 88
    def f2():
        print(X)
    f2()
f1()

# salida: X = 88; X sigue valiendo 99; no se puede invocar a f2() desde el modulo principal. 

# Factory Functions: Closures 

def f1():
    X = 88
    def f2():
        print(X) # Remembers X in enclosing def scope 
    return f2    # Return f2 but don't call it => f1() devuelve el objeto funcion f2()

action = f1()    # Make, return function -> action es ahora una función = f2()
action()         # Call it now: prints 88 


# Otro ejemplo # 

def maker(N):
    def action(X):      # Make and return action
        return X ** N   # action retains N from enclosing scope
    return action 

f = maker(2)    # Pass 2 to argument N 
f(3)            # Pass 3 to X, N remembers 2: 3 ** 2
9
f(4)            # 4 ** 2
16