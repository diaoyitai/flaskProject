function login_card(){   //登录卡片显示
    let l = document.getElementById('login')
    l.style.display='block'
}
function close_login(){     //关闭登录卡片
    document.getElementsByName('account')[0].value=''
    document.getElementsByName('password')[0].value=''
    let l = document.getElementById('login')
    l.style.display='none'
}
//四个查询服务跳转
function Service2(){
        window.open('Service2','_blank')
}
function Service1(){
    window.open('Service1','_blank')
}
function Service3(){
    window.open('Service3','_blank')
}
function Service4() {
    window.open('Service4','_blank')
}
function VIP(){
    window.open('host','_blank')
}
function please_login(){    //点击服务提示登录
    login_card()
    document.getElementById('please').style.display='block'
    setTimeout(function (){
    document.getElementById('please').style.display='none'
    },2000)
}
//点击登录
function login(){
    let a=document.getElementsByName('account')[0].value    //账号
    let p=document.getElementsByName('password')[0].value   //密码
    if(a===''||p===''){ //检查输入是否合法
        document.getElementById('warn').style.display='block'
        setTimeout(function (){
            document.getElementById('warn').style.display='none'
        },2000)
        return
    }
    console.log(a,p)
    console.log("发送请求前")
    $.post('/login',{
        'account':a,
        'password':p
    },function (data){
        console.log("接收响应")
        if(data[0]===true){
            window.location.href='/'
            alert('登录成功！'+data[1])
        }
        if(data[0]===false) {  //登录失败
            document.getElementById('warn').style.display='block'
            setTimeout(function (){
            document.getElementById('warn').style.display='none'
            },2000)
        }
    })

}
//用户建议
function advice(){
    if(document.getElementById('Email').value===''|| document.getElementById('content').value===''){
        alert('提交失败！')
        return
    }
    $.get('advice',{
        'E':document.getElementById('Email').value,
        'c':document.getElementById('content').value
    },function (data){
        if (data===true){
            document.getElementById('Email').value=''
            document.getElementById('content').value=''
            alert('提交成功！')
        }else {
            alert('服务器出错！请稍后再试')
        }

    })
}
//弹出升级管理员界面
function power_open(){
    console.log('点击')
    document.getElementById('CDK').value=''
    document.getElementById('提权').style.display='block'
}
//关闭升级管理员界面
function power_close(){
    document.getElementById('提权').style.display='none'
}
//普通用户升管理员
function power(){
    if (document.getElementById('CDK').value==='')return
    $.post('power', {
        'power':document.getElementById('CDK').value
    },function (data){
            if (data===true){
                alert('恭喜升级为管理员！请重新登录')
                window.location.href='/'
            }
            else {
                alert('升级失败!')
            }
        })
}

//点击退出 退出登录
function exit() {
    $.get('/exit',function (data){
        if (data){      //判断后端是否有正确的返回值
            window.location.href='/'
        }
    })
}
