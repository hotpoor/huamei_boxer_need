# -*- coding: utf-8 -*-
import os
import sys
import time
import pyautogui
import pyperclip
import re



line_str_demo = "优秀学生必读必知丛书；学生必知的十万个为什么@@新华出版社"

def move_and_click(x,y,wait_time=1,button_str="left"):
    pyautogui.moveTo(x,y)
    if wait_time != 0:
        time.sleep(wait_time);
    pyautogui.click(x,y,button=button_str)
def do_search(line_str=line_str_demo,num_id=0):
    move_and_click(376,16,1,"left")
    move_and_click(1900,87,1,"left")
    pyautogui.hotkey("ctrl","l")
    pyperclip.copy("jd.com")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(2)

    line_str_list = line_str.split("@@")
    line_str_list_search = line_str_list[0]
    line_str_list_company = line_str_list[1]
    line_str_list_search_use = line_str_list_search
    line_str_list_search_use = re.sub(r'\([^)]*\)', '', line_str_list_search_use)
    line_str_list_search_use = re.sub(r'\（[^)]*\）', '', line_str_list_search_use)
    for check_str in ["：","---","--"]:
        line_str_list_search_use_number = line_str_list_search_use.find(check_str)
        if line_str_list_search_use_number!=-1:
            line_str_list_search_use=line_str_list_search_use[line_str_list_search_use_number+1:]

    line_str_list_search_now = "%s %s"%(line_str_list_search_use,line_str_list_company)
    pyperclip.copy(line_str_list_search_now)
    move_and_click(677,147,1,"left")
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("ctrl","shift","i")
    time.sleep(2)
    # 900px屏幕宽度
    move_and_click(1070,90,1,"left")
    move_and_click(940,114,0,"left")
    move_and_click(1611,812,0,"left")

    cmd = """
    $(".p-promo-flag").parents(".gl-item").remove()
    if($(".gl-item>.gl-i-wrap>.p-img").first().length==0){
        var url = "https://item.jd.com/12279949.html";
        var newTab = window.open(url, "_blank");
        if (newTab) {
          newTab.onload = function() {
            console.log("新标签页已加载：" + url);
          };
        }
    }else{
        $(".gl-item>.gl-i-wrap>.p-img").first().find("a")[0].click()
    }
    """
    pyperclip.copy(cmd)
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.hotkey("ctrl","shift","i")
    time.sleep(2)
    move_and_click(1070,90,1,"left")
    move_and_click(940,114,0,"left")
    move_and_click(1611,812,0,"left")

    cmd = """
    a=$("ul.p-parameter-list").find("li")
    b=[]
    b_json={}
    for(i=0;i<a.length;i++){
        b_list = $(a[i]).text().replaceAll(" ","").replaceAll("\\n","").split("：")
        b_json[b_list[0]]=b_list[1]    
    }
    b_json["url"]=window.location.href
    b_json["sku-name"]=$(".sku-name").text().replaceAll(" ","").replaceAll("\\n","")
    b_json["aim-sku-name"]="%s"
    b_json["aim-company"]="%s"
    b_json["aim-num-id"]="%s"
    b.push(b_json)
    $("body").append("<textarea id=\\"xialiwei_textarea\\" style=\\"position:fixed;right:0px;top:0px;z-index:9999;\\"></textarea>")
    $("#xialiwei_textarea").val(JSON.stringify(b))
    """%(line_str_list_search,line_str_list_company.replace("\n",""),num_id)
    pyperclip.copy(cmd)
    pyautogui.hotkey("ctrl","v")
    pyautogui.press("enter")

    move_and_click(751,92,1,"left")
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","c")
    time.sleep(1)
    pyautogui.hotkey("ctrl","w")

    move_and_click(154,15,1,"left")
    move_and_click(573,185,1,"left")
    pyautogui.hotkey("ctrl","a")
    pyautogui.hotkey("ctrl","v")
    move_and_click(562,253,1,"left")


file = open('book0.txt', 'r',encoding='utf-8')

lines = file.readlines()
line_start =811
line_end = 1200
lines = lines[line_start:len(lines)]
for line in lines:
    line_start = line_start+1
    print("第%d行:%s"%(line_start,line))
    do_search(line,line_start)

    if line_start >= line_end:
        break
