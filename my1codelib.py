# parent class for all my objects
class my1Object:
  def __init__ (self):
    self.ResetState()
  def ResetState(self):
    self.emsg = "OK"
    self.fail = False
    self.dbug = False
  def CloneError(self,that):
    self.emsg = that.emsg
    self.fail = that.fail
  def CheckError(self,that):
    if that.Failed():
      self.CloneError(that)
      return True
    return False
  def Failed(self):
    return self.fail
  def Fails(self,emsg="** Failed!"):
    self.emsg = emsg
    self.fail = True
    if self.dbug==True:
      print(self.emsg)
  def DoDebug(self):
    return self.dbug
  def DoDebugSet(self,debug=True):
    self.dbug = debug

import os.path

# class to read/write binary data to/from file
class my1BinFile(my1Object):
  def __init__ (self,name=None):
    super().__init__()
    if name==None or not self.LoadPack(name):
      self.name = None
      self.pack = None
  def LoadPack(self,name):
    if not os.path.isfile(name):
      self.Fails("** Cannot find file '"+name+"'!")
      return False
    try:
      data = open(name,'rb')
    except OSError:
      self.Fails("** Cannot open file '"+name+"'!")
      return False
    except:
      self.Fails("** Unknown error opening '"+name+"'!")
      return False
    try:
      self.pack = bytearray(data.read())
      self.name = name
      if self.DoDebug():
        print("## LoadPack: '"+name+"' ("+str(len(self.pack))+")")
    except:
      self.Fails("** Cannot read file '"+name+"'!")
    finally:
      data.close()
    return not self.fail
  def SavePack(self,name,pack,force=False):
    if os.path.isfile(name):
      if force==False:
        self.Fails("** File '"+name+"' exists!")
        return False
    try:
      data = open(name,'rb')
    except OSError:
      self.Fails("** Cannot open file '"+name+"'!")
      return False
    except:
      self.Fails("** Unknown error opening '"+name+"'!")
      return False
    try:
      data.write(name,pack)
      self.pack = pack
      self.name = name
      if self.DoDebug():
        print("## SavePack: '"+name+"' ("+str(len(self.pack))+")")
    except:
      self.Fails("** Cannot write file '"+name+"'!")
    finally:
      data.close()
    return not self.fail
