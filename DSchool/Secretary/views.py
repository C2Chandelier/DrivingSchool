from django.shortcuts import render, redirect, get_object_or_404
from .models import Planning
from Student.models import Student
from Instructor.models import Instructor
from .forms import AddPlanningForm, StudentForm, InstructorForm
from django.contrib import messages

def homeSecretary(request):
    if "user_id" in request.session and request.session.get('user_role') == 'secretary':
        context = {'plannings': Planning.objects.all()}
        return render(request, 'homeSecretary.html', context)
    else:
        return redirect('Instructor:loginInstructor')
    
def studentDetail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'studentDetail.html', context)

def instructorDetail(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    context = {
        'instructor': instructor,
    }
    return render(request, 'instructorDetail.html', context)

def planningStudent(request, pk):
    student = get_object_or_404(Student, pk=pk)  
    plannings = Planning.objects.filter(student=student)
    context = {
        'student': student,
        'plannings': plannings,
    }
    return render(request, 'planningStudent.html', context)

def planningInstructor(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)  
    plannings = Planning.objects.filter(instructor=instructor)
    context = {
        'instructor': instructor,
        'plannings': plannings,
    }
    return render(request, 'planningInstructor.html', context)
    
def studentList(request):
    student_list= Student.objects.all().order_by('-id')
    context = {
        "student_list": student_list,
    }
    return render(request, 'studentList.html', context)   

def instructorList(request):
    instructor_list= Instructor.objects.all().order_by('-id')
    context = {
        "instructor_list": instructor_list,
    }
    return render(request, 'instructorList.html', context)   

def addInstructor(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Secretary:instructorList')  
    else:
        form = StudentForm()
    return render(request, 'addStudent.html', {'form': form})


def addStudent(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('Secretary:studentList')  
    else:
        form = StudentForm()
    return render(request, 'addStudent.html', {'form': form})


def confirmDeleteStudent(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'confirmDeleteStudent.html', {'student': student})

def deleteStudent(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete() 
    return redirect('Secretary:studentList')
  

def editStudent(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    studentTotalDB = student.h_total
    if request.method == 'POST' and form.is_valid():

        new_h_total = int(form.cleaned_data['h_total'])
        if studentTotalDB != new_h_total and new_h_total > studentTotalDB:
           difference = new_h_total - studentTotalDB
           student.h_total = new_h_total
           student.h_remaining += difference
           student.save()
           form.save()

           return redirect('Secretary:studentList')
        else :
            messages.error(request, "Vous ne pouvez pas enlever d'heure à cet étudiant")
            return redirect('Secretary:studentList')
                   
     
    return render(request, 'editStudent.html', {'form': form, 'student': student})


def addPlanning(request, pk):    
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = AddPlanningForm(request.POST)
        if form.is_valid():
            if student.h_remaining > 0:
                student.h_remaining -= 1
                student.save()
                form.instance.student = student
                form.save()
                return redirect('Secretary:studentDetail', pk=student.id)
            else:
                messages.error(request, "Cet étudiant n'as plus de crédit")
                return redirect('Secretary:studentDetail', pk=student.id)
    else:
        form = AddPlanningForm()

    return render(request, 'addPlanning.html', {'form': form, 'student': student})

