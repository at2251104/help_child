from django.db import models
from django.db.models.deletion import CASCADE


class T001Children(models.Model):
    t001_pk01_children_id = models.CharField(verbose_name='園児ID',db_column='T001_PK01_children-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t001_fk01_class_id = models.ForeignKey('T004Class', models.DO_NOTHING, verbose_name='クラスID',db_column='T001_FK01_class-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t001_fk02_parents_id = models.ForeignKey('T002Parents', models.DO_NOTHING,verbose_name='保護者ID', db_column='T001_FK02_parents-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t001_fd01_name = models.CharField(verbose_name='氏名',db_column='T001_FD01_name', max_length=20)  # Field name made lowercase.
    t001_fd02_birthday = models.DateField(verbose_name='誕生日',db_column='T001_FD02_birthday')  # Field name made lowercase.
    t001_fd03_address = models.CharField(verbose_name='住所',db_column='T001_FD03_address', max_length=50)  # Field name made lowercase.
    t001_fd04_createdata = models.DateTimeField(verbose_name='作成日時',db_column='T001_FD04_createdata')  # Field name made lowercase.
    t001_fd05_updatedata = models.DateTimeField(verbose_name='更新日時',db_column='T001_FD05_updatedata', blank=True, null=True)  # Field name made lowercase.
    t001_fd06_sex = models.IntegerField(verbose_name='性別',db_column='T001_FD06_sex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T001_children'
        verbose_name_plural="園児テーブル",

    def __str__(self):
        return self.t001_fd01_name


class T002Parents(models.Model):
    t002_pk01_parents_id = models.CharField(db_column='T002_PK01_parents-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t002_fd01_password = models.CharField(db_column='T002_FD01_password', max_length=100)  # Field name made lowercase.
    t002_fd02_name = models.CharField(db_column='T002_FD02_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t002_fd03_birthday = models.DateField(db_column='T002_FD03_birthday')  # Field name made lowercase.
    t002_fd04_address = models.CharField(db_column='T002_FD04_address', max_length=100)  # Field name made lowercase.
    t002_fd05_mailadd = models.CharField(db_column='T002_FD05_mailadd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t002_fd06_notification = models.BooleanField(db_column='T002_FD06_notification', blank=True, null=True)  # Field name made lowercase.
    t002_fd07_telephonenum = models.CharField(db_column='T002_FD07_telephonenum', max_length=20)  # Field name made lowercase.
    t002_fd08_createdata = models.DateTimeField(db_column='T002_FD08_createdata')  # Field name made lowercase.
    t002_fd09_updatedata = models.DateTimeField(db_column='T002_FD09_updatedata', blank=True, null=True)  # Field name made lowercase.
    t002_fd10_sex = models.IntegerField(db_column='T002_FD10_sex')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T002_parents'

    def __str__(self):
        return self.t002_fd02_name


class T003Childminder(models.Model):
    t003_fk01_class_id = models.ForeignKey('T004Class', models.DO_NOTHING, db_column='T003_FK01_class-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t003_fd01_password = models.CharField(db_column='T003_FD01_password', max_length=100)  # Field name made lowercase.
    t003_fd02_name = models.CharField(db_column='T003_FD02_name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    t003_fd03_birthday = models.DateField(db_column='T003_FD03_birthday')  # Field name made lowercase.
    t003_fd04_address = models.CharField(db_column='T003_FD04_address', max_length=100)  # Field name made lowercase.
    t003_fd05_mailadd = models.CharField(db_column='T003_FD05_mailadd', max_length=255, blank=True, null=True)  # Field name made lowercase.
    t003_fd06_administator = models.BooleanField(db_column='T003_FD06_administator')  # Field name made lowercase.
    t003_fd07_telephonenum = models.CharField(db_column='T003_FD07_telephonenum', max_length=20)  # Field name made lowercase.
    t003_fd08_createdata = models.DateTimeField(db_column='T003_FD08_createdata')  # Field name made lowercase.
    t003_fd09_updatedata = models.DateTimeField(db_column='T003_FD09_updatedata', blank=True, null=True)  # Field name made lowercase.
    t003_fd10_sex = models.IntegerField(db_column='T003_FD10_sex')  # Field name made lowercase.
    t003_fk02_childminder_id = models.CharField(db_column='T003_FK01_childminder-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'T003_childminder'
    
    def __str__(self):
        return self.t003_fd02_name


class T004Class(models.Model):
    t004_pk01_class_id = models.CharField(db_column='T004_PK01_class-id', primary_key=True, max_length=3)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t004_fd01_class_name = models.CharField(db_column='T004_FD01_class-name', max_length=20)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t004_fd02_year = models.IntegerField(db_column='T004_FD02_year')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T004_class'

    def __str__(self):
        return self.t004_fd01_class_name


class T005Kindergaten(models.Model):
    t005_pk01_childen_id = models.OneToOneField('T001Children', on_delete=models.CASCADE,db_column='T005_PK01_childen-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t005_fd01_date = models.DateField(db_column='T005_FD01_date', blank=True, null=True)  # Field name made lowercase.
    t005_fd02_school_time = models.TimeField(db_column='T005_FD02_school-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t005_fd03_exit_time = models.TimeField(db_column='T005_FD03_exit-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t005_fd04_status = models.IntegerField(db_column='T005_FD04_status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T005_kindergaten'

    def __str__(self):
        return str(self.t005_pk01_childen_id)


class T006Message(models.Model):
    t006_pk01_message_id = models.CharField(db_column='T006_PK01_message-id', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t006_fk01_room_id = models.ForeignKey('T011Room', models.DO_NOTHING,db_column='T006_FK01_room-id', max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t006_fd01_send_id = models.CharField(db_column='T006_FD01_send-id', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t006_fd02_contents = models.CharField(db_column='T006_FD02_contents', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t006_fd03_datetime = models.DateTimeField(db_column='T006_FD03_datetime')  # Field name made lowercase.
    

    class Meta:
        managed = False
        db_table = 'T006_message'

    def __str__(self):
        return self.t006_pk01_message_id


class T007Contactbook(models.Model):
    t007_pk01_contactbook_id = models.CharField(db_column='T007_PK01_contactbook-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fk02_childminder_id = models.ForeignKey(T003Childminder, models.DO_NOTHING, db_column='T007_FK02_childminder-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fk01_children_id = models.ForeignKey(T001Children, models.DO_NOTHING, db_column='T007_FK01_children-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd13_updatedata = models.DateTimeField(db_column='T007_FD13_updatedata')  # Field name made lowercase.
    t007_fd12_temperature = models.FloatField(db_column='T007_FD12_temperature', blank=True, null=True)  # Field name made lowercase.
    t007_fd11_temperature_time = models.TimeField(db_column='T007_FD11_temperature-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd10_bathing = models.BooleanField(db_column='T007_FD10_bathing', blank=True, null=True)  # Field name made lowercase.
    t007_fd09_defecation_times = models.IntegerField(db_column='T007_FD09_defecation-times', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd08_defecation_status = models.CharField(db_column='T007_FD08_defecation-status', max_length=10, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd07_mood = models.CharField(db_column='T007_FD07_mood', max_length=10, blank=True, null=True)  # Field name made lowercase.
    t007_fd06_wakeup_time = models.TimeField(db_column='T007_FD06_wakeup-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd05_bed_time = models.TimeField(db_column='T007_FD05_bed-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd04_meal_contents = models.CharField(db_column='T007_FD04_meal-contents', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd03_meal_time = models.TimeField(db_column='T007_FD03_meal-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t007_fd02_infomation = models.CharField(db_column='T007_FD02_infomation', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t007_fd01_date = models.DateField(db_column='T007_FD01_date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T007_contactbook'

    def __str__(self):
        return self.t007_pk01_contactbook_id


class T008Schedule(models.Model):
    t008_pk01_schedule_id = models.CharField(db_column='T008_PK01_schedule-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t008_fk01_class_id = models.ForeignKey(T004Class, models.DO_NOTHING, db_column='T008_FK01_class-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t008_fd01_event = models.CharField(db_column='T008_FD01_event', max_length=100)  # Field name made lowercase.
    t008_fd02_remarks = models.CharField(db_column='T008_FD02_remarks', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t008_fd03_date = models.DateField(db_column='T008_FD03_date')  # Field name made lowercase.
    t008_fd04_updatedata = models.DateTimeField(db_column='T008_FD04_updatedata')  # Field name made lowercase.
    t008_fd05_createdata = models.DateTimeField(db_column='T008_FD05_createdata', blank=True, null=True)  # Field name made lowercase.
    t008_fd06_time = models.TimeField(db_column='T008_FD06_time', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T008_schedule'

    def __str__(self):
        return self.t008_fd01_event


class T010Playset(models.Model):
    t010_pk01_playset_id = models.CharField(db_column='T010_PK01_playset-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd01_playset_name = models.CharField(db_column='T010_FD01_playset-name', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd02_distance_a = models.FloatField(db_column='T010_FD02_distance-a')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd03_distance_b = models.FloatField(db_column='T010_FD03_distance-b', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t010_fd04_distance_c = models.FloatField(db_column='T010_FD04_distance-c')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'T010_playset'

    def __str__(self):
        return self.t010_fd01_playset_name

class T009Position(models.Model):
    t009_pk01_children_id = models.OneToOneField(T001Children, on_delete=models.CASCADE, db_column='T009_PK01_children-id', primary_key=True, max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_pk02_datetime = models.DateTimeField(db_column='T009_PK02_datetime',)  # Field name made lowercase.
    t009_fk01_playset_id = models.ForeignKey(T010Playset, models.DO_NOTHING, db_column='T009_FK01_playset-id', max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_fd01_distance_a = models.FloatField(db_column='T009_FD01_distance-a')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_fd02_distance_b = models.FloatField(db_column='T009_FD02_distance-b')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t009_fd03_distance_c = models.FloatField(db_column='T009_FD03_distance-c')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'T009_position'
        unique_together = (('t009_pk01_children_id', 't009_pk02_datetime'),)

    def __str__(self):
        return self.t009_pk01_children_id


class T011Room(models.Model):
    t011_pk01_room_id = models.CharField(db_column='T011_PK01_room-id', primary_key=True, max_length=100)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t011_fk01_parents_id = models.ForeignKey(T002Parents, models.DO_NOTHING, db_column='T011_FK01_parents-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t011_fk02_chilminder_id = models.ForeignKey(T003Childminder, models.DO_NOTHING, db_column='T011_FK02_chilminder-id', max_length=5)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'T011_room'

    def __str__(self):
        return self.t011_pk01_room_id


class T012Contactbooktem(models.Model):
    t012_pk01_contactbook_id = models.CharField(db_column='T012_PK01_contactbook-id', primary_key=True, max_length=10)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fk01_childminder_id = models.ForeignKey(T003Childminder, models.DO_NOTHING, db_column='T012_FK01_childminder-id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd01_date = models.DateField(db_column='T012_FD01_date', blank=True, null=True)  # Field name made lowercase.
    t012_fd02_information = models.CharField(db_column='T012_FD02_information', max_length=200, blank=True, null=True)  # Field name made lowercase.
    t012_fd03_mealtime = models.TimeField(db_column='T012_FD03_mealtime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    t012_fd04_meal_contents = models.CharField(db_column='T012_FD04_meal-contents', max_length=100, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd05_bed_time = models.TimeField(db_column='T012_FD05_bed-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd06_wakeup_time = models.TimeField(db_column='T012_FD06_wakeup-time', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    t012_fd07_updatedata = models.DateTimeField(db_column='T012_FD07_updatedata')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T012_contactbooktem'

    def __str__(self):
        return self.t012_pk01_contactbook_id