from tkinter import *
from tkinter.scrolledtext import *
from tkinter.messagebox import *
from sqlite3 import *
import sqlite3
import bs4
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



def f1():
	root.withdraw()
	add_page.deiconify()	
def f2() :
	add_page.withdraw()
	root.deiconify()
def f3():
	root.withdraw()
	update_page.deiconify()
def f4():
	update_page.withdraw()
	root.deiconify()
def f5():
	root.withdraw()
	view_st.deiconify()
	btndata.delete(1.0,END)             
	con = None
	try:
		con= connect("s1.csv")
		sql = "select * from student"
		cursor =con.cursor()
		cursor.execute(sql)
		data= cursor.fetchall()
		info = ""	
		for d in data:
			info = info + "rno: " + str(d[0]) + " name: " + str(d[1]) + " marks: " +str(d[2])+"\n"
		btndata.insert(INSERT,info)
	except Exception as e:
		showerror("failure", e)
	finally:
		if con is not None:
			con.close()

def f6():
	view_st.withdraw()
	root.deiconify()
def f7():
	root.withdraw()
	delete_page.deiconify()
def f8():
	delete_page.withdraw()
	root.deiconify()
def add_stu():
	try:
		con=connect("s1.csv")
		sql="insert into student values('%d','%s','%d')"
		cursor= con.cursor()
		rno= int(entrno.get())
		name= entname.get()
		marks=int(entmarks.get())
		if rno <= 0 :
			showerror("Error","Roll no cannot be negative or Zero")
		elif (name.isalpha()) == False:
			showerror("Error","enter valid name")
		
		elif marks < 0 or marks >100:
			showerror("Error","Enter valid marks")
	
		else:
			cursor.execute(sql % (rno, name,marks))
			con.commit()
			showinfo("Inserted","record inserted")
	except ValueError :
		showerror("Error","Enter digits in the field of marks and rno")
						
	except NameError :
		showerror("Error","Enter a valid name")

	
	except IntegrityError as err:
		showwarning("Warning","Roll no already exists")

	except Exception as e:
		print("issue",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
			

		
def upd_stu():
	con = None
	try:
		con = connect("s1.csv")
		sql= "update student set name= '%s',marks = '%d' where rno = '%d' "
		
		cursor=con.cursor()   # connect python and database
		rno= int(entrno1.get())
		name= entname1.get()
		marks=int(entmarks1.get())
		if rno <= 0 :
			showerror("Error","Roll no cannot be negative or Zero")
		elif (name.isalpha()) == False:
			showerror("Error","Enter valid name")
		elif marks < 0 or marks >100:
			showerror("Error","Enter valid marks")
	
		else:
			cursor.execute(sql%(name,marks,rno) )                  
			data = cursor.fetchall()
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Updated","Record updated")
			else:
				showwarning("Warning","Record does not exist")

	except ValueError :
		showerror("Error","Enter a valid roll number")
	except NameError :
		showerror("Error","Enter a valid name")

	except Exception as e:
		print("issue",e)
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
			

def del_stud():
	con = None
	try:
		con = connect("s1.csv")
		
		sql= "delete from student where rno = '%d'"
		cursor=con.cursor()   # connect python and database
		rno= int(entrno2.get())
		if rno <= 0 :
			showerror("Error","Roll no cannot be negative or Zero")
		else:
			cursor.execute(sql %(rno))
			data = cursor.fetchall()
			if cursor.rowcount == 1:
				con.commit()
				showinfo("Deleted","Record deleted")
			else:
				showwarning("Warning","Record does not exist")
	except ValueError :
		showerror("Error","Enter a valid roll number")
	except Exception as e:
		print("issue",e)
		con.rollback()
	
	finally:
		if con is not None:
			con.close()

def graph():
	con = sqlite3.connect('s1.csv')
	data = pd.read_sql_query("select rno,name,marks from student;",con)
	print(data)
	
	name=data['name'].tolist()
	rno = data['rno'].tolist()
	marks=data['marks'].tolist()
	x= np.arange(len(rno))

	plt.bar(rno,marks,width = 0.50 , color=['Red','green','blue'])
	plt.xticks(rno)
	plt.xlabel("Roll Number")
	plt.ylabel("Marks")
	plt.title("Batch Information")
	plt.grid()
	
	plt.show()
			





# S.M.S Page
root=Tk()
root.title("S.M.S")
root.geometry("1200x600+50+50")
root.configure(bg='light blue')



# code for Location ,quote , and temp
try:	# for quote
	web_add="https://www.brainyquote.com/quote_of_the_day"
	res = requests.get(web_add)
	#print(res)
	
	data = bs4.BeautifulSoup(res.text, "html.parser")  
	#data= res.json()
	#print(data)

	info= data.find("img",{"class":"p-qotd"})
	print(info)

	quote= info['alt']						
	print(quote)

	T=Text(root,height=2,width=91,font=('arial',15,'bold'))  
	T.place(x=160 ,y=420)

	T.insert(END,quote)		#inserts the quote into text
	T.configure(state='disabled')	#makes the text permanents

	#for locaion
	web_address= "https://ipinfo.io/"
	res1 = requests.get(web_address)
	#print(res1)
	
	data = res1.json()          
	
	
	city_name = data['city']
	#print(city_name)

	# for temperature
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q="+ city_name
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	web_add= a1 + a2 + a3
	res = requests.get(web_add)
	#print(res)

	data = res.json()
	
	a1= data['main']
	t= a1['temp']
	print( t)

	#at = data['main']['temp']
	#print("another temp= ",at)

	text1=Text(root,height=1,width=8,font=('arial',15,'bold'))
	text1.place(x= 160  ,y=370 )
	text1.insert(END,city_name)
	text2=Text(root,height=1,width=8,font=('arial',15,'bold'))
	text2.place(x=700  ,y=370  )
	text2.insert(END,t)
	text1.configure(state='disabled')
	text2.configure(state='disabled')




except Exception as e:
	print("issue",e)


btnadd= Button(root,text="Add",font=('arial',15,'bold'),width=20,command=f1)
btnadd.pack(pady=10)
btnview= Button(root,text="View",font=('arial',15,'bold'),width=20,command=f5)
btnview.pack(pady=10)
btnupdate= Button(root,text="Update",font=('arial',15,'bold'),width=20,command=f3)
btnupdate.pack(pady=10)
btndelete= Button(root,text="Delete",font=('arial',15,'bold'),width=20,command=f7)
btndelete.pack(pady=10)
btnchart= Button(root,text="Chart",font=('arial',15,'bold'),width=20,command=graph)
btnchart.pack(pady=10)
lblloc = Label(root,text="Location: ",bd=5,font=('arial',15,'bold'))
lblloc.place(x=20,y=370)
lbltemp = Label(root,text="Temp: ",bd=5,font=('arial',15,'bold'))
lbltemp.place(x=600,y=370)
lblqod = Label(root,text="QOTD: : ",bd=5,font=('arial',15,'bold'))
lblqod.place(x=20,y=420)


#ADD Page
add_page= Toplevel(root)
add_page.title("Add Student")
add_page.geometry("600x600+350+100")
add_page.configure(bg='light blue')
lblrno = Label(add_page,text="Enter Roll No: ",bd=5,font=('arial',15,'bold'),width=25)
lblrno.pack(pady=10)
entrno=Entry(add_page,bd=5,font=('arial',15,'bold'),width=30)
entrno.pack(pady=10)
lblname = Label(add_page,text="Enter Name: ",bd=5,font=('arial',15,'bold'),width=25)
lblname.pack(pady=10)
entname=Entry(add_page,bd=5,font=('arial',15,'bold'),width=30)
entname.pack(pady=10)
lblmarks = Label(add_page,text="Enter Marks: ",bd=5,font=('arial',15,'bold'),width=25)
lblmarks.pack(pady=10)
entmarks=Entry(add_page,bd=5,font=('arial',15,'bold'),width=30)
entmarks.pack(pady=10)
btnsave=Button(add_page,text="SAVE ",bd=5,font=('arial',15,'bold'),width=15,command=add_stu)
btnsave.pack(pady=10)
btnback=Button(add_page,text="BACK",bd=5,font=('arial',15,'bold'),width=15,command=f2)
btnback.pack(pady=10)
add_page.withdraw()

#Update page
update_page= Toplevel(root)
update_page.title("Update Student")
update_page.geometry("500x500+350+100")
update_page.configure(bg='light blue')
lblrno1 = Label(update_page,text="Enter Roll No: ",bd=5,font=('arial',15,'bold'),width=25)
lblrno1.pack(pady=10)
entrno1=Entry(update_page,bd=5,font=('arial',15,'bold'),width=30)
entrno1.pack(pady=10)
lblname1 = Label(update_page,text="Enter Name: ",bd=5,font=('arial',15,'bold'),width=25)
lblname1.pack(pady=10)
entname1=Entry(update_page,bd=5,font=('arial',15,'bold'),width=30)
entname1.pack(pady=10)
lblmarks1 = Label(update_page,text="Enter Marks: ",bd=5,font=('arial',15,'bold'),width=25)
lblmarks1.pack(pady=10)
entmarks1=Entry(update_page,bd=5,font=('arial',15,'bold'),width=30)
entmarks1.pack(pady=10)
btnsave1=Button(update_page,text="SAVE ",bd=5,font=('arial',15,'bold'),width=15,command=upd_stu)
btnsave1.pack(pady=10)
btnback1=Button(update_page,text="BACK",bd=5,font=('arial',15,'bold'),width=15,command=f4)
btnback1.pack(pady=10)
update_page.withdraw()

# DELETE PAGE

delete_page= Toplevel(root)
delete_page.title("Delete Student")
delete_page.geometry("500x500+350+100")
delete_page.configure(bg='light blue')
lblrno2 = Label(delete_page,text="Enter Roll No: ",bd=5,font=('arial',15,'bold'),width=25)
lblrno2.pack(pady=10)
entrno2=Entry(delete_page,bd=5,font=('arial',15,'bold'),width=30)
entrno2.pack(pady=10)
btnsave2=Button(delete_page,text="SAVE ",bd=5,font=('arial',15,'bold'),width=15,command=del_stud)
btnsave2.pack(pady=10)
btnback2=Button(delete_page,text="BACK",bd=5,font=('arial',15,'bold'),width=15,command=f8)
btnback2.pack(pady=10)
delete_page.withdraw()

# View page

view_st = Toplevel(root)
view_st.title("View student")
view_st.geometry("500x500+350+100")
view_st.configure(bg='light blue')
btndata= ScrolledText(view_st,width=30,height=10,font=('arial',18,'bold'))
btnback= Button(view_st,text="Back",width=10,font=('arial',18,'bold'),command=f6)

btndata.pack(pady=10)
btnback.pack(pady=10)
view_st.withdraw()





root.mainloop()