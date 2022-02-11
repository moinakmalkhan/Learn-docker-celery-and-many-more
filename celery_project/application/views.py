from django.shortcuts import render
from django.views import View

from .forms import EmailForm


class EmailView(View):
    def get(self, request):
        form = EmailForm()
        context = {"form": form}
        return render(request, "application/email.html", context)

    def post(self, request):
        # send email using the self.cleaned_data dictionary
        form = EmailForm(request.POST)
        if form.is_valid():
            form.send_email()
            return render(
                request, "application/email_success.html", {"message": "Email sent successfully"}
            )
        return render(request, "application/email.html", {"form": form})
