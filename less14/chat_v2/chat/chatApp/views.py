from django import views
from django.shortcuts import render, redirect
from django.views.generic import FormView
from chatApp.forms import RegistrationForm
from chatApp.models import ChatUser

class Registration(FormView):
    form_class = RegistrationForm
    template_name = "registration.html"
    # def get(self,request):
    #     return render(request, Registration.template_name,
    #                   {"form":RegistrationForm()} )
    def post(self,request):
        form_data = RegistrationForm(request.POST)
        if form_data.is_valid():
            chat_users = ChatUser(name=form_data.cleaned_data["name"],
                                  login=form_data.cleaned_data["login"],
                                  password=form_data.cleaned_data["password"],
                                  role_id_id=1)
            chat_users.save()
            return redirect("/")
        return redirect("/registration")




