from django.core.mail import message
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from accounts.models import *
from main.models import *
# Create your views h
from .models import *
from django.db.models import Q


class IndexView(generic.TemplateView):
    template_name = "index.html"


class HomeView(LoginRequiredMixin, generic.TemplateView):
    template_name = "home.html"

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
<<<<<<< HEAD
=======

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
    
class ContactTopOyaView(LoginRequiredMixin,generic.TemplateView):
    template_name="contactTop_oya.html"
>>>>>>> 26a85ba1606eedd39e3e92d603a7746a0b73f3b0


class ContactTopOyaView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactTop_oya.html"


class ContactDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactDetail.html"

    def get_queryset(self):
        renrakucho = T007Contactbook.objects.filter(
            t007_pk01_contactbook_id=1234)
        return renrakucho


class ContactUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactUpdate.html"


class ContactTemplateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "contactTemplate.html"


class MessageAddressView(LoginRequiredMixin, generic.ListView):
    template_name = "messageAddress.html"


class MessageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "message.html"


class AttendView(LoginRequiredMixin, generic.ListView):
    model = T005Kindergaten
    template_name = "attend.html"

    def get_queryset(self):
        toukouenn = T005Kindergaten.objects.all().select_related()
        # 検索box 絞り込み
        if "query" in self.request.GET:
            search = self.request.GET["query"]
            or_lookup = (
                Q(t005_pk01_childen_id__icontains=search)
            )
            toukouenn = toukouenn.filter(or_lookup)

        return toukouenn


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


class PlanListDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = "planListDetail.html"
    model = T008Schedule

    def get_queryset(self):
        pl_detail = T008Schedule.objects.filter(
            t008_fd01_event=11111)
        return pl_detail


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
