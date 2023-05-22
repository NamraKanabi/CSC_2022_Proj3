#function reader is used to read four text files
def reader():
    opener= open("books.txt","r")
    books=opener.read()
    opener= open("students.txt","r")
    students=opener.read()
    opener= open("borrowers.txt","r")
    borrowers=opener.read()
    opener= open("returns.txt","r")
    returns= opener.read()
    
    return books,students,borrowers,returns

#function books_sort receives a string as a parameter and sorts the string into a dictionary
def books_sort(books):
    spliter=books.splitlines()
    book_ID=[]
    book_name=[]
    book_author=[]
    book_price=[]
    book_dict={}
    for x in spliter:
        pause=0
        temp_string=""
        for y in range(len(x)):
            if x[y]!="#":
                temp_string=temp_string+x[y]
            elif x[y]=="#" and pause==0:
                pause=1
                book_ID.append(temp_string)
                temp_string=""
            elif x[y]=="#" and pause==1:
                pause=2
                book_name.append(temp_string)
                temp_string=""
            elif x[y]=="#" and pause==2:
                pause=3
                book_author.append(temp_string)
                temp_string=""
            if y+1==len(x) and pause==3:
                book_price.append(float(temp_string))
                temp_string=""
    for x in range(len(book_ID)):
        book_dict[book_ID[x]]=book_name[x],book_author[x],book_price[x]
    return book_dict

#function students_sort receives a string as a parameter and sorts the string into a dictionary
def students_sort(students):
    spliter=students.splitlines()
    student_ID=[]
    student_name=[]
    classID=[]
    student_dict={}
    for x in spliter:
        pause=0
        temp_string=""
        for y in range(len(x)):
            if x[y]!=",":
                temp_string=temp_string+x[y]
            elif x[y]=="," and pause==0:
                pause=1
                student_ID.append(temp_string)
                temp_string=""
            elif x[y]=="," and pause==1:
                pause=2
                student_name.append(temp_string)
                temp_string=""
            if y+1==len(x) and pause==2:
                classID.append(temp_string)
                temp_string=""
    for x in range(len(student_ID)):
        student_dict[student_ID[x]]=student_name[x],classID[x]
    return student_dict

#function borrowers_sort receives a string as a parameter and sorts the string into a dictionary
def borrowers_sort(borrowers):
    spliter=borrowers.splitlines()
    book_ID=[]
    student_ID=[]
    bor_date=[]
    ret_date=[]
    borrow_dict={}
    for x in spliter:
        pause=0
        temp_string=""
        for y in range(len(x)):
            if x[y]!=";":
                temp_string=temp_string+x[y]
            elif x[y]==";" and pause==0:
                pause=1
                book_ID.append(temp_string)
                temp_string=""
            elif x[y]==";" and pause==1:
                pause=2
                student_ID.append(temp_string)
                temp_string=""
            elif x[y]==";" and pause==2:
                pause=3
                bor_date.append(temp_string)
                temp_string=""
            if y+1==len(x) and pause==3:
                ret_date.append(temp_string)
                temp_string=""
    for x in range(len(book_ID)):
        borrow_dict[book_ID[x]]=student_ID[x],bor_date[x],ret_date[x]
    return borrow_dict

#function returns_sort receives a string as a parameter and sorts the string into a dictionary
def returns_sort(returns):
    spliter=returns.splitlines()
    book_ID=[]
    student_ID=[]
    ret_date=[]
    stat=[]
    return_dict={}
    for x in spliter:
        pause=0
        temp_string=""
        for y in range(len(x)):
            if x[y]!=";":
                temp_string=temp_string+x[y]
            elif x[y]==";" and pause==0:
                pause=1
                book_ID.append(temp_string)
                temp_string=""
            elif x[y]==";" and pause==1:
                pause=2
                student_ID.append(temp_string)
                temp_string=""
            elif x[y]==";" and pause==2:
                pause=3
                ret_date.append(temp_string)
                temp_string=""
            if y+1==len(x) and pause==3:
                stat.append(int(temp_string))
                temp_string=""
    for x in range(len(book_ID)):
        return_dict[book_ID[x]]=student_ID[x],ret_date[x],stat[x]
    return return_dict

