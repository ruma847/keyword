a = input("Enter a word")
found_a = False
for i in a:
    if i == 'A':
        print("A is found")
        found_a = True
        break
    else:
        pass

if not found_a:
    print("A is found")
