def is_leap(year):
    leap = False
    # Write your logic here
    if year in range(1900, 10**5):
        if year%4 == 0:
            if year%100 == 0:
                leap = True if year%400 == 0 else False
            else:
                leap = True
        else:
            leap = False
        return leap
    else:
        print("Out of memory!")

year = int(input())
print(is_leap(year))