from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout #fuction to authenticate the login and logout 
from django.contrib.auth.decorators import login_required #used so that if we need to get to the home page we must login
from django.contrib import messages #it is used to display the messages like usernaem already exists
from modules.models import recipes
from django.core import paginator
from django.core.paginator import Paginator


@login_required(login_url='login')

def MyHtml(request):
    return render(request,"index.html")

#------------------------------------signup----------------------------------------------------------
def Signup(request):
    if request.method=="POST":#entering the required fields to setup signup
        uname=request.POST.get('name')
        email=request.POST.get('email')
        name=request.POST.get('username')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')
        user= User.objects.filter( email = email)
        if user.exists():#checking if user already exists or not
            messages.info(request, "Email already exists") #iif eexists then the message is displayed
            return redirect('signup')
        if pass1 != pass2:#checking if the password you entered is same or not
             messages.info(request, "password is not the same")#if password is not the same then the following message is displayed
             return redirect('signup')
        t=request.POST.get('terms')
        my_user=User.objects.create_user(email,name,pass1) #selecting the required fields for future signins and also creaye_user oonly takes 3 input arguments
        my_user.save()#saving the created user into the database
        return redirect('login') 
    
    return render(request,'register.html')
#------------------------------------------------------end signup------------------------------------------------------------

#-----------------------------------------------------login------------------------------------------------------------------
def logins(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        rem=request.POST.get('remember')
        user=authenticate(request,username=username,password=pass1)#checking if the users username and password are the same or not
        if user is not None :
            login(request,user)
            return redirect("home")
        else:
            messages.info(request, "You entered wrong credentials")
            return redirect("login")

    return render(request,'login.html')
#--------------------------------------------------------------------end login------------------------------------------------

#---------------------------------------------------------------------logout--------------------------------------------------
def LogoutPage(request):
    logout(request)
    return redirect('login')
#----------------------------------------------------------------------end logout---------------------------------------------

#-------------------------------------------------------------------dispaly recipe-------------------------------------------
def addrec(request):
    if request.method == "POST":
        recipe_name = request.POST.get('recipe_name')
        intro = request.POST.get('intro')
        ingredients = request.POST.get('ingredients')
        making = request.POST.get('making')
        nut = request.POST.get('nut')
        protein = request.POST.get('protein')
        recipe_image = request.FILES.get('recipe_image')

        en = recipes(recipe_name = recipe_name, intro = intro, ingredients = ingredients, making = making, nut = nut, protein = protein, recipe_image = recipe_image)
        en.save()
    
    return render(request,'search.html')
# Create your views here.
def food(request):
    recipeData=recipes.objects.all()
    if request.method=="GET":
        st=request.GET.get('recipe_name')
        if st!=None:
            recipeData = recipes.objects.filter(recipe_name__icontains=st)#it is used to search the recipe and icontains is used so that even if we enter one word also it will search it 
    data={
        'recipeData':recipeData
    }
    return render(request,'search.html',data)

def recipes_details(request):
    recipe_name = request.GET.get('recipe_name')
    recipe = recipes.objects.get(recipe_name=recipe_name)
    datas = {
        'recipe': recipe
    }
    return render(request, 'recipe_details.html',datas)

#def chefing(request):
   # chefDatas = chefDatas.objects.all()
    #p = Paginator(chefDatas.object.all(),3)
    #page_number = request.GET.get('page')
    #page=p.get_page(page_number)
    if request.method == "POST":
        chef_name = request.POST.get('chef_name')
        chef_age= request.POST.get('chef_age')
        chef_exp = request.POST.get('chef_exp')
        chef_info = request.POST.get('chef_info')
        recipe_name = request.POST.get('recipe_name')
        cheif_image = request.FILES.get('chef_image')

        en = chef(chef_name = chef_name, chef_age = chef_age, chef_exp = chef_exp, chef_info = chef_info , recipe_name= recipe_name, cheif_image = cheif_image)
        en.save()
        chefData = chef.objects.all()
    dat = {
        'chefData':chefData
    }
    return render(request,"index.html",dat) 
#def showing(request):
    chef_name = request.POST.get('chef_name')
    cheif_image = request.POST.get('cheif_image')
    chefs=chef.objects.get(chef_name = chef_name)
    ch = chef.objects.get(cheif_image = cheif_image)
    data={
        'chefs':chefs,
        'ch' : ch
    }
    return render(request,'search.html',data)
    

def chef_inf(request):
    if request.method == "POST":
        chef_name = request.POST.get('chef_name')
        chef_age= request.POST.get('chef_age')
        chef_exp = request.POST.get('chef_exp')
        chef_info = request.POST.get('chef_info')
        recipe_name = request.POST.get('recipe_name')
        cheif_image = request.FILES.get('chef_image')
        en = chef(chef_name = chef_name , chef_age = chef_age , chef_exp = chef_exp , chef_info = chef_info , recipe_name= recipe_name, cheif_image = cheif_image)
        en.save()
        
    
    return render( request , "chef_details.html")