from django.shortcuts import render, redirect
from django.template import loader
from django.views.generic import DetailView

from Secretary.models import Planning

from .forms import LoginForm
from .models import Student

class PlanningView(DetailView):
    model = Planning 
    template_name = 'Student/homeStudent.html'  
    context_object_name = 'planning' 

def homeStudent(request):
    if "user_id" in request.session and request.session['user_role'] == 'student':
        return PlanningView.as_view()(request)
    else:
        return redirect('Student:loginStudent')

def loginStudent(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = Student.objects.filter(username=username, password=password).first()

            if user is not None:
                request.session['user_id'] = user.id
                request.session['user_role'] = 'student'
                return redirect('Student:homeStudent')
            else:
                return render(request, 'loginStudent.html', {'form': form, 'error_message': 'Invalid login'})

    else:
        form = LoginForm()

    return render(request, 'loginStudent.html', {'form': form})



   



def student(request):
    student_list= Student.objects.all()
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


class StudentView(DetailView):
    model = Student  
    template_name = 'DSchool/student_detail.html'  
    context_object_name = 'student'


class PlanningView(DetailView):
    model = Planning 
    template_name = 'DSchool/planning.html'  
    context_object_name = 'planning'    