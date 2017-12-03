def factors(n):
    facs = []
    for i in range(1, n//2):
        # print(i)
        if n%i ==0:
            facs.append(i)
    facs.append(n)
    return facs

def isPrime(n):
    if n == 2 or n == 3:
        return True
    elif n%2 == 0:
        return False
    elif n%3 == 0:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False


    return True

"""
Using fundamental theorem of arithmetic which states :
Any integer greater than 1 is either a prime number, or can be written as a unique product of prime numbers (ignoring the order)
"""
def fta(newnumm):
    counter = 2;
    while (counter * counter <= newnumm):
        if (newnumm % counter == 0):
            newnumm = newnumm / counter;
            largestFact = counter;
            print((counter*counter), newnumm, largestFact)
        else:
            print(counter)
            counter += 1;


    if (newnumm > largestFact):
        largestFact = newnumm;

    print(largestFact)



def main():
    #600851475143

    fta(600851475143)
    # L = factors(60085147)
    # print(L)
    #
    # for i in L[::-1]:
    #     if(isPrime(i)):
    #         print("Largest prime factor is "+str(i))
    #         break

if __name__=='__main__':
    main()