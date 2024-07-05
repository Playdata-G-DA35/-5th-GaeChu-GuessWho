from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ["username", "name", "email"]
    add_fieldsets = (
        (
            "인증정보",
            {
                "fields":("username", "password1", "password2"),
            }
        ),
        (
            "개인정보",
            {
                "fields":("name", "email", "birthday")
            }
        )
    )
    fieldsets = (
        (
            "인증정보",
            {
                "fields":("username", "password"),
            }
        ),
        (
            "개인정보",
            {
                "fields":("name", "email", "birthday")
            }
        ),
        (
            "권한",
            {
                "fields":("is_active", "is_superuser")
            }
        )
    )

admin.site.register(User, CustomUserAdmin)