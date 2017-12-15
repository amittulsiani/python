class Akhilesh:
     @classmethod
     def upperFuct1(cls,fuc1):
          print ("Upper1")
          def inner1(*args,**kwargs):
              fuc1(*args)
              print("Inner1 \n")       
          return inner1()
     @classmethod
     def upperFuct2(cls,fuc2):
          print ("Upper2")
          def inner2(*args,**kwargs):
              fuc2(*args)
              print("Inner2 \n")
              return fuc2
          return inner2()
        
     @staticmethod
     def upperFuct3(fuc3):
          print ("Upper3")
          def inner3(*args,**kwargs):
              fuc3(*args)
              print("Inner3 \n")
              return fuc3
          return inner3()  

@Akhilesh.upperFuct1
@Akhilesh.upperFuct2
@Akhilesh.upperFuct3

def sum1():
    print ("hello")
