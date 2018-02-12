coins=int(input())
print("the number of coins is",coins)
while(coins !=0) :
    print("P1 turn")
    p1=int(input())
    while(p1==coins) :
        print("play again")
        p1=int(input())
    while (p1>coins) :
        print ("play again")
        p1=int(input())
    while (p1<0) :
        print("play again")
        p1=int(input())
    coins=coins-p1
    while(coins!=0) :
        print("the number of coins is",coins)
        print("P2 turn")
        p2=int(input())
        while (p2>coins) :
            print("play again")
            p2=int(input())
        while(p2>2*p1) :
            print ("play a valid number")
            p2=int(input())
        while (p2<0) :
            print ("play again")
            p2=int(input())
        while(p2==coins) :
            print("P2 wins")
            exit()
        coins=coins-p2
        print("the number of coins is",coins)
        print("P1 turn")
        p1=int(input())
        if (p1==coins) :
            print("P1 wins")
            exit()
        
        while (p1>2*p2) :
            print("enter a valid number")
            p1=int(input())
        while (p1>coins):
            print("play again")
            p1=int(input())
        coins=coins-p1
        
            
                
