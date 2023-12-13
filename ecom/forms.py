from django import forms
from django.contrib.auth.models import User
from .models import Subscription, Product
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['brand', 'category', 'name', 'code', 'product_image', 'price', 'description', 'quantity', 'status']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # Customize widget attributes
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['code'].widget.attrs.update({'class': 'form-control'})
        
        # Customize field labels and help text
        self.fields['product_image'].label = 'Product Image'
        self.fields['price'].help_text = 'Enter the price in your local currency.'

        # Modify choices for the 'status' field
        custom_status_choice = ('custom_status', 'Custom Status')
        self.fields['status'].choices = [custom_status_choice] + self.fields['status'].choices

    def clean_price(self):
        # Custom validation for the 'price' field
        price = self.cleaned_data['price']
        if price < 0:
            raise forms.ValidationError('Price cannot be negative.')
        return price


#address of shipment
class AddressForm(forms.Form):
    Email = forms.EmailField()
    Mobile= forms.IntegerField()
    Address = forms.CharField(max_length=500)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name','feedback']

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# Email Subscription
# forms.py
from django import forms
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']

    widgets = {
        'email': forms.EmailInput(attrs={'class': 'form-control rounded-left', 'placeholder': 'Enter email address'}),
    }
