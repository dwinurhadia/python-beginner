phone = input("Number: ")
dictionary_mapp = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += dictionary_mapp.get(ch, "!") + " "
print(output)