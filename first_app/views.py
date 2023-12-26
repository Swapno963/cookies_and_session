from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
#cookis vs session
# cookis = authentication, shopping cart, dark mode, language, remember me

# session = 


def home(request):
    response = render(request, 'index.html')
    response.set_cookie('name','swapno mondol',expires=datetime.utcnow() + timedelta(days=7)) # stor for 7 days
    return response

def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_coo.html',{'name':name})


def delete_cookie(request):
    response = render(request, 'del.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    data = {
            'name' : 'rahim',
            'age' : 23,
            'language' : 'Bangla'
            }
    request.session.update(data)
    return render(request, 'index.html')

def get_session(request):
    data = request.session.get('name','guest')
    return render(request, 'session.html',{'data':data})


def delete_session(request):
    del request.session['name']
    return render(request, 'del.html')