#!/usr/bin/python3

print('content-type: text/html')
print('Access-Control-Allow-Origin: *')
print()

import cgi, sys, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

sys.path.insert(0, os.getcwd())

message = None
if 'filename' in form:
    fileitem = form['filename']
    fn = os.path.basename(fileitem.filename)
    open('/var/www/cgi-bin/' + fn, 'wb').write(fileitem.file.read())
    message = 'The file "' + fn + '" was uploaded successfully'
else:
    message = 'No file was uploaded'
replyhtml = """
<html>
<body>
<p>%s</p>
</body>
</html>
"""
print(replyhtml % message)
