from django.contrib import admin
from .models import TeamMember, Product, ContactMessage

admin.site.register(TeamMember)
admin.site.register(Product)
admin.site.register(ContactMessage)
