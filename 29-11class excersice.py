




class bank:
    def __init__(self,balance , account):
        self.__balance = balance
        self.__account = account
    def deposit(self,amount_dip):
        try:
            self.__amount_dip=amount_dip
            if (self.__amount_dip>0):
                d_total= self.__balance+self.__amount_dip
                return d_total
            else:
                return "enter corect amount"
        except Exception as exept1:
            print("error:",str(exept1))
            
    def withdrawal(self,amount_with):
        self.__amount_with= amount_with
        w_total= self.__balance-self.__amount_with
        return w_total
        
    def display (self):
        #super().__init__()
        return "user account is {} , user balance is {},".format(self.__account,self.__balance )
s1=bank(500,987500)
print(s1.deposit(5))
print(s1.display())
print(s1.withdrawal(5))
    





















