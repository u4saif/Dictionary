import json
from difflib import SequenceMatcher, get_close_matches


'''This is A APP TO FIND Words Meaning '''
class Dictionary():
    
    def __init__(self):
        data=json.load(open("C:/Users/ssaifuddin/Documents/data.json"))
        self.data=data   

    def translate(self,w):
        if w in self.data:
            return self.data[w]

        elif len(get_close_matches(w,self.data.keys()))>0:
           yn=input("Did you mean %s instead ? Enter Y for yes , N for No."%get_close_matches(w,self.data.keys())[0])
           if yn=="Y" or yn=='y':
            return get_close_matches(w,self.data.keys())
           elif yn=='N' or yn=='n':
            return "Sorry unbale to find your meaning."
           else :
                return "Sorry unbale to understand you ."
        else:
            return "This word does not exist."
    def find(self):
        #while(True):
            
            w=input("Enter your word to find the meaning \n") 

            output=self.translate(w.lower())

            if type(output)==list:
                for i, item in enumerate(output):
                    print(str(i+1)+")",str(item)) 

            else:
                print("\n🙄 " + str(output))
            
def main():
    obj=Dictionary()
    obj.find()
            
if __name__=='__main__':
    main()
