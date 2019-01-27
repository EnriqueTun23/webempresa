from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj=None):
        ''' Aqui se presenta la parte de validacion para que los usuarios no tengan acceso para modefiicar o si dependiendo si el 
        filtro que se ponga o  el grupo mejor dicho '''
        if request.user.groups.filter(name="Personal").exists():
            return('key', 'name')
        else:
            return('created', 'updated')

admin.site.register(Link, LinkAdmin)
