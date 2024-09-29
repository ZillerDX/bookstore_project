# store/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book

# ฟอร์มการจัดการหนังสือ

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'description', 'price', 'stock', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300'}),
            'author': forms.TextInput(attrs={'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300'}),
            'description': forms.Textarea(attrs={'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300'}),
            'price': forms.NumberInput(attrs={'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300'}),
            'stock': forms.NumberInput(attrs={'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300'}),
            'image': forms.ClearableFileInput(attrs={'class': 'block w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring focus:border-blue-300'}),
        }

# ฟอร์มลงทะเบียนผู้ใช้ใหม่
class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# ฟอร์มเข้าสู่ระบบ
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
