from django.contrib import admin
from core.models import Usuario, Tarefa

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id','nome','email')

admin.site.register(Usuario,UsuarioAdmin)

class TarefaAdmin(admin.ModelAdmin):
    list_display = ('id','descricao','setor','usuario','prioridade','status')

admin.site.register(Tarefa,TarefaAdmin)