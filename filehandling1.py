file=open("C:\\Users\\Ansar\\PycharmProjects\\pythonProject1\\myfile.txt", 'r')
#print(file.read()) # read entire content from the file
#print(file.read(10)) # read given characters from the file
#print(file.readline())
#print(file.readlines()) #read the entire content at once in array format

for l in file:
    print(l)
file.close