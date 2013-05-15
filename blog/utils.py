def context_proc(request):
    from django.conf import settings
    return {'settings': settings }