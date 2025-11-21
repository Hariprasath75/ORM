from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from .models import amazon_DB,amazon_DBAdmin
admin.site.register(amazon_DB,amazon_DBAdmin)