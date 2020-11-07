#!/usr/bin/env python

from werkzeug.wrappers import Request, Response

@Request.application
def application(request):
    return Response(request.cookies['__Secure-Name'])

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, application, ssl_context=('./ssl.cert','./ssl.key'))
