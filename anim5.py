
# number of subarrays with sum less than or equal x
from manim import *
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

class Main(Scene):
    def construct(self):
        
        a=[9,9,9,4,29,10,20,31,30,10,20]
        b=[0,30]
        n=len(a)
        m=len(b)

        ans=[0]*len(a)

        ans=array_ob(ans)
        a=array_ob(a)
        b=array_ob(b)

        ans.gr.shift(vec(0,-1))
        a.gr.shift(vec(0,0))
        b.gr.shift(vec(0,2))
        
        self.add(ans.gr)
        self.add(a.gr)
        self.add(b.gr)

        p1=Circle(radius=0.6,color=BLUE)
        p2=Circle(radius=0.6,color=RED)
        
        p1.move_to(a.a[0]).shift(vec(0,0))
        p2.move_to(a.a[0]).shift(vec(-1,0))
        self.add(p1)
        self.add(p2)
        
        
        self.wait(1)
        i=0
        j=-1
        sum=0
        while i<n:
            while j+1<n and sum+a.v[j+1]<=b.v[1]:
                j+=1
                sum+=a.v[j]
                self.play(b.change(0,sum),p2.animate.move_to(a.a[j]),a.a[j].animate.set_color(GREEN))
            
            self.play(
                ans.change(i,j-i+1),
                ans.a[i].animate.set_color(GREEN)
            )
            if(i+1==n):
                break
            arr=[]
            if j>=i:
                arr=[
                    p1.animate.move_to(a.a[i+1]),
                    b.change(0,sum-a.v[i]),
                    a.a[i].animate.set_color(WHITE)
                ]
                sum-=a.v[i]
            else:
                arr=[
                   p1.animate.move_to(a.a[i+1]),
                   p2.animate.move_to(a.a[i-1]) 
                ]
            i+=1
            if j<i-1:
                arr.append(p2.animate.move_to(a.a[i-1]))
                j=i-1
            self.play(*arr)
