$(function () {
    $('.cart').width(innerWidth)
    
    // 选中处理
    $('.cart .confirm-wrapper').click(function () {

        var $span = $(this).find('span')

        request_data = {
            'cartid':$(this).attr('data-cardid')
        }

        $.get('/axf/changecartselect/', request_data, function (response) {
            console.log(response)

            if (response.status == 1) {
                if (response.isselect){
                    $span.removeClass('no').addClass('glyphicon glyphicon-ok')
                } else {
                    $span.removeClass('glyphicon glyphicon-ok').addClass('no')
                }
            }
        })
    })


    // 全选/取消全选
    $('.cart .all').click(function () {
        var isall = $(this).attr('data-all')
        $span = $(this).find('span')

        // 点击后去反
        isall = (isall == 'false') ? true : false

        // 记录
        $(this).attr('data-all', isall)

        if (isall){
            $span.removeClass('no').addClass('glyphicon glyphicon-ok')
        } else {
            $span.removeClass('glyphicon glyphicon-ok').addClass('no')
        }
    })
})