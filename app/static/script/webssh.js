$("#btn_onb").click(function () {
                layer.open({
                    type: 2,
                    title: '建立webssh连接',
                    closeBtn: 1,
                    scrollbar: false,
                    area: ['700px', '550px'],
                    shadeClose: true, //点击遮罩关闭
                    content: ['http://192.168.85.50:8000?host=192.168.85.40&ssh_port=22', 'no'],
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
            })
