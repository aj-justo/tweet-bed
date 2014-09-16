from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic import ListView, View
from tweetsheet.models import Tweet, TweetSheet


class HomeView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('sheet_list'))


class TweetView(ListView):
    model = Tweet
    template_name = 'tweet_list.html'


class TweetSheetView(ListView):
    model = TweetSheet
    template_name = 'tweet_sheet_list.html'