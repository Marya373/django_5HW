from django import forms
from shopapp.models import Product

class LoadImageForProduct(forms.Form):

    product = forms.ModelChoiceField(queryset=Product.objects.all(), 
                                     empty_label='Выберите продукт для загрузки изображения',
                                     widget=forms.Select(attrs={'class': 'form-control'}),
                                     label='Товар:'
                                     )
                                     
    image = forms.ImageField(widget=forms.FileInput())

# class AddProduct(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name', 'description', 'price', 'quantity', 'image']

