#UserName List Generator - D.Patrick Dugan
#There probably is a more pythonic way to do this...
import argparse
import sys

class UserNameGen(object):
        def __init__(self, username, usersfile, outfile, numappend, email):
                self.username = username
                self.usersfile = usersfile
                self.outfile = outfile 
                self.numappend = numappend
                self.email = email
        
        #string functions here
        def FirstLast(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+lastName[0]+lastName[1:]
        def FirstDotLast(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'.'+lastName[0]+lastName[1:]
        def First_Last(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'_'+lastName[0]+lastName[1:]
        
        def FLast(self, firstName, lastName):
                return firstName[0]+lastName[0]+lastName[1:]
        def FDotLast(self, firstName, lastName):
                return firstName[0]+'.'+lastName[0]+lastName[1:]
        def F_Last(self, firstName, lastName):
                return firstName[0]+'_'+lastName[0]+lastName[1:]

        def FirstL(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+lastName[0]
        def FirstDotL(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'.'+lastName[0]
        def First_L(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:]+'_'+lastName[0]

        def FirLas(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:3]+lastName[0].upper()+lastName[1:3]
        def FirDotLas(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:3]+'.'+lastName[0].upper()+lastName[1:3]
        def Fir_Las(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:3]+'_'+lastName[0].upper()+lastName[1:3]

        def FiLast(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:2]+lastName[0].upper()+lastName[1:]
        def FiDotLast(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:2]+'.'+lastName[0].upper()+lastName[1:]
        def Fi_Last(self, firstName, lastName):
                return firstName[0].upper()+firstName[1:2]+'_'+lastName[0].upper()+lastName[1:]

        def LastFirst(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:]+firstName[0].upper()+firstName[1:]
        def LastDotFirst(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:]+'.'+firstName[0].upper()+firstName[1:]
        def Last_First(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:]+'_'+firstName[0].upper()+firstName[1:]

        def LasFir(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:3]+firstName[0].upper()+firstName[1:3]
        def LasDotFir(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:3]+'.'+firstName[0].upper()+firstName[1:3]
        def Las_Fir(self, firstName, lastName):
                return lastName[0].upper()+lastName[1:3]+'_'+firstName[0].upper()+firstName[1:3]
        
        #same methods but all lowercase
        def firstlast(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+lastName[0].lower()+lastName[1:]
        def firstDotlast(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'.'+lastName[0].lower()+lastName[1:]
        def first_last(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'_'+lastName[0].lower()+lastName[1:]

        def flast(self, firstName, lastName):
                return firstName[0].lower()+lastName[0].lower().lower()+lastName[1:]
        def fDotlast(self, firstName, lastName):
                return firstName[0].lower()+'.'+lastName[0].lower()+lastName[1:]
        def f_last(self, firstName, lastName):
                return firstName[0].lower()+'_'+lastName[0].lower()+lastName[1:]
        
        def firstl(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+lastName[0].lower()
        def firstDotl(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'.'+lastName[0].lower()
        def first_l(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:]+'_'+lastName[0].lower()

        def firlas(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:3]+lastName[0].lower()+lastName[1:3]
        def firDotlas(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:3]+'.'+lastName[0].lower()+lastName[1:3]
        def fir_las(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:3]+'_'+lastName[0].lower()+lastName[1:3]

        def filast(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:2]+lastName[0].lower()+lastName[1:]
        def fiDotlast(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:2]+'.'+lastName[0].lower()+lastName[1:]
        def fi_last(self, firstName, lastName):
                return firstName[0].lower()+firstName[1:2]+'_'+lastName[0].lower()+lastName[1:]

        def lastfirst(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:]+firstName[0].lower()+firstName[1]
        def lastDotfirst(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:]+'.'+firstName[0].lower()+firstName[1:]
        def last_first(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:]+'_'+firstName[0].lower()+firstName[1:]

        def lasfir(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:3]+firstName[0].lower()+firstName[1:3]
        def lasDotfir(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:3]+'.'+firstName[0].lower()+firstName[1:3]
        def las_fir(self, firstName, lastName):
                return lastName[0].lower()+lastName[1:3]+'_'+firstName[0].lower()+firstName[1:3]
        
        @staticmethod
        def outputUserName(lineEntry, f=None):
                if f is None:
                        print(lineEntry)
                else:
                        f.write(lineEntry + '\n')        
        
        def run(self):
                usernames = [self.username]
                self.generate_user_names(usernames)
                        
        def load_users_file(self):
                with open(self.usersfile) as names:
                        usernames = [line.strip() for line in names]
                self.generate_user_names(usernames)

        def generate_user_names(self, usernames):
                # if self.numappend is False:
                functions = [
                        self.FirstLast, self.FirstDotLast, self.First_Last,
                        self.FLast, self.FDotLast, self.F_Last, 
                        self.FirstL, self.FirstDotL, self.First_L, 
                        self.FirLas, self.FirDotLas, self.Fir_Las, 
                        self.FiLast, self.FiDotLast, self.Fi_Last,
                        self.LastFirst, self.LastDotFirst, self.Last_First, 
                        self.LasFir, self.LasDotFir, self.Las_Fir, 
                        #lowercase functions
                        self.firstlast, self.firstDotlast, self.first_last, 
                        self.flast, self.fDotlast, self.f_last, 
                        self.firstl, self.firstDotl, self.first_l, 
                        self.firlas, self.firDotlas, self.fir_las,
                        self.filast, self.fiDotlast, self.fi_last,
                        self.lastfirst, self.lastDotfirst, self.last_first,
                        self.lasfir, self.lasDotfir, self.las_fir, 
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
                                        if self.numappend:
                                                if self.email:
                                                        self.outputUserName(lineEntry+self.email, f)
                                                numrange = self.numappend.split(',')
                                                for num in range(int(numrange[0]), int(numrange[1])+1):
                                                        if self.email:
                                                                self.outputUserName(lineEntry+str(num)+self.email, f)
                                                        else:
                                                                self.outputUserName(lineEntry+str(num), f)   
                                        elif self.email:
                                                self.outputUserName(lineEntry+self.email, f)
                                        else: 
                                                self.outputUserName(lineEntry, f)
                        except Exception as e:
                            print(e)
                            continue
                if f is not None:
                        f.close()

if __name__ == '__main__':
        parser = argparse.ArgumentParser(add_help= True, description= "Generates a list of usernames based off of standard naming conventions.")
        parser.add_argument('-u','--username', help="Name of the user to enumerate. 'First Last' format")
        parser.add_argument('-U','--usersfile', help="File with names to generate list in 'First Last' format")
        parser.add_argument('-o','--outfile', action='store', help= "File to save generated usernames in.")
        parser.add_argument('-n',  help='Adds number range to every naming convention. Must be in "x,y" format.')
        parser.add_argument('-e', '--email', help="Appends '@domain.com' to all generated usernames")

        if len(sys.argv)==1:
                parser.print_help()
                sys.exit(1)
        
        args = parser.parse_args()

        try:
                executer = UserNameGen(args.username, args.usersfile, args.outfile, args.n, args.email)
                if executer.usersfile is not None:
                        executer.load_users_file()
                elif executer.username is not None:
                        executer.run()
                else:
                        parser.print_help()
        except Exception as e:
                print(e)