try:
    a = int(input("Enter the number : "))
    b = 1/a
    print(b)

except ZeroDivisionError as e:
    print(f"an error occured : ")
    print(f"{e}")
    print(f"Make sure you are not entring a zero as input")


except ValueError as e:
    print(f"an error occured : ")
    print(f"{e}")
    print(f"Make sure you enter an integer value as an input")

except Exception as e :
    print(e)

print("Thank you !")

