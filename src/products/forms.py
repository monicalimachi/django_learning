from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    title=forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    email=forms.EmailField()
    description=forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class":"new-class-name two",
                "is": "my_id_for_textarea",
                "rows": 10,
                "cols":50
            }
        ))
    price = forms.DecimalField(initial=0.00)    

    class Meta:
        model=Product
        fields=[
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args,**kwargs):
        title=self.cleaned_data.get("title")
        if not "prod" in title:
            raise forms.ValidationError("This is not a valid title, add prod")
        return title

    def clean_email(self, *args,**kwargs):
        email=self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid email")
        return email


class RawProductForm(forms.Form):
    title=forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description=forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                "class":"new-class-name two",
                "is": "my_id_for_textarea",
                "rows": 10,
                "cols":50
            }
        ))
    price = forms.DecimalField(initial=0.00)