def run(x, y, z):
    return x + y * z


# dictionary
params = {
    "y": 20,
    "x": 10,
    "z": 30
}

print(f"run(10,20,30): {run(10, 20, 30)}")
print(f"run(z=30,x=10,y=20): {run(z=30,x=10,y=20)}")
print(f"run(**params): {run(**params)}")
