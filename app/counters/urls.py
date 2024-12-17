from django.urls import path

from . import views

app_name = "counters"

urlpatterns = [
    path("increment/<str:name>/", views.increment_counter, name="increment_counter"),
    path(
        "increment_atomic/<str:name>/",
        views.increment_counter_atomic,
        name="increment_counter_atomic",
    ),
    path(
        "increment_lock/<str:name>/",
        views.increment_counter_lock,
        name="increment_counter_lock",
    ),
]
