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
Hs.page_loading_flag_text_num = 0
do ()->
    Hs.page_2_finish_init = ()->
        document.querySelector(".page_2_finish").classList.add("page_finish_fade_in")
        document.querySelector(".page_2_finish").style.display="block"
        document.querySelector(".page_2_finish").style.opacity="1"
        document.querySelector(".page_media").classList.add("page_finish_fade_in")
        document.querySelector(".page_media").style.display="block"
        document.querySelector(".page_media").style.opacity="1"
        setTimeout ()->
            document.querySelector(".page_zheng").classList.add("page_word_fade_in")
        ,1000
        setTimeout ()->
            document.querySelector(".page_dang").classList.add("page_word_fade_in")
        ,2000
        setTimeout ()->
            document.querySelector(".page_sheng").classList.add("page_word_fade_in")
        ,3000
        setTimeout ()->
            document.querySelector(".page_qi").classList.add("page_word_fade_in")
        ,4000
        setTimeout ()->
            document.querySelector(".page_shou").classList.add("page_word_fade_in")
        ,5000

    Hs.page_1_finish = ()->
        document.querySelector(".page_1_finish").classList.add("page_finish_fade_out")
        setTimeout ()->
            Hs.page_2_finish_init()
        ,1000

    Hs.media_play = ()-> #设置一个叫做Hs.media_play的方法
        document.querySelector("#media").play() #设置id为media标签播放
    Hs.media_pasure = ()-> #设置一个叫做Hs.media_pasure的方法
        document.querySelector("#media").pause() #设置id为media标签暂停
    Hs.loading_animate_play = ()->
        document.querySelector(".page_loading_flag").classList.add("page_loading_flag_animate")
        page_loading_flag_text_timer = setInterval ()->
            Hs.page_loading_flag_text_num = Hs.page_loading_flag_text_num + 5
            document.querySelector(".page_loading_flag_text").innerText = "Loading...#{Hs.page_loading_flag_text_num}%"
            if Hs.page_loading_flag_text_num >=100
                Hs.page_loading_flag_text_num = 100
                clearInterval page_loading_flag_text_timer
                Hs.page_1_finish()
        ,100
    window.addEventListener "load",(evt)-> #给window监听load事件
        Hs.window_resize() #执行Hs.window_resize方法
        Hs.loading_animate_play()
    window.addEventListener "resize",(evt)-> #给window监听resize事件
        Hs.window_resize() #执行Hs.window_resize方法
    document.querySelector(".page_media").addEventListener "click",(evt)->
        if document.querySelector(".page_media").className.indexOf("page_dom_rotate")==-1
            document.querySelector(".page_media").classList.add("page_dom_rotate")
            Hs.media_play()
        else
            document.querySelector(".page_media").classList.remove("page_dom_rotate")
            Hs.media_pasure()


    