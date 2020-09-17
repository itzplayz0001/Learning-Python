thisset = {"name1", "name2", "name3"}
print("[1] View List")
print("[2] Check if user exists")
print("[3] Add user")
print("[4] Remove user")
n = input("What would you like to do? : ")
if n == '1':
    print("\n=== List of Users ===")
    print(len(thisset))
    for x in thisset:
        print(x)

if n == '2':
    find = input("Enter the user's name : ")
    print(find in thisset)

if n == '3':
    add = input("Enter the name you wish to add : ")
    thisset.add(add)
    print(thisset)

if n == '4':
    remo = input("Who do you wish to remove: ")
    thisset.remove(remo)
    print(thisset)
