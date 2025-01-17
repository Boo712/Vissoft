def calculate_sum(n):
    return n * (n + 1) // 2

if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a positive integer greater than 0.")
        else:
            print(f"The sum of numbers from 1 to {n} is: {calculate_sum(n)}")
    except ValueError:
        print("Please enter a valid integer.")