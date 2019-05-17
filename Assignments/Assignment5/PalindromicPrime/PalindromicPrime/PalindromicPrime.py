def isPalindorme(num):
    temp = num
    rev = 0
    while temp != 0:
        rev = (rev * 10) + (temp % 10)
        temp //= 10
    if (num == rev):
        return True
    else:
        return False

def isPrime(num):
    if (num == 1):
        return False
    if (num > 1):
        for i in range (2,num):
            if (num % i) == 0:
                return False
    return True

def main():
    x = 2
    count = 1
    while (count <= 50):
        if (isPalindorme(x) and isPrime(x) and count % 10 == 0):
            print(x)
            count += 1
        elif (isPalindorme(x) and isPrime(x)):
            print(x, end=", ")
            count += 1
        x += 1
main()