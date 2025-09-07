#Python Loops:

count = 1
print("While Loop")
while count <=5:
  print(f"count,{count}")
  count+=1
print("For Loop")
for i in range(1,8):
   print("you are a beginner")
print("For Loop")
for i in range(8):
   print("you are a learner") 
for i in range(5):
    if i == 2:
        continue
    print(i)
#Using Continue skips the iteration on given condition satisfies
for i in range(5):
    if i == 2:
        break
    print(i)
#Using break exits the loops on given condition satisfies

for i in range(1,21):
    
    if i%3 == 0:
        continue
    print(i)
    if i == 17:
        break
#prints numbers from 1 to 20 skipping multiples of 3 and breaks loop when i=17
#inner Loops

n=5
for i in range (n):
    for j in range(i+1):
        print("*",end=" ")
    print()   
#This prints a triangle of stars
