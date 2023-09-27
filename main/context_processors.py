from main.models import Post, Author, Verifikator, Administrator, Translasi
from users.models import User
from el_pagination.decorators import page_template
from django.core.paginator import Paginator


def searchFunction(request):
    search_context = {}

    page_obj = post = Post.objects.all()
    obj_url = ""
    query = ""
    pag_count = ""
    num_post = Post.objects.all().count()
    num_trans = Translasi.objects.all().count()
    num_user = User.objects.filter(role="USER").count()
    # print = request.GET.get()
    if "search" in request.GET:
        query = request.GET.get("q")
        search_opt = request.GET.get("search-box")
        if search_opt == "Judul":
            page_obj = post.filter(judul__icontains=query)
        else:
            page_obj = post.filter(konten__icontains=query)

        paginator = Paginator(page_obj, 5)

        page_number = request.GET.get("page")
        pag_count = len(page_obj)
        page_obj = paginator.get_page(page_number)
        obj_url = "search?q=" + query + "&search-box=" + search_opt + "&search="
    profile = "empty"
    try:
        user = request.user
        if user.role == "USER":
            profile = Author.objects.get(user_id=user.id)
        elif user.role == "VERIFIKATOR":
            profile = Verifikator.objects.get(user_id=user.id)
        else:
            profile = Administrator.objects.get(user_id=user.id)
    except:
        profile = "empty"

    search_context = {
        "page_obj": page_obj,
        "obj_url": obj_url,
        "query": query,
        "pag_count": pag_count,
        "profile": profile,
        "jlh_post": num_post,
        "jlh_trans": num_trans,
        "jlh_user": num_user,
    }

    return search_context
