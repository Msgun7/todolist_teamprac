from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from coplate.views import CustomPasswordChangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    # coplate
    path('', include('coplate.urls')),
    # allauth
    path(
        'email-confirmation-done/',
        TemplateView.as_view(template_name='coplate/email_confirmation_done.html'),
        name='account_email_confirmation_done'
    ),
    path(
        'password/change/',
        CustomPasswordChangeView.as_view(),
        name='account_change_password'
    ),
    path('account/', include('allauth.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
