def print_multiplication_table(n):
    for i in range(1,11):
        for j in range(1, n+1):
            print(f"{i*j}", end="\t")
        print()
mul = int(input("Enter the number:"))
print_multiplication_table(mul)