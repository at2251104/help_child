from django.core.mail import message
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from accounts.models import *
from main.models import *
# Create your views h
from .models import *


class IndexView(generic.TemplateView):
    template_name="index.html"

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name="home.html"

# class LoginView(generic.TemplateView):
#     template_name="login.html"

class LocationAdminView(LoginRequiredMixin,generic.TemplateView):
    template_name="locationAdmin.html"

class LocationParentView(LoginRequiredMixin,generic.TemplateView):
    template_name="locationParent.html"

class LocationConfigView(LoginRequiredMixin,generic.TemplateView):
    template_name="locationConfig.html"

class ContactTopView(generic.ListView,LoginRequiredMixin):
    
    template_name="ContactTop.html"
    model=T001Children
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ユーザ種類別のデータの取り出し方...self.request.user.detail_buyer←ここでrelated_nameを指定する！！！！！！！！！！！！！！！
        context["object_list"] = T001Children.objects.filter(t001_fk01_class_id=self.request.user.detail_buyer.class_id)
        return context
    
    
class ContactTopOyaView(LoginRequiredMixin,generic.TemplateView):
    template_name="contactTop_oya.html"

class ContactDetailView(LoginRequiredMixin,generic.TemplateView):
    template_name="contactDetail.html"

class ContactUpdateView(LoginRequiredMixin,generic.TemplateView):
    template_name="contactUpdate.html"

class ContactTemplateView(LoginRequiredMixin,generic.TemplateView):
    template_name="contactTemplate.html"

class MessageAddressView(LoginRequiredMixin,generic.TemplateView):
    template_name="messageAddress.html"

class MessageView(LoginRequiredMixin,generic.TemplateView):
    template_name="message.html"

class AttendView(LoginRequiredMixin,generic.TemplateView):
    template_name="attend.html"

class TagScanView(LoginRequiredMixin,generic.TemplateView):
    template_name="tagScan.html"

# 名簿画面は作らないことになった
# class NameListView(generic.TemplateView):
#     template_name="nameList.html"

# class NameListDetailView(generic.TemplateView):
#     template_name="nameListDetail.html"

# class NameListAddView(generic.TemplateView):
#     template_name="nameListAdd.html"

# class NameListUpdateView(generic.TemplateView):
#     template_name="nameListUpdate.html"

class PlanListView(LoginRequiredMixin,generic.TemplateView):
    template_name="planlist.html"

class PlanListDetailView(LoginRequiredMixin,generic.TemplateView):
    template_name="planListDetail.html"

class PlanListAddView(LoginRequiredMixin,generic.TemplateView):
    template_name="planListAdd.html"

class PlanListUpdateView(LoginRequiredMixin,generic.TemplateView):
    template_name="planListUpdate.html"

class PlanListDeleteView(LoginRequiredMixin,generic.TemplateView):
    template_name="planListDelete.html"

class ParentConfigView(LoginRequiredMixin,generic.TemplateView):
    template_name="parentConfig.html"

class TeacherConfigView(LoginRequiredMixin,generic.TemplateView):
    template_name="teacherConfig.html"
