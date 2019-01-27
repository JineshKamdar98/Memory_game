import simpleguitk as simplegui
import random

s1=[0,1,2,3,4,5,6,7]
s2=[0,1,2,3,4,5,6,7]
s3=s1+s2
random.shuffle(s3)
attempts=0
count=0
i1=i2=0


list=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]

def restart():
    global attempts,count,i1,i2,list,s3
    attempts=0
    count=0
    i1=0
    i2=0
    label.set_text("Attempts:"+str(attempts))
    list=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    random.shuffle(s3)
    

def click(c):
    global attempts,count,i1,i2
    k=0  
    for i in range(16):
        if(c[0]>k and c[0]<k+50):
            list[i]=True
            count+=1
            if(count==1):
                i1=i
            elif(count==2):
                i2=i
                attempts+=1
                label.set_text("Attempts:"+str(attempts))
            elif(count==3):
                count=1
                if(s3[i1]!=s3[i2]):
                    list[i1]=False
                    list[i2]=False
                i2=i1
                i1=i
        k+=50
    
def draw(canvas):
    global s1,s2,s3,list
    p=5
    p1=50
    x=25
    v=50
    label.set_text("Attempts:"+str(attempts))
    
    for i in range(16):
        canvas.draw_text(str(s3[i]),[p,100],50,"White")
        p+=p1
        
    for i in range(16):
        if(list[i]==False):
            canvas.draw_line([x,0],[x,200],50,"Yellow")
            x+=p1
        if(list[i]==True):
            x+=p1
            
    for i in range(16):
        canvas.draw_line([v,0],[v,200],1,"Blue")
        v+=p1
                
frame=simplegui.create_frame("Memory",800,100)
frame.set_mouseclick_handler(click)
frame.add_button("Restart",restart)
frame.set_draw_handler(draw)
label=frame.add_label(" ")
frame.start()
