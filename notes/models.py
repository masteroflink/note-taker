import uuid
from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.IntegerField(null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    content = models.CharField(max_length=1_000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Metadata
    ordering = ['-updated_at']
