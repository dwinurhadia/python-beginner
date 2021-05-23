def getting_message():
    print("Hello")
    print("Worlds")

print("Starting")
getting_message()
print("Finish")

def greeting_name(first_name, last_name):
    # print("Hello "+ first_name +" welcome to indonesiam")
    print(f"Hi {first_name} {last_name} welcome to indonesia")

greeting_name('Paul','Walker')
greeting_name('Paul', last_name='Walker')

def calculate(number):
    # return number * number
    print(number*number)
    # jika function tidak bisa return maka akan menampilkan nilai None ( atau Null di Java/php/c#)
print(calculate(4))