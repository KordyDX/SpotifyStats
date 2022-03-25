#Prerequisities: Globally installed Python 3.10+, Matplotlib (Library for graph generating)
import base64
import json
import os
from collections import Counter
from tkinter import *

from pylab import rcParams
import matplotlib.pyplot as plt

#JSON TO PY DICTIONARY CONVERSION
f = open ("endsong.json", 'r', encoding='utf8')
dicty = json.loads(f.read())
f.close()

#Iterates dictionary and saves all wanted keys with values into separate lists 
# + names of platforms are shortened to 1 word
def save_data():
    artists_list = []
    days_list = []
    track_list = []
    platform_list = []

    for dictionary in dicty:
        if 'master_metadata_album_artist_name' in dictionary:
            if dictionary['master_metadata_album_artist_name']:
                artists_list.append(dictionary['master_metadata_album_artist_name'])

    for dictionary in dicty:
        if 'ts' in dictionary:
            if dictionary['ts'][0:10]:
                days_list.append(dictionary['ts'][0:10])

    for dictionary in dicty:
        if 'master_metadata_track_name' in dictionary:
            if dictionary['master_metadata_track_name']:
                track_list.append(dictionary['master_metadata_track_name'])

    for dictionary in dicty:
        if 'platform' in dictionary:
            if dictionary['platform']:
                platform_list.append(dictionary['platform'])

    for i in range(len(platform_list)): platform_list[i] = (" ".join(platform_list[i].split()[:1]))

    return [artists_list, days_list, track_list, platform_list]
#Finds each list's most reoccuring values (max 5 values total) and stores then in a list with their occurence count 
def most_frequent(List):
    occurence_count = Counter(List)
    occurence_count = occurence_count.most_common(5)
    name = []
    value = []
    for i in range(0, len(occurence_count)):
        name.append(occurence_count[i][0])
    for i in range(0, len(occurence_count)):
        value.append(occurence_count[i][1])
    return [name, value]
#Method to generate a graph from most_frequents values using matplotlib
def stat_window(i):
    rcParams["toolbar"] = "None"
    plt.figure(switch(i))
    plt.barh(most_frequent(save_data()[i])[0], most_frequent(save_data()[i])[1])
    plt.title(switch(i))
    plt.xlabel("Streams")
    plt.gca().invert_yaxis()
    plt.bar_label(plt.gca().containers[0])
    plt.show()
#C like switch method in Python (Works only in Python 3.10+)
def switch(n):
    match n:
        case 0:
            return "Top artists by streams"
        case 1:
            return "Most streams in a day"
        case 2:
            return "Most played songs by streams"
        case 3:
            return "Most used platforms by streams"
