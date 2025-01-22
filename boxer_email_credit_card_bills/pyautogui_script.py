# 获取邮件ID
# mailids = []
# for (i in document.querySelectorAll("input[name=mailid][type=checkbox]")){
# mailids.push(document.querySelectorAll("input[name=mailid][type=checkbox]")[i].value)   
# }
# JSON.stringify(mailids)

# for (i in document.querySelectorAll("table")){
#     if(i>4){
#     if(document.querySelectorAll("table")[i].textContent.indexOf("对账单生成日")>=0){
#         console.log("i:",i)
#         date_string = document.querySelectorAll("table")[i].textContent.split(" ")[4]
#         break
#     }
#     }
# }
# console.log(date_string)
import pyautogui
import pyperclip
import time
def move_and_click(x,y,t):
    pyautogui.moveTo(x,1117-y)
    time.sleep(t)
    pyautogui.click(x,1117-y)
def move_and_double_click(x,y,t):
    pyautogui.moveTo(x,1117-y)
    time.sleep(t)
    pyautogui.doubleClick(x,1117-y)
def move_and_triple_click(x,y,t):
    pyautogui.moveTo(x,1117-y)
    time.sleep(t)
    pyautogui.tripleClick()
def mouse_down(current_button):
    pyautogui.mouseDown(button=current_button)
def mouse_up(current_button,x,y):
    pyautogui.mouseUp(button=current_button,x=x,y=1117-y)
