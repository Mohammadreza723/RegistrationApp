from django import forms

class SignUpform(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=20)
    phone_number = forms.CharField(max_length=12, min_length=12)
    email = forms.EmailField()
    def clean_phone_number(self):
        phone_number = self.clean_data["phone_number"]
        if not phone_number.is_digit():
            message = "phone number must be digit!!!"
            raise forms.ValidationError(message)
        return phone_number