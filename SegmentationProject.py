import numpy as np
import cv2
n=1
cap = cv2.VideoCapture(0)
#Tomar la posición del frame
def position(event,x,y,flags,param):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		print('current pos {}'.format((x, y))) 
# Definir el codec y crear objeto VideoWriter

fourcc =cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc,20.0,(640,480))

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)

        

        roi=frame[135:345,65:575]
       
        #flip2=cv2.flip(roi,1)
        
        roi = cv2.rectangle(roi,(3,3),(505,205),(0,0,0),thickness =6, lineType=8, shift=0) #recuadro
        

        roi = cv2.rectangle(roi,(55,55),(155,155),(0,255,0),thickness =4, lineType=8, shift=0) #recuadro
        cv2.putText(roi,"+",(52,140),cv2.FONT_ITALIC,4,(0,255,0),5,cv2.LINE_AA) #texto

        roi = cv2.rectangle(roi,(205,55),(305,155),(255,0,0),thickness =4, lineType=8, shift=0) #recuadro
        cv2.putText(roi,"-",(202,140),cv2.FONT_ITALIC,4,(255,0,0),5,cv2.LINE_AA) #texto

        roi = cv2.rectangle(roi,(355,55),(455,155),(0,0,255),thickness =4, lineType=8, shift=0) #recuadro
        cv2.putText(roi,"ESC",(355,125),cv2.FONT_ITALIC,1.6,(0,0,255),2,cv2.LINE_AA) #texto

        roi2=frame[191:289,121:221]
        Brillo= np.array(255*(roi2/255)**0.1,dtype='uint8')
        #frame[191:289,121:221]=Brillo

        roi3=frame[191:289,275:368]
        Brillo= np.array(255*(roi3/255)**0.1,dtype='uint8')
        #frame[191:289,275:368]=Brillo
        
        roi4=frame[191:289,424:518]
        Brillo= np.array(255*(roi4/255)**0.1,dtype='uint8')
        #frame[191:289,424:518]=Brillo



        #escribir el frame con los ultimos cambios 

        #gray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
        #gray_filter = cv2.GaussianBlur(gray,(7,7),0)
        #circulos = cv2.HoughCircles(gray_filter , cv2.HOUGH_GRADIENT,1,40,param1=50,param2=50,minRadius=10,maxRadius=70)

        gray = cv2.cvtColor(roi2,cv2.COLOR_BGR2GRAY)
        gray_filter = cv2.GaussianBlur(gray,(7,7),0)
        circulos = cv2.HoughCircles(gray_filter , cv2.HOUGH_GRADIENT,1,40,param1=50,param2=50,minRadius=10,maxRadius=70)

        gray2 = cv2.cvtColor(roi3,cv2.COLOR_BGR2GRAY)
        gray_filter2 = cv2.GaussianBlur(gray2,(7,7),0)
        circulos2 = cv2.HoughCircles(gray_filter2 , cv2.HOUGH_GRADIENT,1,40,param1=50,param2=50,minRadius=10,maxRadius=70)

        gray3 = cv2.cvtColor(roi4,cv2.COLOR_BGR2GRAY)
        gray_filter3 = cv2.GaussianBlur(gray3,(7,7),0)
        circulos3 = cv2.HoughCircles(gray_filter3 , cv2.HOUGH_GRADIENT,1,40,param1=50,param2=50,minRadius=10,maxRadius=70)
             
        try:
            if(len(circulos)>0):

                circulos = np.uint16(np.around(circulos))
                for i in circulos[0,:]: #se pintan los cirulos en la region de interes
                    n=n-0.01    

                #circulo exterior   
                    cv2.circle(roi2,(i[0],i[1]),i[2],(0,0,255),2)

                        #centro del circulo
                        ##imagen , centro , radio , color , grosor
                    cv2.circle(roi2,(i[0],i[1]),2(255,0,0),2)
                        #se define la fila y la columna de la ubicacion del patron
          
           
                   




            
        except Exception:
            #print("No se detecta el patron")
            a=0

        try:
           




            if(len(circulos2)>0):

                circulos2 = np.uint16(np.around(circulos2))
                for i in circulos2[0,:]: #se pintan los cirulos en la region de interes
                #circulo exterior 
                    n=n+0.01   
                    #print("Detectó el trikiti") 
                    cv2.circle(roi3,(i[0],i[1]),i[2],(0,0,255),2)

                    #centro del circulo
                    ##imagen , centro , radio , color , grosor
                    cv2.circle(roi3,(i[0],i[1]),2(255,0,0),2)
                    #se define la fila y la columna de la ubicacion del patron


                     
                    
                    
                
            
        except Exception:
            #print("No se detecta el patron")
            a=0


        try:
           




            if(len(circulos3)>0):

                circulos3 = np.uint16(np.around(circulos3))
                for i in circulos3[0,:]: #se pintan los cirulos en la region de interes
                #circulo exterior 
                   # print("Detectó el trikiti") 
                    cap.release()
                    out.release()
                    cv2.destroyAllWindows()   
                    cv2.circle(roi4,(i[0],i[1]),i[2],(0,0,255),2)

                    #centro del circulo
                    ##imagen , centro , radio , color , grosor
                    cv2.circle(roi4,(i[0],i[1]),2(255,0,0),2)
                    #se define la fila y la columna de la ubicacion del patron
                


                     
                    
                    
                
            
        except Exception:
            #print("No se detecta el patron")
            a=0
        
        
 
        #print(n)
        if(n<=0):
            n=0.01
        
        
       
        roi=frame[135:345,65:575]
        Brillo= np.array(255*(roi/255)**n,dtype='uint8')
        frame[135:345,65:575]=Brillo                      
        #print("Detectó el trikiti")


        out.write(frame)
        cv2.setMouseCallback('frame',position)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else: 
        break

# si ya muestro trabajo ha terminado se liberan los objetos
# y se cierran todas las ventanas 
cap.release()
out.release()
cv2.destroyAllWindows()