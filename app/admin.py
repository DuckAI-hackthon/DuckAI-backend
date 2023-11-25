from django.contrib import admin
from uploader.models import Image

from app.models import Ai, Favorite, Function, Historic, Chat, ChatHistory

admin.site.register(Ai)
admin.site.register(Favorite)
admin.site.register(Function)
admin.site.register(Historic)
admin.site.register(Chat)
admin.site.register(ChatHistory)

