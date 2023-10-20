from django.shortcuts import render, redirect
from .models import Planning

def homeSecretary(request):
    if "user_id" in request.session and request.session.get('user_role') == 'secretary':
        context = {'plannings': Planning.objects.all()}
        return render(request, 'homeSecretary.html', context)
    else:
        return redirect('Instructor:loginInstructor')


# Create your views here.


   



""" def student(request):
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



class PlanningView(DetailView):
    model = Planning 
    template_name = 'DSchool/planning.html'  
    context_object_name = 'planning'     """
