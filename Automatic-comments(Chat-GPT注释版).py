from datetime import *  # 日期时间模块
from requests import *  # 网络请求模块
from time import sleep  # 时间模块
from random import choice  # 随机模块
from json import loads, dumps  # JSON序列化与反序列化模块
from bs4 import BeautifulSoup  # HTML解析模块
from configparser import ConfigParser  # 解析配置文件模块
import os

# 导入Python模块和库


def check_config_file():  # 获取当前工作目录
    current_path = os.getcwd()  # 拼接config.ini文件路径
    config_path = os.path.join(current_path, "config.ini")  # 判断文件是否存在
    if os.path.isfile(config_path):
        return True
    else:
        return False


# 检查当前工作目录是否有 config.ini 配置文件
# 返回值:True: 工作目录下存在 config.ini 文件;False: 工作目录下不存在 config.ini 文件


def check_string():
    try:
        with open("qwq.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line_number in lines:
            if str(item[0][1]) in line_number:  # 判断行内是否包含关键词
                return True
        if str(item[3][1]) in [18996184]:  # 判断指定数字是否在列表中出现
            return True
        else:
            return False
        f.close()
    except:
        return False


# 读取 qwq.txt 文件内容，并检查文件内容中是否包含特定的关键词或数字
# 返回值：True: 文件内容中包含特定的关键词或数字;False: 文件内容中不包含特定的关键词或数字


def Shielding(content):
    return b"\xe2\x80\xaa".decode("UTF-8").join([i for i in content])  # 屏蔽词转换(可选部分


# 将字符串中的每一个字符都添加转义字符"\xe2\x80\xaa"，最后再将他们拼接起来
# 将给定字符串转换为可被正常显示的字符串，并使用转义字符处理屏蔽词
# 参数：content(str)：需进行处理的字符串
# 返回值：处理后的字符串

awa = []  # 创建一个空列表，用于存储文章
content_num = 0  # 初始化评论数量和点赞数量
like_num = 0
while True:  # 进入循环
    lc_or_lk = str(input("账号登录(K)&cookie(C)"))
    # 获取用户输入，判断是账号登录还是 cookie 登录
    if lc_or_lk == "K":
        # 如果选择了账号登录
        if not check_config_file():
            # 检查配置文件是否存在
            # 如果不存在，则要求用户输入账号和密码
            username = str(input("请输入账号:"))
            password = str(input("请输入密码:"))
        # 如果存在，则从配置文件中获取账号和密码
        else:
            print("侦测到已有配置")
            config = ConfigParser()
            config.read("config.ini")

            username = config.get("Account", "username")
            password = config.get("Account", "password")
        # 创建一个 session，设置请求头
        ses = session()
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
        }
        # 获取页面的 pid 值
        soup = BeautifulSoup(
            get("https://shequ.codemao.cn", headers=headers).text, "html.parser"
        )
        pid = loads(soup.find_all("script")[0].string.split("=")[1])["pid"]
        # 发送登录请求
        a = ses.post(
            "https://api.codemao.cn/tiger/v3/web/accounts/login",
            headers=headers,
            data=dumps({"identity": username, "password": password, "pid": pid}),
        )
        # 判断请求的状态码是否为200
        if a.status_code == 200:
            # 获取cookie
            c = a.cookies
            # 将cookie转换成字典格式
            cookies = utils.dict_from_cookiejar(c)
            # 将authorization和acw_tc两个键值对拼接成字符串类型的cookie
            cookiess = (
                "authorization="
                + cookies["authorization"]
                + ";acw_tc="
                + cookies["acw_tc"]
            )
            # 将cookie赋值给变量cookie
            cookie = cookiess
            # 登陆成功，输出登录成功提示
            print("登录成功!")
            # 设置请求头
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
                "cookie": cookie,
            }
            # 检查配置文件是否存在，如果不存在，则新建一个配置文件，并将账号和密码写入配置文件中
            if not check_config_file():
                config = ConfigParser()
                config.add_section("Account")
                config.set("Account", "username", username)
                config.set("Account", "password", password)
                with open("config.ini", "w") as configfile:
                    config.write(configfile)
            # 结束循环
            break
        else:
            # 输出登录失败提示
            print("不能登录编程猫,请重试")
            # 检查配置文件是否存在，如果存在，则删除配置文件
            if check_config_file():
                os.remove("config.ini")
                # 输出删除成功提示
                print("config.ini原有配置已成功删除！")

    # 如果lc_or_lk等于C，输入cookie并设置http请求header
    elif lc_or_lk == "C":
        cookie = str(input("请输入cookie:"))
        headers = {
            "Content-Type": "application/json",  # 设置请求头Content-Type为json格式
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",  # 设置用户代理User-Agent
            "cookie": cookie,  # 设置cookie
        }
        # 发送POST请求到指定url，并携带headers和data信息
        p = post(
            r"https://api.codemao.cn/nemo/v2/works/{}/like".format(174408420),  # 夹带私货(
            headers=headers,
            data=dumps({}),  # 将空字典转换成json字符串格式作为请求体
        )
        # 判断请求状态是否成功
        if p.status_code == 200:
            print("测试成功!")  # 输出“测试成功”
            break  # 中止循环
        else:
            print("测试失败,请重新获取cookie或重试!")  # 输出“测试失败,请重新获取cookie或重试!”
    else:
        print("输入错误,请重试!")  # 如果lc_or_lk不等于C,则输出错误信息
# 循环，直到用户输入正确为止
while True:
    like_or_content = str(input("仅点赞(L)&点赞评论(A):"))
    if like_or_content == "L" or like_or_content == "A":
        break
    else:
        print("输入错误,请重试!")
        pass
