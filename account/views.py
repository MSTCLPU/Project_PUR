from django.shortcuts import render
from django.contrib.auth import authenticate ,login ,logout
from django.template import Context, loader
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from easy_pdf.views import PDFTemplateView
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from account.forms import UploadPURForm
from account.misc import handle_uploaded_file,get_bhama
from django.contrib.auth.models import User
from reportlab.pdfgen import canvas
from PIL import Image
from account.models import operations,profile
import hashlib,json
from easy_pdf.views import PDFTemplateView
import datetime
from django.core.exceptions import ObjectDoesNotExist
import base64
def authentic(request):
	if request.user.is_authenticated:
		return True
	else:
		return False


def json_response(something):
	return HttpResponse(
		json.dumps(something),
		content_type = 'application/json; charset=utf8'
	)


def logoutit(request):
	logout(request)
	return render(request,'account/login.html')

def loginit(request):
	if request.method == 'GET':
		if authentic(request):
			return render(request, 'account/profile.html')
		else:
			return render(request, 'account/login.html')
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'account/profile.html')
		else:
			return render(request, 'account/login.html')

def dashboard(request):
	if request.user.is_authenticated:
		#Do Other Stuff
		#Authentication done
		return render(request,'account/profile.html')
	else:
		logout(request)
		return HttpResponseRedirect('account/login.html')


def UploadPURForm(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			bhamasa = request.POST['bhamasa']
			#Now Save the stuff to Operations on doctor username
			operation_obj = operations()
			hash_object = hashlib.sha1(bhamasa.encode('utf-8'))
			pur_temp = hash_object.hexdigest()
			try:
				temp_obj = profile.objects.get(username='sanu')
				operation_obj.hospital = temp_obj.hospital
				operation_obj.doctor = temp_obj.first_name + ' ' + temp_obj.last_name
			except(ValueError,ObjectDoesNotExist):
				return render(request,'account/purgen.html')
			operation_obj.pur = pur_temp
			operation_obj.username = request.user
			operation_obj.bhamasahof = bhamasa
			bhamasa_details = get_bhama(bhamasa)
			operation_obj.aadharhof = bhamasa_details['hof_aadhar']
			operation_obj.save()
			bhamasa_details['pur'] = pur_temp;
			return render(request,'account/purgendone.html',{'bhamasa_details' : bhamasa_details})
		else:
			return render(request,'account/purgen.html')
	else:
		return render(request,'account/login.html')

def test(request):
	return render(request,'account/purcert.html')

class HelloPDFView(PDFTemplateView):
    template_name = 'account/purcert.html'		

def cert(request,pur,name):
	request.session['pur'] = pur
	request.session['name'] = name
	return HelloPDFView.as_view()(request)


def createaccount(request):
	if(authentic(request)):
		if(request.method == 'POST'):
			#Make the user with the details
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['email']

			user = User.objects.create_user(username,email, password)
			obj = profile()
			obj.first_name = user.first_name = request.POST['f_name']
			obj.last_name = user.last_name = request.POST['l_name']
			obj.username = username
			obj.aadharid = int(request.POST['aadhaar'])
			obj.hospital = request.POST['hospital']
			obj.designation = request.POST['designation']
			obj.experience = request.POST['experience']
			obj.nationality = 'Indian'
			obj.save()
			user.save()
		
		else:
			return render(request,'account/signup.html')
	else:
		return render(request,'account/signup.html')

def checkpur(request):
	if(authentic(request)):
		if request.method == 'GET':
			#Show PUR Details Check page
			return render(request,'account/purchecker.html')
		elif request.method =='POST':
			pur_temp = request.POST['pur']
			try:
				temp_obj = operations.objects.get(pur=pur_temp)
				bhamasahof = temp_obj.bhamasahof
				aadharhof = temp_obj.aadharhof
				details = get_bhama(bhamasahof)
				details['bhamasahof'] = temp_obj.bhamasahof
				details['aadharhof'] = temp_obj.aadharhof
				return render(request,'account/purchecker.html',{'details': details})
			except (ValueError, ObjectDoesNotExist):
				error = True
				return render(request,'account/purchecker.html',{'error' : error})
	else:
		return render(request,'account/login.html')

def generateBC(request):
	if(authentic(request)):
		#Generate BC
		return render(request,'<Make PDF>')
	else:
		error = True
		return render(request,'<Show Login Page>',{'error' : error})

def androidapi(request,pur_id):
	try:
		temp_obj = operations.objects.get(pur=pur_id)
		bhamasahof = temp_obj.bhamasahof
		aadharhof = temp_obj.aadharhof
		details = get_bhama(bhamasahof)
		details['date'] = str(temp_obj.date)
		details['hospital'] = temp_obj.hospital
		obj = profile.objects.get(username=temp_obj.username)
		details['doctor'] = obj.first_name+' '+obj.last_name
		return HttpResponse(
			json.dumps(details),
			content_type = 'application/json; charset=utf8'
		)
	except (ValueError, ObjectDoesNotExist):
		details['error'] = True
		return HttpResponse(
			json.dumps(details),
			content_type = 'application/json; charset=utf8'
		)

def false(request):
	return HttpResponse("Hello")

def dashboard(request):
	if request.user.is_authenticated:
		obj = profile.objects.get(username = request.user)
		return render(request,'account/profile.html',{'profile':obj})
	else:
		return render(request,'account/login.html')

def hospital(request):
	if request.user.is_authenticated:
		return render(request,'account/hosp_profile.html')
	else:
		return render(request,'account/login.html')