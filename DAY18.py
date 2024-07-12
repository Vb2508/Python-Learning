# voter_list= [{"partyName":"BJP",
#                "partyID":1000,
#                "totalVote":11},

#              {"partyName":"Congress"
#               ,"partyID":420,
#               "totalVote":0
#               }]
# for item in voter_list:
#     item.update({'totalVote':item['totalVote']+1})
#     print(item)

class Voting:
    def __init__(self):
        self.voterslist=[]
        self.title='Hi Voter,'
        self.totalVote=0
        self.votingMachine=[{"partyName":"BJP",
               "partyID":1000,
               "totalVote":0},

             {"partyName":"Congress"
              ,"partyID":420,
              "totalVote":0
              }]

    
       

    def allowVoterForVoting(self,voter):
        print(self.title) 
        result= self.checkEligibility  (voter['age'])
        result1= self.DuplicateVoterCheck(voter['id'])
        if result1==True:
            print('Voter already Voted Once. Thank You Voter.')
            print('__________________________________________________________________________')
            return
        if result==True:
            print('You are eligible to Vote. Go and Vote!!')
            self.checkpartyvotes (voter["partyID"])
            
            self.totalVote= self.totalVote+1
            self.voterslist.append(voter)
            print("Current Voters:-",self.voterslist)
            print("Total votes So Far:",self.totalVote) 
            print('__________________________________________________________________________')

        else:
            print('You are not eligible to Vote. ')


    def checkEligibility(self,age):
        if age>=18:
            return True
        else:
            return False
        
    def checkpartyvotes(self,partyID):
        for item in self.votingMachine:
            if partyID==item["partyID"]:
                item.update({'totalVote':item['totalVote']+1})
            

    def DuplicateVoterCheck(self,id) :
        for item in self.voterslist:
            if id==item["id"]:
                return True
        return None
    
    def winningparty(self):
        for item in self.votingMachine:
           print ("Final Result:",item)
           print("__________________________________________________________________________________")
           

          

    
v=Voting()
print("\nVoting process for different voters:")
v.allowVoterForVoting({'id':1,'name':'Dnyaneshwar' ,'age':26,"partyID":1000})
v.allowVoterForVoting({'id':6,'name':'vivek' ,'age':26,"partyID":1000})
v.allowVoterForVoting ({'id':2,'name':'Swapnil','age':30,"partyID":1000})
v.allowVoterForVoting({'id':3,'name':'Billa','age':32,"partyID":1000})
v.allowVoterForVoting({'id':4,'name':'RS','age':28,"partyID":420})
v.allowVoterForVoting({'id':5,'name':'Billas','age':32,"partyID":420}) 
v.allowVoterForVoting({'id':4,'name':'KB','age':26,"partyID":420})
v.allowVoterForVoting({'id':1,'name':'swapnil','age':30,"partyID":420})
v.winningparty()
