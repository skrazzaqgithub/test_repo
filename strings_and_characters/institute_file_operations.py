file = "authorizationPostCall.py"
file1 = "First_Program_Selenium"
with open(file, 'r') as fo:
    with open(file1, 'w') as fow:
        for line in fo.readlines():
            print(line.strip("\n"))
            fow.write(line) #string.strip() removes the space..
            # print("Line: ", fo.readline())
print("file open for read and writng to the file is completed")

# string1 = "!Rama is good boy!"
# print(string1.strip("!"))

Roles & Responsibilities:

#Writing the scripts
#Execute the scripts
#Modifying the scripts
#Submit for review and make sure it is reviewed by product owner
#Collect the logs
#commiting the code in github