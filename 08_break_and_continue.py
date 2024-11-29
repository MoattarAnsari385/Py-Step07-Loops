# BREAK
for i in range(100):
    if(i == 56):
        break # Exit the loop right now
    print(i)

for i in range(10):
    if(i == 5):
        break
    print(i)
print("")

# CONTINUE
for i in range(100):
    if(i % 2 == 0):
        continue # Skip the even numbers
    print(i)

for i in range(100):
    if(i % 2 != 0):
        continue # Skip the odd numbers
    print(i)