from audioop import reverse
from email.policy import default
from enum import auto
from unicodedata import category
from xmlrpc.client import Boolean
from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager
from django.shortcuts import reverse
from .utils import kalimat_mdo
import datetime
from tinymce import models as tinymce_models
import random

# from django.utils.timezone import now


User = get_user_model()
# Verifikator = get_user_model()


# # Create your models here.
class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, blank=True)
    slug = slug = models.SlugField(
        max_length=250,
        unique=True,
        blank=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    points = models.FloatField(default=0)
    anonym = models.BooleanField(default=False)
    profile_pic = ResizedImageField(
        size=[60, 60],
        quality=200,
        upload_to="authors",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random.randint(1000000000, 9999999999) - random.randint(
                10000, 99999
            )

        super(Author, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("lihat-profil-user", kwargs={"slug": self.slug})


class Administrator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, blank=True)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    profile_pic = ResizedImageField(
        size=[100, 100],
        quality=200,
        upload_to="administrator",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random.randint(1000000000, 9999999999)
        super(Administrator, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("lihat-profil-admin", kwargs={"slug": self.slug})


class Verifikator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, blank=True)
    tipe = models.CharField(max_length=400, default="Individu")
    field = models.CharField(max_length=400, default="Linguistik")
    job_role = models.CharField(max_length=400, default="Null")
    contact = models.CharField(max_length=400, default="62123412341234")
    address = models.CharField(max_length=400, default="Sulawesi Utara")
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    profile_pic = ResizedImageField(
        size=[100, 100],
        quality=200,
        upload_to="verifikator",
        default=None,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = random.randint(1000000000, 9999999999)
        super(Verifikator, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("lihat-profil-verifikator", kwargs={"slug": self.slug})


class Category(models.Model):
    title = models.CharField(max_length=50)
    urutan = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    @property
    def num_posts(self):
        return Post.objects.filter(kategori=self).count()

    @property
    def last_post(self):
        return Post.objects.filter(kategori=self).latest("created")

    def get_url(self):
        return reverse("unggahan", kwargs={"slug": self.slug})

    def get_cat(self):
        return reverse("kategori", kwargs={"slug": self.slug})


class Manado(models.Model):
    kata = models.CharField(max_length=50)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "manado"

    def __str__(self):
        return self.kata

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.kata)
        super(Manado, self).save(*args, **kwargs)


class Penilaian(models.Model):
    title = models.CharField(max_length=50)
    bobot = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "penilaian"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Penilaian, self).save(*args, **kwargs)


class Instrumen(models.Model):
    title = HTMLField()
    penilaian = models.ManyToManyField(Penilaian)
    nilai = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "instrumen"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)[:100]
        super(Instrumen, self).save(*args, **kwargs)


class Translasi(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE, default="")
    # title = models.CharField(max_length=100)
    content = HTMLField()
    poin = models.FloatField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    best = models.BooleanField(default=False)
    penilai = models.ForeignKey(
        Verifikator, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.content[:10]

    class Meta:
        verbose_name_plural = "translasi"


# class Point(models.Model):
#     author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True,default='')
#     penilai = models.ForeignKey(Verifikator, on_delete=models.CASCADE, blank=True,default='')
#     # post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True,default='')
#     points = models.OneToOneField(Translasi, on_delete=models.CASCADE, blank=True, null=True)
#     date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.points)


class Post(models.Model, HitCountMixin):
    judul = models.CharField(max_length=400)
    portal = models.CharField(max_length=400, default="Unknown")
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    user = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    url = models.URLField(max_length=400, blank=True)
    tipe = models.CharField(max_length=400, default="Artikel")
    dinilai = models.BooleanField(default=False)
    konten = models.TextField()
    kategori = models.ForeignKey(Category, on_delete=models.CASCADE, default="8")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    status = models.BooleanField(default=True)
    hit_count_generic = GenericRelation(
        HitCount,
        object_id_field="object_pk",
        related_query_name="hit_count_generic_relation",
    )
    # tags = TaggableManager()
    translasi = models.ManyToManyField(Translasi, blank=True)
    # translasi

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.judul

    def get_url(self):
        return reverse("unggahan", kwargs={"slug": self.slug})

    def get_url_title(self):
        return reverse("unggahan", kwargs={"slug": self.judul})

    @property
    def num_translasi(self):
        return self.translasi.count()

    @property
    def last_trans(self):
        return self.translasi.latest("created")

    @property
    def last_post(self):
        return self.post.latest("created")


class TranslationNote(models.Model):
    user = models.ForeignKey(Verifikator, on_delete=models.CASCADE, default="")
    content = tinymce_models.HTMLField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.content[:10]

    class Meta:
        verbose_name_plural = "translation note"


class Perbandingan(models.Model):
    kalimat_ind = models.TextField()
    kalimat_mdo = models.TextField()
    # post = models.ManyToManyField(Post)
    slug = models.SlugField(max_length=250, unique=True, blank=True)

    class Meta:
        verbose_name_plural = "perbandingan"

    def __str__(self):
        return self.kalimat_mdo

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.kalimat_mdo)[:100]
        super(Perbandingan, self).save(*args, **kwargs)

    @property
    def num_sentence(self):
        return self.translasi.content.count()


class PollResult(models.Model):
    identifier = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    polls = models.CharField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier


class Kandidat(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)
    result = models.ManyToManyField(PollResult, blank=True)

    class Meta:
        verbose_name_plural = "kandidat"

    def __str__(self):
        return self.slug

    def get_url(self):
        return reverse("lihat-profil-user", kwargs={"slug": self.slug})

    def num_polls(self):
        return self.result.count()


class Poll(models.Model):
    creator = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    nama_polling = models.CharField(max_length=400)
    poll_ke = models.IntegerField(blank=True, default=0, unique=True)
    slug = slug = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    kandidat = models.ManyToManyField(Kandidat, blank=True)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama_polling)
        super(Poll, self).save(*args, **kwargs)

    def older_than_one_week(self):
        return (datetime.datetime.today() - self.created).days > 7

    def time_left(self):
        start = (datetime.datetime.today() - self.created).days
        time_left = 7 - start
        return time_left

    @property
    def num_kandidat(self):
        return self.kandidat.count()


class ArticleRequest(models.Model):
    identifier = models.SlugField(max_length=250, unique=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    url_berita = models.CharField(max_length=400)
    status = models.CharField(max_length=400, default="Diproses")
    user = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.identifier


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return "%s/%s" % (instance.user, filename)


class BeVerificator(models.Model):
    nama_lengkap = models.CharField(max_length=400)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    email = models.CharField(max_length=400)
    tipe = models.CharField(max_length=400)
    field = models.CharField(max_length=400)
    job_role = models.CharField(max_length=400, default="Null")
    contact = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    proof = models.FileField(upload_to=user_directory_path)
    status = models.CharField(max_length=400, default="Diproses")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name_plural = "BeVerificator"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nama_lengkap)
        super(BeVerificator, self).save(*args, **kwargs)

    def __str__(self):
        return self.nama_lengkap

    def __repr__(self):
        return "BeVerificator(%s, %s)" % (self.name, self.file)

    def get_url(self):
        return reverse("lihat-profil-user", kwargs={"slug": self.user})

    def get_new(self):
        return reverse("new-ver", kwargs={"slug": self.slug})

    # def get_url(self):
    #     return reverse("detail-berkas", kwargs={"slug": self.slug})
