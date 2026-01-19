# from django import forms
# class StudentForm(forms.Form):
#     name = forms.CharField()
#     age = forms.IntegerField()
#     def clean(self):
#         cleaned_data = super().clean()
#         name = cleaned_data.get('name')
#         age = cleaned_data.get('age')
#         if name and age:
#             if name.lower() == 'admin' and age < 25:
#                 raise forms.ValidationError(
#                     "If name is admin, age must be at least 25"
#                 )
#         return cleaned_data


from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
