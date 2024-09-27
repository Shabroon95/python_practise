class Myclass:
    def __del__(self):
        print("destroyed")

c1=Myclass()
c2=Myclass()
del c1

