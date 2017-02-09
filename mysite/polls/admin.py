from django.contrib import admin
from polls.models import Poll, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']
    inlines = [ChoiceInline]
    list_display = ['question', 'pub_date']
    search_fields = ['question']


admin.site.register(Poll, PollAdmin)
