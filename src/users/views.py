from django.shortcuts import redirect, render
from django.views import View

from .forms import CreateUserForm


class RegistrationView(View):
    template_name = "registration/registration.html"

    def get(self, request):
        context = {
            "form": CreateUserForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        context = {
            "form": form,
        }
        return render(request, self.template_name, context)
