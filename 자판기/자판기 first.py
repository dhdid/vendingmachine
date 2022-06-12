drink_list = ["오아시스", "레몬워터", "옥수수 수염차", "콘트라베이스", "트레비", "밀키스", "펩시", "핫시스", "칠성사이다", "코코 리치", "립톤", "스파클링 사과", "스파클링 포도", "가나", "레쓰비", "칸타타", "카페타임", "게토레이", "코코 포도", "잔치집 식혜"]
price_list = [600, 1500, 1300, 2000, 1000, 800, 800, 1000, 1000, 1000, 1000, 1000, 1000, 600, 600, 1000, 1000, 800, 800, 800] 
inv_list = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10] 

inp_money = int(input("돈을 넣어 주세요")) 
for i in range(len(price_list)):
    if price_list[i] <= inp_money :
        print(drink_list[i])

def buydrink():                                           
    inp_drink = input('음료수를 골라주세요')
    for i in range(len(drink_list)):
        if drink_list[i] == inp_drink:
            if(inp_money >= price_list[i]):
                print(inp_drink + '를 구매하였습니다')
                print("거스름돈은" + str(inp_money - price_list[i]))
                charges_money = inp_money - price_list[i]
                #print("반환\n","추가구매")
                #a = input("선택해주세요.")
                a = input("반환하시겠습니까?")
                if a == "반환" :
                    print(str(inp_money - price_list[i]) +"이 반환돼었습니다")
                #else :
                    #a == "추가구매"
                    #plus_inp_money = int(input("돈을 추가해 주세요"))
                    #charges_money += plus_inp_money
                    #buydrink()
            else:
                print('잔액이 부족합니다.')
                buydrink()  


buydrink()
