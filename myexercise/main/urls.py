from django.urls import path, include

from .views import ProfileView, UserRegisterView, EmailConfirmationSentView, EmailConfirmedView, \
    EmailConfirmationFailedView, UserConfirmEmailView

app_name = "main"

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("register/", UserRegisterView.as_view(), name="register"),
    path('email-confirmation-sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),
    path('confirm-email/<str:uidb64>/<str:token>/', UserConfirmEmailView.as_view(), name='confirm_email'),
    path('email-confirmed/', EmailConfirmedView.as_view(), name='email_confirmed'),
    path('confirm-email-failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'),
]