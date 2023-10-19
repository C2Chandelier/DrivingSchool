from django.shortcuts import render, redirect
from .models import Instructor
from Secretary.models import Secretary, Planning
from Student.models import Student
from .forms import LoginForm, PlanningForm
from django.views import generic


def homeInstructor(request):
    if "user_id" in request.session and request.session['user_role'] == 'instructor':
        
        plannings = Planning.objects.filter(instructor__id=request.session['user_id']).first(),
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
        form = PlanningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Instructor:homeInstructor')
    else:
        form = PlanningForm()
    
    return render(request, 'addPlanningInstructor.html', {'form': form})
      

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
