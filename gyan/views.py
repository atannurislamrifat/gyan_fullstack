
from django.http import HttpResponse 
from django.shortcuts import render,redirect
from gyan.models import form, contact_from,CustomPasswordResetForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
import uuid
from django.utils.crypto import get_random_string
from django.template.loader import render_to_string
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm 
 



# def user_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     context = {
#         'user_email': user.email,
#     }
#     return render(request, 'common/base.html', context)


@login_required(login_url='user_login')
def home(request):
    return render(request,'index.html')

@login_required(login_url='user_login')
def about(request):
    return render(request,'about.html')

def contract(request):   
    
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if contact_from.objects.filter(name=name).exists():
            messages.error(request,'Not submited')
            return redirect('home')
        else:
             data = contact_from.objects.create(name=name, email=email, subject=subject,message=message)
             data.save()
             messages.success(request,'successfully submited')
    return render(request,'contract.html')

@login_required(login_url='user_login')
def base(request):
    return render(request,'common/base.html')
    
def signup(request):
    if request.method == 'POST':
        # Extracting data from the POST request
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        # Checking if passwords match
        if pass1 != pass2:
            # Passwords don't match, handle this accordingly (e.g., show an error message)
            return render(request, 'signup.html', {'error_message': 'Passwords do not match'})
        else:
            # Passwords match, create the user
                   # Send login email
            user = User.objects.create_user(username=uname, email=email, password=pass1)
            user.save()
            
            
            send_welcome_email(user)
       
            return redirect('user_login')  # Redirect to login page after successful signup 
    else:    
        return render(request, 'signup.html')

def send_welcome_email(user):
    subject = 'Welcome to Our Website'
    message = f'Dear {user.username},\n\nThank you for signing up on our website. We are excited to have you on board.'
    recipient_email = user.email
    send_mail(subject, message, 'atannurrifat21395@gmail.com', [recipient_email])
   
   

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')  # Assuming password field name is 'password'
        
        user = authenticate(request, username=username, password=pass1)
        
        # Debugging output
        print(username, pass1)    
        
        if user is not None:
            login(request,user)
            print("User authenticated successfully")  
          
            return redirect('home')  # Redirect to the home page URL after successful login
        
        else:
            print("User authentication failed")  
            return render(request, 'login.html', {'error_message': 'Username or password do not match'})
    else:
        return render(request, 'login.html')   
    
 
def user_logout(request): 
        logout(request)
        return redirect('user_login')
    



def forget_password(request):    
    return render(request, 'password_reset.html')

def password_reset_done(request):
    return render(request, 'password_reset_done.html')

def password_reset_confirm(request):
    return render(request,'password_reset_confirm.html')   



#    if request.method == 'POST':
#         username = request.POST.get('username')
        
#         if not User.objects.filter(username=username).exists():
#             messages.error(request, "No user with this username exists.")
#             return redirect('forget_password')
        
#         user = User.objects.get(username=username)
#         token = get_random_string(20)
        
#         context = {
#             'email': user.email,
#             'domain': request.get_host(),
#             'site_name': 'Your Site',  
#             'uid': user.pk,
#             'user': user,
#             'token': token,
#             'protocol': 'http',
#         }
        
#         subject = 'Password Reset Requested'
#         email_template_name = 'password_reset_email.html'
#         email = render_to_string(email_template_name,context)
#         send_mail(subject, email, 'atannurrifat21395@gmail.com', [user.email], fail_silently=False)
        
#         return redirect('password_reset_done')



# === change password=======

    
def password_change(request):
    if request.method == "POST":
        fm = PasswordChangeForm(user=request.user, data=request.POST)
        if fm.is_valid():
            fm.save()
            update_session_auth_hash(request, fm.user)
            messages.success(request,'successfully change password')
            return redirect('password_change_done')
    else:
         fm = PasswordChangeForm(user=request.user)
    return render(request,'change_password.html',{'form':fm})
    
def password_change_done(request):
    return render(request,'password_change_done.html') 

    

