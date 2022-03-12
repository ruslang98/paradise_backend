from drf_yasg import openapi

label_manual_parameters = [
    openapi.Parameter(
        name="categories",
        in_=openapi.IN_QUERY,
        type=openapi.TYPE_STRING,
        description="categories",
        required=False,
    )
]
