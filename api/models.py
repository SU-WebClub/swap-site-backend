from django.db import models

class Category(models.Model):
    name = models.CharField('カテゴリー名', max_length=255)
    slug = models.SlugField('英語名', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField('イメージ画像', upload_to='category_thumbnail/', blank=True)

    class Meta:
        verbose_name = 'カテゴリー'
        verbose_name_plural = 'カテゴリーリスト'

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('タグ名', max_length=255)
    slug = models.SlugField('英語名', unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'タグ'
        verbose_name_plural = 'タグリスト'

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField('役職名', max_length=30)
    slug = models.SlugField('英語名', unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '役職'
        verbose_name_plural = '役職リスト'

    def __str__(self):
        return self.name

class Author(models.Model):
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    icon = models.ImageField('アイコン', help_text='正方形の画像にしてください', upload_to='author_icon/')
    name = models.CharField('ニックネーム', max_length=15)
    description = models.TextField('自己紹介', max_length=500)
    HomePage = models.CharField(max_length=100, blank=True)
    GitID = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = '記者'
        verbose_name_plural = '記者リスト'

    def __str__(self):
        return self.name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    thumbnail = models.ImageField('サムネ', upload_to='blog_thumbnail/')
    title = models.CharField('タイトル', max_length=75)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=False)
    description = models.CharField('headタグでの説明', max_length=255, blank=False)
    content = models.TextField('本文')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField('公開日', blank=False, null=True)
    is_public = models.BooleanField('公開する', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = '記事'
        verbose_name_plural = 'ブログ投稿'

    def save(self, *args, **kwargs):
        if self.is_public and not self.published_at:
            self.published_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class News(models.Model):
    thumbnail = models.ImageField('サムネ', upload_to='images/')
    title = models.CharField('タイトル', max_length=75)
    content = models.TextField('本文')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, blank=False)

    class Meta:
        verbose_name = 'ニュース'
        verbose_name_plural = 'ニュース投稿'

    def __str__(self):
        return self.title