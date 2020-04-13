def enlarge(i):
    return i * 100

if __name__ == "__main__":
    #only run if invoked from the command line
    #not if imported by another file
    
    my_number = float(input("please input a number: "))
    n = enlarge(my_number)
    print(n)

# cannot be in global scope
#yes