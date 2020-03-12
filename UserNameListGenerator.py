#UserName List Generator - D.Patrick Dugan
#There probably is a more pythonic way to do this...
import argparse
import sys

class UserNameGen(object):
        def __init__(self, usersfile, outfile):
                self.usersfile = usersfile
                self.outfile = outfile 
        
        #string functions here
        def FirstLast(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+lastName[0]+lastName[1:]
        def FirstLastNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:]+lastName[0]+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def FirstDotLast(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'.'+lastName[0]+lastName[1:]
        def FirstDotLastNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:]+'.'+lastName[0]+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def First_Last(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'_'+lastName[0]+lastName[1:]
        def First_LastNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:]+'_'+lastName[0]+lastName[1:]+str(num)+'\n' for num in range(0,11)])
       

        def FLast(self, firstName, lastName):
                return firstName[0]+lastName[0]+lastName[1:]
        def FLastNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+lastName[0]+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def FDotLast(self, firstName, lastName):
                return firstName[0]+'.'+lastName[0]+lastName[1:]
        def FDotLastNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+'.'+lastName[0]+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def F_Last(self, firstName, lastName):
                return firstName[0]+'_'+lastName[0]+lastName[1:]
        def F_LastNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+'_'+lastName[0]+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        

        def FirstL(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+lastName[0]
        def FirstLNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:]+lastName[0]+str(num)+'\n' for num in range(0,11)])
        def FirstDotL(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'.'+lastName[0]
        def FirstDotLNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:]+'.'+lastName[0]+str(num)+'\n' for num in range(0,11)])
        def First_L(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'_'+lastName[0]
        def First_LNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:]+'_'+lastName[0]+str(num)+'\n' for num in range(0,11)])

        def FirLas(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:3]+lastName[0].upper()+lastName[1:3]
        def FirLasNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:3]+lastName[0].upper()+lastName[1:3]+str(num)+'\n' for num in range(0,11)])
        def FirDotLas(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:3]+'.'+lastName[0].upper()+lastName[1:3]
        def FirDotLasNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:3]+'.'+lastName[0].upper()+lastName[1:3]+str(num)+'\n' for num in range(0,11)])
        def Fir_Las(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:3]+'_'+lastName[0].upper()+lastName[1:3]
        def Fir_LasNum(self, firstName, lastName):
                return ''.join([firstName[0].upper()+firstName[1:3]+'_'+lastName[0].upper()+lastName[1:3]+str(num)+'\n' for num in range(0,11)])

        def LastFirst(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:]+firstName[0].upper()+firstName[1:]
        def LastFirstNum(self, firstName, lastName):
                return ''.join([lastName[0].upper()+lastName[1:]+firstName[0].upper()+firstName[1:]+str(num)+'\n' for num in range(0,11)])
        def LastDotFirst(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:]+'.'+firstName[0].upper()+firstName[1:]
        def LastDotFirstNum(self, firstName, lastName):
                return ''.join([lastName[0].upper()+lastName[1:]+'.'+firstName[0].upper()+firstName[1:]+str(num)+'\n' for num in range(0,11)])
        def Last_First(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:]+'_'+firstName[0].upper()+firstName[1:]
        def Last_FirstNum(self, firstName, lastName):
                return ''.join([lastName[0].upper()+lastName[1:]+'_'+firstName[0].upper()+firstName[1:]+str(num)+'\n' for num in range(0,11)])

        def LasFir(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:3]+firstName[0].upper()+firstName[1:3]
        def LasFirNum(self, firstName, lastName):
                return ''.join([lastName[0].upper()+lastName[1:3]+firstName[0].upper()+firstName[1:3]+str(num)+'\n' for num in range(0,11)])
        def LasDotFir(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:3]+'.'+firstName[0].upper()+firstName[1:3]
        def LasDotFirNum(self, firstName, lastName):
                return ''.join([lastName[0].upper()+lastName[1:3]+'.'+firstName[0].upper()+firstName[1:3]+str(num)+'\n' for num in range(0,11)])
        def Las_Fir(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:3]+'_'+firstName[0].upper()+firstName[1:3]
        def Las_FirNum(self, firstName, lastName):
                return ''.join([lastName[0].upper()+lastName[1:3]+'_'+firstName[0].upper()+firstName[1:3]+str(num)+'\n' for num in range(0,11)])
        
        #same methods but all lowercase
        def firstlast(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+lastName[0].lower()+lastName[1:]
        def firstlastNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:]+lastName[0].lower()+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def firstDotlast(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'.'+lastName[0].lower()+lastName[1:]
        def firstDotlastNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:]+'.'+lastName[0].lower()+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def first_last(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'_'+lastName[0].lower()+lastName[1:]
        def first_lastNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:]+'_'+lastName[0].lower()+lastName[1:]+str(num)+'\n' for num in range(0,11)])
       
        def flast(self, firstName, lastName):
                return firstName[0].lower()+lastName[0].lower().lower()+lastName[1:]
        def flastNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+lastName[0].lower()+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def fDotlast(self, firstName, lastName):
                return firstName[0].lower()+'.'+lastName[0].lower()+lastName[1:]
        def fDotlastNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+'.'+lastName[0].lower()+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        def f_last(self, firstName, lastName):
                return firstName[0].lower()+'_'+lastName[0].lower()+lastName[1:]
        def f_lastNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+'_'+lastName[0].lower()+lastName[1:]+str(num)+'\n' for num in range(0,11)])
        
        def firstl(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+lastName[0].lower()
        def firstlNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:]+lastName[0].lower()+str(num)+'\n' for num in range(0,11)])
        def firstDotl(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'.'+lastName[0].lower()
        def firstDotlNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:]+'.'+lastName[0].lower()+str(num)+'\n' for num in range(0,11)])
        def first_l(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'_'+lastName[0].lower()
        def first_lNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:]+'_'+lastName[0].lower()+str(num)+'\n' for num in range(0,11)])

        def firlas(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:3]+lastName[0].lower()+lastName[1:3]
        def firlasNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:3]+lastName[0].lower()+lastName[1:3]+str(num)+'\n' for num in range(0,11)])
        def firDotlas(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:3]+'.'+lastName[0].lower()+lastName[1:3]
        def firDotlasNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:3]+'.'+lastName[0].lower()+lastName[1:3]+str(num)+'\n' for num in range(0,11)])
        def fir_las(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:3]+'_'+lastName[0].lower()+lastName[1:3]
        def fir_lasNum(self, firstName, lastName):
                return ''.join([firstName[0].lower()+firstName[1:3]+'_'+lastName[0].lower()+lastName[1:3]+str(num)+'\n' for num in range(0,11)])

        def lastfirst(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:]+firstName[0].lower()+firstName[1]
        def lastfirstNum(self, firstName, lastName):
                return ''.join([lastName[0].lower()+lastName[1:]+firstName[0].lower()+firstName[1:]+str(num)+'\n' for num in range(0,11)])
        def lastDotfirst(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:]+'.'+firstName[0].lower()+firstName[1:]
        def lastDotfirstNum(self, firstName, lastName):
                return ''.join([lastName[0].lower()+lastName[1:]+'.'+firstName[0].lower()+firstName[1:]+str(num)+'\n' for num in range(0,11)])
        def last_first(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:]+'_'+firstName[0].lower()+firstName[1:]
        def last_firstNum(self, firstName, lastName):
                return ''.join([lastName[0].lower()+lastName[1:]+'_'+firstName[0].lower()+firstName[1:]+str(num)+'\n' for num in range(0,11)])

        def lasfir(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:3]+firstName[0].lower()+firstName[1:3]
        def lasfirNum(self, firstName, lastName):
                return ''.join([lastName[0].lower()+lastName[1:3]+firstName[0].lower()+firstName[1:3]+str(num)+'\n' for num in range(0,11)])
        def lasDotfir(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:3]+'.'+firstName[0].lower()+firstName[1:3]
        def lasDotfirNum(self, firstName, lastName):
                return ''.join([lastName[0].lower()+lastName[1:3]+'.'+firstName[0].lower()+firstName[1:3]+str(num)+'\n' for num in range(0,11)])
        def las_fir(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:3]+'_'+firstName[0].lower()+firstName[1:3]
        def las_firNum(self, firstName, lastName):
                return ''.join([lastName[0].lower()+lastName[1:3]+'_'+firstName[0].lower()+firstName[1:3]+str(num)+'\n' for num in range(0,11)])
        
        @staticmethod
        def outputUserName(lineEntry, f=None):
                if f is None:
                        print(lineEntry)
                else:
                        f.write(lineEntry + '\n')             

        def load_users_file(self):
                with open(self.usersfile) as names:
                        usernames = [line.strip() for line in names]
                self.generate_user_names(usernames)

        def generate_user_names(self, usernames):
                functions = [
                        self.FirstLast, self.FirstLastNum, self.FirstDotLast, self.FirstDotLastNum,self.First_Last, self.First_LastNum,
                        self.FLast, self.FLastNum, self.FDotLast, self.FDotLastNum, self.F_Last, self.F_LastNum,
                        self.FirstL, self.FirstLNum, self.FirstDotL, self.FirstDotLNum, self.First_L, self.First_LNum,
                        self.FirLas, self.FirLasNum, self.FirDotLas, self.FirDotLasNum, self.Fir_Las, self.Fir_LasNum,
                        self.LastFirst, self.LastFirstNum, self.LastDotFirst, self.LastDotFirstNum, self.Last_First, self.Last_FirstNum,
                        self.LasFir, self.LasFirNum,  self.LasDotFir, self.LasDotFirNum, self.Las_Fir, self.Las_FirNum,
                        #lowercase functions
                        self.firstlast, self.firstlastNum, self.firstDotlast, self.firstDotlastNum,self.first_last, self.first_lastNum,
                        self.flast, self.flastNum, self.fDotlast, self.fDotlastNum, self.f_last, self.f_lastNum,
                        self.firstl, self.firstlNum, self.firstDotl, self.firstDotlNum, self.first_l, self.first_lNum,
                        self.firlas, self.firlasNum, self.firDotlas, self.firDotlasNum, self.fir_las, self.fir_lasNum,
                        self.lastfirst, self.lastfirstNum, self.lastDotfirst, self.lastDotfirstNum, self.last_first, self.last_firstNum,
                        self.lasfir, self.lasfirNum,  self.lasDotfir, self.lasDotfirNum, self.las_fir, self.las_firNum,
                        ]
                if self.outfile is not None:
                        f = open(self.outfile, 'w+')
                else:
                        f = None
                for name in usernames:
                        try:
                                firstName, lastName = name.split()
                                for fn in functions:
                                        lineEntry = fn(firstName, lastName)
                                        self.outputUserName(lineEntry, f)
                        except Exception as e:
                            print(e)
                            continue
                if f is not None:
                        f.close()

if __name__ == '__main__':
        parser = argparse.ArgumentParser(add_help= True, description= "Generates a list of usernames based off of standard naming conventions.")
        parser.add_argument('usersfile', help="File with names to generate list from in 'FirstName LastName' format")
        parser.add_argument('-o','--outfile',action='store', help= "File to save generated usernames in.")

        if len(sys.argv)==1:
                parser.print_help()
                sys.exit(1)
        
        args = parser.parse_args()
        try:
                executer = UserNameGen(args.usersfile, args.outfile)
                executer.load_users_file()
        except Exception as e:
                print(e)