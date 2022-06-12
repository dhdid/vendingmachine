drink_list = ["오아시스", "레몬워터", "옥수수 수염차", "콘트라베이스", "트레비", "밀키스", "펩시", "핫시스", "칠성사이다", "코코 리치", "립톤", "스파클링 사과", "스파클링 포도", "가나", "레쓰비", "칸타타", "카페타임", "게토레이", "코코 포도", "잔치집 식혜"]
price_list = [600, 1500, 1300, 2000, 1000, 800, 800, 1000, 1000, 1000, 1000, 1000, 1000, 600, 600, 1000, 1000, 800, 800, 800]
inv_list = [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
num=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]




##############전역변수

inp_money=0
charge=0
drinkPrice=0
r100=0
r500=0
ba_1000=0
ba_500=50
ba_100=50


############## 디스플레이

def chargeDp():
    global charge
    print("+======+==========+=========+")
    print("+======+ 잔액=",charge," +=========+")
    print("+======+==========+=========+")


def dp(mode=0):
    global inp_money
    if mode == 0 :                                #일반 디스플레이
        print("_____________________________")
        print("      |    자판기    |       ")
        chargeDp()
        print("-----------------------------")    
    elif mode == 1:                              #모든 메뉴 디스플레이
        print("_____________________________")
        print("      |    자판기    |       ")
        print("-----------------------------")
        chargeDp()
        print("-----------------------------")  
        for i in range(len(drink_list)):
            if inv_list[i] == 0 :
                print(num[i],":",drink_list[i],"-",price_list[i],">제고 없음")
            else:
                print(num[i],":",drink_list[i],"-",price_list[i])
    elif mode == 2:                              #구매 가능 디스플레이
        print("_____________________________")
        print("      |    자판기    |       ")
        print("-----------------------------")
        chargeDp()
        print("-----------------------------")  
        for x in range(len(drink_list)):
            if inv_list[x] == 0 :
                print(num[x],":",drink_list[x],"-",price_list[x],">제고 없음")
            elif inp_money>=price_list[x]  :
                print(num[x],":",drink_list[x],"-",price_list[x])

#####################관리자 모드

def manage():                                   #관리자 모드 비밀번호 
    x=input("비밀번호를 입력하세요")
    if x=="030128":
        while True:                               
            invprint()
            ch=int(input("1.제고\n2.잔고"))
            if ch == 1:        
                while True:
                    inpInv=input("제품번호를 입력하세요")            
                    if inpInv=="":
                        break
                    else:            
                        inv_list[int(inpInv)-1]+=int(input("추가할 수량을 입력하세요"))        
                        invprint()    

            elif ch == 2 :
                global ba_1000, ba_500, ba_100
                print("1000원",ba_1000,"장을 수거하였습니다.")
                ba_1000=0
                ba_500+=int(input("채울 500원 동전의 개수를 입력하세요."))
                print("500원",ba_500,"개을 채웠습니다.")
                ba_100+=int(input("채울 100원 동전의 개수를 입력하세요."))
                print("100원",ba_100,"개을 채였습니다.")
                return ba_1000, ba_500, ba_100

            else:
                break

    else:
        print("비밀번호가 틀렸습니다.")
        main()

def invprint():
    for i in range(len(drink_list)) :
        print(num[i],":",drink_list[i],"-",inv_list[i],"개 남았습니다.")    
    print("1000원 ",ba_1000,"장/ 500원 ",ba_500,"개 100원 ",ba_100,"개")
 

#################################

######################## 돈계산

def moneyinput():
    global inp_money, charge, ba_1000, ba_500, ba_100
    _1000won = int(input("천원을 투입해주세요"))
    ba_1000+=_1000won    
    _500won = int(input('오백원을 투입해주세요'))
    ba_500+=_500won
    _100won= int(input('백원을 투입해주세요'))
    ba_100+=_100won
    inp_money = _1000won*1000+_500won*500+_100won*100
    charge+=inp_money
    return inp_money, ba_1000, ba_500, ba_100

def chargecomput(x): #거스름돈 계산
    global inp_money, charge
    charge = inp_money - x
    return charge

def chargeDiv():
    global charge, r500, r100, ba_500, ba_100
    a=charge//500
    r500=a
    r100=(charge-a)//100
    ba_500-=r500
    ba_100-=r100
    charge = 0
    return r100, r500, ba_500, ba_100, charge


##################


def canbuydrinklistout(): #구입할수 있는 음료수 출력 및 음료수 구매 
    global drinkPrice
    dp(2)
    buy_drink = int(input("구매할 음료수의 번호를 선택해주세요."))
    if inp_money >= price_list[buy_drink-1] and inv_list[buy_drink-1]>0 :
        drinkPrice=price_list[buy_drink-1]
        print(drinkPrice,"원 입니다.")
        print(drink_list[buy_drink-1],"를 구매하셨습니다.")    
        return drinkPrice
    else:
        canbuydrinklistout()    



#########################################실행

def main():
    dp(0)
    k=input("+====+엔터를 눌러주세요+====+")
    print("-----------------------------")

    if k=="2022156030":
        manage()
    elif k=="" :

        dp(1)
        moneyinput()

        canbuydrinklistout()
    
        chargecomput(drinkPrice)

        dp(0)
        print("1.반환\n2.추가구매")
        retorplus = input("반환을 원하시면 '1.반환'을 추가구매를 원하시면 '2.추가구매'를 입력해주세요.")
        if retorplus == "반환" or int(retorplus) == 1:
            chargeDiv()
            print("500원",r500,"개가 100원",r100,"반환되었습니다.")
        elif retorplus == "추가구매" or int(retorplus) == 2 :
            main()
    
while True :
    main()
