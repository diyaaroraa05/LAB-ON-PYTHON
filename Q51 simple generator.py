#Program to Create a Simple Generator:
def count_up_to(max):
 count = 1
 while count <= max:
  yield count
  count += 1
for num in count_up_to(5):
 print(num) # Outputs: 1, 2, 3, 4, 5
print("This code is written by DIYA ARORA ERP-0221BCA059")
