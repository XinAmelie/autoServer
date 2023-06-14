from django.utils.deprecation import MiddlewareMixin


# 全局关闭csrf_token的认证
class NotUseCsrfTokenMiddlewareMixin(MiddlewareMixin):

    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)
