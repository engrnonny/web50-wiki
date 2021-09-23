from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

# product detail page
# product detail page
# product detail page
def single_entry(request, slug):
    context = {
        "entry": util.get_entry(slug)
        }
    return render(request, "encyclopedia/single_entry.html", context)