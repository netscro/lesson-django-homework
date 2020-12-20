import logging

from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin


class LogMiddleware(MiddlewareMixin):

    def process_request(self, request):
        logging.basicConfig(level=logging.INFO)
        resolved_path_info = resolve(request.path_info)
        logging.info(f'Request --> {request}; View name --> '
                     f'{resolved_path_info.view_name}; '
                     f'route --> {resolved_path_info.route}')

    def process_response(self, request, response):
        logging.info(f'For request --> {request}; Response --> {response}')
        return response

