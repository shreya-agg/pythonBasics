num_terms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0

if num_terms <= 0:
    print("Please enter a positive integer")
elif num_terms == 1:
    print(f"Fibonacci sequence up to {num_terms}:")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < num_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
