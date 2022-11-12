
print("Breaks\n")

number = 10

for i in range(number):
    if i == 5:
        break
    print("for: number:", i)

while number > 0:
    if number == 5:
        break
    print("while: number:", number)
    number -= 1

print("\n Continue\n")

number = 10
for i in range(number):
    if i == 5:
        continue
    print("for: number:", i)

while number > 0:
    if number == 5:
        continue
    print("while: number:", number)
    number -= 1

print("\nelse\n")

number = 5
for i in range(number):
    print("for: number:", i)
else:
    print("for: end of scope")

