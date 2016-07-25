from django.conf.urls import url
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from .models import profile,Qualification,Experience,Certificate
from django.core.urlresolvers import reverse


def home(request):
    return render(request, 'Login/login_page.html')


def check_login(request):
    user = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=user, password=password)

    if user is not None:
        auth_login(request, user)
        return HttpResponseRedirect(reverse('Login:viewprofile'))

    else:
        error_message = "Sorry wrong Credentials"
        return render(request, 'Login/login_page.html', {'error_message': error_message})  # incomplete

def viewprofile(request):


    current=request.user
    current.profile=request.user.profile_set.all()
    current.qualification=request.user.qualification_set.all()
    current.experience=request.user.experience_set.all()
	current.certificate=request.user.certificate_set.all()
    current.range = list(range(1990, 2020))
    return render(request, 'Login/index.html', {'current':current})


def user_logout(request):
    logout(request)
    return redirect('/home/')


def saveprofile(request):

    u = User.objects.get(id=request.user.id)
    p = profile.objects.get(user_id=request.user.id)

    u.email=request.POST.get('mailing_address',u.email)
    u.save()

    p.user = u
    p.full_name = request.POST.get('fullname',p.full_name)                                              #DONE
    p.photo_upload=request.FILES.get('docfile',p.photo_upload)                                          #DONE
    p.date_of_birth=request.POST.get('dateofbirth')
    p.gender=request.POST.get('optradio',p.gender)
    p.present_address=request.POST.get('present_address',p.present_address)
    p.pincode=request.POST.get('pincode',p.pincode)
    a=request.POST.get('permanent_address')
    if a!="":
        p.permanent_address = a
    else:
        p.permanent_address = request.POST.get('present_address')

    p.father_name=request.POST.get('father_name')
    p.father_employment=request.POST.get('father_employment')
    p.father_phone=request.POST.get('father_number',p.father_phone)
    p.mother_name = request.POST.get('mother_name')
    p.mother_employment = request.POST.get('mother_employment')
    p.mother_phone = request.POST.get('mother_number',p.mother_phone)

    p.checkforexperience=request.POST.get('check_experience',p.checkforexperience)
    p.checkforcerti = request.POST.get('check_certi', p.checkforcerti)

    p.bank_name=request.POST.get('bank_name',p.bank_name)
    p.bank_branch=request.POST.get('bank_branch',p.bank_branch)
    p.bank_type=request.POST.get('account_type',p.bank_type)
    p.pan_number=request.POST.get('pan_number',p.pan_number)

#qualification
    request.user.qualification_set.all().delete()
    for i in range(0,len(request.POST.getlist('course'))):
        q = Qualification()
        q.toyear=request.POST.getlist('toyear')[i]
        q.university=request.POST.getlist('university')[i]
        q.course=request.POST.getlist('course')[i]
        q.fromyear=request.POST.getlist('fromyear')[i]
        q.grade=request.POST.getlist('percentage')[i]
        q.user=request.user
        q.save()

#experience
    request.user.experience_set.all().delete()
    for i in range(0,len(request.POST.getlist('company'))):
        e=Experience()
        e.company=request.POST.getlist('company')[i]
        e.designation = request.POST.getlist('designation')[i]
        e.fromyear = request.POST.getlist('from')[i]
        e.toyear= request.POST.getlist('to')[i]
        e.ctc = request.POST.getlist('ctc')[i]
        e.user=request.user
        e.profile=request.POST.getlist('profile')[i]
        e.save()

#certificate
    request.user.certificate_set.all().delete()
    for i in range(0,len(request.POST.getlist('certi_course'))):
        e=Certificate()
        e.course=request.POST.getlist('certi_course')[i]
        e.university = request.POST.getlist('certi_insti')[i]
        e.fromyear = request.POST.getlist('certi_from')[i]
        e.toyear= request.POST.getlist('certi_to')[i]
        e.descp = request.POST.getlist('certi_descp')[i]
        e.user=request.user
        e.save()
	p.save()
    return HttpResponseRedirect(reverse('Login:viewprofile'))

def changepassword(request):
    return render(request, 'Login/changepassword.html')


def savechangepassword(request):
    old = request.POST['oldpassword']
    new = request.POST['newpassword']
    confirm = request.POST['confirmpassword']
    encodedpassword = request.user.password
    a = check_password(password=old, encoded=encodedpassword)
    if a == True:
        if new == confirm:
            request.user.set_password(confirm)
            request.user.save()
            return HttpResponseRedirect(reverse('Login:home_page'))
        else:
            mismatch = "new passwords do not match"
            return render(request, 'Login/changepassword.html', {'mismatch': mismatch})
    else:
        wrongone = "sorry old password do not match"
        return render(request, 'Login/changepassword.html', {'wrongone': wrongone})
