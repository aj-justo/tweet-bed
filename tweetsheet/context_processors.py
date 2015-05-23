from django.conf import settings
from social_auth.db.django_models import UserSocialAuth


def twitter_credentials(request):
    """
    Add to context the Twitter credentials for the authenticated user, if any.
    """
    context = {
        'twitter_consumer_key': settings.TWITTER_CONSUMER_KEY,
        'twitter_consumer_secret': settings.TWITTER_CONSUMER_SECRET
    }
    if request.user.is_authenticated:
        try:
            user = UserSocialAuth.objects.get(user=request.user)
            tokens = user.extra_data.get('access_token')
            if tokens:
                context['twitter_token_secret'] = tokens.split('&')[0].split('=')[1]
                context['twitter_token'] = tokens.split('&')[1].split('=')[1]
        except UserSocialAuth.DoesNotExist:
            context['twitter_token_secret'] = ''
            context['twitter_token'] = ''
    return context