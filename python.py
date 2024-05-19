print("My name is Asim")


#Addition:
OOP=a=88
Programming=b=90
LinearAlgebra=c=85
total=a+b+c
print(total)

#Subtraction:
OOP=a=88
Programming=b=90
LinearAlgebra=c=85
Minus=a-b-c
print(Minus)


#Multiplication:
OOP=a=88
Programming=b=90
LinearAlgebra=c=85
Multi=a*b*c
print(Multi)


#Division:
OOP=a=88
Programming=b=90
LinearAlgebra=c=85
Divide=a/b/c
print(Divide)




# If you pay 15% tax of your earning that is 30000 write a program in python to calculate the tax you pay 

Earning=30000
Taxrate=15/100
Taxpaid=Earning*Taxrate
print(Taxpaid)



#Calculate the percentage of your courses of current semester take values from the table above
totalmarks=300
OOP=a=88
Programming=b=90
LinearAlgebra=c=85
obtainedmarks=a+b+c
obtainedmarks
percentage=(obtainedmarks/totalmarks)*100
print(percentage)


#Use the round of function in python and round of any three numbers to 2,3,4 decimal points
a=87.66666666666667
z=round(a,2)
#taking two digits only after point
print(z)

b=827.54366666666667
y=round(b,3)
print(y)

c=33.759832323
x=round(c,4)
print(x)


# Use type method in python for c = 12.4 and 3000
x=12.4
t=type(x)
print(t)

y=3000
zz=type(y)
print(zz)


# Convert 6.0 into 6
y=6.0
convert=int(y)
print(convert)



# Use string slicing to grab the word 'thin'  from inside 'thinktank'/Slicing
a="Thinktank"
print(a[0:4])



# Use indexing value of your class id to grab character from the string
id = " BSE-22F-102 "
index = 7
character = id[index]
print(character)


# Store ABC in a variable and perform following operations
# Print all strings
a="ABC"
print(a)


#Grab alternate letters from ABC
aa=" ABC "
print(aa[0:-1])

#Reverse your string
reverse=" ABC "
print(reverse[::-1])
#Grab 8 letters from the string and start from the letter which is the first letter of your name.
name="Asim Hayat"
print(name[:8])


# Write the code in python to generate following output using string logic abbcccddddeeeee
# output = ''
for i in range(1, 6):
    output += chr(96 + i) * i
print(output)


# Apply the .format method on semester courses write Name of one course and Name of three courses
print("name of one course is{}".format(' DSA'))
print("name of three courses are{} {} {}".format(' DSA,','Formal Methods',' and SCD'))



#Write intro about you , convert into list structure and then grab all words excluding 1st and last word, from  your introduction
intro="This is Asim. I have completed intermediate from a private college and current doing BS program in SE"
s=intro.split()
print(s[1:-1])


# Name of six courses randomly and arrange them in alphabetical order using indexing in .format method

# Generate six random course names
courses = [
    "Mathematics",
    "Physics",
    "Biology",
    "Chemistry",
    "History",
    "Computer Science"
]
# Sorting
sorted_courses = sorted(courses)
print(sorted_courses)

# .format
print("name of six courses are {0} {1} {5} {2} {4} {3}".format('English ,','Maths,','Science','urdu','islamiyat,','Pst,'))

# Assign the key words to all semester courses and call them using .format method
print("name of six courses are {s0} {s4} {s1} {s5} {s2} {s3}".format(s0='English ,',s1='Maths,',s2='Science and ',s3='urdu',s4='islamiyat,',s5='Pst,'))

# Apply float formatting method on following numbers with precision of 5
a=200.340982589
print('The round of number is{n:1.5}'.format(n=a))


40/66611
b=40/66611
print(b)
print("The round of number is {n:1.4f}".format(n=b))

1.534854395
c=1.534854395
print("The round of number is {n:1.4f}".format(n=c))



# counting in minus 1 to 10
for i in range(-1, -11, -1):
    print(i)



# creating Set and use of add method
course = set()
course.add("OOP")
course.add("SE")
course.add("Communication Skills")
course.add("DS")
course.add("Probability and Statistics")
print(course)
print(type(course))


# Remove a course from the set(indexing not possible in sets)
Courses = {'Mathematics', 'Computer science', 'physics'}
Courses.remove('Mathematics')
print(Courses)


# conversion from list to tupple
even_numbers = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
even_numbers_tuple = tuple(even_numbers)
print(even_numbers_tuple)

#dictionary
word_dict = {
    "apple": "A fruit that is red, round, and tasty.",
    "banana": "A yellow fruit that is soft and can be used in baking.",
}
#keys
words = list(word_dict.keys())
print("Words:", words)
#Values
meanings = list(word_dict.values())
print("Meanings:", meanings)
#Updating key with different word
word_dict["apple"] = "Newkey"
print(word_dict)
print(type(word_dict))
course_dict = {
    1: "Computer Science",
    2: "Data Science",
}
courses = list(course_dict.values())
print("Courses:", courses)
course_ids = list(course_dict.keys())
print("Course ids:", course_ids)
course_dict[1] = "DSA"
courses_and_ids = list(course_dict.items())
print("Courses and ids:", courses_and_ids)


#empty dictionary
student_data = {}
student_data = {
    "John": 101,
    "Alice": 102,
}
student_data.update({"Bob": 103})
print(student_data)
# Convert the dictionary into a list of tuples and print the list
student_list = list(student_data.items())
print(student_list)














