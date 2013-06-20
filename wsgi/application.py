import os

html = """<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>Python 2.7.5 + Nginx + uWSGI on OpenShift</title>
<style>
body {
    background: #333;
    color: rgb(153, 153, 153);
    width: 800px;
    margin: auto;
    font-family: "Helvetica Neue",Helvetica,"Liberation Sans",Arial,sans-serif;
    font-size: 12px;
}
.box {
    background: rgba(0, 0, 0, 0.15);
    margin: 2em;
    padding: 1em;
}
.box > div {
    border-bottom: 1px solid rgba(0, 0, 0, 0.15);
    padding: 0.5em;
}
</style>
</head>
<body>
<div class="box">
<h1>Python 2.7.5 + Nginx + uWSGI</h1>
<h2>Your application environment</h2>
%s
</div>
</body>
</html>
"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    lines = []
    for k, v in os.environ.items():
        if "PASSW" not in k:  # don't show passwords
            lines.append("<div><b>{0}</b> = {1}</div>".format(k, v))
    vals = ''.join(lines)
    return html % vals


if __name__ == "__main__":
    from wsgiref.simple_server import make_server
    make_server('127.0.0.1', 80, application).serve_forever()
