from manim import *;
class Scene2(Scene):
    def construct(self):
        #Intro

        intro=Tex("\"Maths is the only place where truth and beauty mean the same thing.\"",color=BLUE,font_size=32)
        self.play(Write(intro),runtime=5)
        self.wait(2)
        self.play(FadeOut(intro))
        # """
        # slide 1
        topic=Tex("Application of Diffrential Equation in RLC Circuit: ",color=BLUE,font_size=40)
        
        text=Tex("An LCR circuit is made up of three components: an inductor (L), a capacitor (C), and a resistor (R).LCR circuits have many applications as oscillator circuits. Radio receivers and television sets use them for tuning to select a narrow frequency range from ambient radio waves.",font_size=34)
        topic.shift(2*UP)
        self.play(Write(topic))
        
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(topic))
        self.play(FadeOut(text))

        #slide 2
        text2=Tex("The RLC filter is described as a second-order circuit, meaning that any voltage or current in the circuit can be described by a second-order differential equation in circuit analysis.",font_size=34,color=YELLOW)
        text2.shift(2*UP)
        self.play(Write(text2))
        text3=Tex("Here we are going to analyze series LCR circuit.As a result, the resistor, capacitor, and inductor will all have the same amount of current flowing through them.",font_size=34)
        self.play(FadeIn(text3))
        self.wait(1)
        self.play(FadeOut(text3))
        self.play(FadeOut(text2))
        
        #slide 3
        text4=Tex("According Kirchhoff's voltage law (KVL): ",font_size=40,color=BLUE)
        text4.shift(3*UP)
        self.play(FadeIn(text4))
        text5=MathTex(r"V_{L}+V_{C}+V_{R}=V(t)")
        text5.shift(2*UP+2*LEFT)
        self.play(Write(text5))
        self.wait(1)
        text6=MathTex("We know ",r"\; V_{R}=R I(t),\;V_{L}=L\frac{d I(t)}{dt} \;and \;V_{C}=V(0)+\frac{1}{C}\int_{0}^{t}I(\tau)d\tau",font_size=32)
        text6.shift(UP+2*LEFT)
        self.play(Write(text6))
        text7=MathTex(r"R I(t)+L\frac{d I(t)}{dt}+V(0)+\frac{1}{C}\int_{0}^{t}I(\tau)d\tau=V(t)")
        text7.shift(DOWN)
        self.wait(1)
        self.play(Write(text7))
        self.wait(1)
        self.play(FadeOut(text4))
        self.play(FadeOut(text6))
        self.play(FadeOut(text5))
        self.play(FadeOut(text7))

        #slide 4
        text8=Tex("If we assume that the voltage source is an unchanging voltage source and taking time darinvative and deviding whole equation by L",color=BLUE,font_size=30)
        text8.shift(3*UP+2*LEFT)
        self.play(FadeIn(text8))
        self.wait(2)
        text9=MathTex(r"\frac{d^2 I(t)}{dt^2}+\frac{R}{L}\frac{d I(t)}{dt}+\frac{1}{LC}I(t)=0")
        text9.shift(2*UP+2*LEFT)
        self.play(Write(text9))
        text10=MathTex("Now if ",r"\;\alpha=\frac{R}{L} and \;\omega_{0}=\frac{1}{\sqrt{LC}}")
        self.play(Write(text10))
        text11=MathTex(r"\frac{d^2I(t)}{dt^2}+2\alpha\frac{d I(t)}{dt}+\omega^{2}_{0}I(t)=0")
        text11.shift(2*DOWN+2*LEFT)
        self.play(Write(text11))
        self.wait(2)
        self.play(FadeOut(text8))
        self.play(FadeOut(text9))
        self.play(FadeOut(text10))
        self.play(FadeOut(text11))
        self.wait(1)

        #slide5

        text12=Tex("Now this is an auxilary equation.(C.F)")
        text12.shift(3*UP+2*LEFT)
        self.play(Write(text12),color=BLUE)
        text13=MathTex(r"m^{2}+2\alpha m +\omega_{0}^{2}=0")
        text13.shift(UP+2*LEFT)
        self.play(Write(text13))
        text14=Tex("roots of this equation is:",color=BLUE_B)
        text14.shift(2*LEFT)
        self.play(Write(text14))
        text15=MathTex(r"m_{1}=-\alpha+\sqrt{\alpha^{2}-\omega_{0}^{2}} ,m_{1}=-\alpha-\sqrt{\alpha^{2}-\omega_{0}^{2}}")
        text15.shift(2*DOWN+2*LEFT)
        self.play(Write(text15))
        self.wait(1)
        self.play(FadeOut(text12))
        self.play(FadeOut(text14))
        self.play(FadeOut(text13))
        self.play(FadeOut(text15))

        #slide6
        text16=Tex("We know the solution of second order differntial equation: ",color=YELLOW,font_size=32)
        text16.shift(2*UP+2*LEFT)
        self.play(FadeIn(text16))
        text17=MathTex(r"I(t)=A1e^{m_{1}t}+A2e^{m_{2}t}")
        self.play(Write(text17))
        text18=Tex("Here i am assuming the solutions are real and distinct",color=BLUE,font_size=32)
        text18.shift(1*DOWN+2*LEFT)
        self.play(Write(text18))
        self.wait(4)
        self.play(FadeOut(text17))
        self.play(FadeOut(text18))
        self.play(FadeOut(text16))
        
        #outro
        outro1=Text("Created by:")
        outro1.shift(3*UP)
        self.play(FadeIn(outro1))
        outro2=Text("Darshil Shah(22BEC111)",color=BLUE)
        outro2.shift(2*UP)
        self.play(Write(outro2))
        outro3=Text("Researched by:")
        outro3.shift(UP)
        self.play(FadeIn(outro3))
        outro4=Text("1.Harshvardhan Singh (22BEC120)",color=YELLOW_B)
        
        self.play(Write(outro4))
        outro5=Text("2. Shashwat Joshi (22BEC116)",color=BLUE)
        outro5.shift(DOWN)
        self.play(Write(outro5))
        outro6=Text("3. Satyam Rana (22BEC101)",color=YELLOW_B)
        outro6.shift(2*DOWN)
        self.play(Write(outro6))
        outro7=Text("4. Manthan Shah (22BEC113)",color=BLUE)
        outro7.shift(3*DOWN)
        self.play(Write(outro7))
        self.wait(2)



        

