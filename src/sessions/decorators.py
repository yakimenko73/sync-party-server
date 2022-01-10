def handle_unsaved_session(func):
    def inner_function(*args, **kwargs):
        request = args[1]
        if not request.session.session_key:
            request.session.save()

        return func(*args, **kwargs)

    return inner_function
