try:
    age = int(input("Age : "))
    income = 20000
    risk = income/age
    print(age)
    print(risk)
except ZeroDivisionError:
    print("value cannot divided by zero")
except ValueError:
    print("invalid value")