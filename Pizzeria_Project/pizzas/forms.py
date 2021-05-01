from django import forms
from .models import Pizza, Topping, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'Name': ''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'Name': ''}

#Might not use
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'Name': ''}


