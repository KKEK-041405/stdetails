from django import forms

class Form(forms.Form):
    Ipinno = forms.CharField(label='Pinno',max_length=12)    
