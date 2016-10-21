# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

# Views for Students	
def students_list(request):
    #    import pdb; pdb.set_trace()
    students = (
        {'id': 1,
         'first_name': u'Олег',
         'last_name': u'Ячменев',
         'ticket': 2103,
         'image': 'img/avatar03.jpg'},
        {'id': 2,
         'first_name': u'Віталій',
         'last_name': u'Подоба',
         'ticket': 2214,
         'image': 'img/podoba.jpeg'},
        {'id': 3,
         'first_name': u'Андрій',
         'last_name': u'Іванов',
         'ticket': 2307,
         'image': 'img/avatar03.jpg'},
        )
    return render(request, 'students/students_list.html',
        {'students': students})
	
def students_add(request):
    return HttpResponse('<h1>Add Student Form</h1>')

def students_edit(request, sid):
    return HttpResponse('<h1>Edit Student %s</h1>' % sid)

def students_delete(request, sid):
    return HttpResponse('<h1>Delete Student %s</h1>' % sid)
