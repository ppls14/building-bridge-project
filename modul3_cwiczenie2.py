name = "Building Bridge"
def build_bridge(chunk,goal):
    """
    Function returns True if, given a slab of the length given by the chunk variable,
    we are able to build a bridge of the length given by the goal variable.
    """
    n = ((2/3)*((goal/chunk)-1)) #zmienna 'n' określa liczbę łączników potrzebnych do zbudowania mostu
    n1 = int(n)
    if n == n1:
        return True
    else:
        return False

chunk = 2
goal = 26
n = ((2/3)*((goal/chunk)-1)) 
answer = build_bridge(chunk, goal)

print(name)

if (answer):
    print(f"Do zbudowania mostu o długości {goal} jednostek potrzebnych jest {int(n)} łączników i {int(n+1)} płyt.")
else:
    print(f"Dla podanych warunków nie można zbudować mostu.")