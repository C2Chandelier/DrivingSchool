from django.shortcuts import render, redirect
from Secretary.models import Planning
from .forms import LoginForm
from .models import Student

def homeStudent(request):
    if "user_id" in request.session and request.session['user_role'] == 'student':
        context = {
            'plannings': Planning.objects.filter(student__id=request.session['user_id']).order_by('date'),
        }
        return render(request, 'homeStudent.html', context)
    else:
        return redirect('Student:loginStudent')
    
def detailStudent(request):
    context = {
        'student': Student.objects.get(pk=request.session['user_id']),
    }
    return render(request, 'detailStudent.html', context)

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

