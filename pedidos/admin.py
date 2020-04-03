from django.contrib import admin
from django.utils import timezone

from .models import Pedido

# Register your models here.

class PedidoAdmin(admin.ModelAdmin):

    exclude = ['usuario', 'fecha']

    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.fecha = timezone.now()
        super(PedidoAdmin, self).save_model(request, obj, form, change)

admin.site.register(Pedido, PedidoAdmin)