
nums = []

num_of_values = int(input("how many values do you want to add? "))

for i in range(num_of_values):

    values = int(input(f"Enter the value number {i+1}: "))

    nums.append(values)

print(f" your list values: {nums}")

q = input("do you want to get the sum of the values or the average of them? sum/average: ")

if q.lower() =="sum":
    sum = sum(nums)
    print(f"the sum of your list is: {sum}")

elif q.lower() == "average":
    average = sum(nums)/len(nums)
    print(f"the average of you list is: {average}")

print("Thanks for using the program ")


# made by yanal_abu_alrob
