from django.contrib import admin
from .models import Produto

# Register your models here.
@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque', 'slug', 'created_at', 'updated_at', 'status')
    list_filter = ('status', 'created_at', 'updated_at')