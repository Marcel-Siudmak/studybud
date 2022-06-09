from django.contrib import admin
from django.utils.html import format_html
from .models import Idea, Vote
# Register your models here.


class VoteInline(admin.StackedInline):
    model = Vote

@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id','title', 'status', 'showYouTubeURL']
    list_filter = ['status']
    inlines = [
        VoteInline
    ]

    def showYouTubeURL(self, obj):
        if obj.youtube is not None:
            return format_html(f'<a href="{obj.youtube}" target="blank">{obj.youtube}</a>')
        else:
            return ''

    showYouTubeURL.short_description = 'YouTube URL'


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']

