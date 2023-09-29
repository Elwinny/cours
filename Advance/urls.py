from django.contrib import admin
from django.urls import include, path
from core.urls import urlpatterns as core_urls
from django.conf import settings
from user.urls import urlpatterns as user_urls
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic import TemplateView
from core.api.urls import urlpatterns as api_urls  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social_django.urls', namespace='social')),
path('i18n/', include('django.conf.urls.i18n')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(api_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('', include(core_urls)),
    path('user/', include(user_urls)),  # Removed double quotes around 'user/'
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        path('rosetta/', include('rosetta.urls'))
    ]

# Add media URL
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





# from django.contrib import admin
# from django.urls import include , path
# from core.urls import urlpatterns as core_urls
# from django.conf import settings
# from user.urls import urlpatterns as user_urls
# from django.conf.urls.static import static
# from django.conf.urls.i18n import i18n_patterns
# from django.views.generic import TemplateView
# from django api.urls import urlpatterns as api_urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('social_django.urls', namespace='social')),
#     path('i18n/', include('django.conf.urls.i18n')),
#     path('api-auth/', include('rest_framework.urls')),
#     path('api/', include(api_urls)),
# ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += i18n_patterns(
#     path('', include(core_urls)),
#     path("user/", include(user_urls)),

# )

# if 'rosetta' in settings.INSTALLED_APPS:
#     urlpatterns += [
#         path(r'rosetta/', include('rosetta.urls'))
        
#     ]

# # # add media url  

# # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)