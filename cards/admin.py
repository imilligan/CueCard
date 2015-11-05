from django.contrib import admin
from cards.models import Poll, Choice, Source, Author, Card

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    list_display = ('question', 'pub_date')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
admin.site.register(Author)
admin.site.register(Source)
admin.site.register(Card)
# Register your models here.
