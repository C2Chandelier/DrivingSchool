from django.shortcuts import render, redirect
from .models import Planning

def homeSecretary(request):
    if "user_id" in request.session and request.session.get('user_role') == 'secretary':
        context = {'plannings': Planning.objects.all()}
        return render(request, 'homeSecretary.html', context)
    else:
        return redirect('Instructor:loginInstructor')

