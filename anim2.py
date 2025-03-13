#check if an array is sub array of another array
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

def is_prefix (a,b):
    if(len(a)>len(b)):
        return False
    i=0
    while i<len(a):
        if a[i]!=b[i]:
            return False
        i+=1
    return True

class Main(Scene):
    def construct(self):
        a=[1,1,2,1,2,1,3]
        b=[1,2,1,3]
        n=len(a)

        a=array_ob(a)
        b=array_ob(b)
        a.gr.shift(vec(0,1))
        b.gr.shift(vec(0,-1))
        self.add(a.gr)
        self.add(b.gr)

        p1=Circle(radius=0.6,color=BLUE)
        p2=Circle(radius=0.6,color=RED)
        
        p1.move_to(a.a[0])
        p2.move_to(a.a[0]).shift(vec(-1,0))
        self.add(p1)
        self.add(p2)
        
        
        self.wait(1)
        l=0
        r=-1
        while r+1<n:
            if(r-l+1<len(b.v)):
                r+=1
            arr=[]

            if r==0:
                arr.append(p2.animate.move_to(a.a[r]))
            else:
                arr.append(p2.animate.move_to(a.a[r]))
            for i in range(l,r+1):
                arr.append(a.a[i].animate.set_color(YELLOW))
            for i in range(0,r-l+1):
                arr.append(b.a[i].animate.set_color(YELLOW))
            
            self.play(*arr)

            while l<=r and not is_prefix(a.v[l:r+1],b.v):
                arr=[]
                arr.append(b.a[r-l].animate.set_color(WHITE))
                arr.append(a.a[l].animate.set_color(WHITE))
                l+=1
                arr.append(p1.animate.move_to(a.a[l]))
                self.play(*arr)
            
            arr=[]
            for i in range(l,r+1):
                arr.append(a.a[i].animate.set_color(GREEN))
                arr.append(b.a[i-l].animate.set_color(GREEN))
            if len(arr):
                self.play(*arr)
