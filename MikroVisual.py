
# coding: utf-8

# In[ ]:


#EDIT THREAD PYTHON+ARDUINO
import cv2,serial,numpy as np,time
from threading import *
from queue import *
def video(queue_):
    cv2.namedWindow("preview")
    h = 480
    w = 640
    vc = cv2.VideoCapture(0)
    vc.set(cv2.CAP_PROP_FRAME_WIDTH, w)
    vc.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

    if vc.isOpened(): # coba dapat gambar pertama kali
        rval, frame = vc.read()
    else:
        rval = False  

    def play(listNada,warna):  
        N=[1,2,3,4,5,6,7]
        if warna in listNada[4]:
            queue_.put(str(N[4]).encode())#nada5
            cv2.putText(frame,str(N[4]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        elif warna in listNada[5]: 
            queue_.put(str(N[5]).encode())#nada6
            cv2.putText(frame,str(N[5]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        elif warna in listNada[6]: 
            queue_.put(str(N[6]).encode())#nada7
            cv2.putText(frame,str(N[6]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        elif warna in listNada[0]: 
            queue_.put(str(N[0]).encode())#nada1
            cv2.putText(frame,str(N[0]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        elif warna in listNada[1]: 
            queue_.put(str(N[1]).encode())#nada2
            cv2.putText(frame,str(N[1]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        elif warna in listNada[2]: 
            queue_.put(str(N[2]).encode())#nada3
            cv2.putText(frame,str(N[2]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        elif warna in listNada[3]: 
            queue_.put(str(N[3]).encode())#nada4
            cv2.putText(frame,str(N[3]),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        else:
            return    

    def blokNada():
        f=7
        cv2.rectangle(frame,(0,int(h/2)+50),(int(w/f),int(h/2)-50),(0,255,0),-1)
        cv2.rectangle(frame,(int(w/f),int(h/2)+50),(2*int(w/f),int(h/2)-50),(255,0,0),-1)
        cv2.rectangle(frame,(2*int(w/f),int(h/2)+50),(3*int(w/f),int(h/2)-50),(0,0,255),-1)
        cv2.rectangle(frame,(3*int(w/f),int(h/2)+50),(4*int(w/f),int(h/2)-50),(0,255,255),-1)
        cv2.rectangle(frame,(4*int(w/f),int(h/2)+50),(5*int(w/f),int(h/2)-50),(255,250,0),-1)
        cv2.rectangle(frame,(5*int(w/f),int(h/2)+50),(6*int(w/f),int(h/2)-50),(0,166,255),-1)
        cv2.rectangle(frame,(6*int(w/f),int(h/2)+50),(7*int(w/f),int(h/2)-50),(0,255,187),-1)
        return

    def trackInit():#INISIALISASI TRACK
        def nothing(x):
            pass
        img = np.zeros((10,512,3), np.uint8)
        cv2.namedWindow('image')
        # NADA 1
        cv2.createTrackbar('Nada 1 LOW','image',50,179,nothing)
        cv2.createTrackbar('Nada 1 HIGH','image',70,179,nothing)
        # NADA 2
        cv2.createTrackbar('Nada 2 LOW','image',116,179,nothing)
        cv2.createTrackbar('Nada 2 HIGH','image',134,179,nothing)
        # NADA 3
        cv2.createTrackbar('Nada 3 LOW','image',0,179,nothing)
        cv2.createTrackbar('Nada 3 HIGH','image',16,179,nothing)
        # NADA 4
        cv2.createTrackbar('Nada 4 LOW','image',23,179,nothing)
        cv2.createTrackbar('Nada 4 HIGH','image',41,179,nothing)
        # NADA 5
        cv2.createTrackbar('Nada 5 LOW','image',80,179,nothing)
        cv2.createTrackbar('Nada 5 HIGH','image',100,179,nothing)
        # NADA 6
        cv2.createTrackbar('Nada 6 LOW','image',16,179,nothing)
        cv2.createTrackbar('Nada 6 HIGH','image',23,179,nothing)
        # NADA 7
        cv2.createTrackbar('Nada 7 LOW','image',31,179,nothing)
        cv2.createTrackbar('Nada 7 HIGH','image',40,179,nothing)
        cv2.imshow('image',img)
        return
    def track():#CEK POSISI TRACK
        # POSISI TRACKBAR
        #NADA 1
        n1l = cv2.getTrackbarPos('Nada 1 LOW','image')
        n1h = cv2.getTrackbarPos('Nada 1 HIGH','image')
        #NADA 2
        n2l = cv2.getTrackbarPos('Nada 2 LOW','image')
        n2h = cv2.getTrackbarPos('Nada 2 HIGH','image')
        #NADA 3
        n3l = cv2.getTrackbarPos('Nada 3 LOW','image')
        n3h = cv2.getTrackbarPos('Nada 3 HIGH','image')
        #NADA 4
        n4l = cv2.getTrackbarPos('Nada 4 LOW','image')
        n4h = cv2.getTrackbarPos('Nada 5 HIGH','image')
        #NADA 5
        n5l = cv2.getTrackbarPos('Nada 5 LOW','image')
        n5h = cv2.getTrackbarPos('Nada 5 HIGH','image')
        #NADA 6
        n6l = cv2.getTrackbarPos('Nada 6 LOW','image')
        n6h = cv2.getTrackbarPos('Nada 6 HIGH','image')
        #NADA 7
        n7l = cv2.getTrackbarPos('Nada 7 LOW','image')
        n7h = cv2.getTrackbarPos('Nada 7 HIGH','image')
        return([range(n1l,n1h),range(n2l,n2h),range(n3l,n3h),range(n4l,n4h),range(n5l,n5h),range(n6l,n6h),range(n7l,n7h)])

    i=0
    trackInit()
    while rval:
        i = i if i<w else 0
        #frame=cv2.flip(frame,1)
        x0,x1,y0,y1=i,i,int(h/2)+50,int(h/2)-50
        #blokNada()
        hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        warna=int(np.average(hsv[y1:y0,x0:x1+5,0]))
        #warna=int(hsv[int(h/2),int(w/2),0])
        play(track(),warna)
        #cv2.putText(frame,str(track()),(20,450), cv2.FONT_HERSHEY_SIMPLEX, 0.45,(0,255,0),2,cv2.LINE_AA)
        cv2.putText(frame,str(warna),(50,400), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
        cv2.line(frame,(x0, y0),(x1, y1),(0,125,0),2)#(x1.y1)(x2.y2)=(bawah)(atas)
        #cv2.line(frame,(int(w/2), int(h/2)-50),(int(w/2), int(h/2)+50),(0,255,0),2)#(x1.y1)(x2.y2)=(bawah)(atas)
        cv2.rectangle(frame,(0, y0),(w, y1),(255,0,0),3)##(x1.y1)(x2.y2)=(pojok kiri bawah)(pojok kanan atas)
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        i+=5
        if key == 27: # tekan ESC untuk keluar 
            #rval = False
            break
    cv2.destroyWindow("preview")
    queue_.put(None)


def uno(queue_):
    ino=serial.Serial('/dev/ttyACM0',9600)   
    while True:
        data = queue_.get()
        if data is None:
            break
        ino.write(data)#nada1
        #time.sleep(10)
        
queue_ = Queue()
thread_read = Thread(target=video, args=(queue_,))
thread_ardunio = Thread(target=uno, args=(queue_,))

thread_read.start()
thread_ardunio.start()

thread_read.join()
thread_ardunio.join()

