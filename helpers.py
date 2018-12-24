from django.views.generic import View
from django.shortcuts import *
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseBadRequest,HttpResponse


def get_page_data(paginator, page):
    page_list = []

    # ==============分页逻辑===============
    # 条件：页数>=10
    # 当前页<=5时，起始页为1
    # 当前页>(总页数-5)时，起始页为(总页数-9)
    # 其他情况 起始页为(当前页-5)
    # ====================================

    if paginator.num_pages > 10:
        if page.number <= 5:
            start_page = 1
        elif page.number > paginator.num_pages - 5:
            start_page = paginator.num_pages - 9
        else:
            start_page = page.number - 5

        for i in range(start_page, start_page + 10):
            page_list.append(i)
    else:
        for i in range(1, paginator.num_pages + 1):
            page_list.append(i)

    page_data = {'page_list': page_list}
    return page_data

def ajax_required(f):
    """Not a mixin, but a nice decorator to validate than a request is AJAX"""
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()

        return f(request, *args, **kwargs)

    wrap.__doc__ = f.__doc__
    wrap.__name__ = f.__name__
    return wrap


class AuthorRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)


class SuperUserRequiredMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('myadmin:login')

        return super().dispatch(request, *args, **kwargs)

