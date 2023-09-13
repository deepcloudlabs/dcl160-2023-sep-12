from functools import reduce

numbers = [10, 20, 30, 40, None, None, None, 35, 42, None, None, 37, 34]
# descriptive programming: functional programming
# higher-order function, pure function
# filter/map/reduce -> big data -> hadoop -> i) hdfs ii) MapReduce
if_not_none = lambda num: num is not None
# internal loop
values = list(filter(if_not_none, numbers))
print(values)
print(type(if_not_none))
print(type(filter))
to_cube = lambda u: u ** 3

values = list(map(to_cube, filter(if_not_none, numbers)))
print(values)
topla = lambda acc,v : acc + v
total = reduce(topla,map(to_cube, filter(if_not_none, numbers)))
print(total)
