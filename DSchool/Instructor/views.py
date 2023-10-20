from django.shortcuts import render, redirect, get_object_or_404
from .models import Instructor
from Secretary.models import Secretary, Planning
from Student.models import Student
from .forms import LoginForm, PlanningFormAdd, PlanningFormModif
from django.contrib import messages



def homeInstructor(request):
    if "user_id" in request.session and request.session['user_role'] == 'instructor':
        plannings = Planning.objects.filter(instructor__id=request.session['user_id']).order_by('date')
        context ={
            'plannings': plannings
        }
        return render(request, 'homeInstructor.html',context)

    else:
        return redirect('Instructor:loginInstructor')
    
    
def profileStudent(request, student_id):
    return render(request, 'studentProfile.html', {'student': Student.objects.get(pk=student_id)})

def detailInstructor(request):
    context = {
        'instructor': Instructor.objects.get(pk=request.session['user_id']),
    }
    return render(request, 'detailInstructor.html', context)

def addPlanningInstructor(request):
    if request.method == 'POST':
        form = PlanningFormAdd(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            instructor = Instructor.objects.get(pk=request.session['user_id'])
            form.instance.instructor = instructor
            if student.h_remaining > 0:
                student.h_remaining -= 1
                student.save()
                form.save()
                return redirect('Instructor:homeInstructor')
            else:
                messages.error(request, "Cet étudiant n'as plus de crédit")
                return redirect('Instructor:homeInstructor')
    else:
        form = PlanningFormAdd()
    
    return render(request, 'addPlanningInstructor.html', {'form': form}) 

def modifier_entry(request, planning_id):
    planning = get_object_or_404(Planning, pk=planning_id)
    form = PlanningFormModif(request.POST, instance=planning)
    if form.is_valid():
        instructor = Instructor.objects.get(pk=request.session['user_id'])
        form.instance.instructor = instructor
        form.instance.student = planning.student
        form.save()
        return redirect('Instructor:homeInstructor')
    else:
        form = PlanningFormModif(instance=planning)
    return render(request, 'modifier_entry.html', {'form': form, 'planning': planning })

def confirmer_suppression(request, planning_id):
    planning = get_object_or_404(Planning, pk=planning_id)
    return render(request, 'confirmer_suppression.html', {'planning': planning})

def supprimer_planning(request, planning_id):
    planning = get_object_or_404(Planning, pk=planning_id)
    if request.method == 'POST':
        planning.delete()
    return redirect('Instructor:homeInstructor')
    return render(request, 'supprimer_planning.html', {'planning': planning})
      

def loginInstructor(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = Instructor.objects.filter(username=username, password=password).first()
            role = 'instructor'
            if user == None:
                user = Secretary.objects.filter(username=username, password=password).first()
                role = 'secretary'

            if user is not None:
                request.session['user_id'] = user.id
                request.session['user_role'] = role
                if role == 'secretary':
                    return redirect('Secretary:homeSecretary')
                return redirect('Instructor:homeInstructor')
            else:
                return render(request, 'loginInstructor.html', {'form': form, 'error_message': 'Invalid login'})

    else:
        form = LoginForm()

    return render(request, 'loginInstructor.html', {'form': form})
