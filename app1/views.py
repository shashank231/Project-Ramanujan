from django.shortcuts import render, redirect
from .models import *
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required     # login decorator
from django.contrib import messages
from.forms import *


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm() #we imorted it above from forms
        if request.method == 'POST':
            form = CreateUserForm(request.POST)  #is form me sara user ka enter kia hua data save ho jaega
            if form.is_valid():
                user_pro = form.save()
                Profile.objects.create(anna=user_pro)
                user = form.cleaned_data.get('username')   # saved form se sirf username nikala
                messages.success(request, 'Account was created for ' + user) # message display karne ke lie username concatenate kar dia
                return redirect('login')   # jaise hi register ho jaega user login page par chal jaega

        context = {'form': form}
        return render(request, 'app1/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')  # jo username enter kia hai use username me store kia
            password = request.POST.get('password')  # jo password enter kia hai use password me store kia

            user = authenticate(request, username=username, password=password) # ye check karega ki iss username ka ye password hai ki nahi
            if user is not None:         # agar aisa user hai
                login(request, user)     #here login is a django built in command, ye user ko login karega jisko abhi authenticate kia hai
                return redirect('index') #login karne ke bad index page pe redirect kar dega
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'app1/login.html', context)

def logoutUser(request):
	logout(request)     # is logout ko humne upar import kia hai
	return redirect('index')

def index(request):
    return render(request, 'app1/index.html')

def aboutus(request):
    return render(request, 'app1/aboutus.html')

@login_required(login_url='login')
def leaderboard(request):
    leaders = Profile.objects.all().order_by('-score')   # VI - we here use .order_by to order them according to score
    context = {'leaders': leaders}
    return render(request, 'app1/leaderboard.html', context)

@login_required(login_url='login')
def ques(request):
    qun = Display.objects.all()
    paginator = Paginator(qun, 5)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    curr_user = Profile.objects.get(anna=request.user)
    lst1 = curr_user.qdone
    lst = []
    for i in lst1:
        j = int(i)
        lst.append(j)
    score = curr_user.score
    leaders = Profile.objects.all().order_by('-score')
    rank = 1
    for i in leaders:
        if str(i) == str(request.user.username):
            break
        else:
            rank = rank + 1
    context = {'qun': page_obj, 'lst': lst, 'score': score, 'rank': rank}
    return render(request, 'app1/ques.html', context)

@login_required(login_url='login')
def show(request, pk):
    qunn = Display.objects.get(id=pk)
    namn = qunn.qnam
    qu = Question.objects.get(id=pk)
    context = {'namn': namn, 'qu': qu}
    return render(request, 'app1/show.html', context)


@login_required(login_url='login')
def check(request, pk):
    if request.method == 'POST':
        your_ans = request.POST['quantity']
    qu1 = Question.objects.get(id=pk)
    id3 = int(pk) + 1
    id2 = str(id3)
    cor_ans = qu1.ans
    curr_user = Profile.objects.get(anna=request.user)
    if your_ans == cor_ans:
        flag = 1
        if pk not in curr_user.qdone:
            curr_user.score += 1  # curr_user ki profile me score access kia use 1 se badaya.
            curr_user.save()      # VI - us change ko save karna is very very important.
            curr_user.qdone.append(pk)
            curr_user.save()
        else:
            pass
    else:
        flag = 0
    context = {'flag': flag, 'id2': id2, 'id3': id3}
    return render(request, 'app1/check.html', context)

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(anna=request.user)  # User login kar chuka hai, iska matlab request.user hame user dega.
    print(request.user)                                # anna profile model me user hai to use login user set kar dia.
    print(profile.name)
    context = {'profile': profile}
    return render(request, 'app1/profile.html', context)

@login_required(login_url='login')
def update(request):
    cur_user = Profile.objects.get(anna=request.user)
    form = ProfileForm(instance=cur_user)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=cur_user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'app1/update.html', context)






