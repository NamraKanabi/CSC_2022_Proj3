CSC_2022_Proj3

Author: Namra Kanani(me)

Program essentially takes in data for a school library and sorts it.
It takes four text files as input (books.txt, borrowers.txt, returns.txt, students.txt) and outputs one text file (standing.txt).

The four inputs must be formatted as below:
books.txt: [list of books in library]
BOOKID#BOOKNAME#AUTHOR#PRICE

borrowers.txt: [list of books borrowed]
BOOKID;STUDENTID;BORROWDATE;RETURNDATE

returns.txt: [list of books returned]
BOOKID;STUDENTID;RETURNDATE;STATUS

students.txt: [list of students in school]
STUDENTID,STUDENTNAME,CLASSID

The output file will be formatted as below:
standing.txt: [sorted data of books remaining to be returned 
	       money owned by each student]

Class: [ID]

+-----------------+-------------------------------------+--------------+

| Student Name      | Book                                | Due Date     |

+-----------------+-------------------------------------+--------------+

| [test name]     | [test name]                         | [test date]  |

+-----------------+-------------------------------------+--------------+

| Total Books                                           |            1 |

+-------------------------------------------------------+--------------+

+-----------------+----------+

| Student Name    | Due      |

+-----------------+----------+

+-----------------+----------+

| Total Books     |  $0.00   |

+-----------------+----------+




