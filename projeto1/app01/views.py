from django.shortcuts import render
from .forms import UserForm

def index(request):
    return render(request, 'user/index.html')

def create(request):

    if request.method == 'GET':
        form = UserForm()

        context = {
            'form': form,
        }
        return render(request, 'user/criar.html', context= context)
    else:
        form = UserForm(request.POST)
        if form.is_valid():
            print(form)
            form.save()
    return render(request, 'user/index.html')