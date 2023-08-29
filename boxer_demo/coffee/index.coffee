root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs
Hs.base_width = 750
Hs.base_height = 1334
Hs.window_resize = ()->
    window_height =document.querySelector("body").offsetHeight
    Hs.current_width = window_height/Hs.base_height*Hs.base_width
    Hs.current_height = window_height
    document.querySelector(".page").style.width="#{Hs.current_width}px"
    document.querySelector(".page").style.height="#{Hs.current_height}px"
do ()->
    Hs.media_play = ()->
        document.querySelector("#media").play()
    Hs.media_pasure = ()->
        document.querySelector("#media").pause()
    window.addEventListener "load",(evt)->
        Hs.window_resize()
    window.addEventListener "resize",(evt)->
        Hs.window_resize()

    