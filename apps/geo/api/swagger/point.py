from drf_yasg import openapi

point_manual_parameters = [
    openapi.Parameter(
        name="categories",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="categories",
        required=False,
    ),
    openapi.Parameter(
        name="labels",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="labels",
        required=False,
    ),
    openapi.Parameter(
        name="limit",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_INTEGER,
        description="limit",
        required=False,
    ),
]
