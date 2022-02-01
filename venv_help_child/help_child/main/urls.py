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
    path('contactDetail',views.ContactDetailView.as_view(), name="contactDetail"),
    path('contactUpdate',views.ContactUpdateView.as_view(), name="contactUpdate"),
    path('contactUpdate_oya/<int:pk>',views.ContactUpdateOyaView.as_view(), name="contactUpdate_oya"),
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
    path('chilrenDetail',views.ChildrenDetailView.as_view(),name="childrenDetail"),
    path('childminderDetail',views.ChildminderDetailView.as_view(),name="childminderDetail"),
    path('parentsDetail',views.ParentsDetailView.as_view(),name="parentsDetail"),
    path('childrenUpdate/<pk>/',views.ChildrenUpdateView.as_view(),name="childrenUpdate"),
    path('childminderUpdate/<pk>/',views.ChildminderUpdateView.as_view(),name="childminderUpdate"),
    path('childminder2Update/<pk>/',views.ChildminderUpdateView.as_view(),name="childminderUpdate"),
    path('parentsUpdate/<pk>/',views.ParentsUpdateView.as_view(),name="parentsUpdate"),
    path('parentsUpdate/<pk>/',views.ParentsUpdateView.as_view(),name="parentsUpdate"),
    path('childrenDelete/<pk>/',views.ChildrenDeleteView.as_view(),name="childrenDelete"),
    path('childminderDelete/<pk>/',views.ChildminderDeleteView.as_view(),name="childminderDelete"),
    path('parentsDelete/<pk>/',views.ParentsDeleteView.as_view(),name="parentsDelete"),
    path('childrenCreate',views.ChildrenCreateView.as_view(),name="childrenCreate"),
    path('childminderCreate',views.ChildminderCreateView.as_view(),name="childminderCreate"),
    path('childminder2Create',views.Childminder2CreateView.as_view(),name="childminder2Create"),
    path('parentsCreate',views.ParentsCreateView.as_view(),name="parentsCreate"),
    path('parents2Create',views.Parents2CreateView.as_view(),name="parents2Create"),

]
