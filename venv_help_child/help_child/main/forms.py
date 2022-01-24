from cProfile import label
from dataclasses import field
from django import forms
from .models import *


class HomeContactForm(forms.ModelForm):
    class Meta:
        model = T007Contactbook
        fields = ('t007_fd03_meal_time','t007_fd04_meal_contents','t007_fd14_breakfast_time','t007_fd13_breakfast_contents','t007_fd05_bed_time','t007_fd06_wakeup_time','t007_fd07_mood','t007_fd08_defecation_status','t007_fd09_defecation_times','t007_fd10_bathing','t007_fd11_temperature_time','t007_fd12_temperature','t007_fd02_infomation','t007_fd25_pickup_person','t007_fd26_pickup_time')

class SchoolContactForm(forms.ModelForm):
    class Meta:
        model = T007Contactbook
        fields = ('t007_fd16_lunch_time','t007_fd15_lunch_contents','t007_fd27_bed_time','t007_fd17_wakeup_time','t007_fd18_mood','t007_fd20_defecation_status','t007_fd19_defecation_times','t007_fd21_bathing','t007_fd23_temperature_time','t007_fd22_temperature','t007_fd24_infomation','t007_fk02_childminder_id')

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
        't012_fd04_meal_contents','t012_fd05_bed_time','t012_fd06_wakeup_time','t023_fd08_person')
