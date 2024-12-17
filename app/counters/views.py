import time

from django.db import transaction
from django.db.models import F
from django.http import JsonResponse

from .models import Counter


@transaction.atomic
def increment_counter(request, name):
    # Retrieve the counter object
    # (ignore DoesntExist exception for simplification)
    counter = Counter.objects.get(name=name)

    # Simulate a slow API endpoint
    time.sleep(5)

    # Increment and save
    counter.value += 1
    counter.save()

    # return the current state of the counter, as JSON
    return JsonResponse({"name": name, "value": counter.value})


def increment_counter_atomic(request, name):
    """Increment the counter using an atomic update"""
    with transaction.atomic():
        # Atomically increment the counter
        Counter.objects.filter(name=name).update(value=F("value") + 1)
        counter = Counter.objects.get(name=name)

    return JsonResponse({"name": name, "value": counter.value})


def increment_counter_lock(request, name):
    """Increment the counter using `select_for_update`."""
    with transaction.atomic():
        counter = Counter.objects.filter(name=name).select_for_update().get()

        # Simulate a slow API endpoint
        time.sleep(5)

        # Increment and save
        counter.value += 1
        counter.save()

    return JsonResponse({"name": name, "value": counter.value})
