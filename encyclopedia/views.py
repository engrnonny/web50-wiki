from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . import util

# home page
# home page
# home page
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# single entry page
# single entry page
# single entry page
def single_entry(request, slug):
    entry = util.get_entry(slug)
    if entry:
        context = {
            "entry": entry,
            "slug": slug
        }    
    else:          
        context = {
            "slug": slug
        }
    return render(request, "encyclopedia/single_entry.html", context)

# search functionality
# search functionality
# search functionality
def search(request):
    if request.method == "POST":
        q = request.POST["q"]
        if q:
            # return redirect("single_entry", slug=q )
            return HttpResponseRedirect(reverse("encyclopedia:single_entry"), slug=q)

    else:
        pass