needs = {
    "工商银行":[
        # ["ZC0012_hZXNFQaM0HQuZ2cALcVXjec","ZC0012_FATNYXKMuBwuZ2cAHTkpieb","ZC0012_JjbNgJOMgCQuZ2cAuzM67ea","ZC0012_0sLNU0CMaMwuZmYArfmece9","ZC0012_r7_NIjGMM5cuZmYAIEcSXe8","ZC0012_eGjNgZKMG78uZmYAgBdM0e7","ZC0012_zNzN6_iM40cuZmYAk_Hzhe6","ZC0012_6PjNLD~Mym4uZmYATw~Swe5","ZC0012_obHNlYaMkzcuZmYAR5FDFe4","ZC0012_vKzNorGMet4uZWUANbBpMe3","ZC0012_BxfNYXKMQ~cuZWUA_b_r7e2","ZC0012_QlLN0cKMK48uZWUAQQzeMe1","ZC0013_WkrNFwSM81cuZWUAg4KA4dc","ZC0012_XEzNSVqM2n4uZWUABrvBrdb","ZC0012__u7NloWMogYuZWUAXdCeTda","ZC0013_XU3NOCuMii4uZWUARB2Fxd9","ZC0012_7__N~eqMXfkuZGQApYB1Md8","ZC0012_08PN4fKMJIAuZGQAXCXIzd7","ZC0012_UkLNkoGMDakuZGQAQmP~Sd6","ZC0012_zNzNsKOM1HAuZGQABzvOkd5","ZC0012_iZnN9uWMvBguZGQANt74od4","ZC0012_EADN5_SMhyMuZGQAE3ZWDd3","ZC0012_Xk7NWkmMYsYuY2MAg2NVKd2","ZC0012_XU3NbH~MNZEuY2MAZfwxrd1","ZC0012_nIzNWUqMHLguY2MA6w4JWcc"],
        # ["ZC0012_gpLNxtWM5UEuY2MApHwY3cb","ZC0012_5PTNCRqMzGguY2MA0uRZGca","ZC0012_e2vNVEeMlDAuY2MAGEr0oc9","ZL0012_mYnNno2MfNguYmIAZp430c8","ZL0012_GQnNChmMrAguiIgAJQzXPc7","ZL0012_z9_NT1yMa88u8_MAmv7rRc6","ZL0012_1MTNjZ6M8FQubm4AGIZYKc5","ZL0012_z9_Nx9SM~18uDQ0A19hdAc4","ZL0013_BhbNd2SMD6suQUEA66vODc3","ZL0012_gpLNLj2MErYu5~cAYV9kWc2","ZL0012_X0_NmYqMZcEuNjYAv1I7Hc1","ZL0013_KzvNPS6MB6Mu8PAALJd1bbc","ZL0013_7v7Ns6CMPpou6uoAMChuKbb","ZL3412-koJi7_zWwWUAYGAB6qlmQba","ZL2913-ChpXHA9170t1Hh5_Rwuvab9","ZL3412-PS1EMyA04UVQFxd2PFE~Wb8","ZL2912-mIhnKDsisRX5IiJC757qYb7","ZL2912-kYGRSFsz9lKWaGgI97dJUb6","ZL2912-9eUVno0UOp4FBwdnYnQNAb5","ZL3012-x9ci8~AA03cEBwdniI6dAb4","ZL3012-JDTsTF9_~FwXe3sbw1CsFb3","ZL3012-QlJQ8uHnthI0X18_J2mFGb2","ZL3012-Chpzq7iOqQ3wT08QxYsjWb1","ZL3412-ydmq18S4wmaya2s0qvJoSac","ZL2912-AxN~2cr550PuLCxzHU5DSab"],
        # ["ZL3413-fW0rSln2aMxIbGwz7M4sHaa","ZL3012-~uoLQ1AiQ~e7DAxTd081La9","ZL2912-KDgr6PuHb8v4RkYZ1D9RLa8","ZL3413-~Ogfv6z4H7uwISF~iA7FQa7","ZL3012-18eEQlFWOZ1~PT1jrerxTa6","ZL3412-0sKbFQYYnjqABQVb3IftSa5","ZL3412-wNATx9R9CKzFDAxSDVvoBa3","ZL3412-GQmlqLvYNZHSfn4guCokEa2","ZL3412-OysqCRonljIpYGA~Tv4gPa1","ZL3412-4PA8anmV9FChY2M~BoA3K9c","ZL2912-bn7N9uWL5ECKY2M~YBsfD9b","ZL2912-ytpgeWrHYsZnBwdaNfSWU9a","ZL3012-jp4UBRbCK4_2d3cqFMYyM99","ZL2912-UUEme2iFuh5OSkoXBDMaM98","ZL3012-ChrzjJ8Y_lpaTEwRyVAIF96","ZL2912-Nyd0CBuHb8scenomUFu7E95","ZL3012-bn655vXub8t7ERFNghNUT94","ZL2912-TFzv5_SzAKQjDw9T8tpSQ93","ZL2912-x9dR28icJYHjCQlVT_UFG92","ZL3012-JDTM_~xq5UF4S0sXGOM~G91","ZL3412-KzuuTl2lyW19eXklcPqSZ8c","ZL3412-IjKf2snMM5d~Hx9E~wzWP8b","ZL2912-9eVsKzgQ6U2NGxtApu6fB8a","ZL3412-UUFW8eJ791PLfHwnNPybe89","ZL2913-SVkGxNddsxdnMzNofR6PN88"],
        # ["ZL2912-CxvSEwCghCA_amoxgOIkI86","ZL3012-gJCP~OuG81ehY2M5D6Apf85","ZL1312-DR3Ao7BmF7N9WFgCmC0VP84","ZL1312-KTljVEcp9VF~MzNpDd8KN7c","ZL5312-WkpnOCufftrdcnIoXBAIM7b","ZL5512-Dx_R9uWLqAzTFRVMvI6If7a","ZL1312-w9MUOyiaELQDfX0k~UnNU79","ZL0312-zNzmTF~FZ8NNamozq7AvY78","ZL0312-8uLmpbZSGr7bAABZOsN9f77","ZL5512-DBzU7_zYhSEfXFwFdUy1L76","ZL5312-iZngi5jnbsrfFBRNbzWwV75","ZL5312-t6dM38waTekEGxtD20bSH74","ZL2012-kIDzTV6wHrp~MTFp6SgOC73","ZL0312-XEzNt6RLG78gQUEZCjrpf72","ZL5312-Dh6QdWZBQ~eQDAxUoQ27J71","ZL0312-JzcS4POxqg5AIiJ6BZzJQ6c","ZL5512-4fElZnW6fNj~VFQMljKAX6b","ZL5312-5fVyx9Q45kK_cnIlYj9fb6a","ZL5312-Q1MgWEtxgyfxY2M0bdThU69","ZL0212-u6vPdmUZvxu2cXEmR10IC68","ZL0209-U0N1mIuZe992SUke7fN8Z68","ZL5313-RFSPpbYf91PWZWUyZDeRY67","ZL5512-qblyv6wI0HTwenotprcFR67","ZL5312-z99Pv6x940cbWFgPoi8zU66","ZL0312-08Mzjp3uZcHNAgJVmDOKW64"],
        # ["ZL1812-S1td5faJJIBjTEwaeevEM63","ZL0227-IzOKydrixGA3Kip8N5v~e5b",]
        # ["ZL5312-z99Pv6x940cbWFgPoi8zU66","ZL0312-08Mzjp3uZcHNAgJVmDOKW64"],
        # ["ZL1812-S1td5faJJIBjTEwaeevEM63","ZL0227-IzOKydrixGA3Kip8N5v~e5b",]
    ],
    "光大银行":[
        # ["ZC0007_jp7NLzyM9lIuZ2cAESXFdf1","ZC0007_j5_NLzyM9lIuZ2cAgcrf7f1","ZC0007_j5_NLzyM9lIuZ2cAsw3fEf1","ZC0007_j5_NLzyM9lIuZ2cAwEzejf1","ZC0007_jp7NLzyM9lIuZ2cAkiLEXf1","ZC0007_jZ3NLzyM9lIuZ2cAIcH0of1","ZC0007_jZ3NLzyM9lIuZ2cAnPv69f1","ZC0007_jJzNLzyM9lIuZ2cAHobgrf1","ZC0007_jJzNLzyM9lIuZ2cA2NToJf1","ZC0007_j5_NLzyM9lIuZ2cAPxTejf1","ZC0007_k4PNLzyM9lIuZ2cA2aQQpf1","ZC0007_kIDNLzyM9lIuZ2cAlTgo~f1","ZC0007_k4PNLzyM9lIuZ2cAxT4TZf1","ZC0007_kIDNLzyM9lIuZ2cA5BIoGf1","ZC0007_kIDNLzyM9lIuZ2cAtvorgf1","ZC0007_lobNLzyM9lIuZ2cAkzNOYf1","ZC0007_kYHNLzyM9lIuZ2cAEY83Tf1","ZC0007_kYHNLzyM9lIuZ2cAVXE9df1","ZC0007_kIDNLzyM9lIuZ2cAB84rYf1","ZC0007_jZ3NLzyM9lIuZ2cAOSn8jf1","ZC0007_lITNLzyM9lIuZ2cAmRFrbf1","ZC0007_lITNLzyM9lIuZ2cAF8ltZf1","ZC0007_lITNLzyM9lIuZ2cA9yRuJf1","ZC0007_lITNLzyM9lIuZ2cAb_Jltf1","ZC0007_lITNLzyM9lIuZ2cA76Nimf1",],
        # ["ZC0007_jZ3NLzyM9lIuZ2cAIcH0of1","ZC0007_jZ3NLzyM9lIuZ2cAnPv69f1","ZC0007_jJzNLzyM9lIuZ2cAHobgrf1","ZC0007_jJzNLzyM9lIuZ2cA2NToJf1","ZC0007_j5_NLzyM9lIuZ2cAPxTejf1","ZC0007_k4PNLzyM9lIuZ2cA2aQQpf1","ZC0007_kIDNLzyM9lIuZ2cAlTgo~f1","ZC0007_k4PNLzyM9lIuZ2cAxT4TZf1","ZC0007_kIDNLzyM9lIuZ2cA5BIoGf1","ZC0007_kIDNLzyM9lIuZ2cAtvorgf1","ZC0007_lobNLzyM9lIuZ2cAkzNOYf1","ZC0007_kYHNLzyM9lIuZ2cAEY83Tf1","ZC0007_kYHNLzyM9lIuZ2cAVXE9df1","ZC0007_kIDNLzyM9lIuZ2cAB84rYf1","ZC0007_jZ3NLzyM9lIuZ2cAOSn8jf1","ZC0007_lITNLzyM9lIuZ2cAmRFrbf1","ZC0007_lITNLzyM9lIuZ2cAF8ltZf1","ZC0007_lITNLzyM9lIuZ2cA9yRuJf1","ZC0007_lITNLzyM9lIuZ2cAb_Jltf1","ZC0007_lITNLzyM9lIuZ2cA76Nimf1",],
        # ["ZC0007_m4vNLzyM9lIuZ2cAS~eaEf1","ZC0007_morNLzyM9lIuZ2cA2syD6f1","ZC0007_morNLzyM9lIuZ2cAbhuIqf1","ZC0007_lYXNLzyM9lIuZ2cAkr5wNf1","ZC0007_lYXNLzyM9lIuZ2cA7i55zf1","ZC0007_mIjNLzyM9lIuZ2cAwUeiYf1","ZC0007_mYnNLzyM9lIuZ2cA_Ny86f1","ZC0007_mIjNLzyM9lIuZ2cAPvmjlf1","ZC0007_mYnNLzyM9lIuZ2cABHq9rf1","ZC0007_n4_NLzyM9lIuZ2cAPSjQFf1","ZC0007_no7NLzyM9lIuZ2cAifnGLf1","ZC0007_no7NLzyM9lIuZ2cAQBfPxf1","ZC0007_mYnNLzyM9lIuZ2cA6mm09f1","ZC0007_mYnNLzyM9lIuZ2cAMEm~rf1","ZC0007_nY3NLzyM9lIuZ2cAOd_3vf1","ZC0007_nY3NLzyM9lIuZ2cApL_08f1","ZC0007_nY3NLzyM9lIuZ2cAplL8zf1","ZC0007_nY3NLzyM9lIuZ2cAz2v9Tf1","ZC0007_nY3NLzyM9lIuZ2cAepT9Of1","ZC0007_nY3NLzyM9lIuZ2cAJsb2uf1","ZC0007_4_PNLzyM9lIuZ2cAYh0ZXf1","ZC0007_4vLNLzyM9lIuZ2cAkAoPBf1","ZC0007_4_PNLzyM9lIuZ2cAkFIQLf1","ZC0007_4PDNLzyM9lIuZ2cA8kkt3f1","ZL5511-iJgRi5hqvRnaU1MLV5GQH73",],
        # ["ZL5511-iJgRi5hqvRnaU1MLV5GQH73",],

        # ["ZL2011-no6ckIOOc9dIU1MLSBOXD72","ZL0211-nY1hv6zjy28ZOjpiz8oJO71","ZL5512-Dx9v2Ms8F7P~NTVtG82hA6c","ZL5513-j5~C_e6wN5O7XV0FTnuOc6b","ZL5512-FgYZtKe77Um0MTFmp3QpK6a","ZL0214-cmJ0ZHdRjiryPz9ovnLVb69","ZL0312-ZHS0NiXZiy~DERFGVb71K68","ZL5512-Tl62prV56k7KCwtchQjif67","ZL0211-Hw~qc2C8iS12Xl4J6wHfS66","ZL5311-gZErWUrrPpqRc3MkEBjqU64","ZL0112-aHi5qLu1gyfEIiJ0oq~FZ63","ZL5511-RFT~OyisuBygDg5YxvGVX62","ZL5312-HAzZ3c7bxWH1PT1rGQiwV61","ZL0211-NSWDb3ykb8uhExNFddT5B5c","ZL5512-wdFxdmURowdDfn4oOn3hQ5b",],
    ],
    "民生银行":[
        # ["ZC0007_fGzNLD~M9lIuZ2cAtOTkgf1","ZC0007_fGzNLD~M9lIuZ2cASqDmrf1","ZC0007_sKDNLD~M9lIuZ2cA5mElFf1","ZC0007_sKDNLD~M9lIuZ2cAoJEnJf1","ZC0007_fGzNLD~M9lIuZ2cAijnknf1","ZC0007_saHNLD~M9lIuZ2cAzJY07f1","ZC0007_fGzNLD~M9lIuZ2cA49rlEf1","ZC0007_fGzNLD~M9lIuZ2cAWl7kxf1","ZC0007_fGzNLD~M9lIuZ2cACsPnQf1","ZC0007_fGzNLD~M9lIuZ2cAL4Dntf1","ZC0007_fGzNLD~M9lIuZ2cAqHbnRf1","ZC0007_fW3NLD~M9lIuZ2cAQ9v4Ff1","ZC0007_saHNLD~M9lIuZ2cAPgk0gf1","ZC0007_fGzNLD~M9lIuZ2cAllDnKf1","ZC0007_saHNLD~M9lIuZ2cAens0gf1","ZC0007_saHNLD~M9lIuZ2cAyP42rf1","ZC0007_saHNLD~M9lIuZ2cAf8A2vf1","ZC0007_saHNLD~M9lIuZ2cAAFc2Rf1","ZC0007_saHNLD~M9lIuZ2cAsAo2If1","ZC0007_saHNLD~M9lIuZ2cAu9k34f1","ZC0007_tqbNLD~M9lIuZ2cAAcVIXf1","ZC0007_t6fNLD~M9lIuZ2cAcTVRyf1","ZC0007_t6fNLD~M9lIuZ2cAf~1VGf1","ZC0007_t6fNLD~M9lIuZ2cAhv9Vgf1","ZC0007_t6fNLD~M9lIuZ2cAmdlUpf1",],
        # ["ZC0007_t6fNLD~M9lIuZ2cAFYxU1f1","ZC0007_t6fNLD~M9lIuZ2cA3INU6f1","ZC0007_t6fNLD~M9lIuZ2cAcGxUif1","ZC0007_t6fNLD~M9lIuZ2cAO2FUcf1","ZC0007_t6fNLD~M9lIuZ2cA5RtUzf1","ZC0007_t6fNLD~M9lIuZ2cApg1Ugf1","ZC0007_t6fNLD~M9lIuZ2cAFzBULf1","ZC0007_t6fNLD~M9lIuZ2cA4sdXPf1","ZC0007_t6fNLD~M9lIuZ2cAqKNXof1","ZC0007_t6fNLD~M9lIuZ2cAJSJXOf1","ZC0007_t6fNLD~M9lIuZ2cAL_JWpf1","ZC0007_t6fNLD~M9lIuZ2cAZRVVtf1","ZC0007_uqrNLD~M9lIuZ2cAlNSF5f1","ZC0007_uqrNLD~M9lIuZ2cA002BGf1","ZC0007_uqrNLD~M9lIuZ2cA~uSCOf1","ZC0007_uqrNLD~M9lIuZ2cAngyDXf1","ZC0007_uqrNLD~M9lIuZ2cAL2KCsf1","ZC0007_uqrNLD~M9lIuZ2cAS0aFYf1","ZC0007_uqrNLD~M9lIuZ2cAWf~Edf1","ZC0007_uqrNLD~M9lIuZ2cA8KiHVf1","ZC0007_uqrNLD~M9lIuZ2cAIGWFgf1","ZC0007_u6vNLD~M9lIuZ2cAEF~VIf1","ZC0007_u6vNLD~M9lIuZ2cAqqKT0f1","ZC0007_u6vNLD~M9lIuZ2cAdEaT4f1","ZC0007_u6vNLD~M9lIuZ2cARo~Tkf1",],
        # ["ZC0007_u6vNLD~M9lIuZ2cAn9WSZf1","ZC0007_u6vNLD~M9lIuZ2cAdmuTHf1","ZC0007_u6vNLD~M9lIuZ2cAzlCSzf1","ZC0007_u6vNLD~M9lIuZ2cAfV2Sbf1","ZC0007_u6vNLD~M9lIuZ2cAf~uVpf1","ZC0007_u6vNLD~M9lIuZ2cAsz6VGf1","ZC0007_u6vNLD~M9lIuZ2cAQxyUPf1","ZC0007_u6vNLD~M9lIuZ2cAxEWXYf1","ZC0007_u6vNLD~M9lIuZ2cALxWXaf1","ZC0007_u6vNLD~M9lIuZ2cArCqXJf1","ZC0007_uKjNLD~M9lIuZ2cAKhGp7f1","ZC0007_uKjNLD~M9lIuZ2cA7fKibf1","ZC0007_u6vNLD~M9lIuZ2cAh8mXZf1","ZC0024_bn7NhpWMU_cuZWUA9wpoWe2","ZC0024_TV3NpbaMOp4uZWUA6eg7Me1","ZC0024_08PNw9CMDakuZWUAdbvv7dc","ZC0024_MCDNT1yM1XEuZWUAaNIAQdb","ZC0024_gpLNbn2MvBguZWUA_EFLvda","ZC0024_0MDN~eqMhSEuZWUABu5bqd9","ZC0024_rr7NFwSMbMguZGQAAkFemd8","ZC0024_S1vNNySMN5MuZGQAsQRSsd7","ZC0024_qrrNg5CMHLguZGQASXtsBd6","ZC0024_28vN38yM50MuZGQAuDCBpd5",],
        # ["ZC0024_AxPNKTqMz2suZGQAHnshfd4","ZC0024_Dh7NTl2MljIuZGQA0Kerqd3","ZC0024_6PjN~eqMctYuY2MABHAjOd2","ZC0024_~OjNkoGMReEuY2MAWoIWrd1","ZC0024_s6PNpLeMLIguY2MA2LjN7cc","ZC0024_IzPNPi2M9FAuY2MAUosXFcb","ZC0024_lobNWkmM33suY2MApB9uNca","ZC0024_bX3NydqMpAAuY2MAyzSnCc9","ZC0024_9eXNnY6MjCguY2MA~wsEUc8","ZC0024_gJDNEAOMIoYuDQ0At6~uOc7","ZC0024_QlLNZHeMROAu9PQAO~3xJc6","ZC0025_0MDNr7yM2X0umpoAYASfFc5","ZC0024_anrN4_CMTuouo6MA8Hl7Sc4","ZC0024_1MTNY3CM3XkumpoAlC_uSc3","ZC0024_CBjNiZqMTuouwMAAb6lKDc2","ZC0024_JTXNQVKMGb0uEBAAsawxWc1","ZC0024_hJTNt6SMGLwu1NQAhXr7Nbc","ZC0026_UUHNOyiMLoouAQEAn7z~abb","ZC0025_prbNx9SMyGwuICAAYxRZebb","ZC0024_GwvNg5CMmT0u5eUA8WQETba","ZC2924-va2Ifm3~c9eaWlo7IbIrNb9","ZC3024-anqFQlHETenNAgJj~xWMHb8","ZC3424-XU2JTV6O50O4Hx9_Doj1Kb7","ZC2924-WkrEt6T2hiL2SUkp9njDCb6","ZC3424-2cmYGwh4ogatTk4uIBGSXb5",],
        # ["ZC3425-gJBR3M8g6EzIJSVFWExEZb4","ZC2924-ZHS2NSbMTemzcnISnkMxJb3","ZC3424-IzMkHA8iDqqcUFAwHMO0cb2","ZC2924-S1tZm4izQeXoeHgYHEgXUb1","ZC3024-SVl87_ygkTXRCAhXzWHaRac","ZC3024-aXl1EgHqkTWJXV0CPOvoaab","ZC3024-EACQXU5GxGD0FxdIH559Maa","ZC2924-Slq8pbYz2HwQf38gVlYYBa9","ZC3024-0cFZLzy1qg5NGhpFhGpxNa8","ZC3424-IjIByNt5~FxGXl4BaRbSBa7","ZC3424-praZTF9GBqJRVVULZ07VGa6","ZC3024-gZEq28jYuBzWExNNWnrHWa5","ZC3424-m4tQ3M9hsRW3RUUbzMlgJa4","ZC2924-4PAHe2jJAqbfREQaEHd5aa3","ZC3024-~elhFwSKjyt4Tk4QTo85Sa2","ZC3424-zt6LWUr53HhSAABepek8Xa1","ZC2924-YnKS4fI3qQ0MRkYYo32kD9c","ZC2924-ZXVrPi0uvhrAPz9ir8C0H9b","ZC2924-RFQ328hK1XHAGxtGDDioB9a","ZC3424-ydmlcGP~vBiRLCxxPw7Ma99","ZC3424-koLnkYKFDanIbm4zCEBEJ98","ZC3025-NiYDmokDHrqCQ0MekbYDH97","ZC2925-zt7yoLOyZsLTFBRJ0g~nW96","ZC3425-IjL6TV5~5kKqbW0xwPOzC95","ZC3025-iJhmmIttjirqUFAMUAzee94",],
        # ["ZC3026-YXGSuaqbMpYPX18DG7vQT93","ZC2925-NiYT9eYndtKgHBxA3IUMb92","ZC2926-wND6d2Tp~l4VKyt3dt_5N91","ZC3003-PCxTGAuirgonBARYG~~ka91","ZC2927-sKCauapahyPffn4liuJCG8b","ZC3402-~uoNyNuBshbNFRVOcKarc8b","ZC3001-Bxfv7f5XyW3cKSlyGD7LQ8a","ZC3431-pLRYyNvdvxuSICB7jtz0f88","ZC3426-HAxasaJGowdefHwnwf3Zc87","ZC2926-YXGjz9ztoQU0GRlCPZpKQ86","ZC3028-IDD77v0HvBgTJiZ9IMOJL85","ZC2925-obGcBxRnkTXVVlYMNUvwE84","ZC0326-2ckA18QlBqIVYGA6WXSxH83","ZC5328-IzOLNCdWF7MlVFQOxis5I82","ZC5512-AhKDXU7f4UXFcnIo52aJb82","ZC1325-1cVPRFeZym4HSkoQdtMvE81","ZC5325-tKROUUJYpwNCV1cNt6zLe7c","ZC1326-GAhdzd7dP5uBKytx0F8NX7b","ZC5526-9~eyZ3R3rQkTS0sRutxfF7b","ZC5525-hJR8Pi0NzWmZKipzCTJuc7a","ZC0326-o7OSzN~y2Hy2DAxVRexuf79","ZC1326-zt4hhJf8EbXCZmY_PxDbT77","ZC0326-TFyhw9C7ctahSEgRpjW8O77","ZC5526-zt7tcGNNctaGEhJLw0ddD76","ZC1326-Xk6Azt2b239YVFQNqxSWF75",],
        # ["ZC1326-~~slaHs9dND3eHgh~3BHJ75","ZC5529-SVnd2cql0nZyZ2c~Yo~cb74","ZC0228-h5fRhZZMUvZCUlIKPAFtG72","ZC5526-GAgyjp3cCa0kHx9Ht2zVE71","ZC5526-5vZfsaJjf9u7YGA4FxrwN6c","ZC1803-a3u4oLNp4UUEJiZ~diG5f6c","ZC5331-8~M3BxRtWf3rLi52flNQJ6a","ZC5325-CxtlUkGnGLxbAgJVSeuXQ69","ZC0025-LT3JloVPA6caOTluQcAuV68","ZC5326-uKhRSlk8kjahMjJlLtNoZ67","ZC0224-Hg69no1CG7_TcnIly0npZ66","ZC0127-2MiIHg2DcNT0PDxr~Ta6W64","ZC0224-saH4AhHkMZVmREQS6eNsH63","ZC5524-sKBm8eKMBKBtfHwqfwuhB62",],

    ],
    "交通银行":[
        # ["ZC0017_4fHN7f6MWv4uZWUAICCZ4e2","ZC0017_dGTNHA~MLYkuZWUAQtq7Qe1","ZC0017_tqbN5PeM9FAuZWUAgb9E3dc","ZC0017_QVHNv6yM3XkuZWUAj~ofqdb","ZC0017_2MjNiZqMpAAuZWUAOJ_98da","ZC0017_RVXNVkWMjCguZWUAswwLUd9","ZC0017_rr7NemmMV_MuZGQA0c5iEd8","ZC0017_28vNv6yMP5suZGQA281Rqd7","ZC0017_FQXN9~SMB6MuZGQAUnSOhd6","ZC0017_nIzN9OeM7kouZGQAHzb00d5","ZC0017_BxfNrb6MtxMuZGQAlNsZGd4","ZC0017_IzPNr7yMnjouZGQAVcR6Rd3","ZC0017_eGjN5PeMZcEuY2MApU8xCd2","ZC0017_jp7NDR6MTOguY2MAij94ed1","ZC0017_PCzNABOMF7MuY2MA7foCkcc","ZC0017_0sLNY3CM_1suY2MAzhgOScb","ZC0017_PS3NkYKMx2MuY2MA_kfJZca","ZC0017__OzN~eqMrwsuY2MAWNK11c9","ZC0017_IDDNwtGMdtIuYmIAzfqk7c8","ZC0018_gJDNKziMxGAuysoAGbypRc7","ZC0018_QlLNTV6MYcUuc3MAK1R_Jc6","ZC0018_KTnNnI~MiS0uwMAAI_fHMc5","ZC0018__e3NBxSMV_MugYEAylpTRc4","ZC0017_OSnNmIuMCa0uFBQACtmpEc3","ZC0017_3MzNmYqM1nIuIiIARL1Xcc2",],
        # ["ZC0019_q7vNv6yM81cuSUkAJfz_dc1","ZC0017_pbXNvK~MxWEuNDQAhhEJSbc","ZC0017_08PNHQ6MpAAuQ0MA9SOhObb","ZC2917-xtZAfW5kZsKuFxd2cvWECba","ZC2917-u6tmOCt~CKzoDw9ukModPb9","ZC3417-o7PoGAuuw2d8CgprEJ0LQb8","ZC3017-qbmdx9QNXvoIdXUVGkQXBb7","ZC2917-wNB_bH9bUPQ_EBBwiyTNBb6","ZC2917-xNTp3M9CFbETY2MDCgUOJb5","ZC3018-fm5aq7iZNZHqIiJCBy6zKb4","ZC3018-2sq~nI_OEbXnQEAgzTPPRb3","ZC3417-Dh5KBBcX1nJfS0srz4vsWb2","ZC3017-PS3SgpHCTuruIiJCN~rQSb1","ZC3018-cmKQxdZ89VGKQUEeBxhSDac","ZC3417-IjIfABONf9toDAxTbvI1Zab","ZC2917-sqKpJTbZV_N5Dg5R2RvCGaa","ZC2917-3c0P8~Co_lo5JSV6DVi5Ia9","ZC2917-no5RqbrhVvLIa2s0Fu4PTa8","ZC3017-BhaS6_hQbMjZQ0McOUapUa7","ZC3019-Cxv2WkljnjrWeXknh8zqHa6","ZC3417-OirASVrT8FTNWloEl2~NDa4","ZC3017-~OjndWblNJDgeXknRqNeTa3","ZC2918-gZGHorGdfdn7Kip02NYZHa1","ZC2917-U0OLCxjdReEZfX0gjGuTN9c",],
        # ["ZC3418-IjKN3c5IBqJzLS1wvaxLe9b","ZC3017-Dx8xFAcQ9FD4aWk0vbLGB9a","ZC2917-eWlnMiH5e99faWk0dAZIG99","ZC3418-jJxJmom2rQlRKyt2jFR8T98","ZC3017-0sKGT1yfiy_xf38jhUy_C95","ZC3418-koL_zd6HQORTFxdLDEKqT94","ZC3017-aHht2cr21HAZLCxwnbJrT92","ZC3418-5_eiDxzClDBwDQ1R3DiQZ91","ZC2918-IzMvv6xaiS06Kyt3RTvxJ8c","ZC2918-wtLbdmUlctYmVFQPE_xKY8b","ZC3417-QVH1ZHc_jirtKipx_e9hb8a","ZC2918-jZ1buqmFxWFGPz9k_weSP86","ZC2918-mYl18~ApkTXLUlIIh4TyV85","ZC3018-uam7jZ53aMwaZWU_mu9zB84",],
    ],
    "中国银行":[
        # ["ZL0007_a3vNNiWM9lIuZ2cA7Byenf1","ZL0007_aHjNNiWM9lIuZ2cAFKKmmf1","ZL0007_cmLNNiWM9lIuZ2cA1x8M6f1","ZL0007_cGDNNiWM9lIuZ2cAx6snCf1","ZL0007_RFTNNiWM9lIuZ2cAxA9vif1","ZL0007_RVXNNiWM9lIuZ2cA_xZ0Ff1","ZL0007_S1vNNiWM9lIuZ2cADMSflf1","ZL0007_SFjNNiWM9lIuZ2cAIZWm2f1","ZL0007_UkLNNiWM9lIuZ2cAWEwNQf1","ZL0007_VETNNiWM9lIuZ2cADfxsWf1","ZL0007_WkrNNiWM9lIuZ2cAlXeBpf1","ZL0007_W0vNNiWM9lIuZ2cAZ1SfTf1","ZL0007_WUnNNiWM9lIuZ2cAhCm6hf1","ZL0007_Xk7NNiWM9lIuZ2cAE0LBif1","ZL0007_XEzNNiWM9lIuZ2cAe5jrzf1","ZL0007_oLDNNiWM9lIuZ2cA1zwj0f1","ZL0007_prbNNiWM9lIuZ2cAwipPTf1","ZL0007_p7fNNiWM9lIuZ2cAiLxVgf1","ZL0007_pbXNNiWM9lIuZ2cAH6VzXf1","ZL0007_q7vNNiWM9lIuZ2cAMCWR4f1","ZL0007_rr7NNiWM9lIuZ2cAl7XKIf1","ZL0007_r7_NNiWM9lIuZ2cAvOrUxf1","ZL0007_rb3NNiWM9lIuZ2cAW3Dxkf1","ZL0007_s6PNNiWM9lIuZ2cAqlEdKf1","ZL0007_sKDNNiWM9lIuZ2cABsIhHf1",],
        # ["ZL0007_tqbNNiWM9lIuZ2cANa9Emf1","ZL0007_tKTNNiWM9lIuZ2cA~5dglf1","ZL0007_taXNNiWM9lIuZ2cAWTJ~1f1","ZL0007_uKjNNiWM9lIuZ2cA95KjQf1","ZL0007_vq7NNiWM9lIuZ2cAxhTJDf1","ZL0007_vKzNNiWM9lIuZ2cA6MTs1f1","ZL0007_va3NNiWM9lIuZ2cAzF_x4f1","ZL0007_gpLNNiWM9lIuZ2cAraYF1f1","ZL0007_gJDNNiWM9lIuZ2cA0Jojwf1","ZL0007_h5fNNiWM9lIuZ2cAqOBTff1","ZL0007_hZXNNiWM9lIuZ2cA4SJ1Uf1","ZL0007_iprNNiWM9lIuZ2cA6s2Grf1","ZL0007_iJjNNiWM9lIuZ2cAFOWghf1","ZL0007_jp7NNiWM9lIuZ2cAOBXINf1","ZL0007_j5_NNiWM9lIuZ2cAC8fU~f1","ZL0007_koLNNiWM9lIuZ2cA1ZUH8f1","ZL0007_lobNNiWM9lIuZ2cAE0lDsf1","ZL0007_lITNNiWM9lIuZ2cAlNhnTf1","ZL0007_nIzNNiWM9lIuZ2cApZbnzf1","ZL0007_x9fNNiWM9lIuZ2cAe9pTBf1","ZL0007_xdXNNiWM9lIuZ2cAorR6Tf1","ZL0007_1MTNNiWM9lIuZ2cAHEliEf1","ZL0007_2srNNiWM9lIuZ2cAnNaGHf1","ZL0007_3s7NNiWM9lIuZ2cAafzFKf1","ZL0007_ITHNNySM9lIuZ2cAxjg4kf1",],
        # ["ZL0007_JTXNNySM9lIuZ2cAndV3xf1","ZL0007_KTnNNySM9lIuZ2cAW0e45f1","ZL0007_LT3NNySM9lIuZ2cAPSX4yf1","ZL0007_YXHNOCuM9lIuZ2cA~eo~qf1","ZL0007_Z3fNOCuM9lIuZ2cA7t1bVf1","ZL0007_ZHTNOCuM9lIuZ2cAFw5ixf1","ZL0007_cGDNOCuM9lIuZ2cAl7wrkf1","ZL0007_dmbNOCuM9lIuZ2cA2FxPPf1","ZL0007_dGTNOCuM9lIuZ2cAj3tkif1","ZL0007_emrNOCuM9lIuZ2cAqfiO4f1","ZL0007_eGjNOCuM9lIuZ2cAJg6sIf1","ZL0007_fm7NOCuM9lIuZ2cAvfjPrf1","ZL0007_fGzNOCuM9lIuZ2cAi1HmTf1","ZL0007_SVnNOCuM9lIuZ2cAN3KyTf1","ZL0007_TFzNOCuM9lIuZ2cAcNjjRf1","ZL0007_TV3NOCuM9lIuZ2cA0cT2Cf1","ZL0007_U0PNOCuM9lIuZ2cAShEVvf1","ZL0007_X0_NOCuM9lIuZ2cAEEnQof1","ZL0007_orLNOCuM9lIuZ2cA8yoJNf1","ZL0007_oLDNOCuM9lIuZ2cABv0vXf1","ZL0007_obHNOCuM9lIuZ2cA_Io9vf1","ZL0007_q7vNOCuM9lIuZ2cAQnGXcf1","ZL0007_rr7NOCuM9lIuZ2cAk3vDcf1","ZL0020_Dx_NVEeM7kouZ2cAkDnLoec","ZL0020_morNorGMtxMuZ2cALhvHheb",],
        # ["ZL0020_GQnNw9CMnjouZ2cAqCbePea","ZL0020_rr7NTl2MZsIuZmYA~Bhege9","ZL0020_9eXNaXqMSe0uZmYAt_PPRe8","ZL0020_OSnNjJ~MEbUuZmYAmUJXae7","ZL0020_f2_NFgWM~V0uZmYAE~zd~e6","ZL0020_DBzNNySMwGQuZmYAo9_UNe5","ZL0020_4_PNgJOMqQ0uZmYAnptN1e4","ZL0020_MSHN38yMcNQuZWUAyje7ie3","ZL0020_mYnNno2MXvouZWUA958OBe2","ZL0020_KzvNva6MIYUuZWUAUnNMNe1","ZL0020_~urN18SMCKwuZWUAnhp9bdc","ZL0020_MCDNKTqM0HQuZWUAKvIDOdb","ZL0025_xNTNPC~MshYuZWUAqOgjDda","ZL0020_x9fN08CMgCQuZWUAEOYqud9","ZL0020_6_vN8uGMa88uZGQAPW8D2d8","ZL0020_d2fNDh2MMpYuZGQApm~Ynd7","ZL0020_7PzNaHuMGr4uZGQAaAEKbd6","ZL0020_anrNCBuM4kYuZGQAdxme8d5","ZL0020_7PzNDR6Mym4uZGQAouXbEd4","ZL0020_wtLNzd6MnTkuZGQAQ8Vn~d3","ZL0020_x9fN8~CMeNwuY2MAvUfZId2","ZL0020_qrrN7v2MQ~cuY2MAWGI__d1","ZL0020_kYHNLzyMKo4uY2MAA3HiFcc","ZL0021_6PjN2MuM8VUuY2MA2cKsEcb","ZL0020_HAzN2cqM2n4uY2MAikfKMca",],
        # ["ZL0020_eWnNJzSMogYuY2MAri3rOc9","ZL0020_obHNRlWMddEuYmIAI~S~jc8","ZL0020_b3_NNySME7cu1NQADAh8Qc7","ZL0020_YXHNmYqMuh4u5OQA8fOnVc6","ZL0020_3c3NJjWMqw8uAQEAb0eWcc5","ZL0020_o7PNuqmMddEuJCQANY8~Cc4","ZL0020_KzvNsaKM238uNDQAD4WvEc3","ZL0020_dGTN08CMFrIuwcEAy3npUc2","ZL0020_a3vNuaqMwGQuWloApfVmMc1","ZL0020_QVHNXU6MO58upqYAaHsCHbc","ZL0020_q7vNmIuMMZUuLCwA4i7jXbb","ZL0020_MiLNprWMW_8uQ0MAdsLQEba","ZL2920-m4t~5_ReogZBAQFgzJCDIb9","ZL3420-5fXrY3Df4UVbHh5_6XK2ab8","ZL2921-_Oz~dWakrgr9AwNj~j5KLb7","ZL3020-n4_uemkiuBzSTU0tfIELDb6","ZL3420-18e16PuV9lL3PT1d48mxCb5","ZL3020-Hg4n2sl1kTVIYGAAmEW_Tb4",],
    ],
    "招商银行":[
        # ["ZL0007_vq7NVEeM9lIuZ2cAfXPF1f1","ZL0007_vq7NVEeM9lIuZ2cAVRnAhf1","ZL0007_v6_NVEeM9lIuZ2cAYinVif1","ZL0007_v6_NVEeM9lIuZ2cApJjTQf1","ZL0007_v6_NVEeM9lIuZ2cAYXPdLf1","ZL0007_v6_NVEeM9lIuZ2cAMJLbLf1","ZL0007_vq7NVEeM9lIuZ2cACLDGMf1","ZL0007_vq7NVEeM9lIuZ2cAExPFCf1","ZL0007_vq7NVEeM9lIuZ2cAoHfFff1","ZL0007_uanNVEeM9lIuZ2cAPiW08f1","ZL0007_uKjNVEeM9lIuZ2cA8iWkHf1","ZL0007_uKjNVEeM9lIuZ2cAXcal~f1","ZL0007_vKzNVEeM9lIuZ2cAsaHmof1","ZL0007_vKzNVEeM9lIuZ2cAI7vi9f1","ZL0007_vKzNVEeM9lIuZ2cA~4bjQf1","ZL0007_vKzNVEeM9lIuZ2cAXbXgSf1","ZL0007_vKzNVEeM9lIuZ2cAFXfu3f1","ZL0007_vKzNVEeM9lIuZ2cAk_Xvff1","ZL0007_vKzNVEeM9lIuZ2cAJXzrnf1","ZL0007_vKzNVEeM9lIuZ2cABMvrJf1","ZL0007_v6_NVEeM9lIuZ2cAk1bUxf1","ZL0007_vq7NVEeM9lIuZ2cArj_Hhf1","ZL0007_va3NVEeM9lIuZ2cAwFz79f1","ZL0007_aXnNNySM9lIuZ2cAgW64Bf1","ZL0007_anrNNySM9lIuZ2cAoSSJ3f1",],
        # ["ZC0319-jZ04mIsKNJBeCQlR2~0SN73","ZC0319-BxcOCxhCoQWsfHwkTXQMC72","ZC0220-hZX85vUfNZERdXUt6FbbO71","ZC5519-emp2PC_JKo7ZTEwUXQ9aP6c","ZC5519-p7dj~~jDqg4~ZWU9INLeW6b","ZC1819-w9Pa8ONvGb26MDBolIvsY6a","ZC1819-ytppKzg~tRHxVlYB9hvUR69","ZC0320-PCxaSlljgSWSXFwLos3WB68","ZC0219-kIAOLD_C0XX4CQleDMBtB67","ZC0119-cGCV3s1dkzdRLi55jrBJI66","ZC5519-~OhLHwz22X1oVlYB5w53A64","ZC0219-VkY4BBc61HCdVFQCpUqqS63","ZC5319-_OzROCszkjbxNjZg2pRRG62","ZC1819-CBhuzt3s4UXbXFwKQ4fpE61","ZC0219-bn7I3s2H238Kbm44GLtpV5c","ZC0320-0cF0FAcDWPyyRkYQBqZyU5b","ZC0420-bn5kYHMOsxcyODhu0WsjK5a",],

        # ["ZL0016_JxDNLz~MmqYuZ2cAZ6JIvf1","ZL0016_JxDNLz~MmqYuZ2cAvjdP6f1","ZL0016_JxDNLz~MmqYuZ2cAzahClf1","ZL0016_JxDNLz~MmqYuZ2cAi_5C6f1","ZL0016_JxDNLz~MmqYuZ2cA3fRGuf1","ZL0016_JxDNLz~MmqYuZ2cAvo5ECf1","ZL0016_JBPNLz~MmqYuZ2cAdw55cf1","ZL0016_JRLNLz~MmqYuZ2cAfAtrnf1","ZL0016_JhHNLz~MmqYuZ2cAYvBekf1","ZL0016_JhHNLz~MmqYuZ2cAG7VfKf1","ZL0016_JhHNLz~MmqYuZ2cAPARdkf1","ZL0016_JhHNLz~MmqYuZ2cASclSif1","ZL0016_JhHNLz~MmqYuZ2cAtqpT~f1","ZL0016_JhHNLz~MmqYuZ2cAzMVXWf1","ZL0016_IRbNLz~MmqYuZ2cAlZkrcf1","ZL0016_IRbNLz~MmqYuZ2cAmrEvTf1","ZL0016_IRbNLz~MmqYuZ2cALzYicf1","ZL0016_IRbNLz~MmqYuZ2cAFsUjtf1","ZL0016_IRbNLz~MmqYuZ2cAIOUnnf1","ZL0016_JhHNLz~MmqYuZ2cAai5bGf1","ZL0016_JhHNLz~MmqYuZ2cABYRYQf1","ZC2817-mq267f0Gt4tARUUdui~Ye73","ZC2518-RnEJ5_fEAz~YbW01DGDrG72","ZC2617-6t2sAhImnqLcGRlBDHTkH71","ZC2818-s4QmkIDvU286JiZ~ETwGG6c",],
        # ["ZC2617-9cLWOiqZ9srnPT1lyNcsd6b","ZC2717-IxQNEwPBQn56KytzBc7MT6a","ZC2717-Sn2E2cnSRXmkb284moMgS69","ZC2717-0eaYanrw8c1GX18IOK2mX67","ZC2017-rZphTl7pJhp5Q0MUinECW66","ZC2017-l6DyaHhlAz8EdHQjC6Uec65",],

        ["ZL0016_CzzN9OSMmqYuZ2cACbWAaf1","ZL0016_CD_N9OSMmqYuZ2cAKC29Ef1","ZL0016_CD_N9OSMmqYuZ2cAr3yySf1","ZL0016_CD_N9OSMmqYuZ2cAWhWyAf1","ZL0016_CD_N9OSMmqYuZ2cA0huwff1","ZL0016_CD_N9OSMmqYuZ2cAb3Cx0f1","ZL0016_CD_N9OSMmqYuZ2cA6ASzvf1","ZL0016_CD_N9OSMmqYuZ2cAgPyxXf1","ZL0016_CD_N9OSMmqYuZ2cAJqG2_f1","ZL0016_CD_N9OSMmqYuZ2cAZI6wYf1","ZL0016_CD_N9OSMmqYuZ2cASHexef1","ZL0016_CD_N9OSMmqYuZ2cAmS~xCf1","ZL0016_CD_N9OSMmqYuZ2cAB8G2Df1","ZL0016_CD_N9OSMmqYuZ2cAOpyxSf1","ZL0016_CD_N9OSMmqYuZ2cA7b~39f1","ZL0016_CD_N9OSMmqYuZ2cA8KOwgf1","ZL0016_CT7N9OSMmqYuZ2cAlt6g6f1","ZL0016_CT7N9OSMmqYuZ2cAuSajFf1","ZL0016_CT7N9OSMmqYuZ2cAfv~hdf1","ZL0016_CT7N9OSMmqYuZ2cAufmmlf1","ZL0016_CT7N9OSMmqYuZ2cAiYygnf1","ZL0016_CT7N9OSMmqYuZ2cA5iWgdf1","ZL0016_CT7N9OSMmqYuZ2cAx0mhsf1","ZL0016_CT7N9OSMmqYuZ2cAsuCmSf1","ZL0016_CT7N9OSMmqYuZ2cAgnmhaf1",],
        ["ZL0016_CT7N9OSMmqYuZ2cAMwihLf1","ZL0016_CT7N9OSMmqYuZ2cAC0Chtf1","ZL0016_CT7N9OSMmqYuZ2cAq_ansf1","ZL0016_CT7N9OSMmqYuZ2cAsNWm0f1","ZL0016_CT7N9OSMmqYuZ2cAY7em0f1","ZL0016_CT7N9OSMmqYuZ2cArTamcf1","ZL0016_CT7N9OSMmqYuZ2cAOuynSf1","ZL0016_CT7N9OSMmqYuZ2cAyeWmjf1","ZL0016_CT7N9OSMmqYuZ2cAvzSnOf1","ZL0016_CT7N9OSMmqYuZ2cAHVGm9f1","ZL0016_CT7N9OSMmqYuZ2cAYqWkBf1","ZL0016_CT7N9OSMmqYuZ2cA5bymZf1","ZL0016_DjnN9OSMmqYuZ2cA2FnbCf1","ZL0016_DjnN9OSMmqYuZ2cAzh3bIf1","ZL0016_DjnN9OSMmqYuZ2cANXrYpf1","ZL0016_DjnN9OSMmqYuZ2cA7nXbuf1","ZL0016_DjnN9OSMmqYuZ2cAu6DQdf1","ZL0016_DjnN9OSMmqYuZ2cAD~fQmf1","ZL0016_DjnN9OSMmqYuZ2cAnvTRXf1","ZL0016_DjnN9OSMmqYuZ2cA9QLQgf1","ZL0016_DjnN9OSMmqYuZ2cATg_Xgf1",],
    ],

}
for i_list in needs["工商银行"]:
    for i_mailid in i_list:
        gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=VmGFxdWUibUlBARj&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.99%%26ver=12189"%(i_mailid)#周燕华
        # gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%(i_mailid)#boxer
        print(gsyh_url)
        move_and_click(233,1059,1)
        pyautogui.hotkey("command","l")
        # pyperclip.copy("https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%("ZC0012_JjbNgJOMgCQuZ2cAuzM67ea"))
        pyperclip.copy(gsyh_url)
        time.sleep(1)
        pyautogui.hotkey("command","v")
        pyautogui.press("enter")
        time.sleep(5)
        move_and_click(1045,947,1)
        move_and_click(756,612,1)
        move_and_click(1091,580,1)
        move_and_click(1073,555,1)
        move_and_click(1168,256,1)
        # pyautogui.hotkey("command","a")
        # pyautogui.press("delete")
        # move_and_click(1168,256,1)
        pyperclip.copy("""
        for (i in document.querySelectorAll("table")){
            if(i>4){
            if(document.querySelectorAll("table")[i].textContent.indexOf("对账单生成日")>=0){
                console.log("i:",i)
                date_string = document.querySelectorAll("table")[i].textContent.split(" ")[date_string = document.querySelectorAll("table")[i].textContent.split(" ").length-1]
                break
            }
            }
        }
        console.log("工商银行"+date_string+".pdf")
        """)
        pyautogui.hotkey("command","v")
        pyautogui.press("enter")
        time.sleep(2)
        move_and_click(1044,333,1)
        mouse_down("left")
        mouse_up("left",1250,333)
        pyautogui.hotkey("command","c")
        move_and_click(984,800,5)
        move_and_click(1394,260,3)
        move_and_click(864,812,3)
        pyautogui.hotkey("command","a")
        time.sleep(2)
        pyautogui.hotkey("command","v")
        move_and_click(1210,415,3)
        time.sleep(2)
        pyautogui.hotkey("command","w")
