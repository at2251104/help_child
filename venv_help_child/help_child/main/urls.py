from django.urls import path
from . import views

app_name="main"

urlpatterns=[
    path('',views.HomeView.as_view(),name="home"),
    # path('login',views.LoginView.as_view(),name="login"),
    path('locationAdmin',views.LocationAdminView.as_view(),name="locationAdmin"),
    path('locationParent',views.LocationParentView.as_view(),name="locationParent"),
    path('locationConfig',views.LocationConfigView.as_view(),name="locationConfig"),

    path('contactTop',views.ContactTopView.as_view(),name="contactTop"),
    path('contactTop_oya',views.ContactTopOyaView.as_view(),name="contactTop_oya"),
    path('contactDetail',views.ContactDetailView.as_view(),name="contactDetail"),
    path('contactUpdate',views.ContactUpdateView.as_view(),name="contactUpdate"),
    path('contactTemplate',views.ContactTemplateView.as_view(),name="contactTemplate"),


    path('messageAddress',views.MessageAddressView.as_view(),name="messageAddress"),
    path('message',views.MessageView.as_view(),name="message"),

    path('attend',views.AttendView.as_view(),name="attend"),
    path('tagScan',views.TagScanView.as_view(),name="tagScan"),

    path('nameList',views.NameListView.as_view(),name="nameList"),
    path('nameListAdd',views.NameListAddView.as_view(),name="nameListAdd"),
    path('nameListDetail',views.NameListDetailView.as_view(),name="nameListDetail"),
    path('nameListUpdate',views.NameListUpdateView.as_view(),name="nameListUpdate"),

    path('planList',views.PlanListView.as_view(),name="planList"),
    path('planListAdd',views.PlanListAddView.as_view(),name="planListAdd"),
    path('planListDetail/<int:pk>',views.PlanListDetailView.as_view(),name="planListDetail"),
    path('planListUpdate',views.PlanListUpdateView.as_view(),name="planListUpdate"),
    path('planListDelete',views.PlanListDeleteView.as_view(),name="planListDelete"),

    path('parentConfig',views.ParentConfigView.as_view(),name="parentConfig"),
    path('teacherConfig',views.TeacherConfigView.as_view(),name="teacherConfig"),
    
]