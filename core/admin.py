from django.contrib import admin

from core.models import ActivityLog, Instituicoes

class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class InstituicaoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'user')

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Instituicoes, InstituicaoAdmin)
