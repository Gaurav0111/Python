
def computepay(h,r):
    if h<=40:
       Pay=h
    else:
       Pay=40*r+(h-40)*1.5*r
    return Pay

hrs = input('Enter Hours:')
h=float(hrs)
rate = input('Enter Rate:')
r=float(rate)

pay=computepay(h,r)
print(pay)