from django.shortcuts import render
from django.views import generic
# Create your views h

class IndexView(generic.TemplateView):
    template_name="index.html"

class HomeView(generic.TemplateView):
    template_name="home.html"

class LoginView(generic.TemplateView):
    template_name="login.html"

class LocationAdminView(generic.TemplateView):
    template_name="locationAdmin.html"

class LocationParentView(generic.TemplateView):
    template_name="locationParent.html"

class LocationConfigView(generic.TemplateView):
    template_name="locationConfig.html"

class ContactTopView(generic.TemplateView):
    template_name="contactTop.html"

class ContactDetailView(generic.TemplateView):
    template_name="contactDetail.html"

class ContactUpdateView(generic.TemplateView):
    template_name="contactUpdate.html"

class MessageAddressView(generic.TemplateView):
    template_name="messageAddress.html"

class MessageView(generic.TemplateView):
    template_name="message.html"

class AttendView(generic.TemplateView):
    template_name="attend.html"

class TagScanView(generic.TemplateView):
    template_name="tagScan.html"

class NameListView(generic.TemplateView):
    template_name="nameList.html"

class NameListDetailView(generic.TemplateView):
    template_name="nameListDetail.html"

class NameListAddView(generic.TemplateView):
    template_name="nameListAdd.html"

class NameListUpdateView(generic.TemplateView):
    template_name="nameListUpdate.html"

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

class ParentConfigView(generic.TemplateView):
    template_name="parentConfig.html"

class TeacherConfigView(generic.TemplateView):
    template_name="teacherConfig.html"