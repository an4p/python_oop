from django import views
from django.shortcuts import render, redirect
from django.views.generic import FormView
from chatApp.forms import RegistrationForm, LoginForm
from chatApp.models import ChatUser
from chatApp.services import UserService


class Registration(FormView):
    form_class = RegistrationForm
    user_service = UserService() ###add due to services.py
    template_name = "registration.html"
    # def get(self,request):
    #     return render(request, Registration.template_name,
    #                   {"form":RegistrationForm()} )
    def post(self,request):
        form_data = RegistrationForm(request.POST)

        if form_data.is_valid():
            Registration.user_service.save_user(form_data) ###add due to services.py
            return redirect("/")

        return render(request, "registration.html",
                      {"error":form_data.errors, "form":RegistrationForm()})

class LoginController(FormView):
    form_class = LoginForm
    user_service = UserService()
    template_name = "login.html"

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            chat_user = LoginController.user_service.verify_login(login_form)
            if chat_user == None:
                return render(request, "login.html",
                              {"error": "Login incorrect", "form": LoginForm()})
            if chat_user != None and chat_user.role_id.role_name == "admin":
                request.session["login"]= chat_user.login
                request.session["admin"]= True
                return redirect("/admin")
            if chat_user != None and chat_user.role_id.role_name == "user":
                request.session["login"] = chat_user.login
                request.session["admin"] = False
                return redirect("/chat")
        return render(request, "login.html",
                      {"error": login_form.errors, "form": LoginForm()})



