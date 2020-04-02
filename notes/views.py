from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from .models import Notes
from .forms import NoteForm
from django.urls import reverse


# Create[ your views here.
def all_notes(request):
    all_notes = Notes.objects.all()
    context={
        'all_notes':all_notes
    }
    return render(request,'all_notes.html',context)


def details(request, slug):
    note = Notes.objects.get(slug=slug)
    context={
        "note":note
    }
    return render(request,"note_detail.html",context)


def add_note(request):
    if request.method =="POST":
        form= NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
    else:
        form = NoteForm()
    context={
        'form':form
    }
    return render(request,'add.html',context)
    
"""def add_note(request, pk):
    Notes = get_object_or_404(Notes, pk=pk)
    if request.method == "POST":
        form =NoteForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = Notes
            new_form.save()
            return redirect("single_post_view", pk=Notes.pk)
    else:
        form =NoteForm()
    return render(request, "add.html", {"form": form})"""


"""def add_note(request,pk=3):
    form=NoteForm()
    new_form = get_object_or_404(Notes, pk=pk)

    # If this is a POST request then process the Form data
    if request.method == 'POST':

            # Create a form instance and populate it with data from the request (binding):
            form = NoteForm(request.POST)

            # Check if the form is valid:
            if form.is_valid():
                # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
                new_form.due_back = form.cleaned_data['renewal_date']
                new_form.save()

                # redirect to a new URL:
                return HttpResponseRedirect(reverse('notes_add'))

    context = {
            'form': form,
            "new_form":new_form
            }

    return render(request, 'add.html', context)"""
