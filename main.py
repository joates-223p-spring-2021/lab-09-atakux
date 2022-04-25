# -*- coding: utf-8 -*-
"""
Angela DeLeo
CPSC 223P-01
Mon Apr 25, 2022
atakux707@csu.fullerton.edu
"""


def getStudents():
	"""get all the students from the grades file"""
	temp = []
	studentList = []

	with open("grades.txt", 'r') as assignmentFile:
		#parse thru and add to temp list
		for line in assignmentFile:
			line = line.strip('\n')

			#split by comma
			student = line.split(',')

			temp.append(student)

	#remove top line
	temp.pop(0)

	#save only the first column of each row
	for i in range(len(temp)):
		studentList.append(temp[i][0])

	return studentList


def getGrades():
	"""get all the grades from the grades file"""
	grades = []

	with open("grades.txt", 'r') as assignmentFile:
		#parse thru and add to temp list
		for line in assignmentFile:
			line = line.strip('\n')

			#split by comma
			grade = line.split(',')

			grades.append(grade)

	#remove top line
	grades.pop(0)

	return grades


def getAttendance():

	attendance = []

	with open("attendance.txt", 'r') as attendanceFile:
		for line in attendanceFile:
			line = line.strip('\n')

			attend = line.split(',')

			attendance.append(attend)

	attendance.pop(0)

	return attendance


def getDates():
	"""get all dates"""
	with open("attendance.txt") as attendanceFile:
		#only read in the first line to get the titles
		line = attendanceFile.readline()
		line = line.strip('\n')

		#separate by comma
		dates = line.split(', ')

	#remove the student column to keep only dates
	dates.pop(0)

	return dates


def getAssignmentNames():
	"""lists all the assignment names"""
	with open("grades.txt", 'r') as assignmentFile:
		#only read in the first line to get the titles
		line = assignmentFile.readline()
		line = line.strip('\n')

		#separate by comma
		assigns = line.split(', ')

	#remove the student column to keep only assign names
	assigns.pop(0)


	return assigns



class Student:
	#main lists
	students = getStudents()
	assigns = getAssignmentNames()
	dates = getDates()
	
	#full files for parsing:
	fullGrades = getGrades()
	fullAttends = getAttendance()

	#secondary lists
	grades = []
	attendance = []


	def listStudents(self):
		"""option 1: List Students"""
		for i in range(len(self.students)):
			print(self.students[i])

	def listGrades(self):
		"""option 2: List Grades"""
		#access each row
		for i in range(len(self.students)):
			print(f"\n{self.students[i]}", end="\n")
			#access each cell
			for j in range(len(self.assigns)):
				print(f"{self.assigns[j]}: {''.join(self.fullGrades[i][j+1])}")

	def listAttendance(self, person):
		"""option 3: List Attendance"""
		print(self.students[person-1])
		#access each row and column
		for i in range(len(self.dates)):
			status = ''.join(self.fullAttends[person-1][i+1])

			if status == 'p':
				status = "Present"
			elif status == 'a':
				status = "Absent"
			else:
				status = ''

			print(f"{self.dates[i]}: {status}")

	def submitGrade(self, assignmentName):
		"""option 4: Submit Grade"""
		#receive user input for the students grades and store in a list
		for i in range(len(self.students)):
			grade = input(f"\nGrade for {self.students[i]} for {self.assigns[assignmentName - 1]} > ")
			self.fullGrades[i].insert(assignmentName, grade)

		with open("grades.txt", 'r+') as assignmentFile:
			lines = assignmentFile.readlines()

			#get back to the start
			assignmentFile.seek(0)

			#rewrite the first line
			assignmentFile.write(lines[0])

			#writing the student grade to each line
			for i in range(min(len(lines), len(self.fullGrades))):
				assignmentFile.write(lines[i+1].rstrip(',\n'))
				assignmentFile.write(',')
				assignmentFile.write(''.join(self.fullGrades[i][assignmentName])+(','*(len(self.assigns)-assignmentName)))
				assignmentFile.write('\n')
			assignmentFile.truncate()


	def takeAttendance(self, date):
		#receive user input for the students grades and store in a list
		for i in range(len(self.students)):
			attend = input(f"\nStudent {self.students[i]} (p/a) > ")
			self.fullAttends[i].insert(date, attend)

		with open("attendance.txt", 'r+') as attendanceFile:
			lines = attendanceFile.readlines()

			#get back to the start
			attendanceFile.seek(0)

			#rewrite the first line
			attendanceFile.write(lines[0])

			#writing the student grade to each line
			for i in range(min(len(lines), len(self.fullAttends))):
				attendanceFile.write(lines[i+1].rstrip(',\n'))
				attendanceFile.write(',')
				attendanceFile.write(''.join(self.fullAttends[i][date])+(','*(len(self.dates)-date)))
				attendanceFile.write('\n')
			attendanceFile.truncate()




#set asking to true for the while loop
asking = True

#instantiate Student object
student = Student()

#while the user has not quit	
while asking:	
	#display user options
	print("What do you want to do?\n1 - List all students\n2 - List all grades\n3 - List attendance\n4 - Submit a grade\n5 - Take attendance\nQ - Quit\n")
	
	#receive user input
	choice = input("> ").lower()

	#check if user quit
	if choice == 'q':
		asking = False

	#if user clicked 1, call listStudents
	elif choice == '1':
		student.listStudents()
		print("\n")

	#if user clicked 2, call listGrades
	elif choice == '2':
		student.listGrades()
		print("\n")

	#if user clicked 3, call displayAttendance
	elif choice == '3':
		#grab student names
		listOfStudents = getStudents()
		#receive input from user to grab the student 
		#we want to display attendance for
		print("Which student?")

		#display all students w a corresponding number
		for i in range(len(listOfStudents)):
			print(f"{i+1} - {listOfStudents[i]}")

		#receive input and call displayAttendance
		person = int(input("\n> "))
		student.listAttendance(person)

		print("\n")


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
			print("invalid input. try again.")
		finally:
			print("\n")


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
			print("invalid input. try again.")
		finally:
			print("\n")

	#if the users input does not match one of the options,
	#prompt them again to input a proper option
	else:
		print("Invalid choice. Try again.")
		continue
