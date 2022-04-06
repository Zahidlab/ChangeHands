# Register your models here.

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError

from .models import *


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'phone_number', 'department', 'is_superuser')
    list_filter = ('is_superuser','department',)
    fieldsets = (
        (None, {'fields': ('email', 'password','sid')}),
        ('Personal info', {'fields': ('name', 'phone_number', 'profile_pic', 'department', 'facebook_profile', 'id_card_pic')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('sid','email', 'password1', 'password2', 'name', 'phone_number', 'department', 'facebook_profile', 'id_card_pic', 'profile_pic', 'is_superuser')}
        ),
    )
    # search_fields = ('email',)
    ordering = ('date_joined',)
    # filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)
# class UserCreationForm(forms.ModelForm):
#     """A form for creating new users. Includes all the required
#     fields, plus a repeated password."""
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

#     class Meta:
#         model = CustomUser
#         # fields = ('email', '')
#         fields = ("sid", "name", "email", "phone_number","password1", "password2", "department", "profile_pic", "id_card_pic", "facebook_profile")

#     def clean_password2(self):
#         # Check that the two password entries match
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError("Passwords don't match")
#         return password2

#     def save(self, commit=True):
#         # Save the provided password in hashed format
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password1"])
#         if commit:
#             user.save()
#         return user


# class UserChangeForm(forms.ModelForm):
#     """A form for updating users. Includes all the fields on
#     the user, but replaces the password field with admin's
#     disabled password hash display field.
#     """
#     password = ReadOnlyPasswordHashField()

#     class Meta:
#         model = CustomUser
#         # fields = ('email', 'password', 'date_of_birth', 'is_active', 'is_admin')
#         fields = ("sid", "name", "email", "phone_number", "department", "profile_pic", "id_card_pic", "facebook_profile")


# class UserAdmin(BaseUserAdmin):
#     # The forms to add and change user instances
#     form = UserChangeForm
#     add_form = UserCreationForm

#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
#     list_display = ('sid', 'email', 'name', 'department', 'is_admin')
#     list_filter = ('is_admin',)
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('number',)}),
#         ('Permissions', {'fields': ('is_admin',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ("sid", "name", "email", "phone_number","password1", "password2", "department", "profile_pic", "id_card_pic", "facebook_profile"),
           
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ()


# # Now register the new UserAdmin...
# admin.site.register(CustomUser, UserAdmin)
# # ... and, since we're not using Django's built-in permissions,
# # unregister the Group model from admin.
# admin.site.unregister(Group)



admin.site.register(Comment)
admin.site.register(Catagory)
admin.site.register(Product)
admin.site.register(Post)


