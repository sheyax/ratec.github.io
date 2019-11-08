from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import Photo, UpMod
from django.core.files import File
from PIL import Image
from croppie.fields import CroppieField 

class UserRegisterForm (UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    class Meta:
        model = Profile
        fields = ['image', 'x', 'y', 'width', 'height']
    
    def save(self):
        photo = super(ProfileUpdateForm, self).save()
        
        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')
        
       # images =  images.open(photo.image)
        #cropped_images= images.crop((x,y, w+x, h+y))
       # resized_image = cropped_image.resize((200, 200), Images.ANTIALIAS)
        #resized_image.save(photo.image.path)
        
        return photo


class PhotoForm(forms.ModelForm):
    x = forms.FloatField(widget=forms.HiddenInput())
    y = forms.FloatField(widget=forms.HiddenInput())
    width = forms.FloatField(widget=forms.HiddenInput())
    height = forms.FloatField(widget=forms.HiddenInput())
    
    
    class Meta:
        model = Photo
        fields = ('file', 'x', 'y', 'width', 'height', )
        
    def save(self):
        photo = super(PhotoForm, self).save()

        x = self.cleaned_data.get('x')
        y = self.cleaned_data.get('y')
        w = self.cleaned_data.get('width')
        h = self.cleaned_data.get('height')

        image = Image.open(photo.file)
        cropped_image = image.crop((x, y, w+x, h+y))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        resized_image.save(photo.file.path)

        return photo
    
class UpForm(forms.Form):
    image = CroppieField(
        options={
            'viewport': {
                'width': 120,
                'height': 140,
            },
            'boundary': {
                'width': 200,
                'height': 220,
            },
            'showZoomer': True,
        },
    )
    
    class Meta:
        model= UpMod 
        feilds = '__all__'
    
    
        
