class Akhilesh(object):

   def upperFuct(self,fuc):
      print ("Upper")
      def inner():
         fuc()
         print("Inner1")        
      return inner()

def sum1():
   print("Sum")
      


s=Akhilesh()
s.upperFuct(sum1)
