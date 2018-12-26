from django.db import models
from markdownx.models import MarkdownxField

from markdownx.utils import markdownify

class StaticPage(models.Model):
    title = models.CharField(max_length=50)
    url = models.SlugField(max_length=50)
    field = MarkdownxField(blank = True)

    @property
    def formatted_markdown(self):
        return markdownify(self.field).replace("src=\"markdownx","src=\"/media/markdownx")

    def __str__(self):
        return self.title
