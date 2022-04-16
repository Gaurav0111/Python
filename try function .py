while(True) :
    a = input("Enter the number : ")
    if (a == 'q'):
        break


    try:
        a = int(a) 
        if ( a> 6):
            print( f"The number you entered '{a}' is greater than 6 ")

    except Exception as e:
        print(f"You got an error in your program : {e}")

    
print("You quit the game ")
print("Thank you")