from django.conf.urls import url
from authlib import views
from django.conf import settings

urlpatterns = []

if getattr(settings, 'GOOGLE_CLIENT_ID', '') and getattr(settings, 'GOOGLE_CLIENT_SECRET', ''):
    from authlib.google import GoogleOAuth2Client
    urlpatterns += url(
        r"^oauth/google/$",
        views.oauth2,
        {
            "client_class": GoogleOAuth2Client,
        },
        name="accounts_oauth_google",
    ),

if getattr(settings, 'FACEBOOK_CLIENT_ID', '') and getattr(settings, 'FACEBOOK_CLIENT_SECRET', ''):
    from authlib.facebook import FacebookOAuth2Client
    urlpatterns += url(
        r"^oauth/facebook/$",
        views.oauth2,
        {
            "client_class": FacebookOAuth2Client,
        },
        name="accounts_oauth_facebook",
    ),

if getattr(settings, 'TWITTER_CLIENT_ID', '') and getattr(settings, 'TWITTER_CLIENT_SECRET', ''):
    from authlib.twitter import TwitterOAuthClient
    urlpatterns += url(
        r"^oauth/twitter/$",
        views.oauth2,
        {
            "client_class": TwitterOAuthClient,
        },
        name="accounts_oauth_twitter",
    )
