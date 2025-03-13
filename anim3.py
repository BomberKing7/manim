
#for each element in first array count number of elements less tahn or equal it in the second array
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
        
        a=[1,2,4,7,9,10,20,20]
        b=[1,1,2,4,5,6,7,8,20]

        n=len(a)
        m=len(b)

        ans=[0]*len(a)

        ans=array_ob(ans)
        a=array_ob(a)
        b=array_ob(b)

        ans.gr.shift(vec(0,2))
        a.gr.shift(vec(0,1))
        b.gr.shift(vec(0,-1))
        
        self.add(ans.gr)
        self.add(a.gr)
        self.add(b.gr)

        p1=Circle(radius=0.6,color=BLUE)
        p2=Circle(radius=0.6,color=RED)
        
        p1.move_to(a.a[0]).shift(vec(-1,0))
        p2.move_to(b.a[0]).shift(vec(-1,0))
        self.add(p1)
        self.add(p2)
        
        
        self.wait(1)
        i=-1
        j=-1
        while i+1<n:
            i+=1
            self.play(p1.animate.move_to(a.a[i]))
            while j+1<m and b.v[j+1]<=a.v[i]:
                j+=1
                self.play(p2.animate.move_to(b.a[j]),b.a[j].animate.set_color(GREEN))

            self.play(
                Transform(ans.at[i],Tex(str(j+1),color=BLACK).move_to(ans.a[i]))
                ,
                ans.a[i].animate.set_color(GREEN)
                ,
                a.a[i].animate.set_color(GREEN)
                )

