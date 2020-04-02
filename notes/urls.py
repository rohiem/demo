from django.urls import re_path, path
from . import views
app_name = "notes"
urlpatterns = [
    re_path(r'^$', views.all_notes , name='all_notes'),
    re_path(r'^(?P<slug>[-\w]+)$',views.details, name='notes_detail'),
    #path('<slug:slug>',views.details, name='notes_detail'),
    #re_path(r'^add$', views.add_note, name='note_add'),
    path('add/', views.add_note, name="Notes_add"),

]
