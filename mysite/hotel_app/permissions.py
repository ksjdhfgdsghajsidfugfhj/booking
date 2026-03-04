from rest_framework import permissions

class CheckStatusUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS: # get, option, head
            return True
        elif request.user.status == 'owmer':
            return True
