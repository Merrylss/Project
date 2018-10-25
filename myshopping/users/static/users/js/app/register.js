$(function () {
    $('#zphone').click(
        function(){
        //发送验证码
        console.log(111);
        $.get('/users/send_message/', {mobile:$('#mobile').val()}, function(msg) {
            alert(jQuery.trim(msg.msg));
            if(msg.msg=='提交成功'){
                RemainTime();
            }
        });
    });

    //按钮倒计时
    var iTime = 60;
    sTime = ''
    function RemainTime(){
        if (iTime == 0) {
            document.getElementById('zphone').disabled = false;
            sTime="获取验证码";
            iTime = 60;
            document.getElementById('zphone').value = sTime;
            return;
        }else{
            document.getElementById('zphone').disabled = true;
            sTime="重新发送(" + iTime + ")";
            iTime--;
        }
        setTimeout(function() { RemainTime() },1000);
        document.getElementById('zphone').value = sTime;
    }

    // 检查用户输入的手机号是否合法
    function check_mobile() {

        var re = /^1[345678]\d{9}$/; //校验手机号

        if(re.test($('#mobile').val()))
        {
            $('#mobile').next().hide();
            error_mobile = false;
            document.getElementById('zphone').disabled = false;
        }
        else
        {
            $('#mobile').next().html('你输入的手机格式不正确');
            $('#mobile').next().show();
            error_mobile = true;
            document.getElementById('zphone').disabled = true;
        }
    }
});



