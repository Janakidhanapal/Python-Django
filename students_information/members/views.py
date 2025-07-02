from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Student


def student_entry(request):
    return render(request, 'myapp/student_entry.html')


def process_student_entry(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Create a new student entry in the database using the Student model
        student = Student(name=name, gender=gender, dob=dob, email=email, phone=phone)
        student.save()

        context = { 'name': name,
                    'gender': gender }              #store the name in context

        return render(request, 'myapp/process_student_entry.html', context)

    else:
        return HttpResponse("Invalid request method.")


def display_stud_detail(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        student = Student.objects.get(name=name)
        data = {
            'name': student.name,
            'gender': student.gender,
            'dob': student.dob,
            'email': student.email,
            'phone': student.phone
        }
        return JsonResponse(data)
