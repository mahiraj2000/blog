from django.shortcuts import render

def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request,'learning/setsession.html')

def getsession(request):
    name=request.session['name'] = 'Sonam'
    return render(request,'learning/getsession.html',{'name':name})

def delsession(request):
    request.session.flush()
    request.session.clear_expired() 
    return render(request,'learning/delsession.html')    