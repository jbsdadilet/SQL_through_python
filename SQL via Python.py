# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 17:43:17 2019

@author: Adilet
"""

import cx_Oracle

import datetime 
d = datetime.datetime

dbConn = cx_Oracle.connect("AdiletBU/Zaq12wsx@localhost/xe")
cur = dbConn.cursor()  

class User():
                
    def createAccount(self, ID, firstName, lastName):
        self.ID = ID
        self.firstName = firstName
        self.lastName=lastName
        cur.execute("insert into AppUser (ID, firstName, lastName, Cre_Date) values({Id}, '{fN}','{Ln}', sysdate)".format(Id=self.ID, fN=self.firstName, Ln=self.lastName))
        print ("WELCOME "+firstName, lastName)
        dbConn.commit()   

class Volunteering(User):
    
    def chooseActivity(self):
        
        accounts = []
        accounts.append(self.ID)
               
        for e in accounts:
            while e == self.ID:
                print("\nList of activities you can participate: \n1: Planting tree \n2: Cleaning Waste \n3: Plogging \n4: Others")
                firstActivity = 'Planting tree'
                secondActivity ='Cleaning waste'
                thirdActivity = 'Plogging'
                fouthActivity = 'Others helps'
                choice = eval(input("Choose you activity: "))
                if choice == 1:
                    cur.execute("insert into Volunteering (activity_name, FirstName, LastName, Acv_date)values('{fA}','{fN}','{Ln}', sysdate)"\
                                .format(fA=firstActivity,fN=self.firstName, Ln=self.lastName))
                    print(self.firstName+" "+self.lastName+ ", you are registered successfully to "+ firstActivity+" activity")
                    dbConn.commit()
                    break
                elif choice == 2:
                    cur.execute("insert into Volunteering (activity_name, FirstName, LastName, Acv_date)values('{fA}','{fN}','{Ln}',sysdate)"\
                                .format(fA=secondActivity,fN=self.firstName, Ln=self.lastName))
                    print(self.firstName+" "+self.lastName+ ", you are successfully registered to "+ secondActivity+" activity")
                    dbConn.commit()
                    break                        
                elif choice == 3:
                    cur.execute("insert into Volunteering (activity_name, FirstName, LastName, Acv_date)values('{fA}','{fN}','{Ln}',sysdate)"\
                                .format(fA=thirdActivity,fN=self.firstName, Ln=self.lastName))
                    print(self.firstName+" "+self.lastName+ ", you are successfully registered to "+ thirdActivity+" activity")
                    dbConn.commit()
                    break
                elif choice == 4:
                    cur.execute("insert into Volunteering (activity_name, FirstName, LastName, Acv_date)values('{fA}','{fN}','{Ln}',sysdate)"\
                                .format(fA=fouthActivity,fN=self.firstName, Ln=self.lastName))
                    print(self.firstName+" "+self.lastName+ ", you are successfully registered to "+ fouthActivity+" activity")
                    dbConn.commit() 
                    break
            else:
                print('Please make your choice')
                                       
    def makeContribution(self):
        contributions = []
        contributions.append(self.ID)
               
        for i in contributions:
            while i == self.ID:
                print("\nlist of projects for contribution: \n1: Planting tree \n2: Cleaning Waste \n3: Plogging \n4: Other projects")
                firstCon = 'Planting tree'
                secondCon ='Cleaning waste'
                thirdCon = 'Plogging'
                fouthCon = 'Other projects'
                choice = eval(input("Choose of the contribution or suggestion: "))
                userCont = input('Provide your contribution to the project: ')
                
                if choice == 1:
                    cur.execute("insert into Prj_Contribution (name_project, first_Name, Last_Name, contribution, cont_date)values('{fA}','{fN}','{Ln}','{uC}', sysdate)"\
                                .format(fA=firstCon,fN=self.firstName, Ln=self.lastName, uC=userCont))
                    print(self.firstName+" "+self.lastName+ ", THANK YOU for contribution to "+ firstCon+' project')
                    dbConn.commit()
                    break
                elif choice == 2:
                    cur.execute("insert into Prj_Contribution (name_project, first_Name, Last_Name, contribution, cont_date)values('{fA}','{fN}','{Ln}','{uC}',sysdate)"\
                                .format(fA=secondCon,fN=self.firstName, Ln=self.lastName, uC=userCont))
                    print(self.firstName+" "+self.lastName+ ", THANK YOU for contribution to "+ secondCon+" project")
                    dbConn.commit()
                    break                        
                elif choice == 3:
                    cur.execute("insert into Prj_Contribution (name_project, first_Name, Last_Name, contribution, cont_date)values('{fA}','{fN}','{Ln}','{uC}',sysdate)"\
                                .format(fA=thirdCon,fN=self.firstName, Ln=self.lastName, uC=userCont))
                    print(self.firstName+" "+self.lastName+ ", THANK YOU for contribution to "+ thirdCon+" project")
                    dbConn.commit()
                    break
                elif choice == 4:
                    cur.execute("insert into Prj_Contribution (name_project, first_Name, Last_Name, contribution, cont_date)values('{fA}','{fN}','{Ln}','{uC}',sysdate)"\
                                .format(fA=fouthCon,fN=self.firstName, Ln=self.lastName, uC=userCont))
                    print(self.firstName+""+self.lastName+ ", THANK YOU for contribution to "+ fouthCon)
                    dbConn.commit()
                    break
            else:
                print('Please make your choice')
                
class PrintData:
    
    def getDataDB(self):
            
            print("\n1: List of Voleenters \n2: List of Contributed people")
            choice = eval(input("Please make your option: \n"))
            #while choice == 1 or choice == 0:
            if choice == 1:
                target_table = "Volunteering"
                command = ("select * from {}".format(target_table))
                cur.execute(command)
                with open('Volunteers.csv', 'w') as fileWrite:
                    for i in cur:
                        a, b, c, date = i
                        temp = (a, b, c, str(date.date()))
                        convToList=list(temp)
                        print(convToList)
                        fileWrite.write("\n {}".format(convToList))
                fileWrite.close()
                    
                    
            elif choice == 2:
                target_table = "Prj_Contribution"
                command = ("select * from {}".format(target_table))
                cur.execute(command)
                with open('Contribution.csv', 'w') as fileWrite:
                    for i in cur:
                        a, b, c, d, date = i
                        temp = (a, b, c, d, str(date.date()))
                        convToList=list(temp)
                        print(convToList)
                        fileWrite.write('\n {}'.format(convToList))     
                fileWrite.close()
                    
            else:
                print('Choose one of the option')

def main(): 
    
    #creating the account
    Jim = Volunteering()

    enterID = eval(input("Create your ID number: "))
               
    firstLastName = input("Enter your First and Last names: ")
    firstNameSplit = firstLastName.split(" " or ', ')
    fN=firstNameSplit[0]
    Ln=firstNameSplit[1]
    Jim.createAccount(enterID,fN,Ln)
      
    Jim.chooseActivity()
    
    Jim.makeContribution()
  
    getFromDB = PrintData()
    getFromDB.getDataDB()
   
    
main()