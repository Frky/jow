from random import choice

from django.shortcuts import render, redirect, get_object_or_404

from website.models import OneWord
from website.forms import OneWordForm

colors = [
            "#1abc9c", "#16a085", "#2ecc71", "#27ae60", 
            "#f1c40f", "#f39c12", "#e67e22", "#d35400", 
            "#3498db", "#2980b9", "#e74c3c", "#c0392b",
            "#9b59b6", "#8e44ad", "#34495e", "#2c3e50", 
            "#ecf0f1", "#bdc3c7", "#95a5a6", "#7f8c8d", 
        ] 

def index(request):
    tpl = "jow/index.html"
    ctxt = dict()
    ctxt['nb_jow'] = OneWord.objects.count()
    ctxt['fgcolor'] = choice(colors)
    ctxt['bgcolor'] = choice(colors)
    while ctxt['bgcolor'] == ctxt['fgcolor']:
        ctxt['bgcolor'] = choice(colors)
    one_word_form = OneWordForm(
                                    request.POST or None, 
                                    label_suffix="", 
                                    initial={"bg_color": ctxt["bgcolor"], "fg_color": ctxt["fgcolor"]}
                                )
    ctxt['form'] = one_word_form
    if one_word_form.is_valid():
        one_word = one_word_form.save()
        return redirect("one_word", oid=one_word.id)
    return render(request, tpl, ctxt)


def one_word(request, oid):
    tpl = "jow/one_word.html"
    ctxt = dict()
    ctxt["word"] = get_object_or_404(OneWord, id=oid)
    return render(request, tpl, ctxt)
