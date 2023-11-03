from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector as sql
first_name =''
last_name =''
s=''
eml=''
pwd=''

# Create your views here.
def signupaction(request):
    global first_name,last_name,s,eml,pwd
    if request.method =='POST':
        obj=sql.connect(host='localhost', user='root',password='sk@123',database='website')
        cursur = obj.cursor()
        d = request.POST
        for key , value in d.items():
            if key =='first_name':
                first_name=value
            if key =='last_name':
                last_name=value
            if key =='sex':
                s= value
            if key =='email':
                eml=value
            if key =='password':
                pwd=value 

        c = "insert into user Values('{}','{}','{}','{}','{}')".format(first_name,last_name,s,eml,pwd) 
        cursur.execute(c)
        obj.commit() 





    return render(request,'signup_page.html')

from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,ln,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="vivek",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="insert into user Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pwd)
        print(c)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')

def homepage(request):
    return HttpResponse('this is home page and you can login to Longin ')
