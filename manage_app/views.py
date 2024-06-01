
from django.shortcuts import render , HttpResponse , redirect
from .models import Employee , Department
from django.contrib import messages


from .middlewares import auth , guest

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required


# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request , 'homepage/homepage.html')

def about_us_view(request):
    return render(request, 'about_us/about_us.html')


def contact_us_view(request):
    return render(request, 'contact_us/contact_us.html')



def register_view(request):
    
    if request.method == "POST":

        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        email = request.POST.get('email')


        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request,"Username already exists!!")
            return redirect('/register/')


        user = User.objects.create(
            username = username,
            email = email,
            
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, 'Account created successfully !!')

        return redirect('/register/')

        
    else:
        return render(request, 'register/register.html')



def login_view(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print('username is :- ',username)
        print('password is :- ',password)
        if not User.objects.filter(username = username).exists():
            messages.error(request,"Username does not exist !!")
            return redirect("/login/")

        user = authenticate(username = username , password = password)
        print(user)
        if user is None:
            messages.error(request , "Invalid Password !! ")
            return redirect("/login/")
        
        else:
            login(request , user)
            request.session.set_expiry(100)
            messages.error(request, 'You have been logged out , Please Log In again !! ')
            return redirect("/")

       

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect("/")


@login_required(login_url='/login/')
def create_emp(request):
    depts = Department.objects.all()
    context = {
        'depts' : depts
    }
    if request.method == 'GET':
        return render(request , "create_emp/create_emp.html", context)
        
    elif request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = request.POST['salary']
        dept = int(request.POST['dept'])

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'salary': salary,
            'dept': dept
        }
        error_message = None
        if len(first_name)>10 or len(last_name)>10 or len(last_name)== 0:
            messages.error(request , 'first name and last name must be less than 10 characters')
            return redirect('/create_emp')
        elif int(salary)>100000 or int(salary) <10000:
            messages.error(request, 'salary must be between 1000 to 100000')
            return redirect('/create_emp')
        else:
            new_emp = Employee(first_name = first_name , last_name= last_name , salary= salary , dept_id = dept)
            new_emp.save()
            messages.info(request,'Employee added successfully')
            return redirect('/all_emp')

      
    # else:
    #     return HttpResponse('An Exception Occured')
    # return render(request , 'create_emp.html')




# @login_required(login_url='/login/')
# def delete_emp(request, emp_id = 0):
#      if emp_id:
#         try:
#             emp_to_be_removed = Employee.objects.get(id=emp_id)
#             emp_to_be_removed.delete()
#             return HttpResponse("Employee Removed Successfully")
#         except:
#             return HttpResponse("Please Enter A Valid EMP ID")
#      emps = Employee.objects.all()
#      context = {
#         'emps': emps
#      }
#      return render(request , 'delete_emp/delete_emp.html', context)



@login_required(login_url='/login/') 
def remove_emp(request, emp_id):
    if emp_id:
        try:
            emp_to_remove = Employee.objects.get(id = emp_id)
            emp_to_remove.delete()
        except:
            return HttpResponse("Please select a valid employee")
        emps = Employee.objects.all()
        context = {
            'emps' :emps
        }
        # return render(request , 'all_emp/all_emp.html',context)
        return redirect ('/all_emp')

@login_required(login_url='/login/')
def update_emp(request, emp_id):
    emp = Employee.objects.get(pk= emp_id)
    context = {
        'emp': emp
    }
    return render(request, 'update_emp/update_emp.html',context)

@login_required(login_url='/login/')
def do_update_emp(request , emp_id):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary')
        # dept = request.POST.get('dept')

        e = Employee.objects.get(pk=emp_id)
        e.first_name = first_name
        e.last_name = last_name
        e.salary = salary
        # e.dept = dept
        e.save()

        # return render(request, "all_emp/all_emp.html", {
        #     'e':e
        # })
        return redirect("/all_emp")

    else :
        return HttpResponse("Some error ocuured")    

@login_required(login_url='/login/')
def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request , 'all_emp/all_emp.html', context)
