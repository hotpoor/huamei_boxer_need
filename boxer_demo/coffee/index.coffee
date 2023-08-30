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
Hs.page_info =
    "name":null
    "age":null
    "addr":null
    "word":null
do ()->
    Hs.page_7_finish_init = ()->
        document.querySelector(".page_show_right_continue3").classList.remove("page_left_in")
        document.querySelector(".page_button5").classList.remove("hide")
        document.querySelector(".page_button6").classList.add("hide")

        document.querySelector(".page_7_show_cover").classList.add("hide")
        document.querySelector(".page_show_get_img").classList.remove("page_scale_in")

        document.querySelector(".page_show_get_text_name").innerText = ""
        document.querySelector(".page_show_get_text_age").innerText = ""
        document.querySelector(".page_show_get_text_addr").innerText = ""
        document.querySelector(".page_show_get_text_word").innerText = ""


        document.querySelector(".page_star0").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star1").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star2").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star3").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star4").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star5").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star6").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star7").classList.remove("page_finish_fade_in")
        document.querySelector(".page_star8").classList.remove("page_finish_fade_in")

        document.querySelector(".page_star0").classList.add("hide")
        document.querySelector(".page_star1").classList.add("hide")
        document.querySelector(".page_star2").classList.add("hide")
        document.querySelector(".page_star3").classList.add("hide")
        document.querySelector(".page_star4").classList.add("hide")
        document.querySelector(".page_star5").classList.add("hide")
        document.querySelector(".page_star6").classList.add("hide")
        document.querySelector(".page_star7").classList.add("hide")
        document.querySelector(".page_star8").classList.add("hide")

        document.querySelector(".page_flag2").classList.remove("page_flag_up")
        document.querySelector(".page_7_finish").classList.add("page_finish_fade_in")
        document.querySelector(".page_7_finish").style.display="block"
        document.querySelector(".page_7_finish").style.opacity="1"

        setTimeout ()->
            document.querySelector(".page_star0").classList.add("page_finish_fade_in")
            document.querySelector(".page_star0").classList.remove("hide")
        ,500
        setTimeout ()->
            document.querySelector(".page_star1").classList.add("page_finish_fade_in")
            document.querySelector(".page_star1").classList.remove("hide")
        ,1000
        setTimeout ()->
            document.querySelector(".page_star2").classList.add("page_finish_fade_in")
            document.querySelector(".page_star2").classList.remove("hide")
        ,1500
        setTimeout ()->
            document.querySelector(".page_star3").classList.add("page_finish_fade_in")
            document.querySelector(".page_star3").classList.remove("hide")
        ,2000
        setTimeout ()->
            document.querySelector(".page_star4").classList.add("page_finish_fade_in")
            document.querySelector(".page_star4").classList.remove("hide")
        ,2500
        setTimeout ()->
            document.querySelector(".page_star5").classList.add("page_finish_fade_in")
            document.querySelector(".page_star5").classList.remove("hide")
        ,3000
        setTimeout ()->
            document.querySelector(".page_star6").classList.add("page_finish_fade_in")
            document.querySelector(".page_star6").classList.remove("hide")
        ,3500
        setTimeout ()->
            document.querySelector(".page_star7").classList.add("page_finish_fade_in")
            document.querySelector(".page_star7").classList.remove("hide")
        ,4000
        setTimeout ()->
            document.querySelector(".page_star8").classList.add("page_finish_fade_in")
            document.querySelector(".page_star8").classList.remove("hide")
        ,4500










    Hs.page_6_finish_init = ()->
        document.querySelector(".page_6_finish").classList.add("page_finish_fade_in")
        document.querySelector(".page_6_finish").style.display="block"
        document.querySelector(".page_6_finish").style.opacity="1"
    Hs.page_5_finish_init = ()->
        document.querySelector(".page_5_finish").classList.add("page_finish_fade_in")
        document.querySelector(".page_5_finish").style.display="block"
        document.querySelector(".page_5_finish").style.opacity="1"
    Hs.page_4_finish_init = ()->
        document.querySelector(".page_4_finish").classList.add("page_finish_fade_in")
        document.querySelector(".page_4_finish").style.display="block"
        document.querySelector(".page_4_finish").style.opacity="1"
    Hs.page_3_finish_init = ()->
        document.querySelector("#page_3_finish_name").value=""
        document.querySelector("#page_3_finish_age").value=""
        document.querySelector("#page_3_finish_addr").value=""
        document.querySelector(".page_3_finish").classList.add("page_finish_fade_in")
        document.querySelector(".page_3_finish").style.display="block"
        document.querySelector(".page_3_finish").style.opacity="1"
        setTimeout ()->
            document.querySelector(".page_sheng1").classList.add("page_word_fade_in")
        ,1000
        setTimeout ()->
            document.querySelector(".page_qi1").classList.add("page_word_fade_in")
        ,2000
        setTimeout ()->
            document.querySelector(".page_shou1").classList.add("page_word_fade_in")
        ,3000
        setTimeout ()->
            document.querySelector(".page_deng1").classList.add("page_word_fade_in")
        ,4000
        setTimeout ()->
            document.querySelector(".page_ji1").classList.add("page_word_fade_in")
        ,5000
    Hs.page_2_finish_init = ()->
        document.querySelector(".page_center_center").classList.remove("hide")
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
    Hs.page_2_finish = ()->
        document.querySelector(".page_2_finish").classList.remove("page_finish_fade_in")
        document.querySelector(".page_2_finish").classList.add("page_finish_fade_out")
        setTimeout ()->
            Hs.page_3_finish_init()
        ,1000
    Hs.page_3_finish = ()->
        document.querySelector(".page_3_finish").classList.remove("page_finish_fade_in")
        document.querySelector(".page_3_finish").classList.add("page_finish_fade_out")
        setTimeout ()->
            Hs.page_4_finish_init()
        ,1000
    Hs.page_4_finish = ()->
        document.querySelector(".page_4_finish").classList.remove("page_finish_fade_in")
        document.querySelector(".page_4_finish").classList.add("page_finish_fade_out")
        setTimeout ()->
            Hs.page_5_finish_init()
        ,1000
    Hs.page_5_finish = ()->
        document.querySelector(".page_5_finish").classList.remove("page_finish_fade_in")
        document.querySelector(".page_5_finish").classList.add("page_finish_fade_out")
        setTimeout ()->
            Hs.page_6_finish_init()
        ,1000
    Hs.page_6_finish = ()->
        document.querySelector(".page_6_finish").classList.remove("page_finish_fade_in")
        document.querySelector(".page_6_finish").classList.add("page_finish_fade_out")
        setTimeout ()->
            Hs.page_7_finish_init()
        ,1000
    Hs.page_7_finish = ()->
        document.querySelector(".page_7_finish").classList.remove("page_finish_fade_in")
        document.querySelector(".page_7_finish").classList.add("page_finish_fade_out")
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

    Hs.check_page_3_show_cover = (content)->
        document.querySelector(".page_3_show_cover").style.display="block"
        document.querySelector(".page_3_show_cover").innerText = content
        setTimeout ()->
            document.querySelector(".page_3_show_cover").style.display="none"
        ,2000
    Hs.check_page_3_input = ()->
        if document.querySelector("#page_3_finish_name").value == ""
            return Hs.check_page_3_show_cover("请输入您的姓名")
        if document.querySelector("#page_3_finish_age").value == ""
            return Hs.check_page_3_show_cover("请输入您的年龄")
        if document.querySelector("#page_3_finish_addr").value == ""
            return Hs.check_page_3_show_cover("请输入您的地址")
        if document.querySelector("#page_3_finish_word").value == ""
            return Hs.check_page_3_show_cover("请输入您的爱国宣言")
        Hs.page_info =
            "name":document.querySelector("#page_3_finish_name").value
            "age":document.querySelector("#page_3_finish_age").value
            "addr":document.querySelector("#page_3_finish_addr").value
            "word":document.querySelector("#page_3_finish_word").value
        Hs.page_3_finish()
    Hs.chec_page_4_show_cover = ()->
        document.querySelector(".page_4_show_cover").classList.remove("hide")
    Hs.chec_page_4_show_cover_error = ()->
        document.querySelector(".page_4_show_cover_error").classList.remove("hide")
    Hs.check_page_4_option = ()->
        if document.querySelector(".page_4_option_selected").className.indexOf("page_4_option_answer")==-1
            return Hs.chec_page_4_show_cover_error()
        else
            return Hs.chec_page_4_show_cover()
    Hs.chec_page_5_show_cover = ()->
        document.querySelector(".page_5_show_cover").classList.remove("hide")
    Hs.chec_page_5_show_cover_error = ()->
        document.querySelector(".page_5_show_cover_error").classList.remove("hide")
    Hs.check_page_5_option = ()->
        if document.querySelector(".page_5_option_selected").className.indexOf("page_5_option_answer")==-1
            return Hs.chec_page_5_show_cover_error()
        else
            return Hs.chec_page_5_show_cover()
    Hs.chec_page_6_show_cover = ()->
        document.querySelector(".page_6_show_cover").classList.remove("hide")
    Hs.chec_page_6_show_cover_error = ()->
        document.querySelector(".page_6_show_cover_error").classList.remove("hide")
    Hs.check_page_6_option = ()->
        if document.querySelector(".page_6_option_selected").className.indexOf("page_6_option_answer")==-1
            return Hs.chec_page_6_show_cover_error()
        else
            return Hs.chec_page_6_show_cover()






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
    document.querySelector(".page_button").addEventListener "click",(evt)->
        Hs.page_2_finish()
    document.querySelector(".page_button1").addEventListener "click",(evt)->
        Hs.check_page_3_input()
    document.querySelectorAll(".page_4_option").forEach (element)->
        element.addEventListener "click",(evt)->
            document.querySelectorAll(".page_4_option").forEach (element1)->
                element1.classList.remove("page_4_option_selected")
            this.classList.add("page_4_option_selected")
    document.querySelector(".page_button2").addEventListener "click",(evt)->
        Hs.check_page_4_option()

    document.querySelector(".page_show_error_continue").addEventListener "click",(evt)->
        document.querySelector(".page_4_show_cover_error").classList.add("hide")
    document.querySelector(".page_show_right_continue").addEventListener "click",(evt)->
        Hs.page_4_finish()
        document.querySelector(".page_4_show_cover").classList.add("hide")



    document.querySelectorAll(".page_5_option").forEach (element)->
        element.addEventListener "click",(evt)->
            document.querySelectorAll(".page_5_option").forEach (element1)->
                element1.classList.remove("page_5_option_selected")
            this.classList.add("page_5_option_selected")
    document.querySelector(".page_button3").addEventListener "click",(evt)->
        Hs.check_page_5_option()

    document.querySelector(".page_show_error_continue1").addEventListener "click",(evt)->
        document.querySelector(".page_5_show_cover_error").classList.add("hide")
    document.querySelector(".page_show_right_continue1").addEventListener "click",(evt)->
        Hs.page_5_finish()
        document.querySelector(".page_5_show_cover").classList.add("hide")


    document.querySelectorAll(".page_6_option").forEach (element)->
        element.addEventListener "click",(evt)->
            document.querySelectorAll(".page_6_option").forEach (element1)->
                element1.classList.remove("page_6_option_selected")
            this.classList.add("page_6_option_selected")
    document.querySelector(".page_button4").addEventListener "click",(evt)->
        Hs.check_page_6_option()

    document.querySelector(".page_show_error_continue2").addEventListener "click",(evt)->
        document.querySelector(".page_6_show_cover_error").classList.add("hide")
    document.querySelector(".page_show_right_continue2").addEventListener "click",(evt)->
        Hs.page_6_finish()
        document.querySelector(".page_6_show_cover").classList.add("hide")

    document.querySelector(".page_button5").addEventListener "click",(evt)->
        document.querySelector(".page_button6").classList.remove("hide")
        document.querySelector(".page_button5").classList.add("hide")
        
    document.querySelector(".page_button6").addEventListener "click",(evt)->
        document.querySelector(".page_flag2").classList.add("page_flag_up")
        setTimeout ()->
            document.querySelector(".page_7_show_cover").classList.remove("hide")
            document.querySelector(".page_show_get_img").classList.add("page_scale_in")

            document.querySelector(".page_show_get_text_name").innerText = Hs.page_info["name"]
            document.querySelector(".page_show_get_text_age").innerText = Hs.page_info["age"]
            document.querySelector(".page_show_get_text_addr").innerText = Hs.page_info["addr"]
            document.querySelector(".page_show_get_text_word").innerText = Hs.page_info["word"]

            document.querySelector(".page_show_right_continue3").classList.add("page_left_in")

        ,3000
    document.querySelector(".page_show_right_continue3").addEventListener "click",(evt)->
        Hs.page_7_finish()


        
    