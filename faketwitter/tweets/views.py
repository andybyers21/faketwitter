import random
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

from .models import Tweet


def home_view(request, *args, **kwargs):
    """Set the homepage view"""
    # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "pages/home.html", context={}, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """View the requested tweet by id

    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    Return Json data.
    """
    data = {
        "id": tweet_id,
    }

    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
