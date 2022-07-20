from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            obj_user = obj.user
        except AttributeError:
            obj_user = obj.video.user
        if request.user == obj_user:
            return super().has_permission(request, view)
