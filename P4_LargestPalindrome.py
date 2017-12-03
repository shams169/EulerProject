def isPalindrome(n):

    """
    using list indexing
    """
    return str(n) == str(n)[::-1]

    # pal = str(n)
    # start = 0
    # end   = len(pal) -1
    #
    # for i in range(len(pal) // 2):
    #     #print(pal[start], pal[end])
    #     if( pal[start] == pal[end]):
    #         start += 1
    #         end   -= 1
    #         continue
    #     else:
    #         return False
    # return True



def largestPalindromeProduct():
    x = 999*999

    while(x > 0):
        if(isPalindrome(x)):
            return x
        x -= 1


def main():
    #x = isPalindrome(334373)
    print(largestPalindromeProduct())



if __name__ == '__main__':
    main()