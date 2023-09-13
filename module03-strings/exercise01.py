"""
  i) string -> str ✔
 ii) character array ✔
iii) iterable -> for loop, len() ✔
 iv) immutable data structure ✔
  v) utility methods: is___(), upper/lower/title, strip/lstrip/rstrip/replace, ... ✔
 vi) char array vs binary array
"""
full_name1 = "kate austen"
full_name2 = 'sun kwon'
message1 = "kate's house"
message2 = 'kate\'s house 2\\3\n\t'
message3 = """{
 fullname : "jack bauer",
 salary: 100000,
 iban: "tr1",
 department: "HR",
 jobStyle: "FULL TIME",
 birthYear: 1956
}"""
sql_select_asian_countries = """
select code,name,population,surfaceArea
from countries
where continent="Asia"
"""

print(sql_select_asian_countries)
