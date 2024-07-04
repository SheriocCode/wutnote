from django.urls import path
from .views import login_view, protected_view,my_view
urlpatterns = [
   path('login/', login_view),
   path('protected_view/',protected_view),

   path('my/',my_view),
]