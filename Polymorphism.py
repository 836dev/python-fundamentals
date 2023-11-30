class A:
    def show(self):
        print("Show from class A")
class B(A):
    def show (self):
        super().show()
        print("Show from class B")
class C(B):
    def show(self):
        super().show()
        print("Show from class C")

c1=C()
c1.show()
    
