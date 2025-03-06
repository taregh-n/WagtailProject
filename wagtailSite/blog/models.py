from django import forms
from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel

class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + ["intro"]
    subpage_types = ['blog.BlogPage']

class BlogPage(Page):
    image = models.ImageField(upload_to="blog/%Y/%m/%d", blank=True)
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    author = ParentalManyToManyField('blog.Author', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(["date",
                        FieldPanel("author", widget=forms.CheckboxSelectMultiple)],
                        heading="Blog information"),
        "image", "intro", "body"]

    parent_page_types = ['blog.BlogIndexPage']

@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=500, blank=True)

    panels = ["name", "description"]
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
