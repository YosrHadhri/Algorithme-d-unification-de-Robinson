def isVar (x) :
    if x[0]=="?":
       return 0
    else :
        return -1
def isFunc ( x) :
    #if str(x.index("("))!=0 and str(x.index(")"))!=0 and str(x.index("("))<str(x.index(")")):
    if "(" in x and ")" in x:
         return 0
    else :
        return -1    
def isConst (x):
    if "(" not in x and ")" not in x  and "?" not in x :
        return 0
    else :
        return -1
    


def Nbparam(f):
    if isFunc(f)==0:
         
         param=Listparam(f)
         n=len(param)
         return n
def NomFct(f):
    if isFunc(f)==0:
        a=f[f.index("(")-1]
        return a


def Listparam(f) :
    if isFunc(f)==0:
        
        a=f[f.index("(")+1:len(f)-1]
        
        i=0
        List2=list()
        n=len(a)
        while i < n :
            
            
            if i+1 < n and a[i]!="?" and a[i+1]!="(":
                
                List2.append(a[i])
                a=a[i+2:n]
                n=len(a)
            elif  str(i+1) == str(n) and a[i]!="?":
                
                
                List2.append(a[i])
                a=a[i+2:n]
                n=len(a)    
            elif a[i]=="?":
                
                

                if str(i+2)==str(n) or a[i+2]=="," :
                    List2.append(a[i:i+2])
                    a=a[i+3:n]
                    n=len(a)
                    
                    
                    
                   
                elif a[i+2]!="," or a[i+2]!=")":
                    List2.append(a[i:i+3])
                    a=a[i+4:n]
                    n=len(a)
                     
            elif a[i+1]=="(" :
                k=a.find(")")
                 
                if k+1 < n and a[k+1]==")" :
                    
                    
                    List2.append(a[i:k+2])
                    l=len(a[i:k+2])
                    a=a[i+l+1:n]
                    n=len(a)
                    
                else :
                    List2.append(a[i:a.find(")")+1])
                    l=len(a[i:a.find(")")+1])
                    a=a[i+l+1:n]
                    n=len(a)
                    
                     
        return List2
                
             
             
         
             
         
         
    
    
def unifierAtomes2(E1,E2):
   
    if isConst(E1)==0 and isConst(E2)==0 and E1==E2:
        return "NULL"
    
    elif isConst(E1)==0 and isConst(E2)==0 and E1!=E2:
        return "ECHEC"
    elif isConst(E1)==0 and isVar(E2)==0:
       
        return E2+"/"+E1
    elif isConst(E1)==0 and isFunc(E2)==0:
        if E1 in Listparam(E2) :
            return"ECHEC"
        elif E1 not in Listparam(E2) :
            return E1+"/"+E2
    
    elif isVar(E1)==0 :
         
         if isVar(E2)==0 and E1!=E2:
             return E1+"/"+E2
        
         if isConst(E2)==0 and E1==E2:
             return "NULL"
         if isConst(E2)==0 and E1!=E2:
             return E1+"/"+E2   
        
         if isFunc(E2)==0 and E1 in Listparam(E2):
             return "ECHEC"

         elif isFunc(E2)==0 and E1 not in Listparam(E2) :
              return E1+"/"+E2
            
    
        
def unifierAtomes1(E1,E2):
    
    if isFunc(E1)==0 and isFunc(E2)!=0 :
        
        
        return unifierAtomes2(E2,E1)
    
    elif isFunc(E1)!=0 and isFunc(E2)!=0:
        return unifierAtomes2(E1,E2)
        
         
        
    elif isFunc(E1)!=0 and isFunc(E2)==0:
                                        
        return unifierAtomes2(E1,E2)

    elif isFunc(E1)==0 and isFunc(E2)==0:
        
        return unifierFonction(E1,E2)
        
       


   
        
def unifierFonction(E1,E2):
    
   
    if Nbparam(E1)!=Nbparam(E2):
            return "ECHEC"
        
    elif NomFct(E1)!=NomFct(E2):
            return "ECHEC"
        
        
        
          
    elif  Nbparam(E1)==Nbparam(E2) and  NomFct(E1)==NomFct(E2):
             n=Nbparam(E1)
            
             myList2=list()
             c=Listparam(E1)
             d=Listparam(E2)
             for i in range (0,n):
                 
                 k=0
                 m1=c[k]
                 
                 m2=d[k]
                 
                 R1=c[k+1:n]
                 R2=d[k+1:n]
                 myList2.append(str(unifierAtomes1(m1,m2)))
                 z=str(unifierAtomes1(m1,m2))
                 c=rech(z,R1)
                 d=rech(z,R2)
              
                 
                 
                
                         
                     
             return myList2   
                
                 
                 
            
    
    

        

                 
