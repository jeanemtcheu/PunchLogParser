"""
File: punchLogParser.py
Author: Jean Andre Emtcheu
Date: 10/7/2022
Description:  This program classifies students attendance by parsing through scattered swipe log entry data
"""

debug = False

from dataEntry import fill_roster
from dataEntry import fill_attendance_data


def list_students_not_in_class(roster, attendance):
   """
   Compare the swipe log with the given course roster. Place those students that
   did not show up for class into a list.
   :param: the class roster
   :param: the attendance for that day
   :return: the students who did not show up to class
   """
   present = []
   absent = []
   for name in roster:
      full_name = name.split(", ")
      last_name = full_name[0]
      first_name = full_name[1]
      #loop through the attendance list to compare what names are there


      for status in attendance:
         attendanceData = status.split(", ")
         a_l_name = attendanceData[0]
         a_f_name = attendanceData[1]
         a_time = attendanceData[2]
         a_date = attendanceData[3]

         a_full_name = a_l_name +", "+a_f_name
         present.append(a_full_name)

      if name not in present:
         absent.append(name)


   for i in absent:
      print(i)
   #print("first elemnt of the roster " + roster[0]


def list_all_times_checking_in_and_out(name, status):
   """
   Looking at the swiping log, this function will list all in and outs for a
   particular Student. Please note, as coded in the p1.py file given, this
   function was called three times with different student values.
   :param: the name of a student
   :param: the attendance swipe information (name, time and date)
   :return: the swipe information for the time they checked in and the time they checked out, if available
   """
   for i in status:
      full_details = i.split(", ")
      last_name = full_details[0]
      first_name = full_details[1]
      full_name = last_name +', ' + first_name

      if name == full_name:
         print(i)




def list_all_times_checked_in(status):
   """
   This function returns a list of when all student(s) FIRST swipe in.
   :param: the attendance swipe information (name, time and date)
   :return: the initial swipe of each student that swiped in
   """
   checked_in = []
   first_swipe = []
   for i in status:
      full_details = i.split(', ')
      last_name = full_details[0]
      first_name = full_details[1]
      full_name = last_name +', '+ first_name

      if full_name not in checked_in:
         checked_in.append(full_name)
         first_swipe.append(i)

      elif full_name in checked_in:
         break

   for i in first_swipe:
      print(i)

def list_students_late_to_class(time, status):
    """
    When given a timestamp string and the swipe log, a list of those records
    of students who swiped in late into the class is produced. This function
    returns a list of when all student(s) FIRST swipe in.
    :param: the time that class starts
    :param: the attendance swipe information (name, time and date)
    :return: the students who came to class late (after the referenced time in the first parameter)
    """

    checked_in = []
    first_swipe = []

    timestamp = time.split(':')
    time_format = int(''.join(timestamp))

    for i in status:
       full_details = i.split(', ')
       last_name = full_details[0]
       first_name = full_details[1]
       full_name = last_name + ', '  + first_name
       a_time = full_details[2]
       a_time_format = int(''.join(a_time.split(':')))

       if full_name not in checked_in:
          checked_in.append(full_name)
          if time_format < a_time_format:
             print(i)


def get_first_student_to_enter(status):
    """
    Simply, this function returns the student that swiped in first. Note,
    the order of the data entered into the swipe log as not the earliest
    student to enter.
    :param: the attendance swipe information (name, time and date)
    :return: the name of the first student to enter class in a "last-name first" format
    """


    numbers = []
    info = []
    for i in status:
       full_details = i.split(', ')
       last_name = full_details[0]
       first_name = full_details[1]
       full_name = last_name + ', '  + first_name
       a_time = full_details[2]
       a_time_format = int(''.join(a_time.split(':')))

       numbers.append(a_time_format)
       info.append(i)

    earliest = numbers[0]
    for value in numbers:
       position = numbers.index(value)
       name = info[position]
       if value < earliest:
          earliest = value

    for i in status:
       full_details = i.split(', ')
       last_name = full_details[0]
       first_name = full_details[1]
       full_name = last_name + ', '  + first_name
       a_time = full_details[2]
       a_time_format = int(''.join(a_time.split(':')))

       if a_time_format == earliest:
          answer = full_name



    print(answer)





def printList(mylist):
    """
    Simply prints the list. The function should not be able to change any
    values of that list passed in.
    :param: the name of the function along with any argument(s) put in the place of the functions parameter
    :return: the printed output of the function called
    """
    print(mylist)


if __name__ == '__main__':
    # Example, Dr. NIcholas, 9am class

    # load class roster here into a list
    classRoster = fill_roster()

    #figure out which attendance data file to load here

    #load data
    attendData = fill_attendance_data()

    #use different tests
    # make sure roster was filled
    #printList(classRoster)
    # make sure attendance data was loaded
    #printList(attendData)

    #list all those missing
    print("****** Students missing in class *************")
    printList(list_students_not_in_class(classRoster, attendData))
    #list signin/out times for a student
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Lupoli, Shawn", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Allgood, Nick", attendData))
    print("****** List all swipe in and out for a student *******")
    printList(list_all_times_checking_in_and_out("Arsenault, Al", attendData))
    #display when students first signed in (and in attendance)
    print("****** Check in times for all students who attended***")
    printList(list_all_times_checked_in(attendData))
    #display all of those students late to class
    print("****** Students that arrived late ********************")
    printList(list_students_late_to_class("09:00:00", attendData))
      #display first student to enter class
    print("******* Get 1st student to enter class ****************")
    print(get_first_student_to_enter(attendData))



