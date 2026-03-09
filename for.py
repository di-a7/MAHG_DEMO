lis=[0,1,2,3]
for l in lis:
  print(f"{l}")
  break

# create a list of hobbies

hobbies=['cricket','football','badminton','chess','sudoku','Go']
for hobby in hobbies:
  print(f"My hobbies are {hobby}")
  if hobby=='football':
    continue

user_list = []

user = input("Enter your name: ")
for _ in range(1):
    user_list.append(user)
    if user == user_list:
       break
print(user_list)