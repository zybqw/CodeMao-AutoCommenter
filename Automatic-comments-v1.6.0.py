import os
from random import choice, randint
import requests
import json
from bs4 import BeautifulSoup
from configparser import ConfigParser
from time import sleep

CONFIG_FILE_PATH = os.path.join(os.getcwd(), "config.ini")
HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.46",
}


def save_account(username, password):
    """保存账户信息到配置文件"""
    config = ConfigParser()
    config.add_section("Account")
    config.set("Account", "username", username)
    config.set("Account", "password", password)
    with open(CONFIG_FILE_PATH, "w") as configfile:
        config.write(configfile)


def login():
    """登录编程猫，获取cookie"""
    session = requests.Session()
    soup = BeautifulSoup(
        session.get("https://shequ.codemao.cn", headers=HEADERS).text, "html.parser"
    )
    pid = json.loads(soup.find_all("script")[0].string.split("=")[1])["pid"]
    while True:
        cookie_or_account = input("账号登录(K)&cookie(C):")
        if cookie_or_account == "K":
            username = input("请输入账号：")
            password = input("请输入密码：")
            save_account(username, password)
            identity = username
            break
        elif cookie_or_account == "C":
            cookie_str = input("请输入cookie：")
            identity = cookie_str
            break
        else:
            print("输入错误,请重试")

    response = session.post(
        "https://api.codemao.cn/tiger/v3/web/accounts/login",
        headers=HEADERS,
        data=json.dumps({"identity": identity, "password": password, "pid": pid}),
    )
    if response.status_code == 200:
        cookies = requests.utils.dict_from_cookiejar(response.cookies)
        cookie_str = (
            "authorization=" + cookies["authorization"] + ";acw_tc=" + cookies["acw_tc"]
        )
        print("登录成功")
        return cookie_str
    else:
        print("不能登录编程猫，请重试")
        if os.path.exists(CONFIG_FILE_PATH):
            os.remove(CONFIG_FILE_PATH)
            print("config.ini原有配置已成功删除！")
        return None


def like_work(cookie, work_id):
    """对某个作品进行点赞"""
    headers = {
        **HEADERS,
        "cookie": cookie,
    }
    response = requests.post(
        f"https://api.codemao.cn/nemo/v2/works/{work_id}/like",
        headers=headers,
        data=json.dumps({}),
    )
    if response.status_code == 200:
        print(f"点赞成功")
        return True
    else:
        print(f"点赞失败，错误代码：{response.status_code}")
        return False


def comment_work(cookie, work_id):
    """对某个作品进行评论"""
    contents = ["666＃°Д°", "加油！:O", "针不戳:D", "前排:P", "沙发*/ω＼*"]
    emojis = [
        "编程猫_666",
        "编程猫_棒",
        "编程猫_打call",
        "编程猫_加油",
        "雷电猴_哇塞",
        "魔术喵_魔术",
        "星能猫_耶",
    ]
    headers = {
        **HEADERS,
        "cookie": cookie,
    }
    content = shielding(choice(contents))
    emoji = choice(emojis)
    response = requests.post(
        f"https://api.codemao.cn/creation-tools/v1/works/{work_id}/comment",
        headers=headers,
        data=json.dumps(
            {
                "content": content,
                "emoji_content": emoji,
            }
        ),
    )
    if response.status_code == 201:
        print(
            "\n".join(
                [
                    f"评论成功",
                    f"评论内容  {content}",
                    f"附带表情  {emoji}",
                ]
            )
        )
        return True
    else:
        print(f"评论发送失败，错误代码：{response.status_code}\n")
        return False


def write(text):
    with open("qwq.txt", "a+", encoding="utf-8") as file:
        file.write(str(text) + "\n")


def check_string(work_id):
    try:
        with open("qwq.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line_number in lines:
            if str(work_id) in line_number:
                return True
        if str(work_id) in [18996184]:
            return True
        else:
            return False
    except:
        return False


def shielding(content):
    return b"\xe2\x80\xaa".decode("UTF-8").join([i for i in content])  # 屏蔽词转换


def main():
    like_num = content_num = 0
    cookie = login()
    if cookie is None:
        return

    while True:
        like_or_content = input("仅点赞(L)&点赞评论(A):")
        if like_or_content == "L" or like_or_content == "A":
            break
        else:
            print("输入错误,请重试!")

    while True:
        try:
            new = requests.get(
                "https://api.codemao.cn/creation-tools/v1/pc/discover/newest-work?offset=0&limit=20"
            )
            _dict = json.loads(new.text)
            print("\n已获取新作品列表")
            print("点赞总数：" + str(like_num))
            if like_or_content == "A":
                print("评论总数：" + str(content_num))
            for infos in _dict["items"]:
                item = list(infos.items())
                try:
                    print(
                        "\n".join(
                            [
                                f"\n作品编号  {item[0][1]}",
                                f"作者昵称  {item[5][1]}",
                                f"作品名称  {item[1][1]}",
                            ]
                        )
                    )
                    if like_work(cookie, item[0][1]):
                        like_num += 1
                    if (
                        like_or_content == "A"
                        and not check_string(item[0][1])
                        and int(item[7][1]) < 50
                    ):
                        if comment_work(cookie, item[0][1]):
                            content_num += 1
                            write(item[0][1])
                    sleep_time = randint(12, 16)
                    sleep(sleep_time)
                except KeyboardInterrupt:
                    print("用户中断运行")
                    exit()
                except Exception as e:
                    print("程序发生异常: ", e)
            sleep(5)  # 间隔时间
        except:
            sleep(5)
            continue  # 捕获异常后跳过


if __name__ == "__main__":
    main()