def rech (x,T) :
   
    p1 =x[0:x.index("/")]
    p2=x[x.index("/")+1:len(x)]
    n=len(T)
   
    
    for i in range(0,n):
        
        if isFunc(T[i])!=0 and str(p1)==str(T[i]) :
            T[i]=p2
            
        elif isFunc(T[i])==0 and str(p1) in str(T[i]):
            
            T[i]=T[i].replace(p1,p2)
    return T    
            
def unifier2 (E1,E2):
    
    if len(E1)==1 and len(E2)==1 :
        t=str(unifierAtomes1(E1[0],E2[0]))
        
        with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
            Sub.write(t+"\n")
        return t
    elif len(E1)!=1 and len(E2)!=1 :
        print("coucou")
                                
        F1=E1[0:1]
        F2=E2[0:1]
        T1=E1[1:len(E1)]
        T2=E2[1:len(E2)]
        print(F1)
        print(F2)
        Z1=unifier2(F1,F2)
        
        if Z1=="ECHEC":
            return "ECHEC"
        elif Z1=="NULL":
            return unifier(T1,T2)
        else :
            G1=rech(Z1,T1)
            print(str(G1))         
            G2=rech(Z1,T2)
            print(str(G2))         
            Z2=unifier2(G1,G2)
            print(str(Z2))
            if Z2=="ECHEC":
                with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
                     Sub.write(Z2+"\n")
                return "ECHEC"   
                       
                    
        
            
def unifier (E1,E2):    
    
    x=E1[0]
    y=E2[0]
    
    if isFunc(x)!=0 and isFunc(y)!=0 :
        h=str(unifierAtomes1(x,y))
        
       
        with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
            Sub.write(h+"\n")
        return h
    elif isFunc(x)==0 and isFunc(y)!=0  :
       
        h=str(unifierAtomes1(x,y))
       
       
       
        
        with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
            Sub.write(h+"\n")
        return h
    elif isFunc(x)!=0 and isFunc(y)==0  :
        
        h=str(unifierAtomes1(x,y))
        
        
        
       
        
        with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
            Sub.write(h+"\n")
        return h
        
            
        
        
    elif isFunc(x)==0 and isFunc(y)==0 :
        
        L1=Listparam(x)
        L2=Listparam(y)
   
    
    
        if len(L1)==1 and len(L2)==1 :
            
            
            t=str(unifierAtomes1(L1[0],L2[0]))
            
            
            
            with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
                Sub.write(t+"\n")
             
            return t
      
        elif len(L1)!=1 and len(L2)!=1 :
            
            print("coucou")
                                
            F1=L1[0:1]
            F2=L2[0:1]
            T1=L1[1:len(L1)]
            T2=L2[1:len(L2)]
            print(str(T1))
            print(str(T2))
            Z1=unifier2(F1,F2)
            print(Z1)
            print("je suis Z1"+str(Z1))
            
            if len(Z1) > 5 :
                p=Z1[Z1.find("[")+1:Z1.find("]")]
                p1=p.split(", ")
                
                p11=p1[0]
                
                p22=p1[1]
                
                p111=p11[1:len(p11)-1]
                p222=p22[1:len(p22)-1]
               
                G1=rech(p111,T1)
                M1=rech(p222,G1)      
                G2=rech(p111,T2)
                M2=rech(p222,G2)
                
                Z2=unifier2(M1,M2)
                
                if Z2=="ECHEC":
                    with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
                        Sub.write(Z2+"\n")
                    return "ECHEC"
                    
                
            else :
                G1=rech(Z1,T1)
                G2=rech(Z1,T2)
                Z2=unifier2(G1,G2)
                if Z2=="ECHEC":
                    
                    with open ("C:\\Users\dell\Desktop\TP.txt","a") as Sub:
                        
                        Sub.write(Z2+"\n")
                    return "ECHEC"
                        
                        
                        
#x=["p(b,c,?x,?z,f(a,?z,b))"]
#y=["p(?y,?z,?y,c,?w)"]
#z=unifier(x,y)                        

c=["P(?x,f(g(?x)),a)"]
d=["P(b,?xy,?z)"]
z=unifier(c,d)


#e=["q(f(A,?x),?x)"]
#g=["q(f(?z,f(?z,D)),?z)"]
#z=unifier(e,g)

#h=["?x"]
#j=["g(?x)"]
#z=unifier(h,j)













