person={
    "name":"akhil",
    "age":22,
    "add":"hsjnnjne",
    "phone":25344841,
    "phone":25344841
}
print(person)

print(person.items())

print(person.keys())

print(person.values())


print(person.get("phone"))

person.update({"name":"ajay"})
print(person)

person.update({"salary":"25k"})
print(person)

person.popitem()
print(person)

person.pop("age")
print(person)

# tuple ozhiche bakki ellathilum ee function work akum
# dictionary clear akkan
person.clear()
print(person)

# ellathilum ee function work akum
# full delete akkan
del person
print(person)