for i_list in needs["光大银行"]:
    for i_mailid in i_list:
        gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%(i_mailid)
        print(gsyh_url)
        move_and_click(233,1059,1)
        pyautogui.hotkey("command","l")
        # pyperclip.copy("https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%("ZC0012_JjbNgJOMgCQuZ2cAuzM67ea"))
        pyperclip.copy(gsyh_url)
        time.sleep(1)
        pyautogui.hotkey("command","v")
        pyautogui.press("enter")
        time.sleep(3)
        move_and_click(1045,947,1)
        move_and_click(756,612,1)
        move_and_click(1091,580,1)
        move_and_click(1073,555,1)
        move_and_click(1168,256,1)
        # pyautogui.hotkey("command","a")
        # pyautogui.press("delete")
        # move_and_click(1168,256,1)
        pyperclip.copy("""
        date_string=document.querySelectorAll("table>tbody>tr")[16].textContent.replaceAll(" ","").split("\\n")[1]
        if (date_string==""){date_string=document.querySelectorAll("table>tbody>tr")[15].textContent.replaceAll(" ","").split("\\n")[1]}
        else if (date_string=="信用卡账户信息AccountSummary"){date_string=document.querySelectorAll("table>tbody>tr")[18].textContent.replaceAll(" ","").split("\\n")[1]}
        console.log("光大银行"+date_string+".pdf")
        """)
        pyautogui.hotkey("command","v")
        pyautogui.press("enter")
        time.sleep(2)
        move_and_click(1044,391,1)
        mouse_down("left")
        mouse_up("left",1250,391)
        pyautogui.hotkey("command","c")
        move_and_click(984,800,3)
        move_and_click(1394,260,3)
        move_and_click(864,812,3)
        pyautogui.hotkey("command","a")
        time.sleep(2)
        pyautogui.hotkey("command","v")
        move_and_click(1210,415,3)
        time.sleep(2)
        pyautogui.hotkey("command","w")
