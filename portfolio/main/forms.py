from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR NAME*'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'ENTER YOUR EMAIL*'}))
    phone_number = forms.CharField(max_length=13, widget=forms.TextInput(attrs={'placeholder': 'PHONE NUMBER'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'YOUR MESSAGE*'}))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact form'