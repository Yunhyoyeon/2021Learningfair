print('당기 순손익을 알기 위해  총계정원장 중 수익, 비용 계정을 마감하도록 합니다.')
print('우선 수익 계정의 값을 작성해주세요.\n')

Pproductsales = int(input('상품매출이익은 총 얼마입니까?: '))
Pinterest = int(input('이자수익은 총 얼마입니까?: '))
Prent = int(input('임대료는 총 얼마입니까?: '))
Pcommission = int(input('수수료수익은 총 얼마입니까?: '))
Pthistermsell = int(input('당기손익_공정가치측정금융자산처분이익은 총 얼마입니까?: '))
Ptangiblesell = int(input('유형자산처분이익은 총 얼마입니까?: '))
Petc = int(input('이외의 잡이익은 총 얼마입니까?: '))

print()

Totalprofit = Pproductsales + Pinterest + Prent + Pcommission + Pthistermsell + Ptangiblesell + Petc

print('수익의 총 합은',Totalprofit,'입니다.\n\n')
print('다음으로 비용 계정의 값을 작성해주세요.\n')

Eproductsales = int(input('상품매출손실은 총 얼마입니까?: '))
Einterest = int(input('이자비용은 총 얼마입니까?: '))
Erent = int(input('임차료는 총 얼마입니까?: '))
Ecommission = int(input('수수료비용은 총 얼마입니까?: '))
Ethistermsell = int(input('당기손익_공정가치측정금융자산처분손실은 총 얼마입니까?: '))
Etangiblesell = int(input('유형자산처분손실은 총 얼마입니까?: '))
Epay = int(input('종업원급여는 총 얼마입니까?: '))
Ebenefits = int(input('복리후생비는 총 얼마입니까?: '))
Etaxes = int(input('세금과공과비는 총 얼마입니까?: '))
Eetc = int(input('이외의 잡손실은 총 얼마입니까?: '))

print()

Totalexpense = Eproductsales + Einterest + Erent + Ecommission + Ethistermsell + Etangiblesell + Epay + Ebenefits + Etaxes + Eetc

print('비용의 총 합은',Totalexpense,'입니다.\n')

print('수익, 비용 계정을 손익계정에 대체하고 마감 중입니다.\n')
for i in range(3):
    print('      ㆍ')
print()

Netloss = 0
Netincome = 0


if Totalexpense > Totalprofit:
    Netloss = Totalexpense - Totalprofit
    print('손익 계정의 차변 값이 대변 값보다 크므로 당기순손실', Netloss, '이 발생하였습니다.')

elif Totalexpense < Totalprofit:
    Netincome = Totalprofit - Totalexpense
    print('손익 계정의 대변 값이 차변 값보다 크므로 당기순이익', Netincome, '이 발생하였습니다.')

else:
    print('손익 계정의 차변 값과 대변 값이 동일하여 당기순손익이 발생하지 않았습니다.')
