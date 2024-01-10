from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'ENTER YOUR NAME*'}),
        required=True
        )
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'placeholder': 'ENTER YOUR EMAIL*'}), 
        required=True
        )
    phone_number = forms.CharField(
        max_length=13, 
        widget=forms.TextInput(attrs={'placeholder': 'PHONE NUMBER'}),
        required=False)
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'YOUR MESSAGE*'}), 
        required=True)

    def __str__(self):
        return self.name