# 如果用户选择了点赞和评论，则让用户输入评论间隔时间。否则跳过此循环
while True:
    if like_or_content == "A":
        sleep_time = input("评论间隔时间(为防止封号,已经间隔12s)(按秒计):")
        try:
            sleep_time = float(sleep_time)
            break
        except:
            print("输入错误!请重新输入.")
    else:
        break

# 循环获取最新作品的信息
while True:
    new = get(
        "https://api.codemao.cn/creation-tools/v1/pc/discover/newest-work?offset=0&limit=20"
    )  # limit获取数量
    print("\n" + "@zybqw or 猫鱼")
    _dict = loads(new.text)  # 将json格式字符串转换成字典类型
    print(new.text + "\n")  # 输出获取到的内容
    print("=" * 200)  # 分割线
    for infos in _dict["items"]:  # 遍历最新作品信息
        item = list(infos.items())  # 获取作品信息列表
        print("\n" + str(item))
        sentents = ("666＃°Д°", "加油！:O", "针不戳:D", "前排:P", "沙发*/ω＼*")
        picture = (
            "编程猫_666", "编程猫_棒", "编程猫_打call", "编程猫_加油", "雷电猴_哇塞", "魔术喵_魔术", "星能猫_耶",
        )
        emoji = choice(picture)
                # 输出作品信息
        print("作品编号          " + str(item[0][1]))
        print("作品名称          " + str(item[1][1]))
        print("作者编号          " + str(item[3][1]))
        print("作者昵称          " + str(item[5][1]))
        print("评论数量          " + str(item[6][1]))
        print("点赞数量          " + str(item[7][1]))
        item = list(infos.items())  ## 将作品信息列表转换为键值对
        # 随机从sentents列表中选取一条评论，并使用format方法将work_name和nick_name添加进去,如{nick_name}
        content = choice(sentents).format(work_name=item[1][1], nick_name=item[5][1])
        # 发送POST请求，点赞指定作品
        p = post(
            r"https://api.codemao.cn/nemo/v2/works/{}/like".format(item[0][1]),
            headers=headers,  # 添加请求头，headers是一个字典类型的变量，包含了请求所需的各种参数
            data=dumps({}),  # POST请求数据为空，使用dumps方法将空字典转换为JSON字符串格式
        )  # 点赞
        print(datetime.now())  # 打印当前时间
        if str(item[0][1]) not in awa:  # 如果作品ID在awa列表中不存在
            if p.status_code == 200:  # 如果点赞成功
                print("点赞成功")
                sleep(2)
                like_num += 1
            else:  # 如果点赞失败，打印错误码
                print("点赞失败,error code:" + str(p.status_code))
            print("点赞了" + str(like_num) + "次")
            awa.append(str(item[0][1]))  # 将作品ID添加到awa列表中
        else:
            print("已经点赞过了")  # 如果作品ID在awa列表中存在，说明已经点赞过了
        if like_or_content == "A":  # 如果选择A，即要发送评论
            if check_string() or int(item[7][1]) > 50:  # 点赞大于50或已存在不发送
                print("\n" + "已存在或禁止发送")
                # 如果文本内容在禁止发送的关键词列表中，或者作品的点赞数大于50，则不发送评论
            else:
                print("\n" + "不存在")
                # 发送POST请求
                p = post(
                    r"https://api.codemao.cn/creation-tools/v1/works/{}/comment".format(
                        item[0][1]
                    ),  # 请求地址，使用format方法将文本中的{}占位符替换为元组item中第1个元素的值
                    headers=headers,  # 添加请求头，headers是一个字典类型的变量，包含了请求所需的各种参数
                    data=dumps(  # POST请求数据，包含两个字段：content和emoji_content
                        {
                            "content": content,  # 要发送的评论内容，从上文中定义的content变量中获取
                            "emoji_content": emoji,  # emoji表情内容，固定为"编程猫_打call"
                        }
                    ),
                )  # 评论
                content_num += 1
                print("已发送评论" + str(content_num) + "条")
                with open(
                    "qwq.txt", "a+", encoding="utf-8"
                ) as file:  # 以追加模式打开文件qwq.txt
                    file.write(  # 将一堆信息写入文件
                        "\n".join(  # 将多个字符串连接起来，用"\n"分隔
                            [
                                "作品编号    " + format(item[0][1]),
                                "作品名称    " + format(item[1][1]),
                                "作者编号    " + format(item[3][1]),
                                "作者昵称    " + format(item[5][1]),
                                str(datetime.now()),
                            ]
                        )
                    )
                    file.write("\n" + "=" * 50 + "\n")  # 分隔符
                    file.close()  # 关闭文件
                sleep(12)  # 一小时三百个,每分钟5个,12秒一个(忽略计算和网络延迟,理论上是最高速度
                sleep(sleep_time)  # 等待12秒钟，保证不会被反爬虫机制封禁
                # 额外等待sleep_time秒钟，具体值是从命令行参数中传入的
        print("*" * 100)

# 笔记
#   r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
#   w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#   a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#   rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
#   wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#   ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
#   r+	打开一个文件用于读写。文件指针将会放在文件的开头。
#   w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#   a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
#   rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
#   wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
#   ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。

#   not x	    if x is false,then True,else False	   1
#   x and y	    if x is false,then x,else y	           2
#   x or y	    if x is false,then y,else x	           3
# not是 “非” ；and是 “与” ；or是 “或” （可以用数学去理解)
# 1、not True = False 或者 not False = True (非真就是假，非假即真)
# 2、and是一假则假，两真为真，两假则假
# 3、or是一真即真，两假即假，两真则真
# 优先级是 not > and > or
