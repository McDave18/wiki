from django.shortcuts import render
from . import util
import markdown2
from django.shortcuts import render, redirect
import random
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    canonical = util.find_entry_case_insensitive(title)
    if canonical and canonical != title:
        return HttpResponseRedirect(reverse("entry", kwargs={"title": canonical}))

    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"La entrada '{title}' no fue encontrada."
        }, status=404)

    html_content = markdown2.markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
    })


def search(request):
    query = (request.GET.get("q") or "").strip()
    if not query:
        return redirect("index")

    entries = util.list_entries()
    for entry in entries:
        if entry.lower() == query.lower():
            return redirect("entry", title=entry)

    matches = [entry for entry in entries if query.lower() in entry.lower()]
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matches": matches
    })


def create(request):
    if request.method == "POST":
        title = (request.POST.get("title") or "").strip()
        content = (request.POST.get("content") or "").strip()

        if not title or not content:
            return render(request, "encyclopedia/error.html", {
                "message": "Título y contenido son obligatorios."
            }, status=400)

        canonical = util.find_entry_case_insensitive(title)
        if canonical is not None:
            return render(request, "encyclopedia/error.html", {
                "message": f"La entrada '{canonical}' ya existe."
            }, status=409)

        util.save_entry(title, content)
        return redirect("entry", title=title)

    return render(request, "encyclopedia/create.html")


def edit(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": f"La entrada '{title}' no existe y no puede editarse."
        }, status=404)

    if request.method == "POST":
        new_content = (request.POST.get("content") or "").strip()
        if not new_content:
            return render(request, "encyclopedia/error.html", {
                "message": "El contenido no puede estar vacío."
            }, status=400)
        util.save_entry(title, new_content)
        return redirect("entry", title=title)

    return render(request, "encyclopedia/edit.html", {
        "title": title,
        "content": content
    })


def random_entry(request):
    entries = util.list_entries()
    if not entries:
        return render(request, "encyclopedia/error.html", {
            "message": "No hay entradas disponibles para mostrar aleatoriamente."
        })
    title = random.choice(entries)
    return redirect("entry", title=title)