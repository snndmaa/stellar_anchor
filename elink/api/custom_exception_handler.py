from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    print(context ,'\n' , exc)

    if response is not None and (response.status_code == 404 or response.status_code == 400):
        response.data = {
            "message": "new error test"
        }
    return response