#Prices for car brands per model
#Promotion 
#Car brands in each set have similar discount charges and charges.
print('Hello customer')

carBrandPrice=int(input("Input your car price preference"))
if carBrandPrice >= 20000000:
     print('SetA :Mercedes benz,Jaguar,Hummer,Toyota,BMW,\
           SetB :Ferrari,Dodge,Fiat,GMC are avaialble to purchase')
elif 7000000 <= carBrandPrice <20000000:
    print('SetA:Lotus,Buick,Nissan,Lincoln,Mazda,Subaru,\
          SetB: Mini ,Porshe,Volvo are available to purchase')
elif 400000 <= carBrandPrice<7000000:
    print('SetA:Toyota,Honda,Audi,Volkswagen,Ford,\
          SetB: Tesla,Jeep,Kia,Lexus are available to purchase')
elif 200000 <= carBrandPrice <400000:
    print('Infiniti,Jaguar,Lotus,Opel are available to purchase')
else:
    print('Not available at the moment,it may take a while.')
option=int(input('Are you interested in the list of car provided?'))
#Answer with a number   
#Yes=1
#No =2
if option==1:
    print('You can proceed')
elif option==2:
    print('Oops,Sorry')
    
brandChoice=str(input('Choose from the options provided'))
brandModel=int(input('Input brand model preference'))
if brandModel >=17:
    print("The "+ str(brandChoice) +" "+ 'you selected is above the car price preference you inputed.')
    print('The amount per your '+str(brandChoice)+'is'+"$"+str(carBrandPrice)+" "+ "plus additionals charges per set")
elif 15<= brandModel < 17:
    print("This package comes with 10% discount additional charges per set ")
    print("Thanks for purchasing"+" "+brandChoice)
elif 12<= brandModel<15:
    print('The '+str(brandChoice)+" "+"comes with 25% discount additional charges per set")
else:
    print("Not avaialable")
    
terms=input("Do you accept or decline the offer?")
print("Thanks for purchasing your car here")


