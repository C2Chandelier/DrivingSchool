from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import DetailView
from django.shortcuts import render
from django.template import loader
from .forms import StudentForm, AddPlanningForm
from django.shortcuts import render, redirect  
from django.views.generic import ListView


from .models import Student, Planning
# Create your views here.


def student(request):
    student_list= Student.objects.all().order_by('-id')
    template = loader.get_template("DSchool/student.html")
    context = {
        "student_list": student_list,
    }
    return HttpResponse(template.render(context, request))


def planning(request):
    planning_list= Planning.objects.all()
    template = loader.get_template("DSchool/planning-all.html")
    context = {
        "planning_liste": planning_list,
    }
    return HttpResponse(template.render(context, request))


def student_detail_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    context = {
        'student': student,
    }
    return render(request, 'DSchool/student_detail.html', context)    


def planning_view(request, pk):
    student = get_object_or_404(Student, pk=pk)  
    plannings = Planning.objects.filter(student=student)
    context = {
        'student': student,
        'plannings': plannings,
    }
    return render(request, 'DSchool/planning.html', context)



def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('DSchool:student-list')  
    else:
        form = StudentForm()
    return render(request, 'DSchool/add-student.html', {'form': form})




def student_to_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'DSchool/confirm-delete-student.html', {'student': student})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete() 
    return redirect('DSchool:student-list')
  




def edit_student(request, pk):
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

           return redirect('DSchool:student-list')
                   
     


    return render(request, 'DSchool/edit-student.html', {'form': form, 'student': student})





def add_rdv(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'POST':
        form = AddPlanningForm(request.POST)
        if form.is_valid():
            planning = form.save(commit=False)
            planning.student = student  
            planning.save()
            return redirect('DSchool:planning-list', pk=student.id)
    else:
        form = AddPlanningForm()

    return render(request, 'DSchool/add-rdv.html', {'form': form, 'student': student})