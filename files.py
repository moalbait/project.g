try:
    with open("myfile.txt") as lines:
        count= 0
        for line in lines:
            count +=1
            if not line.startswith("since"):
                continue
            print(line.strip())
    print("Total lines starting with 'since': ", count)
except FileNotFoundError:
    print("The file 'myfile.txt' was not found.")

print("__________________________________________________________________")
print("Emails from uct.ac.za domain:")
try:
    with open("emails.txt") as lines:
        for line in lines:
            line =line.strip()
            if line.find('@uct.ac.za')== -1: 
                continue
           #print(line)
except FileNotFoundError:
    print("The file 'myfile.txt' was not found.")

print("__________________________________________________________________")

fname = input("enter file name:")
try:
    lines= open(fname) 
except:
    print("File cannot be opened:", fname)
    exit()

count =0
for line in lines:
        
    if line .startswith("Subject:"):
        count +=1
print('There were', count, 'subject lines in',line)


try:
    with open("writefile.txt", "w") as file:
        file.write("This is new file created in python programming.\n")
        file.write("My name is Mohammed Al-Bayati.\n")
        file.write("I am learing AI and ML.\n")
except :
    print ("Error: could not find the writeflie.txt file")

try:
    with(open('writefile.txt') as file):
        for line in file:
            print(line.strip())
except:
    print("Error: could not find the writeflie.txt file")