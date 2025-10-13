def calculator():
    print("Please give total bil")
    total_bil=input()
    print("Please give tip percentage")
    tip_persent=input()
    print("How many persons share the bill and what are their name?")
    personas=input()
    total_personas=int(personas)

    for i in range(0, total_personas):
        a=[]
        b= input()
        a.append(b)
    total_bil_=int(total_bil)
    tip_persent_=int(tip_persent)
    total_bill_with_tip = total_bil_*tip_persent_/100 + total_bil_

    total_bill_with_tip_per_person= total_bill_with_tip/total_personas

    print("Total bil : ", total_bil)
    print("Total bil with tip per person for :" , total_bill_with_tip_per_person)
    if (tip_persent_>20):
        print("tWhat a generosity")

calculator()
    