needs_all = []
for i_list in needs["民生银行"]:
    for i_mailid in i_list:
        if i_mailid not in needs_all:
            needs_all.append(i_mailid)
is_continue = True
for i_mailid in needs_all:
    print(i_mailid)
    if is_continue:
        if i_mailid =="ZC0224-Hg69no1CG7_TcnIly0npZ66":
            is_continue = False
        continue
    gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=9OQjX0zBvxtlHh55&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.51%%26ver=15696"%(i_mailid)
    print(gsyh_url)
    move_and_click(233,1059,1)
    pyautogui.hotkey("command","l")
    # pyperclip.copy("https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%("ZC0012_JjbNgJOMgCQuZ2cAuzM67ea"))
    pyperclip.copy(gsyh_url)
    time.sleep(1)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(3)
    move_and_click(1045,947,1)
    move_and_click(756,612,1)
    move_and_click(1091,580,1)
    move_and_click(1073,555,1)
    move_and_click(1168,256,1)
    # pyautogui.hotkey("command","a")
    # pyautogui.press("delete")
    # move_and_click(1168,256,1)
    pyperclip.copy("""
    date_string=document.querySelectorAll("table>tbody>tr>td")[86].textContent
    if (date_string.indexOf("/")==-1){
        date_string=document.querySelectorAll("table>tbody>tr>td")[85].textContent
        if (date_string.indexOf("/")==-1){date_string=document.querySelectorAll("table>tbody>tr>td")[102].textContent}
    }else{
        if(date_string.length>20){date_string=document.querySelectorAll("table>tbody>tr>td")[114].textContent}
    }
    console.log("民生银行"+date_string+".pdf")
    """)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(2)
    move_and_click(1044,368,1)
    mouse_down("left")
    mouse_up("left",1250,368)
    pyautogui.hotkey("command","c")
    move_and_click(984,800,3)
    move_and_click(1394,260,2)
    move_and_click(864,812,2)
    pyautogui.hotkey("command","a")
    time.sleep(2)
    pyautogui.hotkey("command","v")
    move_and_click(1210,415,2)
    time.sleep(1)
    move_and_click(916,524,1)
    time.sleep(1)
    pyautogui.hotkey("command","w")
    time.sleep(1)
