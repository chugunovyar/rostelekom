from django.contrib import admin
from .models import Incoming, Client


class ClientappealInline(admin.TabularInline):
    model = Incoming
    extra = 1


@admin.register(Incoming)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('created', 'description')
    list_filter = ('created',)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    search_fields = ('name', 'surname', 'phone')
    list_display = ('name', 'surname', 'phone')
    inlines = [ClientappealInline]
