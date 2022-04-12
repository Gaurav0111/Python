

class Number:
    def __init__(self , num ):
         self.num = num

    def __add__(self , num2):
        print("Lets add")
        return self.num + num2.num 

    def __mul__(self , num2):
        print("Lets multiply")
        return self.num * num2.num 


n1 =Number(4)
n2 =Number(6)
sum =  n1+n2
mul =  n1*n2


# to overload minus operator we will use __sub__
# to overload divide( / ) operator we will use __truediv__
# to overload ( // ) operator we will use __floordiv__



print(sum)
print(mul)