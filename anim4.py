
#merge two sorted arrays
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

        ans=[0]*(n+m)

        ans=array_ob(ans)
        ans.gr.scale(0.8)
        a=array_ob(a)
        b=array_ob(b)

        ans.gr.shift(vec(0,-1))
        a.gr.shift(vec(0,1))
        b.gr.shift(vec(0,2))
        
        self.add(ans.gr)
        self.add(a.gr)
        self.add(b.gr)

        p1=Circle(radius=0.6,color=BLUE)
        p2=Circle(radius=0.6,color=RED)
        p3=Circle(radius=0.6,color=YELLOW)
        
        p1.move_to(a.a[0])
        p2.move_to(b.a[0])
        p3.move_to(ans.a[0])
        self.add(p1)
        self.add(p2)
        self.add(p3)
         
        self.wait(1)
        i=0
        j=0

        while i<n or j<m:
            if i<n and (j==m or a.v[i]<=b.v[j]):
                arr=[]
                arr.append(
                    Transform(
                        ans.at[i+j],
                        Tex(str(a.v[i]),color=BLACK).move_to(ans.at[i+j])
                    )
                )
                arr.append(
                    a.a[i].animate.set_color(GREEN)
                )
                if(i+1<n):
                    arr.append(
                        p1.animate.move_to(a.a[i+1])
                    )
                i+=1
            else:
                arr=[]
                arr.append(
                    Transform(
                        ans.at[i+j],
                        Tex(str(b.v[j]),color=BLACK).move_to(ans.at[i+j])
                    )
                )
                arr.append(
                    b.a[j].animate.set_color(GREEN)
                )
                if(j+1<m):
                    arr.append(
                        p2.animate.move_to(b.a[j+1])
                    )
                j+=1
            arr.append(
                ans.a[i+j-1].animate.set_color(GREEN)
            )
            if(i+j<n+m):
                arr.append(
                    p3.animate.move_to(ans.a[i+j])
                )
            self.play(*arr)
