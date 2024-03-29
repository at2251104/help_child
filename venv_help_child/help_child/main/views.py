from audioop import reverse
import email
from json.tool import main
from pyexpat.errors import messages
from django.core.mail import message
from django.contrib import messages as add_messages
from django.http import request
from django.shortcuts import render
from django.template import context
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from accounts.models import *
from main.models import *
# Create your views h
from .models import *
from django.db.models import Q, F
from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from django.db import transaction
import logging
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView


from datetime import time
logger = logging.getLogger('development')


class BaseView(generic.TemplateView):
    template_name = "base.html"


class HomeView(LoginRequiredMixin, generic.TemplateView):
    model = T013Blog,T008Schedule
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        blog = super().get_context_data(**kwargs)
        schedule = super().get_context_data(**kwargs)
        blog["object_list"] = T013Blog.objects.order_by(
            '-t013_fd06_createdata')
        one_week = datetime.datetime.now() + datetime.timedelta(days = 7)
        schedule["object"] = T008Schedule.objects.filter(t008_fd03_date__range=[datetime.datetime.now(),one_week,])
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
        context["contact"] = T001Children.objects.filter(
            t001_fk01_class_id=self.request.user.detail_buyer.class_id)
        return context

    def get_queryset(self):
        contact = T001Children.objects.all().select_related()
        # 検索box 絞り込み
        if "query" in self.request.GET:
            search = self.request.GET["query"]
            or_lookup = (
                Q(t001_fd08_last_name_kana__icontains=search)|
                Q(t001_fd09_first_name_kana__icontains=search) |
                Q(t001_fd01_last_name__icontains=search) |
                Q(t001_fd07_first_name__icontains=search) 
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
    model = CustomUser

    def get_context_data(self, **kwargs):
        renrakucho = super().get_context_data(**kwargs)
        id = self.request.GET.get("id", "01")
        num = self.request.GET.get("num", "20211201")
        renrakucho["object"] = T007Contactbook.objects.filter(
            t007_fd01_date=datetime.datetime.strptime(num, '%Y%m%d'), t007_fk01_children_id=id)
        return renrakucho

    def get_queryset(self):
        return CustomUser.objects.filter(username=self.request.user.username)


class ContactUpdateView(LoginRequiredMixin, generic.CreateView):
    model = T007Contactbook
    template_name = "contactUpdate.html"
    form_class = SchoolContactForm
    success_url = reverse_lazy('main:contactTop')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        num = self.request.GET.get("num", "20211201")
        id = self.request.GET.get("id", "01")
        a=T012Contactbooktem.objects.all().first()
        
        initial_dict = {
        't007_fk01_children_id': id,
        't007_pk01_contactbook_id': num+id,
        't007_fd15_lunch_contents': a.t012_fd04_meal_contents,
        't007_fd16_lunch_time':datetime.time(a.t012_fd03_mealtime.hour,a.t012_fd03_mealtime.minute),
        't007_fd27_bed_time':a.t012_fd05_bed_time,
        't007_fd17_wakeup_time':a.t012_fd06_wakeup_time,
        't007_fd24_infomation':a.t012_fd02_information
        }
        
        context['form'] = SchoolContactForm(self.request.POST or None, initial=initial_dict)
        # test
        return context

    def form_valid(self, form):
        main = form.save(commit=False)
        main.user = self.request.user
        main.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ContactUpdateOyaView(LoginRequiredMixin, generic.UpdateView):

    model = T007Contactbook
    template_name = "contactUpdate_oya.html"
    form_class = HomeContactForm
    success_url = reverse_lazy('main:contactTop_oya')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        num = self.kwargs.get('pk')
        default_data = {
            't007_pk01_contactbook_id': num,
            't007_fk01_children_id': num[8:]
        }
        homecontact_form = HomeContactForm(initial = default_data)
        context['form'] = homecontact_form

        return context

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ContactTemplateView(LoginRequiredMixin, generic.CreateView):
    model = T012Contactbooktem
    fields = '__all__'
    template_name = "contactTemplate.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.getlist('data', None):
            post = self.request.POST.getlist('data', None)
            a=T003Childminder.objects.get(user__username=self.request.user.username)
            T012Contactbooktem.objects.create(t012_fd03_mealtime=post[0], t012_fd04_meal_contents=post[1],
                                            t012_fd05_bed_time=post[2], t012_fd06_wakeup_time=post[3], t012_fd02_information=post[4],t012_fk01_childminder_id=a)
        return self.get(request, *args, **kwargs,)


class MessageAddressView(LoginRequiredMixin, generic.ListView):
    template_name = "messageAddress.html"


class MessageView(LoginRequiredMixin, generic.TemplateView):
    template_name = "message.html"


class AttendView(LoginRequiredMixin, generic.ListView):
    model = T001Children
    template_name = "attend.html"

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('update_button', None):
            t = T001Children.objects.filter(
                t001_pk01_children_id=self.request.POST.get('update_button')).first()
            t.t001_fd11_kindergaten = not bool(t.t001_fd11_kindergaten)
            t.save()
        elif self.request.POST.get('all_true_button', None):
            T001Children.objects.filter(t001_fk01_class_id=self.request.user.detail_buyer.class_id).update(
                t001_fd11_kindergaten=True)
        elif self.request.POST.get('all_false_button', None):
            T001Children.objects.filter(t001_fk01_class_id=self.request.user.detail_buyer.class_id).update(
                t001_fd11_kindergaten=False)
        return self.get(request, *args, **kwargs,)

    def get_queryset(self):
        toukouenn = T001Children.objects.filter(
            t001_fk01_class_id=self.request.user.detail_buyer.class_id).select_related()
        # 検索box 絞り込み
        # if "query" in self.request.GET:
        #    search = self.request.GET["query"]
        #    or_lookup = (
        #        Q(t005_pk01_childen_id__icontains=search)
        #    )
        #    toukouenn = toukouenn.filter(or_lookup)

        return toukouenn


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
    context_object_name = "objects"
    model=T004Class

    def post(self, request, *args, **kwargs):
        if self.request.POST.getlist('planName', None):
            post = self.request.POST.getlist('planName', None)
            post[0] = T004Class.objects.get(t004_fd01_class_name=post[0])
            T008Schedule.objects.create(t008_fk01_class_id=post[0],
                                        t008_fd01_event=post[2], t008_fd03_date=post[1], t008_fd02_remarks=post[3])
        return self.get(request, *args, **kwargs,)


class PlanListUpdateView(LoginRequiredMixin, generic.TemplateView):
    template_name = "planListUpdate.html"
    def post(self, request, *args, **kwargs):
        if self.request.POST.getlist('planName', None):
            post = self.request.POST.getlist('planName', None)
            post[1] = T004Class.objects.get(t004_pk01_class_id=post[1])
            T008Schedule.objects.create(t008_pk01_schedule_id=post[0], t008_fk01_class_id=post[1],
                                        t008_fd01_event=post[3], t008_fd03_date=post[2], t008_fd02_remarks=post[4])
        return self.get(request, *args, **kwargs,)



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

    def form_valid(self, form):
        main = form.save(commit=False)
        main.save()
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)


class BlogUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = T013Blog
    template_name = "blogUpdate.html"
    form_class = BlogCreateForm
    success_url = reverse_lazy('main:home')

    def form_valid(self, form):
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)


class BlogDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = T013Blog
    template_name = "blogDelete.html"
    success_url = reverse_lazy('main:home')

    def get_context_data(self, **kwargs):
        blog = super().get_context_data(**kwargs)
        blog["object_list"] = T013Blog.objects.all
        return blog


class ChildminderListTopView(generic.ListView, LoginRequiredMixin):

    template_name = "childminderlistTop.html"

    model = T003Childminder,CustomUser

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adult"] = T003Childminder.objects.all().order_by('user__last_name_kana')

        return context

    def get_queryset(self):
        contact = T003Childminder.objects.all().select_related()
        
        # 検索box 絞り込み
        if "query" in self.request.GET:
            search = self.request.GET["query"]
            or_lookup = (
                Q(user__last_name_kana__icontains=search) |
                Q(user__first_name_kana__icontains=search) |
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) 
            )
            contact = contact.filter(or_lookup)
        return contact


class ChildrenListTopView(generic.ListView, LoginRequiredMixin):

    template_name = "childrenlistTop.html"

    model = T001Children, T002Parents, T003Childminder

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Children"] = T001Children.objects.all().order_by(
            't001_fd08_last_name_kana')
        return context

    

    def get_queryset(self):
        contact = T001Children.objects.all().select_related()
        
        # 検索box 絞り込み
        if "query" in self.request.GET:
            search = self.request.GET["query"]
            or_lookup = (
                Q(t001_fd08_last_name_kana__icontains=search)|
                Q(t001_fd09_first_name_kana__icontains=search) |
                Q(t001_fd01_last_name__icontains=search) |
                Q(t001_fd07_first_name__icontains=search) 
            )
            contact = contact.filter(or_lookup)
        return contact


