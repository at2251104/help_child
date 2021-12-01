from django.core.mail import message
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views h

class IndexView(generic.TemplateView):
    template_name="index.html"

class HomeView(LoginRequiredMixin,generic.TemplateView):
    template_name="home.html"

# class LoginView(generic.TemplateView):
#     template_name="login.html"

class LocationAdminView(LoginRequiredMixin,generic.TemplateView):
    template_name="locationAdmin.html"

    def get_context_data(self, **kwargs):
        # request.pathからid部分を抽出('/polls/01'が入ってるので、01だけ取る)
        # ログイン中のuser_idとurlのidの一致チェック
        if self.request.user.userType.id == 3:
            template_name="locationAdmin.html"
        else :
            message.error("日記の作成に失敗しました。")

class LocationParentView(LoginRequiredMixin,generic.TemplateView):
    template_name="locationParent.html"

class LocationConfigView(LoginRequiredMixin,generic.TemplateView):
    template_name="locationConfig.html"

class ContactTopView(LoginRequiredMixin,generic.TemplateView):
    template_name="contactTop.html"
    
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