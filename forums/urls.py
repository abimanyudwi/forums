from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # import this

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("main.urls")),
    path("users/", include("users.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("unicorn/", include("django_unicorn.urls")),
    path("tinymce/", include("tinymce.urls")),
    path("hitcount/", include("hitcount.urls", namespace="hitcount")),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="user-auth/password/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="user-auth/password/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="user-auth/password/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
