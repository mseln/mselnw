from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# from markdownx.admin import MarkdownxModelAdmin

from .models import StaticPage

class StaticPageAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'

# admin.site.register(StaticPage, MarkdownxModelAdmin)
admin.site.register(StaticPage, StaticPageAdmin)
