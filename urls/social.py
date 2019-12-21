from django.conf.urls import url
from authlib import views
from authlib.facebook import FacebookOAuth2Client
from authlib.google import GoogleOAuth2Client
from authlib.twitter import TwitterOAuthClient

urlpatterns = [
    url(
        r"^oauth/facebook/$",
        views.oauth2,
        {
            "client_class": FacebookOAuth2Client,
        },
        name="accounts_oauth_facebook",
    ),
    url(
        r"^oauth/google/$",
        views.oauth2,
        {
            "client_class": GoogleOAuth2Client,
        },
        name="accounts_oauth_google",
    ),
    url(
        r"^oauth/twitter/$",
        views.oauth2,
        {
            "client_class": TwitterOAuthClient,
        },
        name="accounts_oauth_twitter",
    )
]
