
from manim import *
def vec(x,y):
    return x*RIGHT+y*UP

# number of subarrays with number of distinct elements less than or equal x


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
        
        a=[0,1,2,1,4,3,2,3,0]
        c=[0,3]

        mx=0
        for x in a:
            mx=max(mx,x)

        b=[0]*(mx+1)
        n=len(a)
        m=len(b)
        print(m)
        ans=[0]*len(a)
        
        
        ans=array_ob(ans)
        a=array_ob(a)
        b=array_ob(b)
        c=array_ob(c)

        c.a[0].set_color(BLUE)
        c.a[1].set_color(BLUE)

        ans.gr.shift(vec(0,-1))
        a.gr.shift(vec(0,0))
        b.gr.shift(vec(0,2))
        c.gr.shift(vec(0,3))

        self.add(ans.gr)
        self.add(a.gr)
        self.add(b.gr)
        self.add(c.gr)

        p1=Circle(radius=0.6,color=BLUE)
        p2=Circle(radius=0.6,color=RED)
        
        p1.move_to(a.a[0]).shift(vec(0,0))
        p2.move_to(a.a[0]).shift(vec(-1,0))
        self.add(p1)
        self.add(p2)
        
        
        i=0
        j=-1

        while i<n:
            while j+1<n and not (c.v[0]+1>c.v[1] and b.v[a.v[j+1]]==0):
                j+=1
                arr=[
                    a.a[j].animate.set_color(GREEN),
                    p2.animate.move_to(a.a[j])
                ]
                
                x=a.v[j]
                arr.append(
                    b.change(x,b.v[x]+1)
                )
                if(b.v[x]==1):
                    arr.append(
                        c.change(0,c.v[0]+1)
                    )
                    arr.append(
                        b.a[x].animate.set_color(GREEN)
                    )
                self.play(*arr)
            self.play(
                ans.a[i].animate.set_color(GREEN),
                ans.change(i,j-i+1)
            )
            if(i+1==n):
                break
            arr=[]
            if i<=j:
                i+=1
                arr.append(a.a[i-1].animate.set_color(WHITE))
                arr.append(p1.animate.move_to(a.a[i]))
                x=a.v[i-1]
                arr.append(
                    b.change(x,b.v[x]-1)
                )
                if(b.v[x]==0):
                    arr.append(
                        b.a[x].animate.set_color(WHITE)
                    )
                    arr.append(
                        c.change(
                            0,c.v[0]-1
                        )
                    )
            else:
                i+=1
                j=i-1
                arr.append(
                    p1.animate.move_to(a.a[i])
                )
                arr.append(
                    p2.animate.move_to(a.a[i-1])
                )
            self.play(*arr)
