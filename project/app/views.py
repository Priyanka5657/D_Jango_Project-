from django.shortcuts import render
from .models import Student

# Create your views here.
def index(request):
    return render(request,'index.html')

def registartion(request):
    return render(request,'registartion.html')

def registartiondata(request):
    # print (request.method)
    # print (request.POST)
    print (request.FILES)

    my_name = request.POST.get('name')
    my_email = request.POST.get('email')
    my_contact = request.POST.get('contact')
    my_image = request.FILES.get('image')
    my_resume = request.FILES.get('resume')
    my_pass = request.POST.get('pass')
    my_cpass= request.POST.get('cpass')
    save_data = Student.objects.create(stu_name=my_name,stu_email=my_email,stu_cpass=my_cpass,stu_contact=my_contact,stu_pass=my_pass,stu_image=my_image,stu_file=my_resume)
    print("data successful....")
    all_data=Student.objects.all()
    print(all_data)
    print(all_data.values())
    data ={
        'data':all_data.values()
    }
    return render(request,'new.html',data)

