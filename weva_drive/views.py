from django.shortcuts import render, redirect
from weva_drive import models
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
def index(request):
	return render(request,"index.html")
def login(request):
	return render(request,"login/index.html")
def reg(request):
	return render(request,"reg/index.html")
def cust_reg(request):
	return render(request,"reg/newindex.html")

def custom_reg(request):
	name=request.POST['Name']
	phno=request.POST['Number']
	address=request.POST['Address']
	state=request.POST['State']
	district=request.POST['District']
	city=request.POST['city']
	email=request.POST['Email']
	password=request.POST['password']
	le=models.Login.objects.filter(user_name=email)
	if len(le) == 0: 
		reg_data=models.Sam(name=name,phone_number=phno,address=address,state=state,district=district,city=city,email=email,user_type='client')
		reg_data.save()
		log_info=models.Login(user_name=email,password=password,user_type='client',status='active')
		log_info.save()
		messages.warning(request,"Saved successfully")
		return redirect('reg')
	else:
		messages.warning(request,"Email id already exists.")
		return redirect('cust_reg')

def save_reg(request):
	name=request.POST['Name']
	phno=request.POST['Number']
	address=request.POST['Address']
	state=request.POST['State']
	district=request.POST['District']
	city=request.POST['city']
	email=request.POST['Email']
	password=request.POST['password']
	le=models.Login.objects.filter(user_name=email)
	if len(le) == 0:        
		reg_data=models.Sam(name=name,phone_number=phno,address=address,state=state,district=district,city=city,email=email,user_type='service_provider')
		reg_data.save()
		log_info=models.Login(user_name=email,password=password,user_type='service_provider',status='inactive')
		log_info.save()
		messages.warning(request,"Saved Successfully")
		return redirect('reg')
	else:
		messages.warning(request,"Email id already exists.")
		return redirect('reg')
	# reg_data=models.Sam(name=name,phone_number=phno,address=address,state=state,district=district,city=city,email=email,user_type='service_provider')
	# reg_data.save()
	# log_info=models.Login(user_name=email,password=password,user_type='service_provider',status='inactive')
	# log_info.save()
	# return redirect('index')

def check_login(request):
	username = request.POST.get("username", "")
	password = request.POST.get("passw", "")
	log_info = models.Login.objects.filter(user_name=username, password=password)
	try:
		pay_info = models.ServiceproviderPayment.objects.get(se_email=username)
		status=pay_info.status
	except:
		status=None
	for info in log_info:
		if info.status == 'active':
			request.session['semail'] = info.user_name
			request.session['user_type'] = info.user_type
			request.session['pstatus']=status
			if info.user_type == 'service_provider':
				return redirect("../serviceprovider/serviceprovider_dashboard")
			elif info.user_type == 'admin':
				return redirect("../administrator/admin_dashboard")
			elif info.user_type == 'client':
				return redirect("../customer_new/cust_dashboard")
			else:
				messages.warning(request, "Invalid login credentials or inactive account.")
				return redirect('login')
	messages.warning(request, "Invalid login credentials.")
	return redirect('login')
	# return HttpResponse(status)


# def save_client(request):    
#     email=request.POST['email_id']
#     name=request.POST['Name']
#     address=request.POST['Address']
#     phno=request.POST['PhoneNo']
#     state=request.POST['State']
#     dist=request.POST['district']
#     city=request.POST['City']
#     password=request.POST['password'] 
#     le=models.Login.objects.filter(username=email)
#     if len(le) == 0:        
#         reg_data=models.Te(name=name,address=address,phone_no=phno,state=state,district=dist,city=city,email=email,usertype='client')
#         reg_data.save()
#         log_info=models.Login(username=email,password=password,usertype='client',status='active')
#         log_info.save()
#         messages.warning(request,"saved successfully")
#         return redirect('client_reg')
#     else:
#         messages.warning(request,"email id exists")
#         return redirect('client_reg')

			
def logout(request):
			Session.objects.all().delete()
			return redirect('index')
	