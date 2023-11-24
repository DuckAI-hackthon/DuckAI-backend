from django.contrib import admin

from app.models import Ai, Favorite, Function, Historic

admin.site.register(Ai)
admin.site.register(Favorite)
admin.site.register(Function)
admin.site.register(Historic)
