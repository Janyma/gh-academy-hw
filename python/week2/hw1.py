def calculator():
    total_bil=input()
    tip_persent=input()
    total_bil_=int(total_bil)
    tip_persent_=int(tip_persent)
    total_bill_with_tip = total_bil_*tip_persent_/100 + total_bil_
    print("Total bil: ", total_bil)
    print("Total bil with tip: ", total_bill_with_tip)

calculator()
    