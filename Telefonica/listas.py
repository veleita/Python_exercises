def get_sum(num_list):
    return sum(num_list)

def reverse_list(original_list):
    return original_list[::-1]

lst = []

n = int(input("Enter number of elements : "))

for i in range(0, n):
  num = int(input())
  lst.append(num)

print("The sum of the elements of the list is ", get_sum(lst))
print("The reversed list is ", reverse_list(lst))
