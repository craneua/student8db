# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Groups
def groups_list(request):
    groups = (
        {'id': 1,
         'name': u'МтМ - 21',
         'leader': {'id': 1, 'name': u'Олег Ячменев'}},
        {'id': 2,
         'name': u'МтМ - 22',
         'leader': {'id': 2, 'name': u'Віталій Подоба'}},
        {'id': 3,
         'name': u'МтМ - 23',
         'leader': {'id': 3, 'name': u'Андрій Іванов'}},
        )
    return render(request, 'students/groups_list.html', {'groups': groups})

def groups_add(request):
    return HttpResponse('<h1>Add Group Form</h1>')

def groups_edit(request, gid):
    return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
    return HttpResponse('<h1>Delete Group %s</h1>' % gid)
