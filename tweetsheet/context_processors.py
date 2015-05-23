from social_auth.db.django_models import UserSocialAuth


def twitter_credentials(request):
    """
    Add to context the Twitter credentials for the authenticated user, if any.
    """
    context = {}
    if request.user.is_authenticated:
        try:
            user = UserSocialAuth.objects.get(user=request.user)
            tokens = user.extra_data.get('access_token')
            if tokens:
                context['token_secret'] = tokens.split('&')[0].split('=')[1]
                context['token'] = tokens.split('&')[1].split('=')[1]
        except UserSocialAuth.DoesNotExist:
            context['token_secret'] = ''
            context['token'] = ''
    return context