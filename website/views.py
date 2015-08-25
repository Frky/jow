from django.shortcuts import render, redirect, get_object_or_404

from website.models import OneWord
from website.forms import OneWordForm

def index(request):
    tpl = "jow/index.html"
    ctxt = dict()
    one_word_form = OneWordForm(request.POST or None, label_suffix="")
    ctxt['form'] = one_word_form
    ctxt['nb_jow'] = OneWord.objects.count()
    if one_word_form.is_valid():
        one_word = one_word_form.save()
        return redirect("one_word", oid=one_word.id)
    return render(request, tpl, ctxt)


def one_word(request, oid):
    tpl = "jow/one_word.html"
    ctxt = dict()
    ctxt["word"] = get_object_or_404(OneWord, id=oid)
    return render(request, tpl, ctxt)
