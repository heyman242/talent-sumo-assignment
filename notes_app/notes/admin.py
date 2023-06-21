from django.contrib import admin
from .models import RegisteredUser, Note


admin.site.register(RegisteredUser)

admin.site.register(Note)

# Register your models here.
