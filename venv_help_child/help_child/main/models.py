from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import T002Parents,T003Childminder,CustomUser
import datetime
from datetime import date
import math


class T004Class(models.Model):
    t004_pk01_class_id = models.CharField(verbose_name='クラスID',db_column='T004_PK01_class-id', primary_key=True, max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t004_fd01_class_name = models.CharField(verbose_name='クラス名',db_column='T004_FD01_class-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t004_fd02_year = models.IntegerField(verbose_name='学年',db_column='T004_FD02_year')  # Field name made lowercase.

    class Meta:
        db_table = 'T004_class'
        verbose_name_plural="クラステーブル"

    def __str__(self):
        return self.t004_fd01_class_name

# 園児の個人データ
class T001Children(models.Model):
    t001_pk01_children_id = models.CharField(verbose_name='園児ID',db_column='T001_PK01_children-id', primary_key=True, max_length=150)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t001_fk01_class_id = models.ForeignKey(T004Class, models.DO_NOTHING, default='1',verbose_name='クラス名',db_column='T001_FK01_class-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t001_fk02_parents_id = models.ForeignKey(T002Parents, models.DO_NOTHING,default='1',verbose_name='保護者ID', db_column='T001_FK02_parents-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t001_fd01_last_name = models.CharField(verbose_name='姓',max_length=20)  # Field name made lowercase.
    t001_fd07_first_name = models.CharField(('名'), max_length=20)
    t001_fd08_last_name_kana = models.CharField(('姓（かな）'), max_length=20)
    t001_fd09_first_name_kana = models.CharField(('名（かな）'),max_length=20)
    t001_fd06_sex = models.CharField(verbose_name='性別',default='男性',max_length=4,db_column='T001_FD06_sex',choices=(('男性','男性'), ('女性','女性')))  # Field name made lowercase.
    t001_fd02_birthday = models.DateField(verbose_name='誕生日',db_column='T001_FD02_birthday')  # Field name made lowercase.
    t001_fd10_postal_code = models.CharField(('郵便番号（ハイフンなし）'), max_length=7, blank=True, null=True)
    t001_fd03_address = models.CharField(verbose_name='住所',db_column='T001_FD03_address', max_length=50)  # Field name made lowercase.
    t001_fd04_createdata = models.DateTimeField(verbose_name='作成日時',db_column='T001_FD04_createdata',auto_now_add=True, blank=True, null=True)  # Field name made lowercase.
    t001_fd05_updatedata = models.DateTimeField(verbose_name='更新日時',db_column='T001_FD05_updatedata',auto_now=True, blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        db_table = 'T001_children'
        verbose_name_plural="園児テーブル"

    def get_full_name(self):
        full_name = '%s %s' % (self.t001_fd01_last_name, self.t001_fd07_first_name)
        return full_name.strip()

    def Age(self):
        today = int(date.today().strftime('%Y%m%d'))
        birth = int(self.t001_fd02_birthday.strftime('%Y%m%d'))
        age = math.floor((today - birth) / 10000)

        return str(age) + "歳"


    def __str__(self):
        return self.t001_pk01_children_id


# 登降園状態
class T005Kindergaten(models.Model):
    t005_pk01_childen_id = models.OneToOneField('T001Children', on_delete=models.CASCADE,verbose_name='園児ID',db_column='T005_PK01_childen-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t005_fd01_date = models.DateField(verbose_name='日付',default=datetime.date.today,db_column='T005_FD01_date',)  # Field name made lowercase.
    t005_fd02_school_time = models.TimeField(verbose_name='登園時間',db_column='T005_FD02_school-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t005_fd03_exit_time = models.TimeField(verbose_name='降園時間',db_column='T005_FD03_exit-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t005_fd04_status = models.CharField(verbose_name='登園状態',max_length=4,db_column='T005_FD04_status',default = '登園',choices=(('登園','登園'), ('降園','降園'), ('遅刻','遅刻'), ('早退','早退')))  # Field name made lowercase.

    class Meta:

        db_table = 'T005_kindergaten'
        verbose_name_plural="登園状態テーブル"

    def __str__(self):
        return str(self.t005_pk01_childen_id)


class T006Message(models.Model):
    t006_pk01_message_id = models.CharField(verbose_name='メッセージID',db_column='T006_PK01_message-id', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t006_fk01_room_id = models.ForeignKey('T011Room', models.DO_NOTHING,default='1',verbose_name='ルームID',db_column='T006_FK01_room-id', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t006_fd01_send_id = models.CharField(verbose_name='送信者ID',db_column='T006_FD01_send-id', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t006_fd02_contents = models.CharField(verbose_name='内容',db_column='T006_FD02_contents', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t006_fd03_datetime = models.DateTimeField(verbose_name='日時',auto_now=True,db_column='T006_FD03_datetime',blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        
        db_table = 'T006_message'
        verbose_name_plural="メッセージテーブル"

    def __str__(self):
        return self.t006_pk01_message_id


# 連絡帳----------------------------------------------------------------------------
class T007Contactbook(models.Model):
    t007_pk01_contactbook_id = models.CharField(verbose_name='連絡帳ID',db_column='T007_PK01_contactbook-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fk02_childminder_id = models.ForeignKey(T003Childminder, models.DO_NOTHING,default='1',verbose_name='保育士ID', db_column='T007_FK02_childminder-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fk01_children_id = models.ForeignKey(T001Children, models.DO_NOTHING,default='1',verbose_name='園児ID', db_column='T007_FK01_children-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd13_updatedata = models.DateTimeField(verbose_name='保存or投稿日時',db_column='T007_FD13_updatedata')  # Field name made lowercase.
    t007_fd04_meal_contents = models.CharField(verbose_name='前夜食事内容',db_column='T007_FD04_meal-contents', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd03_meal_time = models.TimeField(verbose_name='前夜食事時間',db_column='T007_FD03_meal-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd13_breakfast_contents = models.CharField(verbose_name='今朝食事内容',db_column='T007_FD13_bresakfast-contents', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd14_breakfast_time = models.TimeField(verbose_name='今朝食事時間',db_column='T007_FD14_breakfast-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd05_bed_time = models.TimeField(verbose_name='就寝時間',db_column='T007_FD05_bed-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd06_wakeup_time = models.TimeField(verbose_name='起床時間',db_column='T007_FD06_wakeup-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd07_mood = models.IntegerField(verbose_name='機嫌',db_column='T007_FD07_mood',blank=True, null=True)  # Field name made lowercase.
    t007_fd09_defecation_times = models.IntegerField(verbose_name='排便回数',db_column='T007_FD09_defecation-times', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd08_defecation_status = models.IntegerField(verbose_name='排便状態',db_column='T007_FD08_defecation-status', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd10_bathing = models.BooleanField(verbose_name='入浴の有無',db_column='T007_FD10_bathing',default=True)  # Field name made lowercase.
    t007_fd12_temperature = models.FloatField(verbose_name='検温',db_column='T007_FD12_temperature', blank=True, null=True)  # Field name made lowercase.
    t007_fd11_temperature_time = models.TimeField(verbose_name='検温時間',db_column='T007_FD11_temperature-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd02_infomation = models.CharField(verbose_name='備考',db_column='T007_FD02_infomation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t007_fd25_pickup_person = models.CharField(verbose_name='迎え人',default='父',max_length=4,choices=(('父','父'), ('母','母'),('兄','兄'),('姉','姉'),('祖母','祖母'),('祖父','祖父'),('バス','バス')))  # Field name made lowercase.
    t007_fd26_pickup_time = models.TimeField(verbose_name='迎え時間',blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    t007_fd15_lunch_contents = models.CharField(verbose_name='昼食食事内容',db_column='T007_FD15_lunch-contents', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd16_lunch_time = models.TimeField(verbose_name='昼食食事時間',db_column='T007_FD16_lunch-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd27_bed_time = models.TimeField(verbose_name='就寝時間', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd17_wakeup_time = models.TimeField(verbose_name='起床時間', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd18_mood = models.IntegerField(verbose_name='機嫌',blank=True, null=True)  # Field name made lowercase.
    t007_fd19_defecation_times = models.IntegerField(verbose_name='排便回数', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd20_defecation_status = models.IntegerField(verbose_name='排便状態', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd21_bathing = models.BooleanField(verbose_name='入浴の有無',default=True)  # Field name made lowercase.
    t007_fd22_temperature = models.FloatField(verbose_name='検温', blank=True, null=True)  # Field name made lowercase.
    t007_fd23_temperature_time = models.TimeField(verbose_name='検温時間', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd24_infomation = models.CharField(verbose_name='備考', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t007_fd01_date = models.DateField(verbose_name='日付',default=datetime.date.today,db_column='T007_FD01_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        
        db_table = 'T007_contactbook'
        verbose_name_plural="連絡帳テーブル"

    def __str__(self):
        return self.t007_pk01_contactbook_id


# 行事-----------------------------------------------------------------------------------
class T008Schedule(models.Model):
    t008_pk01_schedule_id = models.CharField(verbose_name='スケジュールID',db_column='T008_PK01_schedule-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t008_fk01_class_id = models.ForeignKey(T004Class, models.DO_NOTHING,default='1',verbose_name='クラスID', db_column='T008_FK01_class-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t008_fd01_event = models.CharField(verbose_name='イベント名',db_column='T008_FD01_event', max_length=100)  # Field name made lowercase.
    t008_fd02_remarks = models.CharField(verbose_name='情報',db_column='T008_FD02_remarks', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t008_fd03_date = models.DateField(verbose_name='開催日',db_column='T008_FD03_date')  # Field name made lowercase.
    t008_fd06_time = models.TimeField(verbose_name='開催時間',db_column='T008_FD06_time', blank=True, null=True)  # Field name made lowercase.
    t008_fd04_updatedata = models.DateTimeField(verbose_name='作成日時',auto_now_add=True,db_column='T008_FD04_updatedata')  # Field name made lowercase.
    t008_fd05_createdata = models.DateTimeField(verbose_name='更新日時',auto_now=True,db_column='T008_FD05_createdata', blank=True, null=True)  # Field name made lowercase.
    

    class Meta:
        
        db_table = 'T008_schedule'
        verbose_name_plural="スケジュールテーブル"

    def __str__(self):
        return self.t008_fd01_event


# 遊具からの位置情報---------------------------------------------------------------------------------------
class T010Playset(models.Model):
    t010_pk01_playset_id = models.CharField(verbose_name='遊具ID',db_column='T010_PK01_playset-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd01_playset_name = models.CharField(verbose_name='遊具名',db_column='T010_FD01_playset-name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd02_distance_a = models.FloatField(verbose_name='アンカーaからの遊具までの距離',db_column='T010_FD02_distance-a')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd03_distance_b = models.FloatField(verbose_name='アンカーbからの遊具までの距離',db_column='T010_FD03_distance-b')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd04_distance_c = models.FloatField(verbose_name='アンカーcからの遊具までの距離',db_column='T010_FD04_distance-c')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'T010_playset'
        verbose_name_plural="遊具テーブル"

    def __str__(self):
        return self.t010_fd01_playset_name

# 園児の位置情報--------------------------------------------------------------------------
class T009Position(models.Model):
    t009_pk01_children_id = models.OneToOneField(T001Children, on_delete=models.CASCADE,verbose_name='園児ID', db_column='T009_PK01_children-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_pk02_datetime = models.DateTimeField(verbose_name='日時',db_column='T009_PK02_datetime',)  # Field name made lowercase.
    t009_fk01_playset_id = models.ForeignKey(T010Playset, models.DO_NOTHING,default='1',verbose_name='遊具ID', db_column='T009_FK01_playset-id', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_fd01_distance_a = models.FloatField(verbose_name='アンカーaからの遊具までの距離',db_column='T009_FD01_distance-a')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_fd02_distance_b = models.FloatField(verbose_name='アンカーbからの遊具までの距離',db_column='T009_FD02_distance-b')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_fd03_distance_c = models.FloatField(verbose_name='アンカーcからの遊具までの距離',db_column='T009_FD03_distance-c')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        
        db_table = 'T009_position'
        unique_together = (('t009_pk01_children_id', 't009_pk02_datetime'),)
        verbose_name_plural="位置情報テーブル"

    def __str__(self):
        return str(self.t009_pk01_children_id)

# 室内の位置情報---------------------------------------------------------------------------------------
class T011Room(models.Model):
    t011_pk01_room_id = models.CharField(verbose_name='ルームID',db_column='T011_PK01_room-id', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t011_fk01_parents_id = models.ForeignKey(T002Parents, models.DO_NOTHING,default='1',verbose_name='保護者ID', )  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t011_fk02_chilminder_id = models.ForeignKey(T003Childminder, models.DO_NOTHING,default='1', verbose_name='保育士ID',db_column='T011_FK02_chilminder-id', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        db_table = 'T011_room'
        verbose_name_plural="ルームテーブル"

    def __str__(self):
        return self.t011_pk01_room_id


# 連絡帳テンプレート---------------------------------------------------------------------------------------
class T012Contactbooktem(models.Model):
    t012_pk01_contactbook_id = models.CharField(verbose_name='連絡帳テンプレートID',db_column='T012_PK01_contactbook-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fk01_childminder_id = models.ForeignKey(T003Childminder, models.DO_NOTHING,default='1',verbose_name='保育士ID', db_column='T012_FK01_childminder-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd01_date = models.DateField(verbose_name='日時',db_column='T012_FD01_date', blank=True, null=True)  # Field name made lowercase.
    t012_fd02_information = models.CharField(verbose_name='備考',db_column='T012_FD02_information', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t012_fd03_mealtime = models.TimeField(verbose_name='食事時間',db_column='T012_FD03_mealtime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    t012_fd04_meal_contents = models.CharField(verbose_name='食事内容',db_column='T012_FD04_meal-contents', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd05_bed_time = models.TimeField(verbose_name='就寝時間',db_column='T012_FD05_bed-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd06_wakeup_time = models.TimeField(verbose_name='起床時間',db_column='T012_FD06_wakeup-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd07_updatedata = models.DateTimeField(verbose_name='更新日時',auto_now=True,db_column='T012_FD07_updatedata')  # Field name made lowercase.

    class Meta:
        
        db_table = 'T012_contactbooktem'
        verbose_name_plural="連絡帳テンプレートテーブル"

    def __str__(self):
        return self.t012_pk01_contactbook_id


class T013Blog(models.Model):
    t013_pk01_blog_id = models.CharField(verbose_name='ブログID',primary_key=True, max_length=10) 
    t013_fd01_title = models.CharField(verbose_name='タイトル',max_length=40)
    t013_fd02_content = models.TextField(verbose_name='本文',blank=True,null=True)
    t013_fd03_photo1 = models.ImageField(verbose_name='写真１',blank=True,null=True)
    t013_fd04_photo2 = models.ImageField(verbose_name='写真２',blank=True,null=True)
    t013_fd05_photo3 = models.ImageField(verbose_name='写真３',blank=True,null=True)
    t013_fd06_createdata = models.DateTimeField(verbose_name='作成日時',auto_now_add=True,)  
    t013_fd07_updatedata = models.DateTimeField(verbose_name='更新日時',auto_now=True,blank=True, null=True)  

    class Meta:
        db_table = 'T013_blog'
        verbose_name_plural = 'ブログテーブル'

        def __str__(self):
            return self.t013_fd01_title