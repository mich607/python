def is_prime(num):
    """ Function to check if a number is prime """
    if num <= 1:
        return False  # 1 and numbers less than 1 are not prime numbers
    elif num == 2:
        return True   # 2 is the only even prime number
    elif num % 2 == 0:
        return False  # Other even numbers are not prime numbers
    else:
        # Check for odd factors from 3 up to the square root of num
        sqrt_num = int(num**0.5) + 1
        for i in range(3, sqrt_num, 2):
            if num % i == 0:
                return False  # If num is divisible by any odd number, it's not prime
        return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
