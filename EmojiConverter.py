message = input("> ")
words = message.split(' ')
emoji = {
    ':)': '😃',
    ':(': '😢'
}
# print(words)
output = ""
for w in words:
    output += emoji.get(w, w) + " "
print(output)
