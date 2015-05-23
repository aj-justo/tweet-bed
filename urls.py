from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from tweetsheet.views import TweetSheetView, TweetView, HomeView, TwitterStatusUpdate

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^sheets/$', TweetSheetView.as_view(), name='sheet_list'),
    url(r'^sheets/(?P<sheet_id>[0-9]+)/$', login_required(TweetView.as_view()), name='tweet_list'),
    url(r'^twitter-update-status/$', login_required(TwitterStatusUpdate.as_view()), name='twitter_update_status'),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('social_auth.urls')),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
