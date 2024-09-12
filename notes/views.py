from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note

# Create your views here.
@login_required(login_url='/accounts/login')
def editor(request):
    print(request.GET)
    doc_id = request.GET.get('doc_id')
    notes = Note.objects.all().order_by('-updated_at')

    if request.method == 'POST':
        doc_id = request.POST.get('doc_id')
        title = request.POST.get('title')
        content = request.POST.get('content', '')

        if doc_id and doc_id != 'None':
            print('doc_id: |', doc_id, '|')
            print('bool: ', bool(doc_id and doc_id != 'None'))
            print('type: ', type(doc_id))
            note = Note.objects.get(pk=doc_id)
            note.title = title
            note.content = content
            note.save()

            return redirect(f'/?doc_id={doc_id}')
        else:
            note = Note.objects.create(title=title, content=content, owner=request.user.id)
            doc_id = note.id
    print(request.user.id)
    print(doc_id)
    if doc_id:
        note = Note.objects.get(pk=doc_id)
    else:
        note = ''

    context = {
        'doc_id': doc_id,
        'notes': notes,
        'note': note,
    }

    print('context: ', context)
    print('first note: ', notes[0].title)

    return render(request, 'home.html', context)

@login_required(login_url='/accounts/login')
def delete_note(request, doc_id):
    note = Note.objects.get(pk=doc_id)
    note.delete()

    return redirect('/')