needs_all = []
for i_list in needs["交通银行"]:
    for i_mailid in i_list:
        if i_mailid not in needs_all:
            needs_all.append(i_mailid)
is_continue = True
for i_mailid in needs_all:
    print(i_mailid)
    if is_continue:
        if i_mailid =="ZC2917-eWlnMiH5e99faWk0dAZIG99":
            is_continue = False
        continue
    gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=9OQjX0zBvxtlHh55&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.51%%26ver=15696"%(i_mailid)
    print(gsyh_url)
    move_and_click(233,1059,1)
    pyautogui.hotkey("command","l")
    # pyperclip.copy("https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%("ZC0012_JjbNgJOMgCQuZ2cAuzM67ea"))
    pyperclip.copy(gsyh_url)
    time.sleep(1)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(3)
    move_and_click(1045,947,1)
    move_and_click(756,612,1)
    move_and_click(1091,580,1)
    move_and_click(1073,555,1)
    move_and_click(1168,256,1)
    # pyautogui.hotkey("command","a")
    # pyautogui.press("delete")
    # move_and_click(1168,256,1)
    pyperclip.copy("""
    date_string=document.querySelectorAll("table>tbody>tr>td>p")[2].textContent.split("的")[1]
    if(date_string==undefined){
        date_string=document.querySelectorAll("table>tbody>tr>td>p")[3].textContent.split("的")[1]
        if(date_string==undefined){date_string=document.querySelectorAll("table>tbody>tr>td>p")[1].textContent.split("是您")[1]}
    }else if(date_string.indexOf("信用卡即将到期失效，新卡会在近期寄往您")>-1){date_string=document.querySelectorAll("table>tbody>tr>td>p")[1].textContent.split("的")[1]}
    console.log("交通银行"+date_string+".pdf")
    """)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(2)
    move_and_click(1044,368,1)
    mouse_down("left")
    mouse_up("left",1290,368)
    pyautogui.hotkey("command","c")
    move_and_click(984,781,3)
    move_and_click(984,800,3)
    move_and_click(1394,260,2)
    move_and_click(864,812,2)
    pyautogui.hotkey("command","a")
    time.sleep(2)
    pyautogui.hotkey("command","v")
    move_and_click(1210,415,2)
    time.sleep(1)
    move_and_click(916,524,1)
    time.sleep(1)
    pyautogui.hotkey("command","w")
    time.sleep(1)
