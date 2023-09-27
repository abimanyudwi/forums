from django.contrib import admin
from .models import (
    Category,
    Author,
    Post,
    Translasi,
    Verifikator,
    Penilaian,
    Instrumen,
    Manado,
    Administrator,
    Perbandingan,
    Kandidat,
    Poll,
    PollResult,
    ArticleRequest,
    BeVerificator,
    TranslationNote,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Translasi)
admin.site.register(Manado)
admin.site.register(Verifikator)
admin.site.register(Penilaian)
admin.site.register(Instrumen)
admin.site.register(Administrator)
admin.site.register(Perbandingan)
admin.site.register(Kandidat)
admin.site.register(Poll)
admin.site.register(PollResult)
admin.site.register(ArticleRequest)
admin.site.register(BeVerificator)
admin.site.register(TranslationNote)
