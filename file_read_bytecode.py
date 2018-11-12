import os
import time
import base64


def multipart_form_post_upload(filepath):
    newline = '\r\n'
    filename = os.path.basename("file1.pdf")
    print("@@@@@@@@@filename" + str(filename))
    print("@@@@@@@@@@filepath" + str(filepath))
    data = []
    headers = {}
    boundary = '----------%d' % int(time.time())
    headers['content-type'] = 'multipart/form-data; boundary=%s' % boundary
    data.append('--%s' % boundary)
    data.append('Content-Disposition: form-data; name="%s"; filename="%s"' % ('File1', filename))
    data.append('Content-Type:')
    data.append('')
    with open(filepath, 'rb') as imageFile:
        contents = base64.b64encode(imageFile.read())
        print(contents)
    data.append(contents.decode('ASCII'))
    data.append('--%s--' % boundary)
    data.append('')
    print(data)
    data_str = newline.join(data)
    headers['content-length'] = len(data_str)

multipart_form_post_upload("E:\TestScripts\DOC180905-0001.jpg")