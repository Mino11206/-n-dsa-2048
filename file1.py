def isPrime(n):
   if n <= 1:
       return False
   for i in range(2, n):
       if n % i == 0:
           return False
   return True


# Nhận một chuỗi các số nguyên từ người dùng, cách nhau bởi dấu cách
input_str = input("Enter a list of numbers separated by space: ")


# Tách chuỗi thành các chuỗi con và chuyển đổi chúng thành số nguyên
numbers = [int(num) for num in input_str.split()]


print("The list of numbers is:", numbers)


# Test the function on the first number of the list if it exists
if numbers:
   num_to_check = numbers[0]
   if isPrime(num_to_check):
       print(f"{num_to_check} is a prime number.")
   else:
       print(f"{num_to_check} is not a prime number.")
