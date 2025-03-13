#check if an array is sub sequence of another array

def vec(x,y):
    return x*RIGHT+y*UP

class array_ob():
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
        a=[5,2,3,1,2,3,4]
        b=[2,1,2,4]
        n=len(a)
        m=len(b)

        a=array_ob(a)
        b=array_ob(b)
        a.gr.shift(vec(0,1))
        b.gr.shift(vec(0,-1))
        self.add(a.gr)
        self.add(b.gr)

        p1=Circle(radius=0.6,color=BLUE)
        p2=Circle(radius=0.6,color=RED)
        p2.shift(vec(1,0))
        
        p1.move_to(a.a[0])
        p2.move_to(b.a[0])

        self.add(p1)
        self.add(p2)
        self.wait(1)

        i=0
        j=0

        while i<n and j<m:
            self.play(p1.animate.move_to(a.a[i]),p2.animate.move_to(b.a[j]))
            
            if a.v[i]==b.v[j]:
                self.play(b.a[j].animate.set_color(GREEN),a.a[i].animate.set_color(GREEN))
                j+=1
            else:
                self.play(a.a[i].animate.set_color(RED))
            i+=1
        self.wait(1)
