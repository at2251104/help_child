# member/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.db.models.fields import EmailField
from django.utils import timezone
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserType(models.Model):
    """ ユーザ種別 """
    typename = models.CharField(verbose_name='ユーザ種別',
                                max_length=150)

    def __str__(self):
        return f'{self.typename}'

USERTYPE_PARENTS = 200
USERTYPE_CHILDMINDER = 100
USERTYPE_DEFAULT = USERTYPE_PARENTS

class CustomUserManager(BaseUserManager):
    """ 拡張ユーザーモデル向けのマネージャー """

    use_in_migrations = True
    ordering = ('email',)

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self ,email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('ユーザ名は名前をローマ字で入力してください。この項目は必須です。'),
        default='01',
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )

    userType = models.ForeignKey(UserType,
                                verbose_name='ユーザ種別',
                                null=True,
                                blank=True,
                                on_delete=models.PROTECT)

    email = models.EmailField(('メールアドレス'),primary_key=True, unique=True,help_text=_('ログイン時に必須'))
    last_name = models.CharField(('姓'), max_length=150)
    first_name = models.CharField(('名'),max_length=150)
    last_name_kana = models.CharField(('姓（かな）'), max_length=150)
    first_name_kana = models.CharField(('名（かな）'),max_length=150)
    sex = models.CharField(('性別'), default='男性',max_length=4, choices=(('男性','男性'), ('女性','女性')))
    birthday = models.DateField(('生年月日'), blank=True, null=True)
    postal_code = models.CharField(('郵便番号（ハイフンなし）'), max_length=7, blank=True, null=True)
    address = models.CharField(('住所'), max_length=50, blank=True, null=True)
    tel = models.CharField(('電話番号（ハイフンなし）'), max_length=11, blank=True, null=True)

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'custom_user'
        verbose_name = ('user')
        verbose_name_plural = ('ユーザー')


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.last_name, self.first_name)
        return full_name.strip()

    def get_full_name_kana(self):
        full_name_kana = '%s %s' % (self.last_name_kana, self.first_name_kana)
        return full_name_kana.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.username

class T002Parents(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                related_name='detail_supplier',
                                help_text=_('登録したユーザ名を選択'),
                                on_delete=models.CASCADE)

    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{self.user} - {self.id}'

    class Meta:
        verbose_name_plural="保護者テーブル"

class T003Childminder(models.Model):
    user = models.OneToOneField(CustomUser,
                                unique=True,
                                related_name='detail_buyer',
                                help_text=_('登録したユーザ名を選択'),
                                on_delete=models.CASCADE)
    # 保育士向けの項目
    class_id = models.ForeignKey("main.T004Class",
                                max_length=3,
                                default='1', 
                                on_delete=models.CASCADE,
                                verbose_name='クラスID',
                                )

    def __str__(self):
        user = CustomUser.objects.get(pk=self.user_id)
        return f'{self.user} - {self.id} - {self.class_id}'

    class Meta:
        verbose_name_plural="保育士テーブル"

