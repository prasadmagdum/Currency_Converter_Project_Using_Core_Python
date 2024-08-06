#currency.py
def display_menu():
    print("1.convert USD to Euro(EUR)")
    print("2.convert USD  to British Pound Sterling (GBP)")
    print("3.convert USD to Japense Yen (JPY)")
    print("4.convert USD to canadian Dollar(CAD)")
    print("5.convert USD to indian Dollar (INR)")
    print("6.convert USD to southafrican (ZAR)")
    print("7.Exit")

def USD_to_EU(value):
    return value *0.94
def USD_to_GBP(value):
    return value *0.79
def USD_to_JPY(value):
    return value *113
def USD_to_CAD(value):
    return value *1.33
def USD_to_INR(value):
    return value *80 
# def USD_to_ZAR(value):
#     return value *18.72
while True:
      display_menu()
      chioce=int(input())
      if chioce==7:
           print("Bye")
           break
      else:
          amount=float(input("Enter an amount in US dollars:"))
          if chioce==1:
              print(amount,"USD",USD_to_EU(amount),"Euro")
          elif chioce==2:
              print(amount,"USD",USD_to_GBP(amount),"GBP")
          elif chioce==3:
              print(amount,"USD",USD_to_JPY(amount),"JPY")
          elif chioce==4:  
              print(amount,"USD",USD_to_CAD(amount),"CAD")
          elif chioce==5: 
              print(amount,"USD",USD_to_INR(amount),"INR")
              #end
                
    
        