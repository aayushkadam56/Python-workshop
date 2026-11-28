#function overriding
#same name function in base+derived class
class base:
    def _init_(self):
        print("base class called")
class derived:
  def _init_(self):
    #base class construster
    super()._init_()
     print("derived class called")
obj=derived()
obj.display()