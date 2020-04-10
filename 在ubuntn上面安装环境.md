#### Ubuntn安装openssh

```markdown
# 安装ssh工具
1.apt-get install openssh-server
2./etc/init.d/ssh restart   #重启SSH服务
  /etc/init.d/ssh stop      #关闭SSH服务
```

#### 将Python3设为默认（ubuntn16）

```markdown
1.sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
2.sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150
# 如果要切换到Python2，执行：
sudo update-alternatives --config python
#ubuntn里面自带的python3.5不带pip命令需要自行安装
apt-get install python3-pip
# 升级一下pip命令
pip install --upgrade pip
sudo apt-get update && sudo apt-get upgrade    // 更新所有包
```

#### Ubuntn安装nginx

##### 1、对于Ubuntu，请将以下内容追加到/etc/apt/source.list文件的末尾

```markdown
deb http://nginx.org/packages/ubuntu/ codename nginx
deb-src http://nginx.org/packages/ubuntu/ codename nginx
# codename为Ubuntu版本  16.04 -- xenial    17.10 -- artful    18.04 -- bionic
```

##### 2、安装并配置秘钥

```markdown
1.apt-get update    #更新库
2.apt-get install nginx    # 安装nginx
# 在/ect/apt目录下载所需秘钥
wget http://nginx.org/keys/nginx_signing.key 
apt-key add nginx_signing.key
```



#### 在ubuntn上面安装mysql

```markdown
1.sudo apt-get install mysql-server              // 安装mysql服务器端
2.sudo apt-get install mysql-client              // 安装mysql客户端
3.sudo apt-get install libmysqlclient-dev
```

#### 设置mysql允许远程访问

```markdown
1.设置mysql允许远程访问，编辑文件/etc/mysql/mysql.conf.d/mysqld.cnf：
sudo vi /etc/mysql/mysql.conf.d/mysqld.cnf
注释 #bind-address:127.0.0.1
2.保存退出，然后进入mysql服务，执行授权命令：
grant all on *.* to root@'%' identified by '你的密码' with grant option;
flush privileges;
3.然后执行quit命令退出mysql服务，执行如下命令重启mysql：
sudo service mysql restart
```

