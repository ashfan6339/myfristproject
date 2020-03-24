class A:
    def __init__(self):
        print("in A Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):
    def __init__(self):

        print("in B Init")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class C(B):

    def __init__(self):
        super().__init__()
        print("in C init")

c1 = C()
