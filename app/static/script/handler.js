function conectwebssh(row) {
    var host_ip=row.title
    var host_port=row.price
    var data='http://192.168.85.50:8000?host='+host_ip+'&ssh_port='+host_port
    console.log(data)
    layer.open({
                    type: 2,
                    title: '建立webssh连接',
                    closeBtn: 1,
                    scrollbar: false,
                    area: ['700px', '580px'],
                    shadeClose: true, //点击遮罩关闭
                    content: [data, 'no'],
                    btn: ['关闭所有'] , //只是为了演示
                    end: function () {
                        var handle_status = $("#handle_status").val();
                        if (handle_status == '1') {
                            layer.msg('连接成功！', {
                                icon: 1,
                                time: 2000 //2秒关闭（如果不配置，默认是3秒）
                            }, function () {
                                history.go(0);
                            });
                        } else if (handle_status == '2') {
                            layer.msg('连接失败！', {
                                icon: 2,
                                time: 2000 //2秒关闭（如果不配置，默认是3秒）
                            }, function () {
                                history.go(0);
                            });
                        }
                    }
                })
}



//删除界面操作提示
function warningTest(row, index) {
    swal(
        {
            title: "操作提示",
            text: '确定删除' + row.name + '吗？',
            type: "warning",
            showCancelButton: true,
            confirmButtonColor: "#DD6B55",
            confirmButtonText: "确定",
            cancelButtonText: "取消",
            closeOnConfirm: false,
            closeOnCancel: false
        },
        function (isConfirm) {
            if (isConfirm) {
                var data = {};
                data["item_id"] = index
                $.ajax({
                    type: "post",
                    url: "/tables/delitem",
                    data: {"item_name": row.name},
                    success: function (data, status) {
                        console.log(data, status)
                    },
                    error: function () {
                        console.log("ERROR")
                    },
                    complete: function (data, status) {
                        if (status == "success") {
                            swal({title: "删除成功！", text: "您已经删除了这条信息。", type: "success"});
                            window.location.reload();

                        }
                    }

                });


            } else {
                window.location.reload();
            }
        }
    )
}


//按钮样式生成
function operateFormatter(value, row, index) {
    return [
        '<button  class="RoleOfupdate btn btn-xs btn-info" id="item_update">更新</button>&nbsp',
        '<button class="RoleOfdelete btn btn-xs btn-danger " id="item_delect">删除</button>&nbsp',
        '<button class="RoleOfconect btn btn-xs btn-success " id="item_ssh">连接</button>&nbsp'
    ].join("");
};

//操作按钮事件
window.operateEvents = {
    //为了安全这里应该吧cookie 传给服务端做认证 过了才能接受item删除
    //编辑  按钮
    'click .RoleOfupdate': function (e, vlaue, row, index) {
    },
    //删除   按钮
    "click .RoleOfdelete": function (e, vlaue, row, index) {
        warningTest(row, index);
    },
    //webssh 按钮
    "click .RoleOfconect": function (e, vlaue, row, index) {
        conectwebssh(row);
    }
}

//main  主方法
$(function () {
    //初始化业务逻辑script
    loadGoods();
    //提示操作框
    toastr.options.positionClass = 'toast-top-center';
})

//Tables 列表初始化
function loadGoods() {
    $('#goods_table')
        .bootstrapTable(
            {
                url: '/tables/data', // 请求后台的URL（*）
                pagination: true, //前端处理分页
                dataType: "json",
                search: false, // 显示搜索框
                showToggle: false, // 是否显示详细视图和列表视图的切换按钮
                sidePagination: "server", // 服务端处理分页
                showColumns: true, // 是否显示所有的列
                showRefresh: false,// 是否显示刷新按钮
                toolbar: '#toolbar', // 工具按钮用哪个容器
                queryParams: function (param) {
                    var temp = {   //这里的键的名字和控制器的变量名必须一直，这边改动，控制器也需要改成一样的
                        limit: param.limit,   //页面大小
                        offset: param.offset,  //页码
                        departmentname: $("#txt_search_departmentname").val(),
                        statu: $("#txt_search_statu").val(),
                        search: param.search
                    };
                    return temp;
                },
                columns: [
                    {
                        checkbox: true,
                        visible: true

                    },
                    {
                        field: 'name',
                        title: '主机名'
                    },
                    {
                        field: 'title',
                        title: '主机地址'
                    },
                    {
                        field: 'price',
                        title: '主机端口'
                    },
                    {
                        field: 'number',
                        title: '主机用户'
                    },
                    {
                        field: 'password',
                        title: '系统类型'

                    },
                    {
                        field: 'time',
                        title: '创建时间'
                    },
                    {
                        field: 'state',
                        title: '状态',
                        formatter: function (value,
                                             row, index) {
                            var ret = "";
                            if (value == 0) {
                                ret = '<a data-toggle="popover" data-content="" data-placement="auto bottom" data-original-title="" title=""><i class="fa fa-circle text-info"></i></a>';
                            }
                            if (value == 1) {
                                ret = '<a data-toggle="popover" data-content="" data-placement="auto bottom" data-original-title="" title=""><i class="fa fa-circle text-danger"></i></a>';
                            }
                            return ret;
                        }
                    },
                    {
                        field: 'action',
                        title: '   动作',
                        events: operateEvents,
                        formatter: operateFormatter
                    },
                ]
            });

}

$('#myModal').on('hidden.bs.modal', function () {
toastr.warning('您已取消操作！');
});


