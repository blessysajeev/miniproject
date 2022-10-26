
from django.shortcuts import render,redirect
from .models import Vehicles
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate

# from django.shortcuts import render
# from django.contrib.auth import login, authenticate
# from django.shortcuts import redirect
# from django.http import HttpResponse
# from .models import Account, demo
# from django.contrib import messages 

def index(request):
    obj=Vehicles.objects.all()
    context={'result':obj}
    return render(request,'index.html',context)


# Create your views here.
# def index(request):
#     if 'search' in request.GET:
#         search = request.GET['search']
#         product = Product.objects.filter(name__icontains=search)
#     else:
#         product = Product.objects.all()
#     categories = Category.objects.all()
#     obj = Deals.objects.all()
#     data = {'product':product, 'categories':categories, 'result':obj}
#     return render(request, 'index.html')


# def showcategory(request, cid):
#     categories = Category.objects.all()
#     cats = Category.objects.get(pk=cid)
#     product = Product.objects.filter(cat=cats)
#     data = {
#         'categories':categories,
#         'product':product
#     }
#     return render(request, 'index.html', data)


#     # if request.method == 'GET':
#     #     category_id = request.GET.get('category_id')
#     #     #print(category_id)
#     #     product = Product.objects.filter(Q(cat=category_id)).values()
#     #     # for p in product:
#     #     #     #product = p.values()
#     #     product=json.dumps(list(product.values()))
#     #     print(product)
#     #         #print(product)
#     #     data ={
#     #         'product':product,
#     #     }
#     #     print(data)
#     #     return JsonResponse(data)
#     #     #print(data)    

    



def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']      
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:   
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('register.html') 
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('register.html') 
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
            print("User Created");
            messages.success(request,"successfully registered")
            return redirect('login')
        else:
            messages.info(request,"password not match")
            return redirect('register.html')
    return render(request, 'register.html')


def login(request):
    # request.session.flush()
    # if 'username' in request.session:
    #     return redirect('home.html')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
    

        if user:
            print(2)
            auth.login(request,user)
            #save email in session
            request.session['username'] = username
            

            return redirect('home.html')
        else:
            print(3)
            messages.info(request,"invalid values")
            return redirect('login')     
    return render(request,'login.html')    

def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')

def home(request):
    if 'username' in request.session:
        username=request.session['username']
        obj=Vehicles.objects.all()
        object={'result':obj,'name':username}
        return render(request,'home.html',object)
    return redirect('login')

def change_password(request):
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']

        user = User.objects.get(email__exact=request.user.email)
        success = user.check_password(current_password)
        if success:
            user.set_password(new_password)
            user.save()
            messages.success(request, 'Password updated successfully.')
            return redirect('login')
        else:
            messages.error(request, 'Password does not match!')
            return redirect('change_password')
    return render(request, 'change/change_password.html')

    
