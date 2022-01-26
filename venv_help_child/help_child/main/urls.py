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
    path('contactUpdate_oya', views.ContactUpdateOyaView.as_view(), name="contactUpdate_oya"),
    path('contactTemplate',views.ContactTemplateView.as_view(),name="contactTemplate"),

    path('attend',views.AttendView.as_view(),name="attend"),
    path('tagScan',views.TagScanView.as_view(),name="tagScan"),

    path('planList',views.PlanListView.as_view(),name="planList"),
    path('planListAdd',views.PlanListAddView.as_view(),name="planListAdd"),
    path('planListDetail',views.PlanListDetailView.as_view(),name="planListDetail"),
    path('planListUpdate',views.PlanListUpdateView.as_view(),name="planListUpdate"),
    path('planListDelete',views.PlanListDeleteView.as_view(),name="planListDelete"),

    path('blogDetail',views.BlogDetailView.as_view(),name="blogDetail"),
    path('blogCreate',views.BlogCreateView.as_view(),name="blogCreate"),
    path('blogUpdate/<int:pk>/',views.BlogUpdateView.as_view(),name="blogUpdate"),
    path('blogDelete/<int:pk>/',views.BlogDeleteView.as_view(),name="blogDelete"),

    path('listTop',views.ListTopView.as_view(),name='listTop'),
    path('childrenlistTop',views.ChildrenListTopView.as_view(),name='childrenlistTop'),
    path('childminderlistTop',views.ChildminderListTopView.as_view(),name='childminderlistTop'),
    path('parentslistTop',views.ParentsListTopView.as_view(),name='parentslistTop'),
    path('listDetail',views.ListDetailView.as_view(),name="listDetail"),
    path('listCreate',views.ListCreateView.as_view(),name="listCreate"),
    path('listUpdate/<int:pk>/',views.ListUpdateView.as_view(),name="listUpdate"),
    path('listDelete/<int:pk>/',views.ListDeleteView.as_view(),name="listDelete"),

]
