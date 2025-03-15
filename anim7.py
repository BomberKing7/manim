from manim import *
from pydub.utils import mediainfo

def duration(sound):
    return mediainfo(sound)['duration']
#manim main.py Main -pqm
# Square : side_length , stroke_color , stroke_width , fill_color , fill_opacity , stroke_color

def vec(x,y):
    return x*RIGHT+y*UP

class array_ob():
    def set(self,i,v):
        self.v[i]=v
        self.at[i]=Tex(str(v),color=BLACK).move_to(self.at[i])
    def change(self,i,v):
        self.v[i]=v
        return Transform(
        self.at[i],
        Tex(str(v),color=BLACK).move_to(self.at[i])
        )
    def __init__(self,a):
        arr=[]
        arrt=[]
        shift=0
        for x in a:
            sq=Square(side_length=1,stroke_color=WHITE,fill_opacity=1)
            tex=Tex(str(x),color=BLACK)
            arr.append(sq)
            arrt.append(tex)
            sq.shift(vec(shift,0))
            tex.shift(vec(shift,0))
            shift+=1
        vg=VGroup(*arr,*arrt)
        vg.move_to(ORIGIN)
        self.v=a
        self.a=arr
        self.at=arrt
        self.gr=vg

class array_ob2():
    def __init__(self,a):
        arr=[]
        arrt=[]

        rarr=[]
        rarrt=[]
        shift=0
        i=-1
        for x in a:
            tarr=[]
            tarrt=[]
            i+=1
            j=-1
            for y in x:
                j+=1
                sq=Square(side_length=1,stroke_color=WHITE,fill_opacity=1)
                sq.shift(vec(j,-i))
                tex=Text(str(y),color=BLACK)
                tex.move_to(sq)

                tarr.append(sq)
                tarrt.append(tex)

                rarr.append(sq)
                rarrt.append(tex)
            
            arr.append(tarr)
            arrt.append(tarrt)
        vg=VGroup(*rarr,*rarrt)
        vg.move_to(ORIGIN)
        self.v=a
        self.a=arr
        self.at=arrt
        self.gr=vg
class Main(Scene):
    def sound(self,sound,dur=1):
        offset=dur-float(duration(sound))
        super().add_sound(sound,time_offset=offset)
    def construct(self):
        self.cur_time=0
        self.main()
    def main(self):
        n=8
        m=10
        a=[[" "]*m]*n
        
        a=array_ob2(a)
        self.add(a.gr)
        r=5
        c=0
        tr=2
        tc=9

        dx=1
        dy=1
        self.sound('click.wav')
        self.play(
            a.a[r][c].animate.set_color(GREEN)
            ,
            a.a[tr][tc].animate.set_color(BLUE)
        )
        
        while True:
            arr=[]
            for j in range(0,m):
                if(j==c):
                    continue
                arr.append(
                    a.a[r][j].animate.set_color(YELLOW)
                )
            for i in range(0,n):
                if(i==r):
                    continue
                arr.append(
                    a.a[i][c].animate.set_color(YELLOW)
                )
            self.sound('click.wav')
            self.play(*arr)
            if r==tr or c==tc:
                self.play(
                    a.a[tr][tc].animate.set_color(RED)
                )
                break
            if r+dx==n or r+dx==-1:
                dx=-dx
            if c+dy==m or c+dy==-1:
                dy=-dy
            self.sound('click.wav')
            self.play(
                a.a[r][c].animate.set_color(YELLOW)
                ,
                a.a[r+dx][c+dy].animate.set_color(GREEN)
            )
            r+=dx
            c+=dy




   
                




            



