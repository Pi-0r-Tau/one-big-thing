from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from one_big_thing.learning import authentication_views, views, info_views

account_urlpatterns = [
    path("accounts/verify/", authentication_views.CustomVerifyUserEmail, name="verify-email"),
    path("accounts/password-reset/", authentication_views.PasswordReset, name="password-reset"),
    path("accounts/change-password/reset/", authentication_views.PasswordChange, name="password-set"),
    path("accounts/password-reset-done/", authentication_views.password_reset_done, name="password-reset-done"),
    path(
        "accounts/password-reset-from-key-done/",
        authentication_views.password_reset_from_key_done,
        name="password-reset-from-key-done",
    ),
    path("accounts/login/", authentication_views.CustomLoginView, name="account_login"),
    path("accounts/signup/", authentication_views.CustomSignupView.as_view(), name="account_signup"),
    path("accounts/verify/resend/", authentication_views.CustomResendVerificationView, name="resend-verify-email"),
    path("accounts/", include("allauth.urls")),
]

info_urlpatterns = [
    path("privacy-notice/", info_views.privacy_notice_view, name="privacy-notice"),
    path("accessibility-statement/", info_views.accessibility_statement_view, name="accessibility-statement"),
    path("support/", info_views.support_view, name="support"),
]

admin_urlpatterns = [path("admin/", admin.site.urls)]

other_urlpatterns = [
    path("", views.index_view, name="index"),
    path("home/", views.homepage_view, name="homepage"),
    path("record-learning/", views.RecordLearningView, name="record-learning"),
    path("record-learning/<uuid:course_id>/", views.RecordLearningView, name="record-learning"),
    path("questions/<str:survey_type>/", views.questions_view, name="questions"),
    path("questions/<str:survey_type>/<int:page_number>/", views.questions_view, name="questions"),
    path("complete-hours/", views.complete_hours_view, name="complete-hours"),
    path("send-learning-record/", views.send_learning_record_view, name="send-learning-record"),
    path("delete-learning-check/<uuid:learning_id>/", views.check_delete_learning_view, name="delete-learning-check"),
    path("additional-learning/", views.additional_learning_view, name="additional-learning"),
    path("intro-pre-survey/", views.intro_to_pre_survey_view, name="intro-pre-survey"),
    path("end-pre-survey/", views.end_pre_survey_view, name="end-pre-survey"),
    path("intro-post-survey/", views.intro_to_post_survey_view, name="intro-post-survey"),
    path("end-post-survey/", views.end_post_survey_view, name="end-post-survey"),
    path("department-links/", views.department_links_view, name="department-links"),
]

urlpatterns = account_urlpatterns + info_urlpatterns + other_urlpatterns

if settings.DEBUG:
    urlpatterns = urlpatterns + admin_urlpatterns
