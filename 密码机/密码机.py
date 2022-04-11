import time


def password(str1, k, *v):
    str2 = ""
    for i in str1:
        str2 += chr(ord(i)+k)
    for i in v[0]:
        str2 = str2[-i:]+str2[:-i]
    return str2


def xpassword(str1, k, *v):
    for i in v[0]:
        str1 = str1[-i:]+str1[:-i]
    str2 = ""
    for i in str1:
        str2 += chr(ord(i)-k)
    return str2


with open("D:/000-EVAN/PycharmProjects/Python_books1/Users.txt", "r+") as file:
    dict1 = eval(file.read())
name = input("Please enter the user name:")
if name in dict1.keys():
    word = input("Please enter the password:")
    while word != dict1[name]:
        word = input("Please enter the password again:")
    print("Login successful!")
    print("--------------------------------")
    time.sleep(0.5)
    print("- User name:%s" % name)
    time.sleep(0.5)
    print("- password:%s" % word)
    time.sleep(0.5)
    print("- Encryption enter 1")
    time.sleep(0.5)
    print("- decryption enter 2")
    time.sleep(0.5)
    print("- Document encryption enter 3")
    time.sleep(0.5)
    print("- Document decryption enter 4")
    time.sleep(0.5)
    print("--------------------------------")
else:
    print("There is no this user name")
    if input("Whether to register new account (n/y)\n") == "y":
        new_name = input("Please set the user name:")
        new_password = input("Please set the password:")
        dict1[new_name] = new_password
        with open("D:/000-EVAN/PycharmProjects/Python_books1/users.txt", "w") as file:
            file.write(str(dict1))
    name = input("Please enter the user name again:")
    if name in dict1.keys():
        word = input("Please enter the password:")
        while word != dict1[name]:
            word = input("Please enter the password again:")
        print("Login successful!")
        print("--------------------------------")
        time.sleep(0.5)
        print("- User name:%s" % name)
        time.sleep(0.5)
        print("- password:%s" % word)
        time.sleep(0.5)
        print("- Encryption enter 1")
        time.sleep(0.5)
        print("- decryption enter 2")
        time.sleep(0.5)
        print("- Document encryption enter 3")
        time.sleep(0.5)
        print("- Document decryption enter 4")
        time.sleep(0.5)
        print("--------------------------------")


x = "y"
while x == "y":
    a = input(">>>")
    if a == "1":
        n = input("Please enter the need to encrypt the information:")
        k1 = int(input("The input values k:"))
        v1 = list(map(int, input("Enter multiple value v(v<%d,Values separated by Spaces):" % len(n)).split()))
        pw = password(n, k1, v1)
        print("Encryption is completed, the password is\n%s" % pw)
    if a == "2":
        n = input("Please enter the need to decrypt the password:")
        k1 = int(input("The input values k:"))
        v1 = list(map(int, input("Enter multiple value v(Values separated by Spaces):").split()))
        sk = xpassword(n, k1, v1)
        print("decryption is completed, the sentence is\n%s" % sk)
    if a == "3":
        path = input("Please enter the path to need to encrypt the document:")
        with open(path, "r+") as f:
            txt = f.read()
            k1 = int(input("The input values k:"))
            v1 = list(map(int, input("Enter multiple value v(v<%d, Values separated by Spaces):" % len(txt)).split()))
            pw = password(txt, k1, v1)
            file_name = input("Please enter the document name:")
            with open(file_name, "w") as f2:
                f2.write(pw)
            print("Encryption completed.")
    if a == "4":
        path = input("Input the path need to decrypt files:")
        with open(path, "r+") as f:
            txt = f.read()
            k1 = int(input("The input values k:"))
            v1 = list(map(int, input("Enter multiple value v(Values separated by Spaces):").split()))
            xw = xpassword(txt, k1, v1)
            file_name = input("Please enter the document name:")
            with open(file_name, "w") as f2:
                f2.write(xw)
            print("Decrypt the complete.")
    x = input("To continue or exit(y/n)\n")
print("Thank you for your use.")