from django.contrib.auth import authenticate
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import *
from .models import Police


class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name":"username",
            "placeholder":"Username"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name":"password",
            "placeholder":"Password"})

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError(_("Invalid Credentials"))

        return super(UsersLoginForm, self).clean(*args, **keyargs)


class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = Police
        fields = [
        #'bhamashah',

            'username',
            'first_name',
            'last_name',
            'ward',
            'designation',
            #'bhamashah',

            "email",
            "confirm_email",
            "password",
            'confirm_password'
        ]

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label="Email")
    confirm_email = forms.EmailField(label="Confirm Email")
    confirm_password =forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)
    designation=forms.CharField()
    ward=forms.CharField()

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            "name": "email"})
        self.fields['confirm_email'].widget.attrs.update({
            'class': 'form-control',
            "name": "confirm_email"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name": "password"})

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        confirm_email = self.cleaned_data.get("confirm_email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        designation = self.cleaned_data.get("designation")
        ward = self.cleaned_data.get("ward")
        #bhamashah = self.cleaned_data.get("bhamashah")


        #data = b(bhamashah)
        #print(data)



        '''if data is not None and 'AADHAR_ID' in data:
            if aadhaar != data['AADHAR_ID']:
                raise forms.ValidationError('Entered Aadhaar ID does not matched with Aadhaar associalted to this Bhamashah Card')
        else:
            raise forms.ValidationError(
                'Unknown Error Occured!')'''

        if email != confirm_email:
            raise forms.ValidationError("Email must match")

        if password != confirm_password:
            raise forms.ValidationError("Password must match")



        email_qs = Police.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already registered")

        #if not aadhaar.isdigit() or not len(aadhaar)==12:
        #    raise forms.ValidationError("Invalid Aadhar ID")

        username_qs = Police.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("User with this username already registered")

        if len(password) < 8:  # you can add more validations for password
            raise forms.ValidationError("Password must be greater than 8 characters")

        return super(UsersRegisterForm, self).clean(*args, **keyargs)




class criminal_form(forms.ModelForm):
    class Meta:
        model=Criminal
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(criminal_form, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            "name":"name"})
        self.fields['father_name'].widget.attrs.update({
            'class': 'form-control',
            "name":"father_name"})

        self.fields['age'].widget.attrs.update({
            'class': 'form-control',
            "name":"age"})
        self.fields['caste'].widget.attrs.update({
            'class': 'form-control',
            "name":"caste"})
        self.fields['ward'].widget.attrs.update({
            'class': 'form-control',
            "name":"ward"})
        self.fields['birth_mark_desc'].widget.attrs.update({
            'class': 'form-control',
            "name":"birth_mark_desc"})
        self.fields['height'].widget.attrs.update({
            'class': 'form-control',
            "name":"height"})
        self.fields['complexion'].widget.attrs.update({
            'class': 'form-control',
            "name":"complexion"})
        self.fields['eyes'].widget.attrs.update({
            'class': 'form-control',
            "name":"eyes"})

# name = models.CharField(max_length=255, blank=False)

#     father_name = models.CharField(max_length=255)
#     age = models.IntegerField(max_length=255)
#     caste = models.CharField(max_length=255)
#     ward=models.ForeignKey(null=True)
#     birth_mark_desc=models.TextArea()
#     height=models.CharField(max_length=255)
#     complexion=models.CharField(max_length=255)
#     eyes=models.CharField(max_length=255)
