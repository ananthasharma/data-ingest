from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from services.models import (UserRoleAssociation)

class HttpHeaderAuthentication(authentication.BaseAuthentication):
    
    def do_auth(self, user_unumber):
        # check database
        role_ids = UserRoleAssociation.objects.filter(status__exact='Y').filter(user__exact=user_unumber).all()
        print(f"there are {len(role_ids)} roles")
        return role_ids

    
    def authenticate(self, request):
        print("Auth service invoked")
        user_id = request.headers.get('USER-ID')
        print(f"privileges for user_id {user_id}")
        role_ids = self.do_auth(user_id)
        print(f"found {len(role_ids)} privileges for user_id {user_id}")

        u = User()
        u.Meta.groups = role_ids # to set in response headers using myapi.request_control_middleware.AuthMiddleware class

        if(len(role_ids)==0):
            print("no privileges found")
            raise exceptions.AuthenticationFailed('no privileges available')


        return (u, None) # authentication successful