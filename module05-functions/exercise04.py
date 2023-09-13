# SyntaxError: non-default argument follows default argument
def gun(x=10, y, z=30):
    return x + y * z

gun(10,20)

