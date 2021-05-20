customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

print(customer["name"])
customer["name"] = "Indo Smith"
print(customer.get("name"))
print(customer.get("name1"))