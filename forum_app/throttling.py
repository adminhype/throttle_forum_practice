from rest_framework.throttling import UserRateThrottle


class PostThrottle(UserRateThrottle):
    scope = 'posts'

    def allow_request(self, request, view):
        if request.method == 'POST':
            return super().allow_request(request, view)
        return True


class CommentThrottle(UserRateThrottle):
    scope = 'comments'

    def allow_request(self, request, view):
        if request.method == 'POST':
            return super().allow_request(request, view)
        return True
