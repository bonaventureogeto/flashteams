from django.contrib import admin
from .models import User, BlackList


admin.sit.register(User, BlackList)
