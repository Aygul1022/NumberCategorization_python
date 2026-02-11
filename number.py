def is_even(num):
        return num % 2 == 0
    
def is_odd(num):
        return num % 2 != 0
    
def is_prime(num):
        if num <= 1:
            return False
        elif num == 2:
            return True
        else:
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    return False
            return True
    
def main():
        try:
            number = int(input("Enter a number: \n"))
            categorise = []
            
            if is_even(number):
                categorise.append("Even")
            else:
                categorise.append("Odd")
            
            if is_prime(number):
                categorise.append("Prime")
            
            print(f"The number : {number}")
            
            if categorise:
                print(f"is categorised as: ")
                for i in categorise:
                    print(f" - {i}")
            else:
                print("does not belong to any categories")
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
if __name__ == "__main__":
        main()