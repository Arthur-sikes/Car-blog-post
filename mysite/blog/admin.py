from django.contrib import admin
from .models import Post,PostSeries,PostCategory
from tinymce.widgets import TinyMCE
from django.db import models

class PostAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["title", "published_date"]}),
        ("URL", {'fields': ["post_slug"]}),
        ("Series", {'fields': ["post_series"]}),
        ("Content", {"fields": ["author","text"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
        }
admin.site.register(PostSeries)
admin.site.register(PostCategory)
admin.site.register(Post,PostAdmin)
# Register your models here.
