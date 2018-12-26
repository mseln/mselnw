from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import StaticPage
admin.site.register(StaticPage, MarkdownxModelAdmin)
