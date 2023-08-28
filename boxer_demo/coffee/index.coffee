root = exports ? this
# !!!! Hotpoor root object
root.Hs or= {}
Hs = root.Hs
Hs.base_width = 750
Hs.base_height = 1334
Hs.window_resize = ()->
    window_height = $("body").height()
    Hs.current_width = window_height/Hs.base_height*Hs.base_width
    Hs.current_height = window_height
    $(".page").css
        "width":"#{Hs.current_width}px"
        "height":"#{Hs.current_height}px"
$ ->
    Hs.media_play = ()->
        $("#media")[0].play()
    Hs.media_pasure = ()->
        $("#media")[0].pause()

    $(window).on "load",(evt)->
        Hs.window_resize()
    $(window).on "resize",(evt)->
        Hs.window_resize()
    