from drf_yasg import openapi

from rest_framework import status

registration_responses = {
    status.HTTP_200_OK: openapi.Response(
        description="Success registration",
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
                        "User with given phone number already exists",
                    ],
                ),
            },
            type=openapi.TYPE_OBJECT,
            title="Error response schema",
        ),
    ),
}