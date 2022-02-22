from django import forms
from .models import Restaurant,Review,Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = [ "name" ]

class RestaurantForm(forms.ModelForm):
    class Meta:
        model   = Restaurant
        fields  = [ "name","description","category","prefecture","city","address","image","lat","lon","ip" ]

class ReviewForm(forms.ModelForm):
    class Meta:
        model   = Review
        fields  = [ "title","content","restaurant","star","ip" ]



