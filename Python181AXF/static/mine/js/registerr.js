$(function () {
    $('.register').width(innerWidth)


    // 邮箱验证 (失去焦点，即是输入完成后验证)
    $('#email input').blur(function () {

        var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式

        // 空，不需要验证处理
        if ($(this).val() == '') return

        // 格式是否正确
        if (reg.test( $(this).val() ) ){  // 符合
            // 账号是否可用 [必须发给服务器]
            // 只需要 服务器 提示 可用true/不可用false
            // 通过ajax和服务器通信


            $('#email-t').popover('hide')

            $('#email').removeClass('has-error').addClass('has-success')
            $('#email>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {    // 不符合
            $('#email-t').popover('show')

            $('#email').removeClass('has-success').addClass('has-error')
            $('#email>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }


    })


    // 密码验证
    $('#password input').blur(function () {

        var reg = new RegExp("^[a-zA-Z0-9_]{6,10}$"); //正则表达式

        // 空，不需要验证处理
        if ($(this).val() == '') return

        // 格式是否正确
        if ( reg.test( $(this).val() ) ){  // 符合
            $('#password').removeClass('has-error').addClass('has-success')
            $('#password>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {    // 不符合
            $('#password').removeClass('has-success').addClass('has-error')
            $('#password>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })

    // 验证密码
    $('#password-d input').blur(function () {
        // 空，不需要验证处理
        if ($(this).val() == '') return

        var f_val = $('#password input').val()
        var d_val = $('#password-d input').val()

        // 格式是否正确
        if ( f_val == d_val ){  // 符合
            $('#password-t').popover('hide')
            $('#password-d').removeClass('has-error').addClass('has-success')
            $('#password-d>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {    // 不符合
            $('#password-t').popover('show')
            $('#password-d').removeClass('has-success').addClass('has-error')
            $('#password-d>span').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })

    // 验证昵称
    $('#name input').blur(function () {
        // 空，不需要验证处理
        if ($(this).val() == '') return

        // 格式是否正确
        if ( $(this).val().length>=3 || $(this).val().length<=10 ){  // 符合
            $('#name').removeClass('has-error').addClass('has-success')
            $('#name>span').removeClass('glyphicon-remove').addClass('glyphicon-ok')
        } else {    // 不符合
            $('#name').removeClass('has-success').addClass('has-error')
            $('#name').removeClass('glyphicon-ok').addClass('glyphicon-remove')
        }
    })

    // 注册按钮
    $('#subButton').click(function () {
        console.log('注册')

        var isregister = true

        $('.register .form-group').each(function () {
            if( !$(this).is('.has-success') ) {
                isregister = false
            }
        })

        if (isregister){    // 允许注册
            $('.register form').submit()
        }
    })
})