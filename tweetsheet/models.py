from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class TweetSheet(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    creation_date = models.DateTimeField(default=timezone.now)
    action_date = models.DateTimeField(default=timezone.now, null=True, blank=True)
    hash_tags = models.CharField(max_length=140, null=True, blank=True,
                                help_text="Tags to be included in all tweets included in the sheet. "
                                          "Note that the length of the text of every tweet has to allow "
                                          "for this to be included or it won't fit.")
    creator = models.ForeignKey(User)
    header_image = models.ImageField(null=True, blank=True)

    def get_date(self):
        d = self.action_date or self.creation_date
        return d.date().strftime("%d %b %Y")

    def __unicode__(self):
        u = self.get_date()
        if self.title:
            u = "%s (%s)" % (self.title, u)
        return u

    @classmethod
    def latest_sheet(cls):
        try:
            return cls.objects.all().order_by('-creation_date')[0]
        except IndexError:
            return None


class Tweet(models.Model):
    text = models.CharField(max_length=140)
    tweet_sheet = models.ForeignKey(TweetSheet, related_name="tweets")

    def __unicode__(self):
        return self.text

    def render_button(self):
        html = '<a href="%s" class="btn btn-primary">Tweet</a>' % self.get_link
        return html

    def get_link(self):
        return "#"

    def get_number(self):
        tweets = self.tweet_sheet.tweets.all().order_by('pk').values_list('pk', flat=True )
        number = list(tweets).index(self.pk) + 1  # we start at 1
        return number


