"""
This is the form file for making the update on operation done, or rather PUR Updated"

"""
from django import forms
from django.core.validators import MinLengthValidator

class UploadPURForm(forms.Form):
	bhamasa = forms.CharField(max_length=20,validators=[MinLengthValidator(11)])
	mobile = forms.IntegerField()
	hofphoto = forms.FileField()
	def extension(self):
		name, extension = os.path.splitext(self.file.name)
		return extension
