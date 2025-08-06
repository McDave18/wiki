from django.shortcuts import render
from . import util
import markdown2
from django.shortcuts import render, redirect


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"La entrada '{title}' no existe."
        })
    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })

def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()

    # Si el título coincide exactamente (ignorando mayúsculas/minúsculas)
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("entry", title=entry)

    # Si hay coincidencias parciales
    matches = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matches": matches
    })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title").strip()
        content = request.POST.get("content").strip()

        # Validar si ya existe
        if util.get_entry(title) is not None:
            return render(request, "encyclopedia/error.html", {
                "message": f"La entrada '{title}' ya existe."
            })

        # Guardar entrada y redirigir
        util.save_entry(title, content)
        return redirect("entry", title=title)

    return render(request, "encyclopedia/create.html")
