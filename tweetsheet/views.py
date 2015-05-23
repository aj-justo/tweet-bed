import json
from django.conf import settings
from django.core.urlresolvers import reverse
from django.http.response import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponseServerError
from django.template import RequestContext
from django.views.generic import ListView, View
from social_auth.db.django_models import UserSocialAuth
import twitter
from tweetsheet.models import Tweet, TweetSheet
from context_processors import twitter_credentials


class HomeView(View):
    """Take users to the list of available tweet sheets (public page)"""
    def get(self, request):
        return HttpResponseRedirect(reverse('sheet_list'))


class TweetView(ListView):
    """Displays a list of Tweets belonging to a particular Tweet Sheet"""
    model = Tweet
    template_name = 'tweet_list.html'

    def render_to_response(self, context, **kwargs):
        return super(TweetView, self).render_to_response(
            RequestContext(self.request, context, processors=[twitter_credentials]), **kwargs)


class TweetSheetView(ListView):
    """Displays a list of available Tweet Sheets"""
    model = TweetSheet
    template_name = 'tweet_sheet_list.html'


class TwitterStatusUpdate(View):
    """Called via AJAX to update the status of the authenticated user (aka tweeting)"""

    def _get_twitter_user_credentials(self, request):
        """Return tuple with twitter credentials for the authenticated user, if any"""
        user = UserSocialAuth.objects.get(user=request.user)
        tokens = user.extra_data.get('access_token')
        secret = tokens.split('&')[0].split('=')[1]
        token = tokens.split('&')[1].split('=')[1]
        if tokens:
            return (secret, token)
        return tuple()

    def post(self, request, *args, **kwargs):
        credentials = self._get_twitter_user_credentials(request)
        api = twitter.Api(consumer_key=settings.TWITTER_CONSUMER_KEY,
                          consumer_secret=settings.TWITTER_CONSUMER_SECRET,
                          access_token_key=credentials[1],
                          access_token_secret=credentials[0])
        try:
            status = api.PostUpdate(request.POST.get('status'))
            return HttpResponse(status)
        except twitter.TwitterError, e:
            return HttpResponseBadRequest(e.message[0].get('message'))
        except Exception:
            return HttpResponseServerError()
