def cust(num):
    try:
        return int(num) + 1

    except:
        raise ValueError("Please enter a proper value") # error is generated according to us

print(cust("asdvfs")) 