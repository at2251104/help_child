from django.shortcuts import render
from django.views import generic
# Create your views h

class IndexView(generic.TemplateView):
    template_name="index.html"

class HomeView(generic.TemplateView):
    template_name="home.html"

# class LoginView(generic.TemplateView):
#     template_name="login.html"

# 位置情報関連----------------------------------------------------------------
class LocationAdminView(generic.TemplateView):
    template_name="locationAdmin.html"

class LocationParentView(generic.TemplateView):
    template_name="locationParent.html"

class LocationConfigView(generic.TemplateView):
    template_name="locationConfig.html"

# 連絡帳関連------------------------------------------------------------------
class ContactTopView(generic.TemplateView):
    template_name="contactTop.html"

class ContactTopOyaView(generic.TemplateView):
    template_name="contactTop_oya.html"

class ContactDetailView(generic.TemplateView):
    template_name="contactDetail.html"

class ContactUpdateView(generic.TemplateView):
    template_name="contactUpdate.html"

class ContactTemplateView(generic.TemplateView):
    template_name="contactTemplate.html"

# 登降園関連--------------------------------------------------------------------
class AttendView(generic.TemplateView):
    template_name="attend.html"

class TagScanView(generic.TemplateView):
    template_name="tagScan.html"

# 予定表関連--------------------------------------------------------------------
class PlanListView(generic.TemplateView):
    template_name="planlist.html"

class PlanListDetailView(generic.TemplateView):
    template_name="planListDetail.html"

class PlanListAddView(generic.TemplateView):
    template_name="planListAdd.html"

class PlanListUpdateView(generic.TemplateView):
    template_name="planListUpdate.html"

class PlanListDeleteView(generic.TemplateView):
    template_name="planListDelete.html"
