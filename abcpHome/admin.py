# abcpHome/admin.py
from django.contrib import admin
from .models import TechDot, PageContent

# Register the TechDot model
admin.site.register(TechDot)

# Register the PageContent model
admin.site.register(PageContent)
