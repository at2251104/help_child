from pyexpat.errors import messages
from django.core.mail import message
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from accounts.models import *
from main.models import *
# Create your views h
from .models import *
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
import tkinter
from django.db import transaction


class IndexView(generic.TemplateView):
    template_name = "index.html"


class HomeView(LoginRequiredMixin, generic.TemplateView):
    model = T013Blog
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        blog = super().get_context_data(**kwargs)
        blog["object_list"] = T013Blog.objects.order_by(
            '-t013_fd06_createdata')
        return blog

# class LoginView(generic.TemplateView):
#     template_name="login.html"


class LocationAdminView(LoginRequiredMixin, generic.TemplateView):
    template_name = "locationAdmin.html"


class LocationParentView(LoginRequiredMixin, generic.TemplateView):
    template_name = "locationParent.html"


class LocationConfigView(LoginRequiredMixin, generic.TemplateView):
    template_name = "locationConfig.html"


class ContactTopView(generic.ListView, LoginRequiredMixin):

    template_name = "ContactTop.html"
    model = T001Children

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ユーザ種類別のデータの取り出し方...self.request.user.detail_buyer←ここでrelated_nameを指定する！！！！！！！！！！！！！！！
        context["object_list"] = T001Children.objects.filter(
            t001_fk01_class_id=self.request.user.detail_buyer.class_id)
        return context

    def get_queryset(self):
        contact = T001Children.objects.all().select_related()
        # 検索box 絞り込み
        if "query" in self.request.GET:
            search = self.request.GET["query"]
            or_lookup = (
                Q(t005_pk01_childen_id__icontains=search)
            )
            contact = contact.filter(or_lookup)
        return contact


class ContactTopOyaView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactTop_oya.html"
    model = T001Children

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = T001Children.objects.filter(
            t001_fk02_parents_id=self.request.user.detail_supplier.id)
        return context


class ContactDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactDetail.html"
    context_object_name = 'object'
    model = T007Contactbook

    def get_context_data(self, **kwargs):
        renrakucho = super().get_context_data(**kwargs)
        id = self.request.GET.get("id", "01")
        num = self.request.GET.get("num", "20211201")
        renrakucho["object"] = T007Contactbook.objects.filter(
            t007_fd01_date=datetime.datetime.strptime(num, '%Y%m%d'), t007_fk01_children_id=id)
        return renrakucho


class ContactUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactUpdate.html"


class ContactTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactTemplate.html"

    def book_new(request):
        form = HomeContactForm(request.POST or None)
        if form.is_valid():
            book = T007Contactbook()
            book.t007_fd03_meal_time = form.cleaned_data['t007_fd03_meal_time']
            book.t007_fd04_meal_contents = form.cleaned_data['t007_fd04_meal_contents']
            book.t007_fd14_breakfast_time = form.cleaned_data['t007_fd14_breakfast_time']
            book.t007_fd13_breakfast_contents = form.cleaned_data['t007_fd13_breakfast_contents']
            book.t007_fd05_bed_time = form.cleaned_data['t007_fd05_bed_time']
            book.t007_fd06_wakeup_time = form.cleaned_data['t007_fd06_wakeup_time']
            book.t007_fd07_mood = form.cleaned_data['t007_fd07_mood']
            book.t007_fd08_defecation_status = form.cleaned_data['t007_fd08_defecation_status']
            book.t007_fd09_defecation_times = form.cleaned_data['t007_fd09_defecation_times']
            book.t007_fd10_bathing = form.cleaned_data['t007_fd10_bathing']
            book.t007_fd11_temperature_time = form.cleaned_data['t007_fd11_temperature_time']
            book.t007_fd02_infomation = form.cleaned_data['t007_fd02_infomation']
            book.t007_fd25_pickup_person = form.cleaned_data['t007_fd25_pickup_person']
            book.t007_fd26_pickup_time = form.cleaned_data['t007_fd26_pickup_time']

            T007Contactbook.objects.create(
                t007_fd03_meal_time=book.t007_fd03_meal_time,
                t007_fd04_meal_contents=book.t007_fd04_meal_contents,
                t007_fd14_breakfast_time=book.t007_fd14_breakfast_time,
                t007_fd13_breakfast_contents=book.t007_fd13_breakfast_contents,
                t007_fd05_bed_time=book.t007_fd05_bed_time,
                t007_fd06_wakeup_time=book.t007_fd06_wakeup_time,
                t007_fd07_mood=book.t007_fd07_mood,
                t007_fd08_defecation_status=book.t007_fd08_defecation_status,
                t007_fd09_defecation_times=book.t007_fd09_defecation_times,
                t007_fd10_bathing=book.t007_fd10_bathing,
                t007_fd11_temperature_time=book.t007_fd11_temperature_time,
                t007_fd02_infomation=book.t007_fd02_infomation,
                t007_fd25_pickup_person=book.t007_fd25_pickup_person,
                t007_fd26_pickup_time=book.t007_fd26_pickup_time,
            )
            return redirect('main:ContactTop')
        return render(request, 'templates/contactTemplate.html', {'form': form})


