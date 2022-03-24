from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs): #*args, **kwargs
    #return HttpResponse("<h1>Hello World</h1>") #String of HTML code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contact Page</h1>")
    return render(request, "contact.html",{})

def about_view(request, *args,**kwargs):
    #return HttpResponse("<h1>About page</h1>")
    my_context={
        "my_title":"This is about us",
        "my_number":123,
        "this_is_true": True,
        "my_list":[123,231,312,"Abc"],
        "my_html":"<h1>Hello World</h1>"
    }
    return render(request, "about.html", my_context)