from django.shortcuts import render
from django.views import View


class FormHandler(View):
    def get(self, request):
        # name = request.GET["username"] ####1 plain text
        # name = request.COOKIES.get("user_name", None) ###2 cookie
        name = request.session.get("user_name", None) ###3 session
        if name == None:
            name = request.GET["username"]
            response = render(request, "answer.html", {"uname":name})
            # response.set_cookie("user_name", name, 10000) ###2
            request.session["user_name"] = name ###3
            return response
        else:
            return render(request, "answer.html", {"uname":name})

