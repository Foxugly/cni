from django.shortcuts import render
from document.models import OrderOfBusinessForm, OrderOfBusiness, Subject
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _


def oob_add(request):
    c = {}
    if request.method == 'POST':
        form = OrderOfBusinessForm(request.POST)
        if form.is_valid():
            f = form.save()
            if 'subject[]' in request.POST:
                f.subjects.all().delete()
                for sub in request.POST.getlist('subject[]'):
                    s = Subject(subject=sub)
                    s.save()
                    f.subjects.add(s)
            f.save()
            return HttpResponseRedirect('/document/oob/%d/' % f.id)
        else:
            c['form'] = [form]
            messages.error(request, "Error")
    else:
        c['form'] = [OrderOfBusinessForm(), ]
    c['url'] = "/document/oob/add/"
    c['title'] = _("New order of business")
    return render(request, 'oob.tpl', c)


def oob_view(request, id):
    c = {}
    inst = OrderOfBusiness.objects.get(id=id)
    print inst
    if request.method == 'POST':
        form = OrderOfBusinessForm(request.POST, instance=inst)
        if form.is_valid():
            f = form.save()
            if 'subject[]' in request.POST:
                f.subjects.all().delete()
                for sub in request.POST.getlist('subject[]'):
                    s = Subject(subject=sub)
                    s.save()
                    f.subjects.add(s)
            f.save()
            return HttpResponseRedirect('/document/oob/%d/' % f.id)
        else:
            c['form'] = [form]
            messages.error(request, "Error")
    else:
        c['form'] = [OrderOfBusinessForm(instance=inst), ]
        print
    c['url'] = "/document/oob/" + str(id) + '/'
    c['title'] = _("Update order of business")
    c['instance'] = inst
    return render(request, 'oob.tpl', c)
