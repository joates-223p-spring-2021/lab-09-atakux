# -*- coding: utf-8 -*-
"""
Angela DeLeo
CPSC 223P-01
Mon Apr 25, 2022
atakux707@csu.fullerton.edu
"""





#file opening functions

def listStudents():
	"""lists all the students"""

	studentList = []

	#open the attendance file
	with open("attendance.txt", 'r') as attendanceFile:		
		#loop thru all the lines
		for student in attendanceFile:

			#remove commas and endlines
			studentList.append(student.replace(',,,,,,,,,,,,,,,,', ' ').strip('\nap '))

	#remove the top line
	studentList.pop(0)

	#return the list of students
	return studentList



def getDates():
	"""grab all the dates listed in attendance file"""

	with open("attendance.txt", 'r') as attendanceFile:
		#read the first line of the file
		dates = attendanceFile.readline()
		
		#remove commas and endlines
		dates = dates.replace('\n', '').split(', ')

		#remove the first column (student)
		dates.pop(0)

	return dates




def getAssignmentNames():
	"""lists all the assignment names"""

	#open the grades file
	with open("grades.txt", 'r') as assignmentFile:
		assigns = assignmentFile.readline()
		#read each line into assignmentList
		assigns = assigns.replace('\n', '').split(', ')

		#remove Student
		assigns.pop(0)

	#return the list of assignment names
	return assigns



def listGrades():
	"""lists all the grades"""
	gradesList = []

	#grab all the grades
	with open("grades.txt", 'r') as assignmentFile:
		#loop thru all the lines
		for line in assignmentFile.readlines():

			#remove commas and new lines
			gradesList.append(line.replace('\n', '').split(',,,,,, '))

	#remove the first line
	gradesList.pop(0)

	return gradesList


def listAttendance():
	"""lists all the attendance"""
	attendList = []

	with open("attendance.txt", 'r') as attendanceFile:
		#loop thru all the lines
		for line in attendanceFile.readlines():

			#remove commas and new lines
			attendList.append(line.replace('\n', '').split(',,,,,,,,,,,,,,,, '))

	#remove the first line
	attendList.pop(0)

	return attendList





#student class
class Student:
	#declare the main lists using our file functions
	students = listStudents()
	assignments = getAssignmentNames()
	assignGrades = listGrades()
	rollCall = listAttendance()
	datesList = getDates()

	#declare the last two main lists as empty
	listOfGrades = []
	listOfRolls = []


	
	def displayAssignmentNames(self):
		"""display assignment names	"""
		for i in range(len(self.assignments)):
			print(self.assignments[i])



	#option 1
	def displayStudents(self):
		"""display students"""
		for i in range(len(self.students)):
			print(self.students[i])		

		#spacing
		print("\n")



	#option 2
	def displayGrades(self):
		"""display students grades"""
		#parse thru the files
		for i in range(len(self.students)):
			#print student name	
			print(f"\n{self.students[i]}", end='\n')

			for j in range(0,6):
				print(f"{self.assignments[j]}: ",end='')
				print(f"{''.join(self.assignGrades[i][j+1:j+j+2])}")

		#spacing
		print("\n")




#need to figure out how to print the thingies
#*************************************************************
	#option 3
	def displayAttendance(self, person):
		"""display attendance of a given student"""
		status = ''
		#print students name
		print(self.students[person-1])
		
		#print all the days
		for i in range(0,16):
			status = ''.join(self.rollCall[person-1][i+1:])

			if 'p' in status:
				print(f"{self.datesList[i]}: Present")
			elif 'a' in status:
				print(f"{self.datesList[i]}: Absent")
			else:
				print(f"{self.datesList[i]}: ")

		#spacing
		print("\n")
