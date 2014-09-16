from django.contrib import admin
from django.forms import ModelForm, fields, widgets
from tweetsheet.models import TweetSheet, Tweet


class TweetAdminForm(ModelForm):
    text = fields.CharField(widget=widgets.Textarea(attrs={'style': 'width:450px'}))


class TweetAdmin(admin.ModelAdmin):
    form = TweetAdminForm


admin.site.register(TweetSheet)
admin.site.register(Tweet, TweetAdmin)
