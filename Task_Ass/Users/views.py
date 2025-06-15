from django.shortcuts import get_object_or_404, render,redirect

from django.http import HttpResponse
from .forms import add_users
from .models import Users_db


#create CRUD which means create read update delete 
#CRUD= create, read ,delete ,update 

# Create your views here.
#this the function t show the homepage and other pages 
def home(request):
    users=Users_db.objects.all()
    
    #return the object 
    return render(request, 'homepage.html', {'users':users})

#create the function to add the user details in the database 
def create_user(request):
    if request.method == 'POST':
        form = add_users(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = add_users()
    return render(request, 'user_form.html', {'form': form})

#delete the function to add the user details in the database

def delete_user(request, user_id):
    user = get_object_or_404(Users_db, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('homepage')
    return render(request, 'confirm_delete.html', {'user': user})