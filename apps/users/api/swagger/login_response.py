from drf_yasg import openapi

from rest_framework import status

login_responses = {
    status.HTTP_200_OK: openapi.Response(
        description="Success",
        examples={
            "application/json": {
                "data": "Success login",
                "error": None,
            }
        },
    ),
    status.HTTP_422_UNPROCESSABLE_ENTITY: openapi.Response(
        description="Error",
        schema=openapi.Schema(
            properties={
                "data": openapi.Schema(type=openapi.TYPE_STRING, enum=[None]),
                "error": openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=[
                        "Invalid credentials",
                        "User is not active",
                    ],
                ),
            },
            type=openapi.TYPE_OBJECT,
            title="Error response schema",
        ),
    ),
}