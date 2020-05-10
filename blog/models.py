from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.html import strip_tags
import markdown
# Create your models here.
#文章分类
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#标签
class Tag(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


#文章
class Post(models.Model):
    # 文章标题
    title = models.CharField('标题',max_length=70)
    # 文章正文
    body = models.TextField()
    #文章创建、修改时间
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    modified_time = models.DateTimeField('修改时间')

    def save(self, *args, **kwargs):
        self.modified_time = timezone.now()

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
        ])
        self.excerpt = strip_tags(md.convert(self.body))[:54]
        super().save(*args, **kwargs)

    # 文章摘要，blank可以为空
    excerpt = models.CharField(max_length=200, blank=True)

    #分类与标签作为外键
    category = models.ForeignKey(Category, verbose_name='分类',on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name='标签',blank=True)

    # 文章作者，User从 django.contrib.auth.models 导入
    author = models.ForeignKey(User , verbose_name='作者',on_delete=models.CASCADE)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

