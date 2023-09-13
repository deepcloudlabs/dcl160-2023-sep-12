# SyntaxError: non-default argument follows default argument
def gun(x, y=10, z=20):
    return x + y * z

gun(10,20)
gun(30)

