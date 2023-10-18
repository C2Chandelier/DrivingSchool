from django.shortcuts import render, redirect
from .models import Instructor
from Secretary.models import Secretary, Planning
from Student.models import Student
from .forms import LoginForm, PlanningForm
from django.views import generic


def homeInstructor(request):
    if "user_id" in request.session and request.session['user_role'] == 'instructor':
        
        plannings = Planning.objects.filter(instructor=2)
        context ={
            'plannings': plannings
        }
        return render(request, 'planning.html',context)

    else:
        return redirect('Instructor:loginInstructor')
    
    
class StudentProfileView(generic.DetailView):
    model = Student
    template_name = 'student_profile.html'
    context_object_name = 'student'

class InstructorProfileView(generic.DetailView):
    model = Instructor
    template_name = 'instructor_profile.html'
    context_object_name = 'instructor'

def add_entry_planning(request):
    if request.method == 'POST':
        form = PlanningForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Instructor:homeInstructor')
    else:
        form = PlanningForm()
    
    return render(request, 'DSchool/new_entry.html', {'form': form})
      

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
