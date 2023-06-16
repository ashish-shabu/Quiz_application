import csv
from os import system
import os
import winsound
import json
import getpass
import warnings
import random
from string import digits,ascii_letters,punctuation
from glob import glob
def starting(z=0):
    if z==0:
        f=open("assets/psd.bin","wb")
        c='y'
        while c in ('Y','y'):
            print("Use 6 or more characters with a mix of letters,numbers & symbols")
            psd=input("Create password ")
            s=input("confirm ")
            if psd!=s:
                print("! Those passwords didn't match. Try again.")
            else:
                if psdvaild(psd):
                    print("Password is valid")
                    c='n'
                else:
                    print("Invalid Password !!")
                    print()
        hint=input("Enter a Recovery Key: ")
        g=[len(hint)]
        psd+=hint
        a=[ord(i) for i in psd]
        print("Please enter a nonnegative order(number) for security!")
        print("For more protection enter an order from the interval [4,32]")
        k=int(input("Enter the order: "))
        if k<=0:
            print("invalid order")
            winsound.Beep(440, 500)
            k=int(input("Enter a new order: "))
            if k<=0:
                print("invalid order!!!")
                winsound.Beep(440, 500)
                print("The order has changed to the default value: 9")
                k=9
        t=[int(i) for i in str(k)]
        l2=[len(t)]
        qr=[i//k for i in a]+[i%k for i in a]+t+g+l2
        f.write(bytearray(qr))
        f.close()
        print("Password entered successfully!!!")
        winsound.PlaySound("assets/03.wav",winsound.SND_FILENAME)
    else:
        with open('assets/passwords.csv','r') as filein:
                reader=csv.reader(filein)
                l=[]
                for row in reader:
                    if z==row[0]:
                        c="y"
                        while c in ('Y','y'):
                            print("Use 6 or more characters with a mix of letters,numbers & symbols")
                            row[1]=input("Create password ")
                            q=input("confirm ")
                            if row[1]!=q:
                                print("! Those passwords didn't match. Try again.")
                            else:
                                if psdvaild(row[1]):
                                    print("Password is valid")
                                    print()
                                    c='n'
                                else:
                                    print("Invalid Password !!")
                                    print()
                        print("Create a recovery key...!")
                        print("This will help you reset your password if you forget it.")
                        row[2]=input("Enter a Recovery Key : ")
                    l.append(row)       
                with open('assets/passwords.csv','w',newline='') as fileout:
                    csvwriter = csv.writer(fileout)
                    csvwriter.writerows(l)
                    print("Password entered successfully!!!")
                    winsound.PlaySound("assets/03.wav",winsound.SND_FILENAME)        
    
def APsdUplogin(q):
    n,h=pcheck()
    ch="y"
    i=0
    while ch in ('Y','y'):
        winsound.PlaySound("assets/01.wav",winsound.SND_FILENAME)
        if q==1:
            print("Enter the Admin passord to continue: ",end='')
        elif q==2:
            print("Enter the password for Confirmation: ",end='')
        t=input()
        if t==n:
            winsound.PlaySound("assets/07.wav",winsound.SND_FILENAME)
            print("\n System Starting.... \a\a\a\a\a\a")
            if q==1:
                start(1)
                break
            elif q==2:
                ch=input("Do you want to change the password?(Y/N)")
                if  ch in ('Y','y'):
                    print("Enter a new password: ",end='')
                    winsound.PlaySound("assets/05.wav",winsound.SND_FILENAME)
                    starting()
                    break
               
        else:
            print("\n... Entered Password is wrong ...")
            if i==5:
                print("No attempts left !")
            else:
                print('Attempts Remaining:',5-i,"!"*i)
            winsound.PlaySound("assets/06.wav",winsound.SND_FILENAME)
            i+=1
            if i==6:
                print("Forgot your password ?")
                while ch in ('y','Y'):
                    h1=input("Enter Your Recovery Key: ")
                    if h1==h:
                        print("Enter a new password :")
                        winsound.PlaySound("assets/05.wav",winsound.SND_FILENAME)
                        starting()
                        n,h=pcheck()
                        i=0
                        break
                    else:
                        print("\n... Entered Recovery Key is wrong ...")
                        winsound.PlaySound("assets/06.wav",winsound.SND_FILENAME)
                        ch=input("Do you want to continue?(Y/N)")

def PlayerSearch(j,ch,r=0):
    if ch==1:
        r=input("\n Enter the Name to search : ")
    elif ch==2:
        if r==0:
            r=input("\n Enter the User Id to search : ")
    if j==1:
        filein=open('assets/details.csv','r')
        if len(filein.readlines())==1:
            print("No one has registered yet")
            found=1
        else:
            filein.seek(0)
            found=0
        reader=csv.reader(filein)
        for row in reader:
            uid,name,email,age,dob,school,pno=row
            if row[2-ch]==r:
                print("User ID: ",uid)
                print("Player Name: ",name)
                print("Email: ",email)
                print("Age: ",age)
                print("DOB: ",dob)
                print("School: ",school)
                print("Phonenumber: ",pno)
                found=1
    else:
        filein=open('assets/results.csv','r')
        if len(filein.readlines())==1:
            print()
            print("No one has played the game!!!")
            found=1
        else:
            filein.seek(0)
            found=0
        reader=csv.reader(filein)
        for row in reader:
            uid,name,c,ic,score,p=row
            if row[2-ch]==r:
                print("User ID: ",uid)
                print("Player Name: ",name)
                print("No of correct answer: ",c)
                print("No of incorrect answer: ",ic)
                print("Total Score: ",score)
                print("Percentage: ",p)
                found=1
    if(found==0):
         print("\n Entered Name not found in search!!! ")
         filein.close()

def PlayerList(w1):
    if w1==1:
        filein=open('assets/details.csv','r')
        if len(filein.readlines())!=1:
            filein.seek(0)
            reader=csv.reader(filein)
            print(f"{'User ID' :^10}{'Player Name' :^30}{'Email ID' :^35}{'Player Age' :^20}{'Date Of Birth' :^30}{'School Name' :^30}{'Phone Number' :^25}")
            next(reader)
            for row in reader:
                uid,name,email,age,dob,school,pno=row
                print(f"{uid :^10}{name :^30}{email :^35}{age :^20}{dob :^30}{school :^30}{pno :^25}")
        else:
            print("No one has registered yet")
        filein.close()
    else:
        filein=open('assets/results.csv','r')
        if len(filein.readlines())!=1:
            filein.seek(0)
            reader=csv.reader(filein)
            print(f"{'User ID' :<10}{'Player Name' :^30}{'No of Questions' :^30}{'No of correct answers' :^30}{'No of incorrect answers' :^20}{'Total Score' :^30}{'Percentage' :>10}")
            next(reader)
            for row in reader:
                uid,name,n,c,ic,score,p=row
                print(f"{uid :<10}{name :^30}{n :^30}{c :^30}{ic :^20}{score :^30}{p :>10}")
        else:
            print("No one has played this game!!!")
        filein.close()
        
def clrscreen():
    system("cls")
def Help(r):
    if r==1:print('''Admin Functionalities...
    ⁕ Setup Admin Panal
    ⁕ Login/Logout
    ⁕ View Player Details, Reports, Feedbacks ,Reviews
    ⁕ Add/Update Questions
    ⁕ View/Update Admin Password
    ⁕ Full Control of all files''')   
        
    else:print('''Player Functionalities...
    ⁎ Register/Login/Logout
    ⁎ Play
    ⁎ View your Details/Report
    ⁎ Write Feedbacks/Reviews")
    ⁎ View User ID and Password/Update Password''')    
def pcheck(d=0):
    if d==0:
        f=open("assets/psd.bin","rb")
        n=list(f.read())
        k=1
        g=1
        if len(n)>0:
            l2=n[-1]
            g=n[-2]
            k=n[-(2+l2):-2]
            k=int(''.join([str(i) for i in k]))
            n=n[:-(2+l2)]
        l=len(n)//2
        f.close()
        qr=[i for i in zip(n[:l],n[l:])]
        a=[chr(k*i[0]+i[1]) for i in qr]
        a=''.join(a)
        n=a[:-g]
        h=a[-g:]
        return n,h
    else:
        with open('assets/passwords.csv','r') as filein:
            reader=csv.reader(filein)
            for row in reader:
                u,p,r=row
                if d==u:
                    return u,p,r

def play(e,l):
    score = 0
    with open(l, 'r+') as f:
        try:
            j = json.load(f)
            n = len(j)
            if n<10:
                print("Sorry!! Questions not entered yet")
                print()
                return
            else:
                print('''\n==========RULES==========
1. Each round consists of 10 random questions.
   To answer, you must press A/B/C/D (case-insensitive).
   Your final score will be given at the end.
2. Each question consists of 1 point.
   There's no negative point for wrong answers.''')
                print("\n==========QUIZ START==========")
        except:
            print("Sorry!! Questions not entered yet")
            return
        for i in range(10):
            ch = random.randint(0, n-1)
            print(f'\nQ{i+1} {j[ch]["question"]}\n')
            for option in j[ch]["options"]:
                print(option)
            answer = input("\nEnter your answer: ")
            try:
                if j[ch]["answer"][0] == answer[0].upper():
                    print("\nYou are correct")
                    score+=1
                else:
                    print("\nYou are incorrect")
                    print("The correct answer is Option",j[ch]["answer"])
            except:
                print("\nYou are incorrect")
                print("The correct answer is Option",j[ch]["answer"])
            del j[ch]
            if i==9:    
                c=score
                ic=10-score
                p=str(round((c/10)*100,2))+'%'
                print(f'\nUser ID: {e}')
                print(f'\nNo Of Correct Answers: {c}')
                print(f'\nNo Of Incorrect Answers: {ic}')
                print(f'\nFINAL SCORE: {score}')
                print(f'\nPERCENTAGE: {p}')
                with open('assets/details.csv', 'r') as filein:
                    reader=csv.reader(filein)
                    for row in reader:
                        uid,name=row[0],row[1]
                        if uid==e:
                            fileout=open("assets/results.csv","a",newline='')
                            writer = csv.writer(fileout,delimiter=',')
                            writer.writerow([uid,name,c,ic,score,p])
                            fileout.close()
                            
                
                


def quizQuestions(w,z=0):
    if z==0:
        print('\n==========ADD QUESTIONS==========\n')
        ques = input("Enter the question that you want to add:\n")
        print("Enter the 4 options with character initials (A, B, C, D)")
        opt = [input() for i in range(4)]
        ans = input("Enter the answer:\n")
        with open(w, 'r+') as f:
            '''try:
                q=json.load(f)
            except:
                q=[]'''
            q=json.load(f)
            q+=[{"question": ques, "options": opt, "answer": ans}]
            f.seek(0)
            json.dump(q, f)
            print("Question successfully added.")
            
    else:
         with open(w, 'r') as f:
            try:
                j = json.load(f)
            except:
                j=[]
            n = len(j)
            if n==0:
                    print("No Questions entered yet")
                    return
            ch=input("Do you want to update the questions(Y/N)")
            while ch in('y','Y'):
                print("1. Edit individually")
                print("2. Delete all")
                choice=input("Enter Your Choice: ")
                if choice=='1':
                    print("U. Update")
                    print("D. Delete")
                    v=input("Enter Your Choice: ").upper()
                    du(j,v,n)
                    ch='n'

                elif choice=='2':
                    j=[]
                    ch='n'
                else:
                    print("invalid choice")
                    ch=input("Do you want to continue(Y/N)")
            with open(w, 'w') as f:
                json.dump(j, f)
         
def see(j,k=0,b=0,m=0):
    if m==0:
        if b==0:
            print("Before editing....")
        else:
            print("After editing....")
        print(f'\nQ{k} {j[k-1]["question"]}\n')
        for option in j[k-1]["options"]:
            print(option)
        print("The correct answer Option",j[k-1]["answer"])
        print()
    else:
        with open(j, 'r+') as f:
            try:
                q = json.load(f)
                f.close()
            except:
                q=[]
            n = len(q)
            if n==0:
                    print("No Questions entered yet")
                    print()
            else:
                for i in range(n):
                    print(f'\nQ{i+1} {q[i]["question"]}\n')
                    for option in q[i]["options"]:
                        print(option)
                    print("The correct answer Option",q[i]["answer"])
                    print()
    
def du(j,v,n):
    print("No of questions =",n)
    if v=='U':
        while 1:
            k=int(input("Enter Q.No to change: "))
            while 1:
                if k in range(0,n+1):
                    break
                else:
                    print("Q.No out of range..!")
                    k=int(input("Enter a new Q.No: "))    
            print("Displaying for confirmation!")
            print(f'\nQ{k} {j[k-1]["question"]}\n')
            c=input("Is this the question?(Y/N): ")
            if c in ('y','Y'):
                see(j,k)
                while 1:
                    print("What you can do")
                    print('1. edit question')
                    print('2. edit answer')
                    print('3. change options')
                    c1=input("Enter your choice: ")
                    if c1=='1':
                        print("Current question: ",j[k-1]["question"])
                        j[k-1]["question"]=input("edit the question as: ")
                        see(j,k,1)
                    elif c1=='2':
                        print("Current answer: ",j[k-1]["answer"])
                        j[k-1]["answer"]=input("edit the answer (with character initials (A, B, C, D)[options]) as: ")
                        see(j,k,1)
                    elif c1=='3':
                        g=['A','B','C','D']
                        while 1:
                            print('Enter the option',g,'to change: ',end='')
                            l=input().upper()
                            if l=='A':
                                print("Current option ",j[k-1]["options"][0])
                                j[k-1]["options"][0]='A. '+input("edit option as: ")
                                g.remove('A')
                            elif l=='B':
                                print("Current option ",j[k-1]["options"][1])
                                j[k-1]["options"][1]='B. '+input("edit option as: ")
                                g.remove('B')
                            elif l=='C':
                                print("Current option ",j[k-1]["options"][2])
                                j[k-1]["options"][2]='C. '+input("edit option as: ")
                                g.remove('C')
                            elif l=='D':
                                print("Current option ",j[k-1]["options"][3])
                                j[k-1]["options"][3]='D. '+input("edit option as: ")
                                g.remove('D')
                            if len(g)==0:
                                break
                            else:
                                see(j,k,1)
                                l=input("Do you want to edit other options ?(Y/N): ")
                                if l not in ('y','Y'):
                                    see(j,k,1)
                                    break
                    else:
                        print("invalid choice")
                        print("Try again")
                    if c1 in ('1','2','3'):
                        print("More edition needed for Q.No",k,".... ?(Y/N): ",end='')
                        c=input()
                        if c not in ('y','Y'):
                            break
                    
                k=input("Do you want to edit other questions?(Y/N): ")
                if k not in ('y','Y'):
                    return j
            else:
                print("Q.No might be wrong!")
                print("Try again!!!")
    elif v=='D':
        print('''Warning! Q.No changes after every deletion.....
The Successor will get the Q.No of Predecessor..
e.g If you delete Q.No 2, after deletion Q.No 3 will become Q.No 2 and so on
So be careful while entering the Q.Nos'.........''')
        while 1:
            k=int(input("Enter Q.No to delete: "))
            print("Displaying for confirmation!")
            print(f'\nQ{k} {j[k-1]["question"]}\n')
            c=input("Is this the question?(Y/N): ")
            if c in ('y','Y'):
                j.pop(k-1)
                print("Question deleted successfully....")
                print('''.............................
.................
.........
.''')
                
                k=input("Do you want to delete other questions?(Y/N): ")
                if k not in ('y','Y'):
                    #break
                    return j
            else:
                print("Q.No might be wrong!")
                print("Try again!!!")

            
def details(userid):
    print("Enter Your Details Below")
    name=input("Name:")
    email=input("Email:")   
    age=int(input("Age(in digits):"))
    dob=input("DOB(eg dd/mm/yyyy):")
    school=input("School Name:")
    phonenumber=input("Phone Number:")
    fileout=open("assets/details.csv","a",newline='')
    writer = csv.writer(fileout)
    writer.writerow([userid,name,email,age,dob,school,phonenumber])
    fileout.close()
    psd=ascii_letters+digits+'@'+'#'+'_'
    while 1:
        password=random.sample(psd,6)
        pswd=("".join(password))
        if psdvaild(pswd,1):
            break;
    print("Creating User.....")
    print("Your User Id is",userid)
    print("Generating a strong Password.............")
    print("Suggested password :",pswd)
    c=input("Use suggested password(Y/N)")
    while c in ('N','n'):
        print("Use 6 or more characters with a mix of letters,numbers & symbols")
        pswd=input("Create password ")
        t=input("confirm ")
        if pswd!=t:
            print("! Those passwords didn't match. Try again.")
        else:
            if psdvaild(pswd):
                print("Password is valid")
                c='y'
            else:
                print("Invalid Password !!")
    print("Create a recovery key...!")
    print("This will help you reset your password if you forget it.")
    rkey=input("Enter a Recovery Key : ")
    filein=open("assets/passwords.csv","a",newline='')
    writer = csv.writer(filein,delimiter=',')
    writer.writerow([userid,pswd,rkey])
    filein.close()
    print()
    print("Details Entered Successfully")
    print("Your User Id is",userid)
    print("Your password is",pswd)
    print("Your recovery key is",rkey)



def fcheck(j,f=0,h1=0,l=0,p=0):
    if j==1:
        isfile=os.path.isfile('assets/psd.bin')
        if f==0:
            ie(isfile,j)
        else:
            return isfile
    elif j==2:
        isfile=os.path.isfile(l)
        if isfile:
            isfile=os.path.getsize(l)!=0
        if f==0:
            ie(isfile,j,l,p)
        else:
            return isfile
    elif j==3:
        if f==0:
            isfile=os.path.isfile('assets/details.csv') and os.path.isfile('assets/passwords.csv')
            if isfile:
                isfile=os.path.getsize('assets/details.csv')!=0 and os.path.getsize('assets/passwords.csv')!=0
            if l==0 :
                ie(isfile,j)
            else:
                return isfile
        else:
            isfile=os.path.isfile('assets/results.csv')
            if isfile:
                isfile=os.path.getsize('assets/results.csv')!=0
            if l==0:
                ie(isfile,j,f,h1,p)
            else:
                return isfile
    elif j==4:
        isfile=os.path.isfile('assets/feedbacks.txt')
        if isfile:
            isfile=os.path.getsize('assets/feedbacks.txt')!=0
def ie(u,v,w=0,h2=0,y=0):
    if u:
        if v==1:
            APsdUplogin(1)
        elif v==2:
            quizQuestions(w,h2)
        elif v==3:
            if w==0:
                fn=open('assets/passwords.csv','r')
                f=fn.readlines()
                l1=len(f)-1
                userid=10000
                if l1>0:
                    userid+=l1 
                fn.close()
                usercheck(userid)
            else:
                if fcheck(2,1,l=y):
                    play(h2,y)
                else:
                    print("Sorry!! Questions not entered yet")
                    print()
    else:
        if v==1:
            print("Welcome to Admin Profile Creation Tool")
            print("Lets get started !!")
            print("Enter a password for admin panal!!")
            winsound.PlaySound("assets/05.wav",winsound.SND_FILENAME)
            starting()
            f=input("Do you want to continue?(Y/N): ")
            if f in ('Y','y'):
                APsdUplogin(1)
        elif v==2:
            f1= open(w, "w")
            q=[]
            json.dump(q, f1)
            f1.close()
            quizQuestions(w,h2)
        elif v==3:
            if w==0:
                f1= open("assets/details.csv", "w")
                f1.write("User ID,Name,Email,Age,DOB,School,Phonenumber\n")
                f1.close()
                f2=open("assets/passwords.csv","w")
                f2.write('User ID,Password,Recovery Key\n')
                f2.close()
                usercheck(10000)
            else:
                f1= open("assets/results.csv", "w")
                f1.write("User ID,Name,No of Qns,Correct,Incorrect,Score,Percentage\n")
                f1.close()
                if fcheck(2,1,l=y):
                    play(h2,y)
                else:
                    #print("Game not started yet!!")
                    print("Sorry!! Questions not entered yet")
                    print()
        

def user(y=0):
    print("A. Admin")
    print("P. Player")
    while 1:
        choice=input("Enter Your Choice: ").upper()
        if choice=='A':
            print()
            print("Welcome To Admin Portal")
            fcheck(1)
            break
        elif choice=='P':
            print()
            print("Welcome To Player Portal")
            fcheck(3)
            break
        else:
            print("Invalid choice!")
            print("Try Again!!")
            print()
            
        
def login(q):
    ch="y"
    found=0
    i=0
    k=0
    while ch in ('Y','y'):
        if q==1:
            print("Enter the User Id:",end='')
        elif q==2:
            print("Enter the User Id for Confirmation:",end='')
        winsound.PlaySound("assets/01.wav",winsound.SND_FILENAME)
        t=input()
        try:
            u,p,r=pcheck(t)
            while ch in ('Y','y'):
                if q==1:
                    print("Enter the passord:",end='')
                elif q==2:
                    print("Enter the password for Confirmation:",end='')
                winsound.PlaySound("assets/05.wav",winsound.SND_FILENAME)
                upwd=input()
                if upwd==p:
                    winsound.PlaySound("assets/07.wav",winsound.SND_FILENAME)
                    print("\n System Starting.... \a\a\a\a\a\a")
                    if q==1:
                        start(2,u,p)
                        ch="n"
                        return ch
                    elif q==2:
                        ch=input("Do you want to change the password?(Y/N): ")
                        if  ch in ('Y','y'):
                            print("Enter a new password !!")
                            winsound.PlaySound("assets/05.wav",winsound.SND_FILENAME)
                            starting(u)
                            ch='n'
                            print()
                            break
                else:
                    print("\n... Entered Password is wrong ...")
                    if i==5:
                        print("No attempts left !")
                    else:
                        print('Attempts Remaining:',5-i,"!"*i)
                    winsound.PlaySound("assets/06.wav",winsound.SND_FILENAME)
                    i+=1
                    if i==6:
                        print("Forgot your password ?")
                        while ch in ('y','Y'):
                            h1=input("Enter Your Recovery Key: ")
                            if h1==r:
                                print("Enter a new password :")
                                winsound.PlaySound("assets/05.wav",winsound.SND_FILENAME)
                                starting(u)
                                u,p,r=pcheck(t)
                                i=0
                                print()
                                print("please enter your new password to continue!!!")
                                print("..........................")
                                print("................")
                                print("........")
                                break
                            else:
                                print("\n... Entered Recovery Key is wrong ...")
                                winsound.PlaySound("assets/06.wav",winsound.SND_FILENAME)
                                ch=input("Do you want to continue?(Y/N)")
        except:
            k+=1
            print()
            print("Couldn't find your Account!")
            print("Incorrect User Id")
            if k==3:
                winsound.PlaySound("assets/06.wav",winsound.SND_FILENAME) 
                print("It seems like you are not registered!!")
                print("Returning to the home screen....")
                print("Welcome Back To  The Player Portal")
                print("1. Login")
                print("2. Register")
                print()
                return ch
                
            else:
                print("Try Again!!")
                winsound.PlaySound("assets/06.wav",winsound.SND_FILENAME)

def usercheck(o=0):
    if fcheck(1,1,):
        print("1. Login")
        print("2. Register")
        ch='y'
        while ch in ('Y','y'):
            try:
                choice=int(input("Enter Your Choice: "))
            except:
                choice=0
            if choice==1:
                ch=login(1)
            elif choice==2:
                details(o)
                f=input("Do you want to continue?(Y/N): ")
                if f in ('Y','y'):
                    ch=login(1)
                break
            else:
                print("Invalid choice")
                print("Try again!!")
                print()
                
    else:
        print()
        print("Sorry!! Registration not started yet")

def feedbacks(e1):
    if e1==1:
        with open('assets/feedbacks.txt', 'a') as fo:
            fo.write(input()+'\n')
            print("Thanks for your feedback...")
    elif e1==2:
        with open('assets/feedbacks.txt', 'r') as fo:
            for each in fo:
                print("*",each, end='')


def psdvaild(passwd,l=0):
    SpecialSym=punctuation
    val = True
    if len(passwd) < 6:
        if l==0:print('length should be at least 6')
        val = False          
    if len(passwd) > 20:
        if l==0:print('length shouldnot be greater than 20')
        val = False
    if passwd.startswith(" ") or passwd.endswith(" "):
        if l==0:print("Your Password can't start or end with a blankspace")
        val = False
    if not any(char.isdigit() for char in passwd):
        if l==0:print('Your Password should have at least one numeral')
        val = False          
    if not any(char.isupper() for char in passwd):
        if l==0:print('Your Password should have at least one uppercase letter')
        val = False          
    if not any(char.islower() for char in passwd):
        if l==0:print('Your Password should have at least one lowercase letter')
        val = False          
    if not any(char in SpecialSym for char in passwd):
        if l==0:print('Your Password should have at least one Special character ($@#_...)')
        val = False
    if val:
        return val

def about():
    print()
    print('''
            Quiz Generator
             Version 1.01
The latest version is already installed
''')

def start(v,h=0,s=0):
    while 1:
        if v==1:
            print("1. Player Details")
            print("2. Reports")
            print("3. View Feedbacks")
            print("4. Quiz Questions")
            print("5. See Admin Password")
            print("6. Change Admin Password")
            print("7. Help")
            print("8. Quit")
            print("9. About Us")
        else:
            print("1. Play")
            print("2. To view Player Details")
            print("3. View Report")
            print("4. Write a Feedback")
            print("5. View User ID and Password")
            print("6. Change Password")
            print("7. Help")
            print("8. Quit")
            print("9. About Us")
        try:
            choice=int(input("Enter Your Choice: "))
        except:
            choice=0
        if choice==1:
            if v==1:
                if fcheck(3,l=1):
                    print("1. Search By Name")
                    print("2. Search By User Id")
                    print("3. List all")
                    ch=int(input("Enter Your Choice: "))
                    if ch==1:
                        PlayerSearch(1,ch)
                    elif ch==2:
                        PlayerSearch(1,ch)
                    elif ch==3:
                        PlayerList(1)
                    print()
                else:
                    print("No one has registered yet!!")
                    print()
                
            else:
                #k=[r[0:-5] for r in glob("*.json")]
                k=[r[7:-5] for r in glob("assets/*.json") ]
                if len(k)==0:
                    print("Quiz not available !!!")
                    print()
                else:
                    print("Subject(s) available: ")
                    for i in k :
                        print(i)
                    g=0
                    while 1:
                        c1=input("Select Subject: ").lower()
                        for i in k:
                            #if c1 in i:
                            if c1==i:
                                fcheck(3,1,h,p="assets/"+c1+".json")
                                g+=1
                        if g==0:
                            print("Entered subject not available!!")
                            print("Try Again:")
                        else:
                            break
                
                
                
        elif choice==2:
            if v==1:
                if fcheck(3,1,l=1):
                    print("1. Search By Name")
                    print("2. Search By User Id")
                    print("3. List all")
                    ch=int(input("Enter Your Choice: "))
                    if ch==1:
                        PlayerSearch(2,ch)
                    elif ch==2:
                        PlayerSearch(2,ch)
                    elif ch==3:
                        PlayerList(2)
                    print()
                else:
                    
                    print("No one has played game !!")
                    print()
            else:
                PlayerSearch(1,2,h)
                print()
        elif choice==3:
            if v==1:
                print("Feedbacks:")
                if fcheck(4):
                    feedbacks(2)
                else:
                    print("No feedbacks yet")
                print()
            else:
                if fcheck(3,1,l=1):
                    print("1. View Your Report")
                    print("2. List all")
                    ch=int(input("Enter Your Choice: "))
                    if ch==1:
                        PlayerSearch(2,2,h)
                    elif ch==2:
                        PlayerList(2)
                    print()
                else:
                    #print("It seems that you didn't play the game")
                    print("No one has played this game !!")
                    print("Play game to view your report !!")
                    print()
        elif choice==4:
            if v==1:
                #k=[r[0:-5] for r in glob("*.json")]
                k=[r[7:-5] for r in glob("assets/*.json") ]
                if len(k)!=0:
                    print("Subject(s) available: ")
                for i in k :
                    print(i)
                print()
                print("Create/Update Quizzes....")
                print()
                print("1. Add New Questions")
                print("2. Update Questions")
                print("3. View Questions")
                ch=int(input("Enter Your Choice: "))
                if ch==1:
                    c1=input("Select Subject: ").lower()
                    if c1 not in k:
                        print("Creating a new Quiz....")
                    else:
                        print("Updating existing one")
                    print("Add Questions !!!")
                    fcheck(2,l="assets/"+c1+".json")
                    print()
                elif ch==2:
                    g=0
                    while 1:
                        if len(k)==0:
                            print("No Quiz created to update !!!")
                            print()
                            break
                        c1=input("Select Subject: ").lower()
                        for i in k:
                            if c1 in i:
                                print("Update Questions !!!")
                                fcheck(2,l="assets/"+c1+".json",p=1)
                                print()
                                g+=1
                        if g==0:
                            print("Entered subject not available!!")
                            print("Try Again:")
                        else:
                            break
                elif ch==3:
                    g=0
                    while 1:
                        if len(k)==0:
                            print("No Quiz created to view !!!")
                            print()
                            break
                        c1=input("Select Subject: ").lower()
                        for i in k:
                            if c1 in i:
                                print("View Questions !!!")
                                see("assets/"+c1+".json",m=1)
                                print()
                                g+=1
                        if g==0:
                            print("Entered subject not available!!")
                            print("Try Again:")
                        else:
                            break
  
                    
                    
            else:
                print("Write a Feedback:")
                feedbacks(1)
                print()
        elif choice==5:
            if v==1:
                print("Admin Password & Recovery Key:")
                n,h=pcheck()
                print("Password: ",n)
                print("Recovery Key: ",h)
                print()
            else:
                print("User ID,Password:")
                h,s,r=pcheck(h)
                print("User ID: ",h)
                print("Password: ",s)
                print("Recovery Key: ",r)
                print()
        elif choice==6:
            if v==1:
                print("To Change Admin Password.....")
                APsdUplogin(2)
                print()
            else:
                print("To Change Password.....")
                login(2)
                h,s,r=pcheck(h)
                print()
        elif choice==7:
            print("Help")
            if v==1:
                Help(1)
            else:
                Help(2)
            print()
        elif choice==8:
            print("Program Exiting...........")
            print("Thanks for using program")
            print()
            break;
        elif choice==9:
            about()
        else:
            print("Invalid choice")
            print("Try again!!")
            
print('....Welcome to Quiz Game.... ')
user()


