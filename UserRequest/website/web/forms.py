from django import forms

class projectform(forms.Form):
    projectname= forms.CharField(max_length=20,
    widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Project Name',
    'id':'inputName'
    }))

    projectdesc= forms.CharField(widget=forms.Textarea(attrs={
    'class':'form-control',
    'rows':'5',
    'id':'comment',
    'placeholder':'Project Details'
    }))

    name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Name',
    'id':'inputName'
    }))

    email=forms.EmailField(max_length=30,widget=forms.TextInput(attrs={
    'class':'form-control',
    'placeholder':'Email ID',
    'id':'inputName'
    }))
