from abc import ABC, abstractmethod


class A(ABC):
    def a(self):
        self.b()

    def e(self):
        self.c()

    @abstractmethod
    def b(self):
        ...

    @abstractmethod
    def c(self):
        ...


class B(A):
    def b(self):
        self.a()

    def c(self):
        self.e()


class C(B):
    def f(self):
        pass


# Abstract
class D(A):
    def b(self):
        self.f()

    @abstractmethod
    def f(self):
        ...


class E(D):
    def c(self):
        self.a()

    def f(self):
        self.e()

    def g(self):
        self.f()


class F(ABC):
    def a(self):
        self.b()
        self.f()

    @abstractmethod
    def b(self):
        ...

    @abstractmethod
    def f(self):
        ...
