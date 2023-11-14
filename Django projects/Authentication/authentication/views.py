from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .tokens import generate_token
from Linc import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site

# Create your views here.
def home(request):
    return render(request, 'index.html')



def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        pass_conf = request.POST['pass_conf']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist")

        if User.objects.filter(username=username):
            messages.error(request, "Email already register")
            return redirect("/signin")

        if len(username) > 15:
            messages.error(request, "Username should be utmost 15 characters")

        if password != pass_conf:
            messages.error(request, "Passwords doesn't match")

        if not username.isalnum():
            messages.error(request, "Username must be alpha-numeric")
        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = False

        myuser.save()

        messages.success(request, "Your account has been created successfully")

        # Welcome email

        subject = "Welcome to Linc Academy"
        message = "Hello " + myuser.first_name + "!!\n" + "Thank you for visiting our website.\n Please check your gmail account to activate your account\n" + "Thank you\n"

        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently="True")

        # Email address confirmation
        current_site = get_current_site(request)
        email_subject = "Confirm your Email - Linc Academy"
        message2 = render_to_string('email_conf.html', {
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('/signin')
    return render(request, 'signup.html')



def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, 'index.html', {'fname': fname})
            # messages.info(request, f"You are now logged in as {username}")
        else:
            messages.error(request, "Username or Password incorrect")
            return redirect('home')
    return render(request, 'signin.html')


def signout(request):
   logout(request)
   messages.success(request, "Logged out successfully")
   return redirect('/')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')
