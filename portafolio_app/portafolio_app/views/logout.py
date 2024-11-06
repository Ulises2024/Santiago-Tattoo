from django.contrib.auth import logout
from django.shortcuts import redirect

def load(request):
    print('logout')
    try:    
        logout(request)
    except Exception as e:
        print('Error: ', e)        
    return redirect('/')