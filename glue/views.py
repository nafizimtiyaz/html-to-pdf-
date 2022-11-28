from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User,auth
from  django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from  django.contrib import messages
from .models import new

@login_required()
# Create your views here.
def home(request):
    return redirect('/resume')


def signup(request):
    if request.method == 'POST':
        username = request.POST['uname']
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']

        if (password == password2):

            if User.objects.filter(username=username).exists():  # user name filter means if username taken
                messages.info(request, 'user email taken Use another email')
                return render(request, 'signup.html')


            elif User.objects.filter(email=email).exists():  # if email taken then give error messege

                messages.info(request, 'email is already taken use another email')

                messages.info(request, 'Email do not match')
                return render(request, 'signup.html')


            else:
                user = User.objects.create_user(username=username, password=password2, email=email)
                user.save()
                messages.info(request, 'Account successfully created')
                return redirect('/')
        else:
            # pass not match
            messages.info(request, 'password not match')
            return render(request, 'signup.html')

    else:
        return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'successfully login!')
            return redirect('/home')
        else:
            messages.info(request, 'invalid user')
            return render(request, 'login.html')

    else:
        return render(request,'login.html')

@login_required()
def logout_view(request):
    auth.logout(request)
    return redirect('/')

@login_required()
def resume(request):
    if request.method=='POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        url = fs.url(filename)
        image = url
        Name=request.POST['name']
        Email=request.POST['email']
        Description=request.POST['description']


        SSC_School = request.POST['s_school']
        SSC_P = request.POST['s_s_p_year']
        HSC_School = request.POST['h_school']
        HSC_P = request.POST['h_s_p_year']
        Hons_School = request.POST['hons_school']
        Hons_P = request.POST['hons_p_year']
        Work_ex_one = request.POST['work_ex_c_name_one']
        Work_desig_one = request.POST['work_desig_one']
        Work_year = request.POST['work_year_one']
        Work_ex_two = request.POST['work_ex_c_name_two']
        Work_desig_two = request.POST['work_desig_two']
        Work_two = request.POST['work_year_two']
        Work_ex_three = request.POST['work_ex_c_name_three']

        Work_three = request.POST['work_year_three']
        Soft_Skill = request.POST['soft_skill']
        x = new(user=request.user,image=image,name=Name,email=Email,description=Description,s_school=SSC_School,s_s_p_year=SSC_P,h_school=HSC_School,
                h_s_p_year=HSC_P,hons_school=Hons_School,hons_p_year=Hons_P,work_ex_c_name_one=Work_ex_one,work_desig_one=Work_desig_one,work_year_one=Work_year,
                work_ex_c_name_two=Work_ex_two,work_desig_two=Work_desig_two,work_year_two=Work_two,work_ex_c_name_three=Work_ex_three,
                work_year_three=Work_three,soft_skill=Soft_Skill)
        x.save()
        return redirect('/home')
    else:
        return render(request,'home.html')

@login_required()
def demo(request):
    input=new.objects.all()
    return render(request,'index.html',{'input':input})

def r_delet(request):
    a=new.objects.all()
    a.delete()
    return redirect('/home')