needs_all = []
for i_list in needs["中国银行"]:
    for i_mailid in i_list:
        if i_mailid not in needs_all:
            needs_all.append(i_mailid)
is_continue = False
for i_mailid in needs_all:
    print(i_mailid)
    if is_continue:
        if i_mailid =="ZC2917-eWlnMiH5e99faWk0dAZIG99":
            is_continue = False
        continue
    gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=9OQjX0zBvxtlHh55&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.51%%26ver=15696"%(i_mailid)
    print(gsyh_url)
    move_and_click(233,1059,1)
    pyautogui.hotkey("command","l")
    # pyperclip.copy("https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%("ZC0012_JjbNgJOMgCQuZ2cAuzM67ea"))
    pyperclip.copy(gsyh_url)
    time.sleep(1)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(8)
    move_and_click(1045,947,1)
    move_and_click(756,612,1)
    move_and_click(1091,580,1)
    move_and_click(1073,555,1)
    move_and_click(1168,256,1)
    # pyautogui.hotkey("command","a")
    # pyautogui.press("delete")
    # move_and_click(1168,256,1)
    pyperclip.copy("""
    document.querySelectorAll(".down_big>a")[1].click()
    """)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(2)
    # pyautogui.hotkey("command","w")
    # time.sleep(1)
needs_all = []
for i_list in needs["招商银行"]:
    for i_mailid in i_list:
        if i_mailid not in needs_all:
            needs_all.append(i_mailid)
