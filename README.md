# swjtu_auto_fill
西南交大课程评价自动填写

Oct 02 2023, 正常运行，已测试✔️
Apr 10 2023， 已更新

# How to use[如何使用]

配置Python环境，安装Selenium+WebDriver

下载main.py

# 修改帐号密码

在main.py中修改以下内容

## username -> 改为自己的统一登录帐号
## password -> 改为自己的统一登录密码

## select_mode -> 指定选项,当为 “select” 时所有选择题都会填入 select_value 所指向的分数
## select_value -> 指定想填入的分数

## select_range -> 指定随机填写范围,当 select_mode != "select" 时生效, 闭区间.
## text_msg -> 指定填入 16 17 两题的内容

运行即可

# [TODO]
## 还会持续更新(每学期,Maybe)
## 以后更新直接截取流量发包(可能),这个脚本花了两三个小时写出来,这学期的填完了，等下学期研究
