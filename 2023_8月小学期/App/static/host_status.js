{//初始化      监听导航栏
    $(document).ready(function () {
        $('.nav-link').click(function () {   //当有导航栏被点击的时候
            $('.nav-link').removeClass('active'); //所有导航栏元素移除active被选中效果
            $(this).addClass('active');       //被点击元素添加active被选中效果
            let target = $(this).data('target');//导航栏项的data-target属性的值是目标内容的ID
            $('.section').hide();//所有内容隐藏
            $('#' + target).show();//target就是导航栏目标内容的ID   显示目标内容
        });
        $('.nav-link').eq(0).click();       //打开网页自动点击第一个导航栏
    });
}

//向后端请求系统信息
function sys_info(){
    document.getElementById('zc').src='../static/img/0'+(Math.floor(Math.random() * 3) + 1)+'.gif'
    console.log( document.getElementById('zc').src)
    $.get('sys_info',function (data){
        console.log(data)
        document.getElementById('sud').innerText=data.time
        document.getElementById('sn').innerText=data.user.name
        document.getElementById('st').innerText=data.type
        document.getElementById('su').innerText=data.user.user
        document.getElementById('ss').innerText=data.start
        document.getElementById('sp').innerText=data.battery.power_plugged
        document.getElementById('se').innerText=data.battery.percent
        document.getElementById('sr').innerText=data.battery.available_time

    })
}

//磁盘饼图设置
const options={
            series : [
                {
                    name: '访问来源',
                    type: 'pie',    // 设置图表类型为饼图
                    radius: '70%',  // 饼图的半径，外半径为可视区尺寸（容器高宽中较小一项）的 55% 长度。
                    data:[          // 数据数组，name 为数据项名称，value 为数据项值
                        {value:1, name:null},
                        {value:99, name:null},
                    ]
                }
            ]
        };
//向后端请求磁盘信息
function disk_info(){
    document.getElementById('zc').src='../static/img/0'+(Math.floor(Math.random() * 3) + 1)+'.gif'
    $.get('disk_info',function (data){
        console.log(data)
            document.getElementById('dud').innerText=data.time

            document.getElementsByClassName('dC')[0].innerText=data.C.free
            document.getElementsByClassName('dC')[1].innerText=data.C.used
            document.getElementsByClassName('dC')[2].innerText=data.C.total

            document.getElementsByClassName('dD')[0].innerText=data.D.free
            document.getElementsByClassName('dD')[1].innerText=data.D.used
            document.getElementsByClassName('dD')[2].innerText=data.D.total

            document.getElementsByClassName('dE')[0].innerText=data.E.free
            document.getElementsByClassName('dE')[1].innerText=data.E.used
            document.getElementsByClassName('dE')[2].innerText=data.E.total
            //配置饼图
            let CChart = echarts.init(document.getElementById('C盘图'));
            let temp=100-parseFloat(data.C.percent)
            options.series[0].data[0].value=data.C.percent
            options.series[0].data[0].name=data.C.percent+'已使用'
            options.series[0].data[1].value=temp
            options.series[0].data[1].name=temp+'未使用'
            CChart.setOption(options)
            //D
            let DChart = echarts.init(document.getElementById('D盘图'));
            temp=100-parseFloat(data.D.percent)
            options.series[0].data[0].value=data.D.percent
            options.series[0].data[0].name=data.D.percent+'%已使用'
            options.series[0].data[1].value=temp
            options.series[0].data[1].name=temp+'%未使用'
            DChart.setOption(options)
            //E
            let EChart = echarts.init(document.getElementById('E盘图'));
            temp=100-parseFloat(data.E.percent)
            options.series[0].data[0].value=data.E.percent
            options.series[0].data[0].name=data.E.percent+'已使用'
            options.series[0].data[1].value=temp
            options.series[0].data[1].name=temp+'未使用'
            EChart.setOption(options)

    })
}

