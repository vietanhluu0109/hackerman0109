person = {
    "name":"AG.ChR0Me",
    "age":15,
}
print(person)

person["status"] = "single"
print(person)

person["locate"] = "Ha Noi"
print(person)

txt = input("favourite:")
d = input("type here:")
person[txt] = d
print(person)