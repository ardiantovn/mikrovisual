
# coding: utf-8

# In[ ]:


#V5 WEBCAM+SCAN+GUI+ARDUINO
import cv2,numpy as np, serial, time
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
    ino=serial.Serial('/dev/ttyUSB1',57600)
    #r,g,b,y,p=[range(0,13),range(100,143),range(203,241),range(51,60),range(268,279)]
    N=[262,294,330,349,392]
    if warna in listNada[0]: 
        ino.write(N[0])#nada1
        time.sleep(1.5)
    elif warna in listNada[1]: 
        ino.write(N[1])#nada2
        time.sleep(1.5)
    elif warna in listNada[2]: 
        ino.write(N[2])#nada3
        time.sleep(1.5)
    elif warna in listNada[3]: 
        ino.write(N[3])#nada4
        time.sleep(1.5)
    else:
        ino.write(N[4])#nada5
        time.sleep(1.5)
    return      

def trackInit():#INISIALISASI TRACK
    def nothing(x):
        pass
    img = np.zeros((300,512,3), np.uint8)
    cv2.namedWindow('image')
    # NADA 1
    cv2.createTrackbar('Nada 1 LOW','image',0,179,nothing)
    cv2.createTrackbar('Nada 1 HIGH','image',0,179,nothing)
    # NADA 2
    cv2.createTrackbar('Nada 2 LOW','image',0,179,nothing)
    cv2.createTrackbar('Nada 2 HIGH','image',0,179,nothing)
    # NADA 3
    cv2.createTrackbar('Nada 3 LOW','image',0,179,nothing)
    cv2.createTrackbar('Nada 3 HIGH','image',0,179,nothing)
    # NADA 4
    cv2.createTrackbar('Nada 4 LOW','image',0,179,nothing)
    cv2.createTrackbar('Nada 4 HIGH','image',0,179,nothing)
    # NADA 5
    cv2.createTrackbar('Nada 5 LOW','image',0,179,nothing)
    cv2.createTrackbar('Nada 5 HIGH','image',0,179,nothing)
    cv2.imshow('image',img)
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
    return([range(n1l,n1h),range(n2l,n2h),range(n3l,n3h),range(n4l,n4h),range(n5l,n5h)])
    
i=0
trackInit()
while rval:
    i = i if i<w else 0
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    x0,x1,y0,y1=i,i,int(h/2)+50,int(h/2)-50
    warna=int(np.average(hsv[y1:y0,x0:x1+5,0]))
    play(track(),warna)
    cv2.putText(frame,str(warna),(50,400), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
    cv2.line(frame,(x0, y0),(x1, y1),(0,255,0),2)#(x1.y1)(x2.y2)=(bawah)(atas)
    cv2.rectangle(frame,(0, y0),(w, y1),(255,0,0),3)##(x1.y1)(x2.y2)=(pojok kiri bawah)(pojok kanan atas)
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    i+=5
    if key == 27: # tekan ESC untuk keluar 
        #rval = False
        break
cv2.destroyWindow("preview")