#function data_sort sorts all the dictionaries into a form that can be used to make tables
def data_sort(book_dict,student_dict,borrow_dict,return_dict):
    class_list=[]
    class_data={}
    temp_list=[]
    not_ret=[]
    due_list=[]
    
    for key,value in student_dict.items(): #for loop used to sort data by classes
        class_list.append(value[1])
    class_list=list(set(class_list))
    class_list.sort()
    for x in class_list:
        temp_list=[]
        for key,value in student_dict.items():
            if value[1]==x:
                temp_list.append(key)
        class_data[x]=temp_list
    
    for key,value in borrow_dict.items(): #for loop used to sort data for table 1 and 2
        if key not in return_dict.keys():
            not_ret.append(key)
            
        elif return_dict[key][2]==1 or return_dict[key][2]==2:
            not_ret.append(key)
            if return_dict[key][2]==1:
                due_list.append(key)
        if key in return_dict.keys() and return_dict[key][2]>3:
            due_list.append(key)
    
    return not_ret,class_data,due_list

#function table_maker accepts sorted data and writes it onto standing.txt in a table format and also prints it
def table_maker(book_dict,student_dict,borrow_dict,return_dict,not_ret,class_data,due_list):
    filer= open("standing.txt","w")
    calendar=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    for key,value in class_data.items():
        book_num=0
        total_due=0
        print("\n"+"Class: "+key)
        filer.write("\n"*2+"Class: "+key)
        filer.write("\n"+"+"+"-"*17+"+"+"-"*37+"+"+"-"*14+"+")
        filer.write("\n"+"|"+" Student Name    "+"|"+" Book"+" "*32+"|"+" Due Date     "+"|")
        filer.write("\n"+"+"+"-"*17+"+"+"-"*37+"+"+"-"*14+"+")
        for x,y in borrow_dict.items():
            if y[0] in value:
                if x in not_ret:
                    filer.write("\n"+"| "+"{:<16}".format(student_dict[y[0]][0])+"| "+"{:<36}".format(book_dict[x][0][0:36])+"| "+calendar[int(y[2][2:4])-1]+" "+y[2][4:6]+", 20"+y[2][0:2]+" |")
                    book_num+=1
        filer.write("\n"+"+"+"-"*17+"+"+"-"*37+"+"+"-"*14+"+")
        filer.write("\n"+"| "+"Total Books"+" "*43+"|"+"{:>13}".format(book_num)+" |")
        filer.write("\n"+"+"+"-"*17+"-"*38+"+"+"-"*14+"+")
        print("Total books currently borrowed: "+str(book_num))
        
        filer.write("\n"+"+"+"-"*17+"+"+"-"*10+"+")
        filer.write("\n"+"|"+" Student Name    "+"|"+" Due      "+"|")
        filer.write("\n"+"+"+"-"*17+"+"+"-"*10+"+")
        for x,y in borrow_dict.items():
            if y[0] in value:
                if x in due_list:
                    filer.write("\n"+"| "+"{:<16}".format(student_dict[y[0]][0])+"|"+"{:^10}".format("$"+"{:.2f}".format(book_dict[x][2]))+"|")
                    total_due+=book_dict[x][2]
        filer.write("\n"+"+"+"-"*17+"+"+"-"*10+"+")
        filer.write("\n"+"| "+"Total Books     "+"|"+"{:^10}".format("$"+"{:.2f}".format(total_due))+"|")
        filer.write("\n"+"+"+"-"*17+"+"+"-"*10+"+")
        print("Total amount due for books: "+"$"+"{:.2f}".format(total_due))
    
#main function to run the whole program   
def main():
    books,students,borrowers,returns = reader()
    book_dict=books_sort(books)
    student_dict=students_sort(students)
    borrow_dict=borrowers_sort(borrowers)
    return_dict=returns_sort(returns)
    not_ret,class_data,due_list=data_sort(book_dict,student_dict,borrow_dict,return_dict)
    table_maker(book_dict,student_dict,borrow_dict,return_dict,not_ret,class_data,due_list)
    
main()