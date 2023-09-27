from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Translator, Verifikator
from main.models import Verifikator as Verif
from django import forms
from main.models import Author, Administrator, BeVerificator
from django.contrib.admin.decorators import display
from django.template.loader import get_template


class NewUserForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Surel",
            }
        ),
    )
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Pengguna",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Kata Sandi",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Konfirmasi Kata Sandi",
            }
        ),
    )

    class Meta:
        model = Translator
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class NewVerifikatorForm(forms.ModelForm):
    nama_lengkap = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Lengkap",
            }
        ),
    )
    field = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Bidang Pekerjaan",
            }
        ),
    )
    job_role = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Posisi/Jabatan",
            }
        ),
    )
    contact = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Kontak/No Hp",
            }
        ),
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Alamat",
            }
        ),
    )
    proof = forms.FileField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto", "style": "text-align:center;"}
        ),
    )

    class Meta:
        model = BeVerificator
        fields = ("nama_lengkap", "field", "job_role", "contact", "address", "proof")

    def save(self, commit=True):
        nama_lengkap = super(NewVerifikatorForm, self).save(commit=False)
        if commit:
            nama_lengkap.save()
        return nama_lengkap


class AddVerifikatorForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Pengguna",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Surel",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Kata Sandi",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Konfirmasi Kata Sandi",
            }
        ),
    )

    class Meta:
        model = Verifikator
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(AddVerifikatorForm, self).save(commit=False)
        # user.email = self.instance.email
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Pengguna",
            }
        ),
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Kata Sandi",
            }
        ),
    )

    class Meta:
        # model = Verifikator
        fields = ("username", "password")


class UpdateAuthorForm(forms.ModelForm):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Lengkap",
            }
        ),
    )
    profile_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto", "style": "text-align:center;"}
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Author
        fields = ("fullname", "profile_pic")


class UpdateVerifForm(forms.ModelForm):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Lengkap",
            }
        ),
    )
    profile_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto", "style": "text-align:center;"}
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Verif
        fields = ("fullname", "profile_pic")


class UpdateAdminForm(forms.ModelForm):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto",
                "style": "text-align:center;",
                "placeholder": "Nama Lengkap",
            }
        ),
    )
    profile_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto", "style": "text-align:center;"}
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Administrator
        fields = ("fullname", "profile_pic")


class AcceptVerifikatorForm(UserCreationForm):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Nama Pengguna",
                "readonly": "readonly",
            }
        ),
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Surel",
                "readonly": "readonly",
            }
        ),
    )
    password1 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Kata Sandi",
            }
        ),
    )
    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Konfirmasi Kata Sandi",
            }
        ),
    )

    class Meta:
        model = Verifikator
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(AcceptVerifikatorForm, self).save(commit=False)
        # user.email = self.instance.email
        if commit:
            user.save()
        return user


class UpdateNewVerifForm(forms.ModelForm):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Nama Lengkap",
            }
        ),
    )
    tipe = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Tipe",
            }
        ),
    )
    field = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Bidang",
            }
        ),
    )
    job_role = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Posisi/Jabatan",
            }
        ),
    )
    contact = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Kontak",
            }
        ),
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Alamat",
            }
        ),
    )
    profile_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto mb-2", "style": "text-align:center;"}
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Verif
        fields = (
            "fullname",
            "profile_pic",
            "tipe",
            "field",
            "job_role",
            "contact",
            "address",
        )


class UpdateIndVerifForm(forms.ModelForm):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Nama Lengkap",
            }
        ),
    )
    # tipe = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control mx-auto mb-2",
    #             "style": "text-align:center;",
    #             "placeholder": "Tipe",
    #         }
    #     ),
    # )
    field = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Bidang",
            }
        ),
    )
    job_role = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Posisi/Jabatan",
            }
        ),
    )
    contact = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Kontak",
            }
        ),
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Alamat",
            }
        ),
    )
    profile_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto mb-2", "style": "text-align:center;"}
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Verif
        fields = (
            "fullname",
            "profile_pic",
            # "tipe",
            "field",
            "job_role",
            "contact",
            "address",
        )


class UpdateOrgVerifForm(forms.ModelForm):
    fullname = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Nama Organisasi",
            }
        ),
    )
    # tipe = forms.CharField(
    #     required=True,
    #     widget=forms.TextInput(
    #         attrs={
    #             "class": "form-control mx-auto mb-2",
    #             "style": "text-align:center;",
    #             "placeholder": "Tipe",
    #         }
    #     ),
    # )
    field = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Bidang",
            }
        ),
    )
    contact = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Kontak",
            }
        ),
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control mx-auto mb-2",
                "style": "text-align:center;",
                "placeholder": "Alamat",
            }
        ),
    )
    profile_pic = forms.ImageField(
        required=True,
        widget=forms.FileInput(
            attrs={"class": "form-control mx-auto mb-2", "style": "text-align:center;"}
        ),
    )

    # if request.user.role ==

    class Meta:
        model = Verif
        fields = (
            "fullname",
            "profile_pic",
            # "tipe",
            "field",
            "contact",
            "address",
        )
