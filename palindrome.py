num = input()
try:
    val = int(num)
    if num == str(num)[::-1]:
        print('yes')
    else:
        print('NO')
except ValueError:
    print("That's not a valid number, Try Again !")
