#here we create each form as class 

from django import forms
from .models import Users_db
class add_users(forms.ModelForm):
    #create the meta data 
    class Meta:
        model=Users_db
        fields='__all__'
        labels={
            'username': 'Username',
            'Phone_num': 'phone_num',
            'email': 'Email',
            'Gender': 'gender',
            'birthday':' Birthday'
        }
        widgets={
            'username':forms.TextInput(attrs={
                'placeholder':'e.g. write yourname', 
                'class': 'form-control'}),

            'Phone_num':forms.NumberInput(attrs={
                'class': 'form-control'}),

            'email':forms.TextInput(attrs={
                'class': 'form-control'}),

            'Gender':forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'birthday':forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'})
        }