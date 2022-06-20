from django.shortcuts import render
from django.http import HttpResponse
import os
import socket
import cx_Oracle


def index(request):
    os.environ['TNS_ADMIN'] = '/usr/lib/oracle/18.3/client64/lib/network/admin'
    connection = cx_Oracle.connect('dbfirst', 'ATP_password', 'ATP_alias')

    cursor = connection.cursor()
    data = ''
    for row in cursor.execute("SELECT * FROM dept"):
        print (row)
        data = data + str(row)
    cursor.close()
    connection.commit()
    connection.close()
    data = data[2:len(data)-3]
    final_result = str(data)
    return HttpResponse(final_result)
