from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def load(request):

    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            secret = request.POST.get('secret')
            print(f'username: {username}')
            print(f'secret: {secret}')
            #user = User.objects.get(username='username')
            #user.check_password(secret)
            user = authenticate(username=username, password=secret)
            login(request, user) 
            print('autenticación correcta.') 
            return redirect('index')
        except Exception as e:
            print(f'Error: {e}')
        return render(request, 'loginpage.html', {'show': 'show', 'message_error': 'USUARIO O CONTRASEÑA INCORRECTOS.'})
    else:
        return render(request, 'loginpage.html', {'show': None, 'message_error': None})

