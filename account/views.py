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
from PIL import Image
from account.models import operations,profile
import hashlib,json
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
			return render(request, 'account/purchecker.html')
		else:
			return render(request, 'account/login.html')
	elif request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render(request, 'account/purchecker.html')
		else:
			return render(request, 'account/login.html')

def dashboard(request):
	if request.user.is_authenticated:
		#Do Other Stuff
		#Authentication done
		return render(request,'<Show Dashboard>')
	else:
		logout(request)
		return HttpResponseRedirect('<Show Login Page>')


def UploadPURForm(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = UploadPURForm(request.POST)
			if form.is_valid():
				bhamasa = form.cleaned_data['bhamasa']
				#Now Save the stuff to Operations on doctor username
				operation_obj = operations()
				hash_object = hashlib.sha1(form.cleaned_data['bhamasa'])
				pur_temp = hash_object.hexdigest()
				operation_obj.pur = pur_temp
				operation_obj.username = request.user.id
				operation_obj.bhamasahof = bhamasa
				operation_obj.filename = file_path
				bhamasa_details = get_bhama(bhamasa)
				operation_obj.aadharhof = bhamasa_details['hof_aadhar']
				operation_obj.mobile = form.cleaned_data['mobile']
				operation_obj.save(commit=True)
				return render(request,'<success_url for created PUR>',bhamasa_details)
			form = UploadPURForm()
			return render(request, 'account/purgenerator.html', {'form': form})
		else:
			return render(request,'account/purgenerator.html')
	else:
		return render(request,'account/login.html')
				

def createaccount(request):
	if(authentic(request)):
		if(request.method == 'POST'):
			#Make the user with the details
			profile = profile(request.POST)
			if profile.is_valid():
				user = User.objects.create_user(profile.cleaned_data['username'], profile.cleaned_data['email'], request.POST['password'])
				user.first_name = profile.cleaned_data['first_name']
				user.last_name = profile.cleaned_data['last_name']
				user.save()
			else:
				profile = profile()
		else:
			return render(request,'<Create Account Page>',{'profile' : profile})
	else:
		profile = profile()
		return render(request,'<Create Account Page>',{'profile' : profile})

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
		details['mobile'] = temp_obj.mobile
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

