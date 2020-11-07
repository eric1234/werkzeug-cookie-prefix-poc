Werkzeug/Flask Cookie Prefix Vulnerability POC
==============================================

I saw a recent issue pop up in the Ruby world where decoding cookie names lead
to a low-level vulnerability due to the trust provided by cookie prefixes. For
more info on the Ruby vulnerability see:

https://hackerone.com/reports/895727

I decided to see what other platforms had this same or similar issue. Although
Flask does not do URL decoding as with the Ruby platform it does unquote both
the cookie name and value.

The spec seems to indicate the value is treated differently by specifying quote
characters, backslash for escaping, octet encodings, etc but the cookie name
is just specified as a simple token.

https://tools.ietf.org/html/rfc6265#section-4.1.1

This unquoting of the cookie name could potentially allow an attacker to bypass
the security provided by the cookie prefix. This POC demonstrates this by
having the `curl` HTTP command line client have two cookies. One insecure,
the other secure. When the server reads the secure cookie it receives the
insecure value.

Executing POC
-------------

I have two versions of the server. One using raw Werkzeug (named `w.py`), the
other using Flask (named `f.py`). Start either one by running the file. It
will boot a HTTP server that returns the value of the secure cookie.

In a separate terminal run `test` and you should see the ensure value returned.
