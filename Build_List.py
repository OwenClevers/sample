def make_list():
    result = [] #Initially assign an empty list
    in_val = 0 #Loop at least once
    while in_val >= 0:
        in_val = eval(input("Enter an integer (-1 quits) : "))
        if in_val >= 0:
            result +=[in_val] #Add an item to the list
    return result
def main():
    col = make_list()
    print(col)
main()