is_continue = False
for i_mailid in needs_all:
    print(i_mailid)
    if is_continue:
        if i_mailid =="ZC2917-eWlnMiH5e99faWk0dAZIG99":
            is_continue = False
        continue
    gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=VmGFxdWUibUlBARj&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.99%%26ver=12189"%(i_mailid)#周燕华
    # gsyh_url = "https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=9OQjX0zBvxtlHh55&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.51%%26ver=15696"%(i_mailid)
    print(gsyh_url)
    move_and_click(233,1059,1)
    pyautogui.hotkey("command","l")
    # pyperclip.copy("https://mail.qq.com/cgi-bin/frame_html?t=newwin_frame&sid=QlIcV0R_JYH8Ly9I&url=/cgi-bin/readmail?folderid=1%%26folderkey=%%26t=readmail%%26mailid=%s%%26mode=pre%%26maxage=3600%%26base=11.55%%26ver=16904"%("ZC0012_JjbNgJOMgCQuZ2cAuzM67ea"))
    pyperclip.copy(gsyh_url)
    time.sleep(1)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(8)
    move_and_click(1045,947,1)
    move_and_click(756,612,1)
    move_and_click(1091,580,1)
    move_and_click(1073,555,1)
    move_and_click(1168,256,1)
    # pyautogui.hotkey("command","a")
    # pyautogui.press("delete")
    # move_and_click(1168,256,1)
    pyperclip.copy("""
    document.querySelectorAll(".down_big>a")[1].click()
    """)
    pyautogui.hotkey("command","v")
    pyautogui.press("enter")
    time.sleep(2)


