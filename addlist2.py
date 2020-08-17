def sum_positive(n):
    sum = 0
    for item in n:
        item = item if item > 0 else item * -1
        sum += item
    return sum
def count_evens(n):
    count = 0
    for item in n:
        if item % 2 == 0:
            count += item
        elif item % 2 != 0:
            count += 0
        elif n == []:
            return 0
    return count
def reverse(n):
    for i in range(len(n)-1, -1,-1):
        print(n[i], end=' ')
def main():
    col = [2,-5,6,-8]
    n = [2,3,4,5,6]
    x = []
    print(sum_positive(col))
    print(count_evens(n))
    print(count_evens(x))
    print(reverse(col))
    print(reverse(n))
main()
