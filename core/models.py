from django.db import models
from stdimage import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify


# Create your models here.
class Base(models.Model):
    created_at = models.DateTimeField('Data de criação',auto_now_add=True)
    updated_at = models.DateTimeField('Data de alteração',auto_now=True)
    status = models.BooleanField('Ativo?',default=True)

    class Meta:
        abstract = True


class Produto(Base):
    nome = models.CharField('Nome',max_length=100)
    descricao = models.TextField('Descrição', blank=True, null=True)
    preco = models.DecimalField('Preço',max_digits=8,decimal_places=2)
    estoque = models.IntegerField('Quantidade em estoque')
    imagem = StdImageField('Imagem',upload_to='produtos',variations={'thumbnail':(124,124)})
    slug = models.SlugField('Slug',editable=False)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
    

def produto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(produto_pre_save,sender=Produto)