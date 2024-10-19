from django.db import models

class Usuario(models.Model):
    nome = models.CharField (max_length=100)
    email = models.EmailField (max_length=100)
    
    def __str__(self) -> str:
        return self.nome

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
    ]

    STATUS_CHOICES = [
        ('a_fazer', 'A Fazer'),
        ('fazendo', 'Fazendo'),
        ('pronto', 'Pronto'),
    ]

    usuario = models.ForeignKey (Usuario, on_delete=models.CASCADE)
    descricao = models.CharField (max_length=100)
    setor = models.CharField (max_length=100)
    prioridade = models.CharField(
        max_length=10,
        choices=PRIORIDADE_CHOICES,
        default='media',
    )
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='a_fazer',
    )
    data_cadastro= models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.descricao