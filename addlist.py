def main():
    #Set up the variables
    sum = 0.0
    entries = int(input("How many number to add: "))
    ints = []

    #Enter list elements
    
    for y in range(1, entries+1):
        print("Enter number "+str(y)+": ",end='')
        num = eval(input())
        ints =ints + [num]
        sum+=num

    #calculate average
    print('Numbers Entered: ')
    for num in ints:
        print(num,end=' ')
    print()

    print("Sum = ",sum," and Average = ",sum/entries)
main()
