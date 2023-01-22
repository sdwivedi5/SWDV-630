class Teams:
  def __init__(self, members):
    self.__myTeam = members

  def __len__(self):
    return len(self.__myTeam)
    
  def __contains__(self, substr):
        if substr in self.__myTeam:
            return True
        else:
            return False
            
   # required for the iterator protocol
  def __next__(self):
        if not self.__myTeam:
            raise StopIteration
        value = self.__myTeam.pop(0)
        return value

    # required for the iterator protocol. It *has* to return self
  def __iter__(self):
        return self
        
            
def main():
  classmates = Teams(['John', 'Steve', 'Tim'])
  print("This is printing whether Steve and Tim as part of the team")
  print ('Steve' in classmates)   
  print ('Tim' in classmates)
  
  print("This is printing len of team using len method")
  print (len(classmates))
  
  it = iter(classmates)
  
  print("This is printing all classmates using iteration")
  print(next(it))
  print(next(it))
  print(next(it))


   


main()



