class A:
    def a(self):
        self.b()

    def e(self):
        self.c()


class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(B):
    def f(self):
        pass


class D(A):
    def b(self):
        self.f()


class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


class F:
    def a(self):
        self.b()
        self.f()
