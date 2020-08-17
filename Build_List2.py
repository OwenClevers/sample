def build_list():
    lst = [] #Initialize list to empty
    n = 0
    print("Enter elements of the list: EXIT exits")
    while n >= 0:
        print("Enter ",n," Element",end=': ')
        val = input()
        if val == 'Exit' or val == 'EXIT' or val == 'exit':
            break
        else:
            lst += [val]
            n += 1
    return lst
def main():
    col = build_list()
    print(col)
main()
    
