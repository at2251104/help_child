
# member/adapter.py

from allauth.account.adapter import DefaultAccountAdapter
from .models import *

class AccountAdapter(DefaultAccountAdapter):

    def save_user(self, request, user, form, commit=True):
        """
        This is called when saving user via allauth registration.
        We override this to set additional data on user object.
        """
        # Do not persist the user yet so we pass commit=False
        # (last argument)
        user = super(AccountAdapter, self).save_user(request, user, form, commit=False)
        #user.userType = form.cleaned_data.get('userType')
        user.userType = UserType(request.POST['userType'])

        if not user.userType:
            user.userType = UserType(USERTYPE_DEFAULT) # デフォルトのユーザ種別を設定

        # ユーザIDを取得するために一旦保存する
        user.save()

        if int(user.userType.id) == USERTYPE_SUPPLIER:
            # 保護者
            supplier = T002Parents()
            supplier.user_id = user.id
            supplier.companyName = request.POST['notification']
            supplier.save()
        else:
            # 保育士
            user.userType = UserType(USERTYPE_BUYER)
            buyer = T003Childminder()
            buyer.user_id = user.id
            buyer.nearestStation = request.POST.get('class_id', False)
            buyer.save()