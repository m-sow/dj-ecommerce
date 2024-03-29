from random import choices
from tkinter import Widget
from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

PAYMENT_CHOICES=(
    ('S','Stripe'),
    ('P', 'Paypal')
)

class CheckoutForm(forms.Form):
    street_address=forms.CharField()
    apartment_address=forms.CharField(required=False)
    country = CountryField(blank_label='(select country)').formfield(
         widget=CountrySelectWidget(attrs={
             'class':'custom-select d-block w-100s'
         })
    )
    zip=forms.CharField()
    same_billing_address=forms.BooleanField(required=False)
    save_info=forms.BooleanField(required=False)
    payment_option=forms.ChoiceField(widget=forms.RadioSelect(), choices=PAYMENT_CHOICES)
    