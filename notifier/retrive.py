import sqlite3
from datetime import *
import platform, os
import time
import win10toast



def delnotify(tt, tod):
    con = sqlite3.connect('tasks.db')
    c = con.cursor()
    c.execute("DELETE FROM tasks WHERE date = :tod AND time = :tt",
              {
                  'tod': tod,
                  'tt': tt
              })
    print("deleted"+tt)
    con.commit()
    con.close()
    return 0


def shutdown():
    name = platform.system()
    if name == 'Windows':
        print("shut")
        os.shutdown("shutdown /s /t 1")
    elif name == 'Mojav':
        os.system("shutdown -h now")
    elif name == 'Linux':
        os.system("shutdown -i")


def retrive():
    con = sqlite3.connect('tasks.db')
    c = con.cursor()
    tod = date.today()
    tod = str(tod)
    now = datetime.now().time()
    timee = []
    c.execute("SELECT time FROM tasks WHERE date = :tod",
              {
                  'tod': tod
              })
    t = c.fetchall()
    for i in t:
        timee.append(str(i[0]))
    if len(timee) != 0:
        timee.sort()
        for i in range(len(timee)):
            timee[i] = datetime.strptime(timee[i], '%H:%M:%S').time()
        for j in range(len(timee)):
            if timee[j] < now:
                tt = timee[j].strftime("%H:%M:%S")
                c.execute("SELECT title,content FROM tasks WHERE date = :tod AND time= :tt",
                          {
                              'tod': tod,
                              'tt': tt
                          })
                t = c.fetchall()
                cont = ''
                titl = ''
                for k in t:
                    titl += str(k[0])
                    cont += str(k[1])
                toaster = win10toast.ToastNotifier()
                toaster.show_toast("missed reminders", titl+cont, duration=30)
                print("toasted")
                delnotify(tt, tod)
            elif now < timee[j]:
                nows = now.strftime("%H:%M:%S")
                tims = timee[j].strftime("%H:%M:%S")
                tdif = datetime.strptime(tims, "%H:%M:%S") - datetime.strptime(nows,"%H:%M:%S")
                time.sleep(tdif.seconds)
                tt = timee[j].strftime("%H:%M:%S")
                c.execute("SELECT title,content FROM tasks WHERE date = :tod AND time= :tt",
                          {
                              'tod': tod,
                              'tt': tt
                          })
                t = c.fetchall()
                print("you have {} notifications today so please don't close the application".format(t))
                cont = ''
                titl=''
                for k in t:
                    titl += str(k[0])
                    cont += str(k[1])
                toaster = win10toast.ToastNotifier()
                toaster.show_toast(titl, cont, duration=5)
                time.sleep(2)
                '''if titl == 'shutdown' or titl == 'Shutdown' or titl == 'SHUTDOWN':
                    shutdown()
                    print('shutdown')'''
                print("toasted")
                
                delnotify(tt, tod)
    else:
        toaster = win10toast.ToastNotifier()
        toaster.show_toast("reminders", "No Reminders Today ;.)", duration=30)
        quit()

    con.commit()
    con.close()


retrive()
