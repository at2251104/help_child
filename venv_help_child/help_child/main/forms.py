from cProfile import label
from dataclasses import field
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class HomeContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['t007_pk01_contactbook_id'].widget = forms.HiddenInput()
        self.fields['t007_fk01_children_id'].widget = forms.HiddenInput()

        
    class Meta:
        model = T007Contactbook
        fields = ('t007_fk01_children_id', 't007_pk01_contactbook_id', 't007_fd03_meal_time', 't007_fd04_meal_contents', 't007_fd14_breakfast_time', 't007_fd13_breakfast_contents', 't007_fd05_bed_time', 't007_fd06_wakeup_time',
                  't007_fd07_mood', 't007_fd08_defecation_status', 't007_fd09_defecation_times', 't007_fd10_bathing', 't007_fd11_temperature_time', 't007_fd12_temperature', 't007_fd02_infomation', 't007_fd25_pickup_person', 't007_fd26_pickup_time')
        widgets = {
            't007_fd03_meal_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd14_breakfast_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd05_bed_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd06_wakeup_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd11_temperature_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd26_pickup_time': forms.DateTimeInput(attrs={"type": "time"}),
        }

class SchoolContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['t007_pk01_contactbook_id'].widget = forms.HiddenInput()
        self.fields['t007_fk01_children_id'].widget = forms.HiddenInput()


    class Meta:
        model = T007Contactbook
        fields = ('t007_fk01_children_id', 't007_pk01_contactbook_id', 't007_fd16_lunch_time', 't007_fd15_lunch_contents', 't007_fd27_bed_time', 't007_fd17_wakeup_time', 't007_fd18_mood', 't007_fd20_defecation_status',
                  't007_fd19_defecation_times', 't007_fd21_bathing', 't007_fd23_temperature_time', 't007_fd22_temperature', 't007_fd24_infomation', 't007_fd28_person')
        widgets = {
            't007_fk01_children_id':forms.TextInput(attrs={'readonly': 'readonly',}),
            't007_fd16_lunch_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd27_bed_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd17_wakeup_time': forms.DateTimeInput(attrs={"type": "time"}),
            't007_fd23_temperature_time': forms.DateTimeInput(attrs={"type": "time"}),
        }

class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = T013Blog
        fields = ('t013_pk01_blog_id','t013_fd01_title','t013_fd02_content','t013_fd03_photo1',
        't013_fd04_photo2','t013_fd05_photo3',)

class KindergatenForm(forms.ModelForm):
    class Meta:
        model = T001Children
        fields = ('t001_fd11_kindergaten',)
class TemplateCreateForm(forms.ModelForm):
    class Meta:
        model = T012Contactbooktem
        fields = ('t012_pk01_contactbook_id','t012_fk01_childminder_id','t012_fd01_date','t012_fd02_information','t012_fd03_mealtime',
        't012_fd04_meal_contents','t012_fd05_bed_time','t012_fd06_wakeup_time')

class ChildrenEditForm(forms.ModelForm):
    class Meta:
        model = T001Children
        fields = ('t001_pk01_children_id','t001_fk01_class_id','t001_fk02_parents_id','t001_fd01_last_name','t001_fd07_first_name',
        't001_fd08_last_name_kana','t001_fd09_first_name_kana','t001_fd06_sex','t001_fd02_birthday','t001_fd10_postal_code','t001_fd03_address')

class AdultEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username','last_name','first_name','last_name_kana','first_name_kana','email','sex','birthday',
        'postal_code','address','tel')

class AdultCreateForm(UserCreationForm):
 
  class Meta:
    model = CustomUser
    
    fields = ('username','last_name','first_name','last_name_kana','first_name_kana','sex','birthday',
    'postal_code','address','tel','email',
    )
 
class ChildminderForm(forms.ModelForm):
    class Meta:
        model = T003Childminder
        fields = ('user','class_id')


class ParentsForm(forms.ModelForm):
    class Meta:
        model = T002Parents
        fields = ('user',)

class ChildminderEditForm(forms.ModelForm):
    class Meta:
        model = T003Childminder
        fields = ('class_id',)
