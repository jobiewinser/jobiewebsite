from django.contrib import admin, auth
from core.models import Technology, TechnologyType, Language

class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type']
admin.site.register(Technology, TechnologyAdmin)

class TechnologyTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']

class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Language, LanguageAdmin)