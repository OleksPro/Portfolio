from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100, widget=forms.TextInput(),
        required=True
        )
    email = forms.EmailField(widget=forms.TextInput(), 
        required=True
        )
    phone_number = forms.CharField(
        max_length=13, 
        widget=forms.TextInput(),
        required=False
        )
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(), 
        required=True
        )

    def __str__(self):
        return self.name