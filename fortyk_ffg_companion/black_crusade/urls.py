from django.urls import path

from .views import (
    index_page,
    bc_weapon_detail,
    bc_weapon_update
)

app_name = "bc"
urlpatterns = [
    path("weapon/<int:pk>/update/", view=bc_weapon_update, name="weapon-update"),
    path("weapon/<int:pk>/", view=bc_weapon_detail, name="weapon-detail"),
    path("", view=index_page, name="index"),
]
