from django.shortcuts import render,redirect
from core.models import Usuario,Tarefa
from django.contrib import messages

def index (request):
    return redirect('/gerenciamento/')

def usuario (request):
    id_usuario=request.GET.get('id')
    dados={}
    if id_usuario:
        dados['usuario'] = Usuario.objects.get(id=id_usuario)
    return render(request, 'usuario.html',dados)

def usuario_submit (request):
    if request.POST:
        id_usuario = request.POST.get('id_equipamento') 
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        if id_usuario:
            usuario = Usuario.objects.get(id = id_usuario)
            usuario.nome=nome
            usuario.email=email
            usuario.save()
            messages.success(request,"Usuário salvo com sucesso!")
        else:        
            Usuario.objects.create(nome=nome,
                              email=email)
            messages.success(request,"Usuário salvo com sucesso!")
    else:
        messages.success(request,"Erro ao cadastrar usuário!")
    return redirect('/usuario/')


def tarefa (request):
    id_tarefa=request.GET.get('id')
    usuarios=Usuario.objects.all()
    prioridades = dict(Tarefa.PRIORIDADE_CHOICES)
    dados={}
    if id_tarefa:
        dados['tarefa'] = Tarefa.objects.get(id=id_tarefa)
    dados['usuarios']=usuarios
    dados['prioridades']=prioridades
    return render(request, 'tarefa.html',dados)

def tarefa_submit (request):
    if request.POST:
        id_tarefa = request.POST.get('id_tarefa')
        descricao = request.POST.get('descricao')
        setor = request.POST.get('setor')
        id_usuario = request.POST.get('usuario')
        usuario = Usuario.objects.get(id = id_usuario)
        prioridade = request.POST.get('prioridade')
        status='a_fazer'
        if id_tarefa:
            tarefa = Tarefa.objects.get(id = id_tarefa)
            tarefa.descricao=descricao
            tarefa.setor=setor
            tarefa.usuario=usuario
            tarefa.prioridade=prioridade
            if tarefa.status=="":
                tarefa.status=status='a_fazer'
            tarefa.save()
            messages.success(request,"Tarefa salva com sucesso!")
        else:        
            Tarefa.objects.create(descricao=descricao,
                              setor=setor,
                              usuario=usuario,
                              prioridade=prioridade,
                              status=status)
            messages.success(request,"Tarefa salva com sucesso!")
    else:
        messages.success(request,"Erro ao cadastrar tarefa!")
    return redirect('/tarefa/')


def gerenciamento(request):
    tarefas = Tarefa.objects.all()
    
    tarefas_a_fazer = tarefas.filter(status='a_fazer')
    tarefas_fazendo = tarefas.filter(status='fazendo')
    tarefas_feito = tarefas.filter(status='pronto')
    
    prioridades = dict(Tarefa.PRIORIDADE_CHOICES)
    statusList = dict(Tarefa.STATUS_CHOICES)
    
    return render(request, 'gerenciamento.html', {
        'tarefas_a_fazer': tarefas_a_fazer,
        'tarefas_fazendo': tarefas_fazendo,
        'tarefas_feito': tarefas_feito,
        'prioridades': prioridades,
        'statusList':statusList,
    })

def mudar_status_tarefa(request, tarefa_id):
    if request.POST:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        status = request.POST.get('status')

        tarefa.status = status
        tarefa.save()
        messages.success(request, 'Status da tarefa atualizado com sucesso.')
    else:
        messages.error(request, 'Tarefa não encontrada.')
    
    return redirect('/gerenciamento/')  # Redireciona para a página de gerenciamento

def excluir_tarefa(request, tarefa_id):
    try:
        tarefa = Tarefa.objects.get(id=tarefa_id)
        tarefa.delete()
        messages.success(request, 'Tarefa excluída com sucesso.')
    except Tarefa.DoesNotExist:
        messages.error(request, 'Tarefa não encontrada.')
    
    return redirect('/gerenciamento/')  # Redireciona para a página de gerenciamento