class MessageAddressView(LoginRequiredMixin, generic.ListView):
    template_name = "messageAddress.html"


class MessageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "message.html"


class AttendView(LoginRequiredMixin, generic.ListView):
    model = T001Children
    template_name = "attend.html"

    def get_queryset(self):
        toukouenn = T001Children.objects.filter(t001_fk01_class_id=self.request.user.detail_buyer.class_id).select_related()
        # 検索box 絞り込み
        #if "query" in self.request.GET:
        #    search = self.request.GET["query"]
        #    or_lookup = (
        #        Q(t005_pk01_childen_id__icontains=search)
        #    )
        #    toukouenn = toukouenn.filter(or_lookup)

        return toukouenn

    def kindergaten(request):
        if request.method == 'POST' :
            enji = request.POST.getlist["update_button"]

            with transaction.atomic() :

                T001Children.objects.filter(
                    t001_pk01_children_id=enji
                ).update(
                    t001_fd11_kindergaten=False,
                )
            messages.info(request, f'登園状態にしました。')

            return render(request, "attend.html",)

class TagScanView(LoginRequiredMixin, generic.TemplateView):
    template_name = "tagScan.html"

# 名簿画面は作らないことになった
# class NameListView(generic.TemplateView):
#     template_name="nameList.html"

# class NameListDetailView(generic.TemplateView):
#     template_name="nameListDetail.html"

# class NameListAddView(generic.TemplateView):
#     template_name="nameListAdd.html"

# class NameListUpdateView(generic.TemplateView):
#     template_name="nameListUpdate.html"


class PlanListView(LoginRequiredMixin, generic.TemplateView):
    template_name = "planlist.html"


class PlanListDetailView(LoginRequiredMixin, ListView):
    template_name = "planListDetail.html"
    paginate_by = 2
    paginate_orphans = 1
    context_object_name = "object"

    model = T008Schedule

    # def get_context_data(self, **kwargs):
    #     planListdetail = super().get_context_data(**kwargs)
    #     num = self.request.GET.get("num", "20211207")
    #     planListdetail["object"] = T008Schedule.objects.filter(
    #         t008_fd03_date=datetime.datetime.strptime(num, '%Y%m%d'))
    #     return planListdetail

    def get_queryset(self):
        planListdetail = T008Schedule.objects.all()
        num = self.request.GET['num']
        if num is not None:
            planListdetail = T008Schedule.objects.filter(
                t008_fd03_date=datetime.datetime.strptime(num, '%Y%m%d'))
        return planListdetail


class PlanListAddView(LoginRequiredMixin, generic.TemplateView):
    template_name = "planListAdd.html"


class PlanListUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "planListUpdate.html"


class PlanListDeleteView(LoginRequiredMixin, generic.TemplateView):
    template_name = "planListDelete.html"


class ParentConfigView(LoginRequiredMixin, generic.TemplateView):
    template_name = "parentConfig.html"


class TeacherConfigView(LoginRequiredMixin, generic.TemplateView):
    template_name = "teacherConfig.html"


class BlogDetailView(LoginRequiredMixin, generic.TemplateView):
    model = T013Blog
    template_name = "blogDetail.html"

    def get_context_data(self, **kwargs):
        blog = super().get_context_data(**kwargs)
        id = self.request.GET.get("id", "00")
        blog["object_list"] = T013Blog.objects.filter(
            t013_pk01_blog_id=id
        )
        return blog

class BlogCreateView(LoginRequiredMixin, generic.CreateView):
    model = T013Blog
    template_name = "blogCreate.html"
    form_class = BlogCreateForm
    success_url = reverse_lazy('main:home')

    def form_valid(self,form):
        main = form.save(commit=False)
        main.save()
        #messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        #messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)

class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = T013Blog
    template_name = "blogUpdate.html"
    form_class = BlogCreateForm
    success_url = reverse_lazy('main:home')

    def form_valid(self,form):
        #messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        #messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)

class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = T013Blog
    template_name = "blogDelete.html"
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        blog = super().get_context_data(**kwargs)
        blog["object_list"] = T013Blog.objects.all
        return blog
