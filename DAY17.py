class Voting:
    def __init__(self):
        self.voterslist=[]
        self.title='Hi Voters'
        self.totalVote=0



    def allowVoterForVoting(self,voter):
        print(self.title) 
        result= self.checkEligibility  (voter['age'])
        result1= self.DuplicateVoterCheck(voter['id'])
        if result1==True:
            print('Thank You Voter')
        if result==True:
            print('Go and Vote')
            self.totalVote= self.totalVote+1
            self.voterslist.append(voter)
            print(self.voterslist, "adding voter")
            print(self.totalVote)    
        else:
            print('You are not eligible to Vote')    
        
    def checkEligibility(self,age):
        if age>=18:
            return True
        else:
            return False
        
    def DuplicateVoterCheck(self,id) :
        for item in self.voterslist:
            if id==item["id"]:
                print(id,"checked")
            else:
                print("arrest Voter")    
        
v=Voting()
v.allowVoterForVoting({'id':1,'name':'Dnyaneshwar','age':26})
v.allowVoterForVoting ({'id':2,'name':'Swapnil','age':30})
v.allowVoterForVoting({'id':3,'name':'Billa','age':32})
v.allowVoterForVoting({'id':3,'name':'Billa','age':32})
