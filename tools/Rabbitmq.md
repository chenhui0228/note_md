# Rabbitmq

### Install

<pre>
echo 'deb http://www.rabbitmq.com/debian/ testing main' | sudo tee /etc/apt/sources.list.d/rabbitmq.list
wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | sudo apt-key add -
sudo apt-get update

sudo apt-get install rabbitmq-server
</pre>

### command

#### 启动服务
- 启动RabbitMQ服务
- `sudo systemctl enable rabbitmq-server`
- `sudo systemctl start rabbitmq-server`
- `sudo systemctl restart rabbitmq-server`
- 打开管理页面
`sudo rabbitmq-plugins enable rabbitmq_management`
- 用刚设置的账户登录管理页面   http://127.0.0.1:15672

#### 用户命令
- 添加用户 
`rabbitmqctl add_user username password `
- 删除用户 
`rabbitmqctl delete_user username `
- 修改密码 
`rabbitmqctl change_password username newpassword `
- 列出所有用户
`rabbitmqctl list_users `
- 设置用户权限   [-p vhostpath]  是指设置用户在某个虚拟机上的权限
`rabbitmqctl set_permissions [-p vhostpath] username regexp regexp regexp` 
- 清除用户权限 
`rabbitmqctl clear_permissions [-p vhostpath] username `
- 列出用户权限 
`rabbitmqctl list_user_permissions username`
- 设置用户角色 tagsName解释
`rabbitmqctl set_user_tags username tagsname`

#### 队列命令
- 返回queue的信息，如果省略了-p参数，则默认显示的是"/"vhosts的信息。
`rabbitmqctl list_queues [-p <vhostpath>] [<queueinfoitem> ...]  `
- 返回exchange的信息。
`rabbitmqctl list_exchanges [-p <vhostpath>] [<exchangeinfoitem> ...] `
- 返回绑定信息
`rabbitmqctl list_bindings [-p <vhostpath>] [<bindinginfoitem> ...] `
- 返回链接信息
`rabbitmqctl list_connections [<connectioninfoitem> ...] `
- 返回目前所有的
`rabbitmqctl channels list_channels [<channelinfoitem> ...] `
- 返回consumers
`rabbitmqctl list_consumers [-p <vhostpath>] `
- 显示broker的状态 environment #显示环境参数的信息 report #返回一个服务状态report
`rabbitmqctl status` 
- 清除队列
`rabbitmqctl reset`

#### 虚拟机命令
- 创建虚拟主机 
`rabbitmqctl add_vhost vhostpath` 
- 删除虚拟主机 
`rabbitmqctl delete_vhost vhostpath `
- 列出所有虚拟主机 
`rabbitmqctl list_vhosts `
- 列出虚拟主机上的所有权限 
`rabbitmqctl list_permissions [-p vhostpath]`

#### 应用和集群管理
- 停止RabbitMQ应用，关闭节点 
`rabbitmqctl stop `
- 停止RabbitMQ应用 
`rabbitmqctl stop_app `
- 启动RabbitMQ应用 
`rabbitmqctl start_app `
- 显示RabbitMQ中间件各种信息 
`rabbitmqctl status `
- 重置RabbitMQ节点 
`rabbitmqctl reset `
`rabbitmqctl force_reset `
从它属于的任何集群中移除，从管理数据库中移除所有数据，例如配置过的用户和虚拟宿主, 删除所有持久化的消息。 
force_reset命令和reset的区别是无条件重置节点，不管当前管理数据库状态以及集群的配置。如果数据库或者集群配置发生错误才使用这个最后 的手段。 
注意：只有在停止RabbitMQ应用后，reset和force_reset才能成功。