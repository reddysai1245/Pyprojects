from django.shortcuts import render
from django.http import HttpResponse
import win10toast
from datetime import datetime
import sqlite3
import time
import multiprocessing
import os
import platform


def conn(dat, tim, tskt, tskc):
    con = sqlite3.connect('tasks.db')
    c = con.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS tasks (title text,content text,time text,date text)")
    c.execute("INSERT INTO tasks VALUES(:tskt,:tskc,:tim,:dat)",
              {
                  'tskt': tskt,
                  'tskc': tskc,
                  'tim': tim,
                  'dat': dat
              })
    con.commit()
    con.close()


def notifyy(tt, cc):
    toaster = win10toast.ToastNotifier()
    toaster.show_toast(tt, cc, duration=10)


# Create your views here.

def hel():
    os.system("py retrive.py")
    return None
def hi(request):

    return render(request, 'finale/hi.html', {'name': 'aditya'})


def add(request):
    dat = str(request.POST["dat"])
    tim = str(request.POST["tim"])
    tskt = str(request.POST["taskt"])
    tskc = str(request.POST["taskc"])
    op = str(request.POST['exampleRadios'])
    tim = tim+":00"
    if op == 'shutdown':
        tskt = op
    conn(dat, tim, tskt, tskc)
    p1=multiprocessing.Process(target=hel)
    p1.start()
    return render(request, 'finale/hi.html', {'name': 'task added'})


