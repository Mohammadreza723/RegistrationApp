from django.shortcuts import render
from django.views import View
from .forms import SignUpform

class Hello(View):
    def get(self, request):
        form = SignUpform()
        context = {
            "name": "Mohammadreza",
            "form": form,
        }
        return render(request=request, template_name="example.html", context=context)