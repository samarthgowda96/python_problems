def currency_converter(amount):
    #convert amount into pennies so that the math is easier
    amount = amount * 100
    hundred = 0
    fifty = 0
    ten =0
    five=0
    one=0
    quarter=0
    dime=0
    nickel=0
    penny=0
    while amount >0:
        if amount - 10000 >= 0:
            hundred +=1
            amount -= 10000
        elif amount - 5000 >= 0:
            fifty+=1
            amount -= 5000
        elif amount-1000 >=0:
            ten+=1
            amount-=1000
        elif amount-500>=0:
            five+=1
            amount-=500
        elif amount-100>=0:
            one+=1
            amount-=100
        elif amount-25>=0:
            quarter+=1
            amount-=25
        elif amount-10>=0:
            dime+=1
            amount-=10
        elif amount-5>=0:
            nickel+=1
            amount-=5
        else:
            penny+=1
            amount-=1
    #when there is no more money
    print("You will need {} hundred dollar bills, {} fifty dollar bills, {} ten dollar bills, {} five dollar bills, {} one dollar bills, {} quarters, {} dimes, {} nickels, and {} pennies.".format(hundred, fifty, ten, five, one, quarter, dime, nickel, penny))


if __name__ == "__main__":
    submitted_amount = float(input("How much money are you converting? ").replace("$","").replace(" ",""))
    currency_converter(submitted_amount)
