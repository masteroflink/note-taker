from .views import editor, delete_note
from django.urls import path


urlpatterns = [
    path('', editor, name='editor'),
    path('delete_note/<uuid:doc_id>/', delete_note, name='delete_note')
]
