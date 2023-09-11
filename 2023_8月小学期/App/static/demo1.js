function query(){
    //查询中...
    document.getElementById('状态').innerText='查询中...'
    document.getElementById('t').style.display='none'
    let ip=document.getElementById('ip').value
    $.get('http://ip-api.com/json/'+ip,function (data){
        console.log(data)
        document.getElementById('状态').innerText=data.status
        if (data.status==='success'){   //请求成功
            document.getElementById('t').style.display='block'
            document.getElementById('城市').innerText=data.city
            document.getElementById('国家').innerText=data.country
            document.getElementById('国家简称').innerText=data.countryCode
            document.getElementById('运营商').innerText=data.isp
            document.getElementById('IP').innerText=data.query
            document.getElementById('省份').innerText=data.regionName
            document.getElementById('省份简称').innerText=data.region
            document.getElementById('时区').innerText=data.timezone
            document.getElementById('经度').innerText=data.lon
            document.getElementById('纬度').innerText=data.lat
            baiduMap(data.lon,data.lat,data.city,12)
        }
        else {
            baiduMap(116.514, 39.915,'北京',5)
        }

    })
}

function baiduMap(lon,lat,city,num){
    var map = new BMap.Map("allmap"); // 百度地图API功能
   // 创建Map实例
	map.centerAndZoom(new BMap.Point(lon, lat), num);  // 初始化地图,设置中心点坐标和地图级别
	//添加地图类型控件
	map.addControl(new BMap.MapTypeControl({
		mapTypes:[
            BMAP_NORMAL_MAP,
            BMAP_HYBRID_MAP
        ]}));
	map.setCurrentCity(city);          // 设置地图显示的城市 此项是必须设置的
	map.enableScrollWheelZoom(true);     //开启鼠标滚轮缩放

}