class ParentsListTopView(generic.ListView, LoginRequiredMixin):

    template_name = "parentslistTop.html"

    model = T002Parents,CustomUser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["adult"] = T002Parents.objects.all().order_by('user_id')
        return context

    def get_queryset(self):
        contact = T002Parents.objects.all().select_related()
        # 検索box 絞り込み
        if "query" in self.request.GET:
            search = self.request.GET["query"]
            or_lookup = (
                Q(user__first_name_kana__icontains=search) |
                Q(user__last_name_kana__icontains=search) |
                Q(user__first_name__icontains=search) |
                Q(user__last_name__icontains=search) 
            )
            contact = contact.filter(or_lookup)
        return contact




class ChildrenDetailView(LoginRequiredMixin, generic.TemplateView):
    model = T001Children
    template_name = "childrenDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.GET.get("id", "00")
        context["Children"] = T001Children.objects.filter(
            t001_pk01_children_id=id
        )
        return context


class ListCreateView(LoginRequiredMixin, generic.CreateView):
    model = T013Blog
    template_name = "blogCreate.html"
    form_class = BlogCreateForm
    success_url = reverse_lazy('main:home')





class ChildminderDetailView(LoginRequiredMixin, generic.TemplateView):
    model = CustomUser
    template_name = "childminderDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Email = self.request.GET.get("Email", "00")
        context["Childminder"] = CustomUser.objects.filter(
            email=Email
        )
        return context


class ParentsDetailView(LoginRequiredMixin, generic.TemplateView):
    model = CustomUser
    template_name = "parentsDetail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        Email = self.request.GET.get("Email", "00")
        context["Parents"] = CustomUser.objects.filter(
            email=Email
        )
        return context


class ChildrenUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = T001Children
    template_name = "childrenUpdate.html"
    form_class = ChildrenEditForm
    success_url = reverse_lazy('main:childrenlistTop',)

    def form_valid(self, form):
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)


class ChildminderUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = "childminderUpdate.html"
    form_class = AdultEditForm

    def get_success_url(self):
        return reverse('main:childminder2Update',kwargs= {'pk':self.kwargs['pk']})

    def form_valid(self,form):
        #messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        #messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)

class Childminder2UpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = "childminderUpdate.html"
    form_class = ChildminderEditForm
    success_url = reverse_lazy('main:childminderlistTop')

    
    def form_valid(self,form):
        #messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)


class ParentsUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = "parentsUpdate.html"
    form_class = AdultEditForm
    success_url = reverse_lazy('main:parentslistTop')
    
    def form_valid(self,form):
        #messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)


class ChildrenDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = T001Children
    template_name = "childrenDelete.html"
    success_url = reverse_lazy('main:childrenlistTop')

    

class ChildminderDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CustomUser
    template_name = "childminderDelete.html"
    success_url = reverse_lazy('main:childminderlistTop')


class ParentsDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = CustomUser
    template_name = "parentsDelete.html"
    success_url = reverse_lazy('main:parentslistTop')


class ChildrenCreateView(LoginRequiredMixin, generic.CreateView):
    model = T001Children
    template_name = "childrenCreate.html"
    form_class = ChildrenEditForm
    success_url = reverse_lazy('main:childrenlistTop')



    def form_valid(self, form):
        main = form.save(commit=False)
        main.save()
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)


class ChildminderCreateView(LoginRequiredMixin, generic.CreateView):
    model = CustomUser, T003Childminder
    template_name = "childminderCreate.html"
    form_class = AdultCreateForm
    success_url = reverse_lazy('main:childminder2Create')

    def form_valid(self, form):
        main = form.save(commit=False)
        main.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)



class ParentsCreateView(LoginRequiredMixin, generic.CreateView):
    model = CustomUser
    template_name = "parentsCreate.html"
    form_class = AdultCreateForm
    success_url = reverse_lazy('main:parents2Create')

    def form_valid(self, form):
        main = form.save(commit=False)
        main.save()


        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)

class Childminder2CreateView(LoginRequiredMixin, generic.CreateView):
    model = T003Childminder
    template_name = "childminder2Create.html"
    form_class = ChildminderForm
    success_url = reverse_lazy('main:childminderlistTop')

    def form_valid(self,form):
        main = form.save(commit=False)
        main.save()
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)

class Parents2CreateView(LoginRequiredMixin, generic.CreateView):
    model = T002Parents
    template_name = "parents2Create.html"
    form_class = ParentsForm
    success_url = reverse_lazy('main:parentslistTop')

    def form_valid(self,form):
        main = form.save(commit=False)
        main.save()
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)
# aaaaa
class ClassCreateView(LoginRequiredMixin, generic.CreateView):
    model = T004Class
    template_name = "classCreate.html"
    form_class = ClassCreateForm
    success_url = reverse_lazy('main:home')


    def form_valid(self, form):
        main = form.save(commit=False)
        main.save()
        # messages.success(self.request,'ブログを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request,"ブログの作成に失敗しました。")
        return super().form_invalid(form)
