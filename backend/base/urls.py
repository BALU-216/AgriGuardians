from django.urls import path, include
from . import views
from . import api_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns=[
             path('api/signup/', api_views.api_signup, name='api_signup'),
             path('api/login/', api_views.api_login, name='api_login'),
             path('api/me/', api_views.api_me, name='api_me'),
             path('api/predict/', api_views.api_predict, name='api_predict'),
             path('api/history/', api_views.api_history, name='api_history'),
             path('signup/', views.signup, name='signup'),
             path('login/', views.loginPage, name='login'),
             path('logout/',views.logoutUser, name='logout'),
             path("predict/", views.predict_view, name="predict"),
             path("profile/edit/", views.edit_profile, name="edit_profile"),
             path("history/", views.prediction_history, name="history"),
             path("generate-report/", views.generate_report, name="generate_report"),
            ]



urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



