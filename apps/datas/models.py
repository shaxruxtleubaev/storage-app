from django.db.models import *

class URLs(Model):

    url = URLField(
        verbose_name='URL', 
        max_length=100000
    )
    description = TextField(
        verbose_name='Description to URL'
    )
    date = DateField(
        verbose_name='Date added',
        auto_now=True
    )

    def __str__(self):
        return f'{self.url}'

    class Meta:
        verbose_name = 'url'
        verbose_name_plural = 'urls'

class Files(Model):

    file = FileField(
        verbose_name='File', 
        upload_to='files'
    )
    description = TextField(
        verbose_name='Description to file'
    )
    date = DateField(
        verbose_name='Date added',
        auto_now=True
    )

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'file'
        verbose_name_plural = 'files'

class Text(Model):

    text = TextField(
        verbose_name='Text'
    )
    description = TextField(
        verbose_name='Description to text'
    )
    date = DateField(
        verbose_name='Date added',
        auto_now=True
    )

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'text'
        verbose_name_plural = 'texts'

class Image(Model):

    image = ImageField(
        verbose_name='Image', 
        upload_to='images'
    )
    description = TextField(
        verbose_name='Description to image'
    )
    date = DateField(
        verbose_name='Date added',
        auto_now=True
    )

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'image'
        verbose_name_plural = 'images'

class Video(Model):

    video = FileField(
        verbose_name='Video', 
        upload_to='videos'
    )
    description = TextField(
        verbose_name='Description to video'
    )
    date = DateField(
        verbose_name='Date added',
        auto_now=True
    )

    def __str__(self):
        return f'{self.description}'

    class Meta:
        verbose_name = 'video'
        verbose_name_plural = 'videos'
