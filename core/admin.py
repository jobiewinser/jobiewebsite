from django.contrib import admin, auth
from core.models import Technology, TechnologyType, Language

class TechnologyAdmin(admin.ModelAdmin):
    search_fields = ['name', 'type']
admin.site.register(Technology, TechnologyAdmin)

class TechnologyTypeAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(TechnologyType, TechnologyTypeAdmin)

class LanguageAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Language, LanguageAdmin)




from django.apps import apps
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model) #Register all models that aren't already registered
    except:
        pass #If the model is already registed, don't bother