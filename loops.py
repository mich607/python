# while loop
numbers = 25
while numbers <=30:
    print(numbers)
    numbers = numbers + 1

# decrementing
count = 10
while count >=1:
    print(count)
    count -=1

# break and continue statement
z = 100
while z <= 105:
    print(z)
    if z == 103:
        break
    z += 1

# skipping a value
m = 34
while m < 40:
    m += 1
    if m == 37:
        continue
print(m)

#loop
for num in range(10):
    print(num)
for z in range(1,10):
    print(z)

for w in range(100,110,4):
    print(w)