//请求CPU信息
function cup_info(){
    $.get('cpu_info',function (data){
        console.log(data)
        document.getElementById('cmore').innerText=data.逻辑处理器
        document.getElementById('cless').innerText=data.内核
        //配置cpu折线图
        let cpu_used=echarts.init(document.getElementById('cpu_used'));
        options_cpu.series[0].data=data.used
        cpu_used.setOption(options_cpu)

    })
}
//CPU利用率折线图
const options_cpu = {
      xAxis: {
        type: 'category',
        data:['0.4s', '0.8s', '1.2s', '1.6s', '2.0s']
      },
      yAxis: {
        name: 'cpu利用率(%)',
        type: 'value',
        min: 0,
        max: 100
      },
      series: [{
        type: 'line',
        data:[],
        label: {
            show: true,
        }
      }]
};
function network(){
    $.get('network',function (data){
        console.log(data)
        let str=''
        for (let i = 0; i <data.r_s.ip.length ; i++) {
            str+=data.r_s.ip[i]+'<br>'
        }
        document.getElementById('ip').innerHTML=str

        document.getElementById('nr').innerText=data.r_s.recv
        document.getElementById('ns').innerText=data.r_s.sent
        let all=''
        let one=''
        let tr='<tr>'
        let td='<td>'
        let tr0='</tr>'
        let td0='</td>'
        for (let i = 0; i < data.tcp.length; i++) {
            one=tr+
                td+data.tcp[i].protocol+td0+
                td+data.tcp[i].local_address+td0+
                td+data.tcp[i].foreign_address+td0+
                td+data.tcp[i].state+td0+
                td+data.tcp[i].pid+td0
                +tr0
            all+=one
        }

        document.getElementById('tcp').innerHTML=all
    })
}
//内存柱状图
const  options1_memory={
        title: {
            text: '运行内存',
        },
        xAxis: {
            type: 'category',
            data: ['Total', 'Used', 'Free']
        },
        yAxis: {
            max:0,
            type: 'value',
        },
        series: [{
            name: 'Memory',
            type: 'bar',
            data: [],
            label: {
                show: true,
                formatter: '{c} MB',
            },
            itemStyle: {
                color: function(params) {
                    let colorList = ['#4657aa', '#9a1e3a', '#1e8039']; // 设置柱状图的颜色
                        return colorList[params.dataIndex];
                }
            },
        }]
}
const options2_memory = {
  tooltip: {
    formatter: '{b} : {c}%'
    },
  series: [
    {
      name: 'Pressure',
      type: 'gauge',
      progress: {
        show: true
      },
      axisLabel: {
        formatter: '{value}%' // 设置y轴的单位
      },
      detail: {
        valueAnimation: true,
        formatter: '{value}%'
      },
      data: [
        {
          value: 77,
        }
      ]
    }
  ]
};
//内存信息
function memory_info(){
    $.get('memory_info',function (data){
        console.log(data)
        let m1=echarts.init(document.getElementById('m1'));
        let m2=echarts.init(document.getElementById('m2'));
        let m1r=echarts.init(document.getElementById('m1r'));
        let m2r=echarts.init(document.getElementById('m2r'));
        let a=[data.svmem.total,data.svmem.used,data.svmem.free]
        let b=[data.swap.total,data.swap.used,data.swap.free]
        //运行内存
        options1_memory.series[0].data=a
        options1_memory.yAxis.max=Math.ceil(data.svmem.total);
        options1_memory.title.text='运行内存'
        m1.setOption(options1_memory)
        options2_memory.tooltip.formatter='运行内存 : {c}%'
        options2_memory.series[0].data[0].value=data.svmem.percent
        m1r.setOption(options2_memory)
        //交换内存
        options1_memory.title.text='交换内存'
        options1_memory.series[0].data=b
        options1_memory.yAxis.max=Math.ceil(data.swap.total);
        m2.setOption(options1_memory)
        options2_memory.tooltip.formatter='交换内存 : {c}%'
        options2_memory.series[0].data[0].value=data.swap.percent
        m2r.setOption(options2_memory)

    })
}
function process_info(){
    $.get('process_info',function(data){
        console.log(data)
        let tr='<tr>'
        let th='<th>'
        let tr0='</tr>'
        let th0='</th>'
        let n,s,p,one
        let all=''
        for (let i = 0; i < data.length; i++) {
            n=data[i].name
            s=data[i].status
            p=data[i].pid
            m=parseFloat(data[i].memory_percent)
            one=tr+
                th+n+th0+
                th+s+th0+
                th+p+th0+
                th+m.toFixed(3)+th0+
                tr0
            all+=one
        }
        document.getElementById('process').innerHTML=all
    })
}

//桌宠
{
   // 获取元素
const dragElement = document.getElementById("drag-element");

   // 禁止图片预览拖动
dragElement.addEventListener("dragstart", function(e) {
  e.preventDefault();
});
// 鼠标按下事件
dragElement.addEventListener("mousedown", function(e) {
    let offsetX = e.clientX - dragElement.offsetLeft;
    let offsetY = e.clientY - dragElement.offsetTop;

    // 鼠标移动事件
  document.addEventListener("mousemove", moveElement);

  // 鼠标松开事件
  document.addEventListener("mouseup", function() {
    document.removeEventListener("mousemove", moveElement);
});

  // 移动元素函数
  function moveElement(e) {
      if ((e.clientY - offsetY)<=0||(e.clientY - offsetY)>=750)return
    dragElement.style.left = (e.clientX - offsetX) + "px";
    dragElement.style.top = (e.clientY - offsetY) + "px";
  }
});

}


{//定时器  实时刷新数据
  setInterval(cup_info, 2000);
  setInterval(network, 2000);
  setInterval(memory_info, 1000);
  setInterval(process_info, 2000);
}