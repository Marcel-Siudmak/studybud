from django.contrib import admin
from .models import Idea, Votes
# Register your models here.

admin.site.register(Idea)
admin.site.register(Votes)
