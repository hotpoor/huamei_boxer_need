root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs
Hs.base_width = 750 #画面基础宽度
Hs.base_height = 1334 #画面基础高度
Hs.window_resize = ()-> #设置一个叫做Hs.window_resize的方法
    window_height =document.querySelector("body").offsetHeight #获取body标签的当前高度
    Hs.current_width = window_height/Hs.base_height*Hs.base_width #计算当前画面基础宽度
    Hs.current_height = window_height #计算当前画面基础高度
    document.querySelector(".page").style.width="#{Hs.current_width}px" #设置class为page标签的宽度
    document.querySelector(".page").style.height="#{Hs.current_height}px" #设置class为page标签的高度
do ()->
    Hs.media_play = ()-> #设置一个叫做Hs.media_play的方法
        document.querySelector("#media").play() #设置id为media标签播放
    Hs.media_pasure = ()-> #设置一个叫做Hs.media_pasure的方法
        document.querySelector("#media").pause() #设置id为media标签暂停
    window.addEventListener "load",(evt)-> #给window监听load事件
        Hs.window_resize() #执行Hs.window_resize方法
    window.addEventListener "resize",(evt)-> #给window监听resize事件
        Hs.window_resize() #执行Hs.window_resize方法

    