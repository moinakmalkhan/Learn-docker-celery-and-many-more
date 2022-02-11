from django import forms

from .tasks import send_email_task


class EmailForm(forms.Form):
    name = forms.CharField(
        label="Name of Person",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=100,
    )
    email = forms.EmailField(
        label="Email of Person",
        required=True,
        widget=forms.EmailInput(attrs={"class": "form-control"}),
    )
    subject = forms.CharField(
        label="Subject of email",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )
    message = forms.CharField(
        label="Message", widget=forms.Textarea(attrs={"class": "form-control"}), required=True
    )

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        print(self.cleaned_data)
        send_email_task.delay(
            name=self.cleaned_data.get("name"),
            email=self.cleaned_data.get("email"),
            subject=self.cleaned_data.get("subject"),
            message=self.cleaned_data.get("message"),
        )
