def max_three(num1, num2, num3):
    return max(num1, num2, num3)

def is_vocal(character):
    vocals = ['a', 'e', 'i', 'o', 'u']
    if character in vocals:
        return True
    else:
        return False

print("Test max_three")
num1 = int(input("- Enter num1\n"))
num2 = int(input("- Enter num2\n"))
num3 = int(input("- Enter num3\n"))
print("The greatest number is", str(max_three(num1, num2, num3)))

print("\nTest is_vocal")
character = input("Enter a character\n")
print(character, "is ", end='')
if is_vocal(character) == False:
    print("not ", end='')
print("a vocal")
