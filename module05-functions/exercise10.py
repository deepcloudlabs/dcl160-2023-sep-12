my_global = 42
def fun():
    global my_global
    my_global = my_global + 1
    return my_global ** 2

fun()
fun()
fun()

print(my_global)
