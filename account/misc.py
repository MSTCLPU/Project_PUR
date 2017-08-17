import requests
def handle_uploaded_file(f,dest):
	with open('/account/static/'+dest, 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def get_bhama(bhamasa):
	url = 'https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/Bhamashah/hofAndMember/'+ bhamasa +'?client_id=ad7288a4-7764-436d-a727-783a977f1fe1'
	r = requests.get(url)
	json_resp = r.json()

	data_list = {
		'hof_name':json_resp['hof_Details']['NAME_ENG'],
		'hof_aadhar' : json_resp['hof_Details']['AADHAR_ID'],
		'hof_dob' : json_resp['hof_Details']['DOB'],
		'hof_bhamasa' : bhamasa,
		'hof_mid' : json_resp['hof_Details']['M_ID'],
		'hof_gender' : json_resp['hof_Details']['GENDER'],
		'hof_picture' : get_photo(bhamasa),
		'spouse_name' : json_resp['family_Details'][0]['NAME_ENG'],
		'spouse_aadhar' : json_resp['family_Details'][0]['AADHAR_ID'],
		'spouse_dob' : json_resp['family_Details'][0]['DOB'],
		'spouse_gender' : json_resp['family_Details'][0]['GENDER'],
		'spouse_mid' : json_resp['family_Details'][0]['M_ID'],
	}
	return data_list

def get_photo(bhamasa):
	url = 'https://apitest.sewadwaar.rajasthan.gov.in/app/live/Service/hofMembphoto/'+ bhamasa +'/0?client_id=ad7288a4-7764-436d-a727-783a977f1fe1'
	r = requests.get(url)
	photo_resp = r.json()
	return str(photo_resp['hof_Photo']['PHOTO'])