from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("forum/profil/", views.profil, name="profil"),
    path("forum/", views.forum_cat, name="forum"),
    path("forum-all/", views.forum, name="forum-all"),
    path("forum/search", views.search, name="search"),
    path("forum/resend", views.resend, name="resend"),
    path("forum/unggahan/<slug>", views.unggahan, name="unggahan"),
    path("forum/unggah-artikel/", views.unggah_artikel, name="unggah-artikel"),
    path("forum/konten-artikel/", views.konten_artikel, name="konten-artikel"),
    path("forum/tambah-pengumuman/", views.konten_pengumuman, name="tambah-pengumuman"),
    path("forum/daftar-user/", views.daftar_user, name="daftar-user"),
    path("forum/requested-article/", views.requested_article, name="requested-article"),
    path("forum/export-entri/", views.export_entri, name="export-entri"),
    path(
        "forum/permintaan-verifikator/",
        views.permintaan_verifikator,
        name="permintaan-verifikator",
    ),
    path(
        "forum/verifikasi-terjemahan/",
        views.verifikasi_terjemahan,
        name="verifikasi-terjemahan",
    ),
    path("forum/daftar-kata/", views.daftar_kata, name="daftar-kata"),
    path(
        "forum/lihat-profil/user/<slug>",
        views.lihat_profil_user,
        name="lihat-profil-user",
    ),
    path(
        "forum/lihat-profil/verifikator/<slug>",
        views.lihat_profil_verifikator,
        name="lihat-profil-verifikator",
    ),
    path("forum/password_reset", views.password_reset_request, name="password_reset"),
    path("forum/kategori/<slug>", views.kategori, name="kategori"),
    path("forum/new-ver/<slug>", views.new_ver, name="new-ver")
    # path('posts/',posts, name=posts),
]
