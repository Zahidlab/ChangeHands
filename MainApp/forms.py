# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm

# from .models import CustomUser

# # Create the form class.

# class RegisterForm(UserCreationForm):


#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = ("sid", "name", "email", "phone_number","password1", "password2", "department", "profile_pic", "id_card_pic", "facebook_profile", )

#         widgets = {
#             "username": forms.TextInput(
#                 attrs={
#                     "class": "form-control",
#                     "placeholder": "Email Address",
#                 }
#             ),
#         }

#     def __init__(self, *args, **kwargs):
#         super(RegisterForm, self).__init__(*args, **kwargs)

#         for fieldname in ["email", "password1", "password2"]:
#             self.fields[fieldname].help_text = None

#     # # @transaction.atomic
#     # def save(self):
#     #     user = super().save(commit=False)
#     #     user.is_student = True
#     #     user.save()
#     #     student = Student.objects.create(user=user, sid = self.sid, department = self.department, id_card_pic = self.id_card_pic, fb_profile = self.fb_profile)
#     #     return user



