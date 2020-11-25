# sentence = '从前有座山，'
#
# def mountain():
#     print('山里有座庙，')
#
# class Temple:
#     sentence = '庙里有个老和尚，'
#     def reading(self):
#         print('在讲一个长长的故事。')

import random
import string
# a=int(''.join(random.choice(string.digits) for i in range(4)))%2==1
# print(a)
# area = ["11"]  # 选择哪个区域这个传哪个区域码
# b=random.choice(area)
# print(b)

#
# data='''
# <?xml version="1.0" encoding="GBK"?>
# <INSUREQ>
#   <MAIN>
#     <SOURCETYPE>2</SOURCETYPE>
#     <ZONENO>3300</ZONENO>
#     <BRNO>33012255</BRNO>
#     <TRANSRNO>${__Random(1000000000000000,9999999999999999,)}</TRANSRNO>
#     <TRANSRDATE>20201107</TRANSRDATE>
#     <TRANSRTIME>93543</TRANSRTIME>
#     <BANK_CODE>1200</BANK_CODE>
#     <TELLERNO>99999999999</TELLERNO>
#     <INSUID>0026</INSUID>
#     <APPLNO />
#     <TB_DATE>20201107</TB_DATE>
#     <PAYACC>6221803300008340712</PAYACC>
#     <SENDMETHOD>1</SENDMETHOD>
#     <DISPUTE_PROCESS />
#     <ARBITRATION />
#     <INSU_SPEC />
#     <SALE_ID>20120737341</SALE_ID>
#     <FIRST_PAYWAY />
#     <NEXT_PAYWAY />
#     <REPAYNOTICE />
#     <BRNM>zhongguoyouzhengyinhang</BRNM>
#   </MAIN>
#   <TBR>
#     <TBR_NAME>cehngqiuyun</TBR_NAME>
#     <TBR_SEX>2</TBR_SEX>
#     <TBR_BIRTH>19660916</TBR_BIRTH>
#     <TBR_IDTYPE>1</TBR_IDTYPE>
#     <TBR_IDNO>330724196609166821</TBR_IDNO>
#     <TBR_ADDR>zhonguoshiujinchengben</TBR_ADDR>
#     <TBR_POSTCODE>322124</TBR_POSTCODE>
#     <TBR_TEL />
#     <TBR_MOBILE>13566924041</TBR_MOBILE>
#     <TBR_EMAIL>13566924041@139.com</TBR_EMAIL>
#     <TBR_MARRIAGE />
#     <TBR_EFF_DATE>20270209</TBR_EFF_DATE>
#     <TBR_WORKTYPE>0201001</TBR_WORKTYPE>
#     <TBR_BBR_RELA>5</TBR_BBR_RELA>
#     <TBR_INCOME>10000000</TBR_INCOME>
#     <TBR_CNTY_CODE>CHN</TBR_CNTY_CODE>
#     <TBR_HEIGHT />
#     <TBR_WEIGHT />
#     <TBR_UNIT />
#     <TBR_PROV>3300</TBR_PROV>
#     <TBR_CITY>zhongguo</TBR_CITY>
#     <TBR_ED />
#     <TBR_HM>0</TBR_HM>
#     <TBR_TP>2</TBR_TP>
#   </TBR>
#   <BBR>
#     <BBR_NAME>cehngqiuyun</BBR_NAME>
#     <BBR_SEX>2</BBR_SEX>
#     <BBR_BIRTH>19660916</BBR_BIRTH>
#     <BBR_IDTYPE>1</BBR_IDTYPE>
#     <BBR_IDNO>330724196609166821</BBR_IDNO>
#     <BBR_ADDR>zhonguo</BBR_ADDR>
#     <BBR_POSTCODE>322124</BBR_POSTCODE>
#     <BBR_TEL />
#     <BBR_MOBILE>13566924041</BBR_MOBILE>
#     <BBR_EMAIL>13566924041@139.com</BBR_EMAIL>
#     <BBR_MARRIAGE />
#     <BBR_EFF_DATE>20270209</BBR_EFF_DATE>
#     <BBR_INCOME>10000000</BBR_INCOME>
#     <BBR_WORKTYPE>0201001</BBR_WORKTYPE>
#     <BBR_CNTY_CODE>CHN</BBR_CNTY_CODE>
#     <BBR_HEIGHT />
#     <BBR_WEIGHT />
#     <BBR_UNIT />
#     <BBR_PROV>3300</BBR_PROV>
#     <BBR_CITY>zhonguo</BBR_CITY>
#     <BBR_ED />
#   </BBR>
#   <SYRS />
#   <PRODUCTS>
#     <PRODUCT>
#       <PRODUCTID>YB707</PRODUCTID>
#       <MAINSUBFLG>1</MAINSUBFLG>
#       <AMT_UNIT>10</AMT_UNIT>
#       <PAYMETHOD />
#       <CHARGE_PERIOD>1</CHARGE_PERIOD>
#       <CHARGE_YEAR>0</CHARGE_YEAR>
#       <COVERAGE_PERIOD>2</COVERAGE_PERIOD>
#       <COVERAGE_YEAR>5</COVERAGE_YEAR>
#       <AMT>0</AMT>
#       <PREMIUM>1000000</PREMIUM>
#       <REVMETHOD />
#       <REVAGE>0</REVAGE>
#       <DVDMETHOD />
#       <ALFLAG />
#       <DUTY_START_DATE />
#       <DUTY_END_DATE />
#     </PRODUCT>
#   </PRODUCTS>
#   <HEALTH_NOTICE>
#     <NOTICE_ITEM>Y</NOTICE_ITEM>
#   </HEALTH_NOTICE>
#   <LOAN_INFO>
#     <NOTICE_ITEM />
#   </LOAN_INFO>
# </INSUREQ>
# '''
#
# print(len(data.encode('gbk')))
# # from easygui import raw_input

file=open('C:/Users/Administrator/Desktop/开门红压力测试/sj/sj00.txt','w',encoding='utf-8')
transNo=100114589525433429891572
contno=121984251573
prtNo=18245902220547
for m in range(100000):
    transNo = transNo + 1
    contno = contno+1
    prtNo = prtNo + 1
    file.writelines('SN' + str(transNo) + ','+'MM' + str(contno)+',' + str(prtNo) + '\n')

#     'SN' + str(transNo) + ','
#     + 'MM' + str(contno) +
# ',' + prtNo + '\n'

# file=open('C:/Users/Administrator/Desktop/开门红压力测试/sj/sj20.txt','w',encoding='utf-8')
# transNo=11113511111
# name=29386320393
# for m in range(100000):
#     transNo=transNo+1
#     name = name + 1
#     file.writelines(str(transNo)+','+str(name)+'\n')