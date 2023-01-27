from user.models import AnonymousUser,Language

def auth(request):
    if hasattr(request, 'user'):
        user = request.user
    else:
        user = AnonymousUser()

    return {
        'user': user,
        'request':request,
        'language':request.LANGUAGE_CODE,
        'languages':Language.objects.exclude(code=request.LANGUAGE_CODE),
    }
