# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.
dictionaryData = {}

numberOfLoops = int(input("How many times would you like to input course ID's and Names? "))

for x in range(numberOfLoops):
    gettingTheID = input("What is the course ID? ")
    gettingTheCourseName = input("What is the name of the course ")
    dictionaryData[gettingTheID] = gettingTheCourseName

courseIdInput = input("Insert a course ID ")
print()
for key in dictionaryData:

    if key.count(courseIdInput) > 0:
        print (key, dictionaryData[key])


