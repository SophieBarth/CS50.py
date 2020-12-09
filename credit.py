def main():
    a = 0
    while a == 0:
        num = input("Please enter your credit card number: ")
        check1 = checknum(num)
        if check1 == 1:
            check2= checkluhn(num)
            if check2 == 1:
                check3=checktype(num)
                a = 1

def checknum(n):
    try:
        val = int(n)
        return 1
    except ValueError:
        print("This is not a credit card number. Characters and signs are not allowed.")
        return 0


def checkluhn(n):
    #lists for second numbers from back
    secnum = []
    m = [int(i) for i in str(n)]

    #go through elements in num from back and take every second, go until last
    for i in range(len(m) - 2, -1, -2):
        secnum.append(m[i] * 2)

    #go through secnum and store every number and add the digits, store in secdignum and then add these in sumsec
    secdignum = []
    for ele in secnum:
        elesum = 0
        for digit in str(ele):
            elesum += int(digit)
        secdignum.append(elesum)
    sumsec = sum(secdignum)

    #take the last number in num and add every second from then
    firnum = []
    for j in range(len(m) - 1, -1, -2):
        firnum.append(m[j])
    sumfir = sum(firnum)

    #add up the sums
    luhnsum = sumfir + sumsec

    #check if the sums last digit is a zero
    if luhnsum % 10 != 0 :
        print("This is not a credit card number.")
        return 0
    else:
        return 1

def checktype(n):
    print("The type is: ", end="")
    typenum = []
    m = [int(i) for i in str(n)]

    #go through elements in num from back and take every second, go until last
    for i in range(0, len(m)-1):
        typenum.append(m[i])
    #check American Express
    if len(m) == 15 and typenum[0] == 3 and typenum[1] in [4,7]:
        print("American Express")
    elif len(m) == 16 and typenum[0] == 5 and (typenum[1] in [1,2,3,4,5]):
        print("MasterCard")
    elif len(m) in [13, 16] and typenum[0] == 4:
        print("Visa")
    else:
        print("INVALID")

main()