#Tkinter window for user interaction
def tkwindow():
    root = Tk()
    root.geometry("300x200")
    root.configure(background="#189e3d")
    root.title("Spotify Stats")
    root.resizable(False, False)
    icon = \
    """
    AAABAAEAICAAAAEAIACoEAAAFgAAACgAAAAgAAAAQAAAAAEAIAAAAAAAABAAAMMOAADDDgAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEGhHQBDoh4EP58bKz6fGW4+nxmu
    Pp4Z2z2eGPM9nhj+PZ4Y/j2eGPM+nhnbPp8Zrj6fGW4/nxsrQ6IeBEGhHAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEGhHQBDoh8EP58aOD6f
    GZk9nhjgPZ4Y+z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y+z2eGOA+nxmZP58a
    OEOiHwRBoR0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEyoKgA7nRcA
    QKAbGz6fGYs9nhjqPZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89
    nhj/PZ4Y/z2eGP89nhjqPp8Zi0CgGxs8nRcATKgpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AABDoh8ANpoPAD+fGjc9nhnDPZ4Y/j2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y
    /z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj+PZ4Zwz+fGjc2mQ8AQ6IfAAAAAAAAAAAA
    AAAAAAAAAAAAAAAARKIfADaZEQA/nhpDPZ4Y2j2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89
    nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y2j+e
    GkM2mRIARKIfAAAAAAAAAAAAAAAAAEimJAA9nhgAP58aNz2eGNo9nhj/PZ4Y/z2eGP89nhj/PZ4Y
    /z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/
    PZ4Y/z2eGP89nhj/PZ4Y2j+fGjc9nhgASKUkAAAAAAAAAAAAP58aAD+gGxs+nhnDPZ4Y/z2eGP89
    nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2e
    GP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/Pp4Zwz+gGxs/nxoAAAAAAEOiHgBJpiQDPp8Z
    iz2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/
    PZ4Y/z2eGP89nhj/PZ4Y/z6gGP8+oBj/PZ8Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/Pp8Zi0mmJAND
    oh4APp8ZAD+fGjk9nhjqPZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2e
    GP89nhj/PZ4Y/z2eGP89nhj/PZ8Y/z6gGP89nRj/L3oT/yFTDf81iBX/PZ8Y/z2eGP89nhj/PZ4Y
    /z2eGP89nhjqP58aOT6fGQBGpSMDPp8ZmD2eGP89nhj/PZ4Y/z2eGP89nhj/O5gX/zyaGP8+nxj/
    PqEY/z6hGP8+oBj/PqAY/z6gGP8+oRj/PqEY/z2eGP85kxf/LXUS/xk/Cv8FDQL/AAAA/yVeD/8+
    oBj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP8+nxmYRqUjAz+gGis9nhjfPZ4Y/z2eGP89nhj/PqAY/zOD
    FP8RKwf/Ei8I/xxJDP8kXg//Km0R/y52Ev8veBP/LnYS/ypsEf8jWg7/GUAK/w0gBf8CBgH/AAAA
    /wYOAv8bRgv/N44W/z2fGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGN8/oBorPp8abj2eGPs9nhj/
    PZ4Y/z2eGP8+oBj/MHwT/wgTA/8AAQD/AAAA/wAAAP8AAQD/AQMB/wIEAf8BAwH/AAEA/wAAAP8A
    AAD/AgUB/wweBf8dSwz/Mn8U/z2dGP8+oRj/PqAY/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y+z6f
    Gm4+nxmtPZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nBj/NIYV/ypsEf8hVA3/GUAK/xQyCP8QKgf/DycG
    /xAqB/8UMgj/GkIL/yNaDv8udxL/OJIW/z2fGP8+oRj/PZ4Y/zODFP8tdBL/O5gX/z2eGP89nhj/
    PZ4Y/z2eGP89nhj/Pp8ZrT6eGdo9nhj/PZ4Y/z2eGP89nhj/PZ4Y/z6gGP8/ohn/P6IZ/z6hGP89
    nxj/PJwY/zuZF/87mBf/O5kX/zycGP89nxj/PqEZ/z+iGf8+oRn/PJwY/zODFP8dSwz/BxID/wIF
    Af8oZhD/PqAY/z2eGP89nhj/PZ4Y/z2eGP8+nhnaPZ4Y8z2eGP89nhj/PZ4Y/z2eGP89nhj/NIYV
    /yxwEv81hxX/OpcX/z2dGP8+oBj/PqEY/z6hGP8+oBj/PZ8Y/zycGP85lBf/MoIU/yZjEP8WNwn/
    BhAD/wAAAP8AAAD/BAoC/yptEf8+oBj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGPM9nhj+PZ4Y/z2eGP89
    nhj/PZ8Y/zqVF/8QKAf/AQIA/wcSA/8PJgb/FzoJ/x1JDP8gUQ3/IFMN/x9ODP8aRAv/FDMI/wwg
    Bf8FDQL/AQIA/wAAAP8AAAD/AwgB/xMwCP8tcxL/PJwY/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y
    /j2eGP49nhj/PZ4Y/z2eGP89nhj/OpcX/xQzCP8BAgD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/
    AAAA/wAAAP8AAAD/AAAA/wAAAP8CBQH/ChkE/xlBCv8tdBL/O5gX/z6gGP8+oBj/PqEY/z2fGP89
    nhj/PZ4Y/z2eGP89nhj+PZ4Y8z2eGP89nhj/PZ4Y/z2eGP89nxj/OJAW/yptEf8eTAz/FDMI/w0i
    Bf8JGAT/BxMD/wcRA/8IFAP/ChoE/w8mBv8WOQn/IFMN/y1zEv83jhb/PZ4Y/z6hGP8+oRj/PJsY
    /y54E/8paRD/OZMW/z2fGP89nhj/PZ4Y/z2eGPM+nhnaPZ4Y/z2eGP89nhj/PZ4Y/z6fGP8+ohj/
    P6MZ/z6hGP88nBj/OpUX/zePFv82ihX/NYkV/zaMFf84kRb/O5cX/z2dGP8+oRj/PqIZ/z6hGP8+
    oBj/OpYX/y10Ev8XOgn/BAoC/wAAAP8dTAz/PZ4Y/z2eGP89nhj/Pp4Z2j6fGa09nhj/PZ4Y/z2e
    GP89nhj/M4QU/ydkEP8wehP/OJAW/zyaGP89nxj/PqEY/z6iGf8/ohn/PqIZ/z6hGP8+nxj/PJwY
    /zqWF/81iRX/LHES/x5ODP8PJQb/AwgB/wAAAP8AAAD/AAAA/xlACv89nhj/PZ4Y/z2eGP8+nxmt
    Pp8abj2eGPs9nhj/PZ8Y/ziSFv8OJQb/AAAA/wMJAf8KGgT/Ei0H/xk+Cv8dSwz/IFMN/yFWDv8h
    VA3/H04M/xtEC/8VNQj/DiQG/wcSA/8CBQH/AAAA/wAAAP8AAAD/AAAA/wQKAv8XOwr/NIgV/z2f
    GP89nhj/PZ4Y+z6fGm4/oBorPZ4Y3z2eGP89nxj/N44W/wsbBP8AAAD/AAAA/wAAAP8AAAD/AAAA
    /wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AQMB/wkXBP8aQgr/
    L3kT/zybGP8+nxj/PZ4Y/z2eGP89nhjfP6AaK0elIwM+nxmYPZ4Y/z2eGP89nhj/LXMS/xc5Cf8L
    HAX/BQwC/wEEAf8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP8AAAD/AQIA/wMHAf8HEwP/DyYG/xtF
    C/8pahH/NowV/z2eGP8+oBj/PZ4Y/z2eGP89nhj/PZ4Y/z6fGZhGpSMDPp8ZAD+fGjk9nhjqPZ4Y
    /z2eGP8+oBj/PZ0Y/ziRFv8ygRT/K28R/yZgD/8hVQ3/H04M/x1LDP8eTQz/IFIN/yRcDv8paRD/
    L3kT/zWJFf86lxf/PZ8Y/z6hGP89nxj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhjqP58aOT6fGQBD
    oh4ASaYkAz6fGYs9nhj/PZ4Y/z2eGP89nhj/PZ8Y/z6gGP8+oRj/PqEY/z6hGP8+oBj/PqAY/z6g
    GP8+oBj/PqEY/z6hGP8+oBj/PZ8Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y
    /z6fGYtJpiQDQ6IeAAAAAAA/nxoAP6AbGz6eGcM9nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/
    PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89
    nhj/PZ4Y/z2eGP8+nhnDP6AbGz+fGgAAAAAAAAAAAEilJAA9nhgAP58aNz2eGNk9nhj/PZ4Y/z2e
    GP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y
    /z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y2j+fGjc9nhgASKUkAAAAAAAAAAAAAAAAAESiHwA3mhIA
    P54aQz2eGNo9nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89
    nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGNo/nhpDNpkRAESiHwAAAAAAAAAAAAAA
    AAAAAAAAAAAAAEOiHwA2mg8AP58aNz2eGcM9nhj+PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y
    /z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP49nhnDP58aNzaaDwBDoh8A
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEyoKgA8nRYAQKAbGz6fGYs9nhjqPZ4Y/z2eGP89
    nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhjqPp8Zi0Cg
    Gxs8nRcATKgpAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBoR0AQ6If
    BD+fGjg+nxmZPZ4Y4D2eGPs9nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGP89nhj/PZ4Y/z2eGPs9nhjg
    Pp8ZmT+fGjhDoh8EQaEdAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAQaEcAEOiHgQ/nxsrPp8Zbj6fGa4+nhnaPZ4Y8z2eGP49nhj+PZ4Y8z6e
    Gdo+nhmuPp8Zbj+fGytDoh4EQaEcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA/4AB
    //4AAH/8AAA/+AAAH/AAAA/gAAAHwAAAA4AAAAGAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAABgAAAAcAAAAPgAAAH8AAAD/gAAB/8
    AAA//gAAf/+AAf8=
    """
    icondata = base64.b64decode(icon)
    tempFile = "icon.ico"
    iconfile = open(tempFile, "wb")
    iconfile.write(icondata)
    iconfile.close()
    root.wm_iconbitmap(tempFile)
    os.remove(tempFile)

    button1 = Button(root, text="Artists", height=1, width=7, command=lambda: stat_window(0))
    button1.place(relx=0.4, rely=0.4, anchor=CENTER)
    
    button2 = Button(root, text="Days", height=1, width=7, command=lambda: stat_window(1))
    button2.place(relx=0.6, rely=0.4, anchor=CENTER)
    
    button3 = Button(root, text="Tracks", height=1, width=7, command=lambda: stat_window(2))
    button3.place(relx=0.4, rely=0.6, anchor=CENTER)
    
    button4 = Button(root, text="Platform", height=1, width=7, command=lambda: stat_window(3))
    button4.place(relx=0.6, rely=0.6, anchor=CENTER)
    root.mainloop()
#Final method call
tkwindow()