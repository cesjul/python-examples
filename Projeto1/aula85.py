class A:
    def escrever(self):
        print('A')

class B(A):
    def escreverb(self):
        print('B')

class C(B):
    def escrever(self):
        super().escrever()
        print('C')

c = C()
c.escrever()