#*************************************************************



	#option 4
	def submitGrade(self, assignmentName):
		"""submit grades and write them to the grades.txt"""

		#receive user input for the students grades and store in a list
		for i in range(len(self.students)):
			grade = input(f"\nGrade for {self.students[i]} for {self.assignments[assignmentName - 1]}: ")
			self.listOfGrades.append(grade)

		#write the grades to the grades.txt file
		with open("grades.txt", 'r+') as assignmentFile:
			lines = assignmentFile.readlines()

			#get back to the start
			assignmentFile.seek(0)

			#rewrite the first line
			assignmentFile.write(lines[0])

			#writing the student grade to each line
			for i in range(min(len(lines), len(self.listOfGrades))):
				assignmentFile.write(lines[i+1].rstrip('\n'))
				assignmentFile.write(' ')
				assignmentFile.write(str(self.listOfGrades[i]))
				assignmentFile.write(' ,,,,,, ')
				assignmentFile.write('\n')

			assignmentFile.truncate()

		#spacing
		print("\n")




	#option 5
	def takeAttendance(self, date):
		"""take attendance and write them to attendance.txt"""
		for i in range(len(self.students)):
			attended = input(f"\nStudent {self.students[i]} (p/a): ")
			self.listOfRolls.append(attended)

		with open("attendance.txt", 'r+') as attendanceFile:
			lines = attendanceFile.readlines()

			#get back to the start
			attendanceFile.seek(0)

			#rewrite the first line
			attendanceFile.write(lines[0])

			#writing the student roll to each line
			for i in range(min(len(lines), len(self.listOfRolls))):
				attendanceFile.write(lines[i+1].rstrip('\n'))
				attendanceFile.write(' ')
				attendanceFile.write(str(self.listOfRolls[i]))
				attendanceFile.write(' ,,,,,,,,,,,,,,,, ')
				attendanceFile.write('\n')

			attendanceFile.truncate()

		#spacing
		print("\n")	




#set asking to true for the while loop
asking = True

#instantiate Student object
student = Student()
listOfStudents = list(listStudents())

#while the user has not quit	
while asking:	
	#display user options
	print("What do you want to do?\n1 - List all students\n2 - List all grades\n3 - List attendance\n4 - Submit a grade\n5 - Take attendance\nQ - Quit\n")
	
	#receive user input
	choice = input("> ").lower()

	#check if user quit
	if choice == 'q':
		asking = False

	#if user clicked 1, call displayStudents
	elif choice == '1':
		student.displayStudents()

	#if user clicked 2, call displayGrades
	elif choice == '2':
		student.displayGrades()

	#if user clicked 3, call displayAttendance
	elif choice == '3':
		#receive input from user to grab the student 
		#we want to display attendance for
		print("Which student?")

		#display all students w a corresponding number
		for i in range(len(listOfStudents)):
			print(f"{i+1} - {listOfStudents[i]}")

		#receive input and call displayAttendance
		person = int(input("\n> "))
		student.displayAttendance(person)


	#if user clicked 4, call submitGrade
	elif choice == '4':
		#grab the assignment names list from the file
		assigns = getAssignmentNames()

		#receive input from the user to decide which 
		#assignment to input into
		print("Which assignment?")

		#display all assignment names w a corresponding number
		for i in range(len(assigns)):
			print(f"{i+1} - {assigns[i]}")

		#receive input and call submitGrade
		try:
			submition = int(input("\n> "))
			student.submitGrade(submition)
		except:
			print("invalid input. try again.\n")


	#if user clicked 5, call takeAttendance
	elif choice == '5':
		#grab the dates list from the file
		dates = getDates()

		#receive input from the user to decide which
		#date to take attendance for
		print("Which date?")

		#display all dates w a corresponding number
		for i in range(len(dates)):
			print(f"{i+1} - {dates[i]}")

		#receive input and call takeAttendance
		try:
			day = int(input("\n> "))
			student.takeAttendance(day)
		except:
			print("invalid input. try again.\n")

	#if the users input does not match one of the options,
	#prompt them again to input a proper option
	else:
		print("Invalid choice. Try again.")
		continue
