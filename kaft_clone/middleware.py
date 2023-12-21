def session_check(get_response):
    def middleware(request):
        if not request.session.session_key:
            request.session.save()

        print(f"SESSION_KEY: {request.session.session_key}")
        response = get_response(request)
        return response
    return middleware
