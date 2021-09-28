
from django.contrib import messages

from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.urls import reverse
from . import util

# home page
# home page
# home page
def index(request):
    if request.method == "POST":
        q = request.POST["q"]
        if q:
            entry = util.get_entry(q)
            if entry:
                return redirect(f'wiki/{q}/')
            else:
                return redirect(f'search/q={q}/')

    else:
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

# search result page
# search result page
# search result page
def search(request, q):
    entries = util.list_entries()
    search_result = [k for k in entries if q in k]
    context = {
        "search_result": search_result,
        "q": q
    }
    return render(request, "encyclopedia/search.html", context)

# New entry page
# New entry page
# New entry page
def new_entry(request):
    if request.method == "POST":
        title = request.POST["title"]
        check_entry = util.get_entry(title)
        if check_entry:
            messages.error(request, "Entry already exist")
            return render(request, "encyclopedia/new_entry.html")
        else:
            content = request.POST["content"]
            if content:
                util.save_entry(title, content)
                return redirect("single-entry", slug=title )

    else:
        return render(request, "encyclopedia/new_entry.html")

# Edit entry page
# Edit entry page
# Edit entry page
def edit_entry(request, slug):
    if request.method == "POST":
        content = request.POST["content"]
        title = request.POST["title"]
        if content:
            print(content)
            print(title)
            util.save_entry(title, content)
            return redirect("single-entry", slug=title )

    else:
        entry = util.get_entry(slug)
        if entry:
            context = {
                "entry": entry,
                "slug": slug
            }  
        return render(request, "encyclopedia/edit_entry.html", context)
    