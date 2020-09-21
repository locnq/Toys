import pandas as pd
import os
from tqdm import tqdm
import time
import numpy as np


DEFAULT_TYPE = "str"

COLUMN_NAME = [
    "OpenID",
    "Date",
    "ic1",
    "ic2",
    "ic3",
    "ic4",
    "ic5",
    "BanTime",
    "Reason1",
    "Reason2",
    "Reason3",
    "RoleID",
    "ic6",
    "Name",
    "ic7"
]

COLUMNS_TO_DROP = [
    "ic1",
    "ic2",
    "ic3",
    "ic4",
    "ic5",
    "Reason2",
    "Reason3",
    "ic6",
    "ic7",
]

def _load_logo():
    """ Load logo """
    with open('logo', 'r') as r:
        logo = r.readlines()
        r.close()
    for i in logo:
        i = i.replace('\n', '')
        print(i)
    print()
    print('Team OP\'s Tool')
    print('--Made by Nguyen Q Loc--')
    print()

def _load_dataframe():
    global COLUMN_NAME
    global COLUMNS_TO_DROP

    # IMPORT TRANSLATE REASON
    Reason = ["使用hosts或VPN等软件拦截反作弊数据方法",
              "违规修改游戏程序代码或数据",
              "使用vituralApp启动游戏",
              "绕过模拟器检测",
              "使用修改器",
              "使用修改资源文件方法",
              "自动瞄准作弊",
              "修改枪械后坐力作弊",
              "加速自瞄作弊",
              "虚拟机",
              "修改人物模型",
              "游戏全局加速作弊",
              "使用非官方客户端",
              "使用顶号扰乱反作弊数据方法",
              "范围伤害作弊",
              "全屏子弹作弊",
              "使用第三方插件",
              "子弹穿墙作弊",
              "透视作弊",
              "绕过模拟器匹配隔离",
              "使用定制外挂",
              "跳跃距离修改作弊",
              "模拟器过检测9041",
              "修改跳跃高度",
              "除草除树作弊",
              "修改倍镜作弊",
              "使用加减速工具",
              "离线回扫作弊处罚",
              "绕过设备检测",
              "存在与作弊玩家组队行为",
              "使用PC模拟器外挂",
              "在游戏中存在非法违规行为",
              "修改游戏代码或数据",
              "使用修改器类工具修改游戏数据",
              "新注册高击杀+组队(游客)",
              "使用模拟器进行游戏"]
    ReasonEng = ["Use hosts or VPN software to intercept anti-cheat data",
                 "Modify game program code or data in violation of regulations",
                 "Use vituralApp to start the game",
                 "Bypass emulator detection",
                 "Use modifier",
                 "Use the method of modifying resource files",
                 "Automatic targeting cheating",
                 "Modified firearm recoil cheating",
                 "Speed up self-pointing cheating",
                 "virtual machine",
                 "Modify the character model",
                 "Game global acceleration cheating",
                 "Use unofficial client",
                 "Use top numbers to disrupt anti-cheat data methods",
                 "Area damage cheating",
                 "Full screen bullet cheat",
                 "Use third-party plugins",
                 "Bullet cheating through the wall",
                 "Perspective cheating",
                 "Bypass the simulator match isolation",
                 "Use custom plug-ins",
                 "Jump distance modification cheating",
                 "Simulator over detection 9041",
                 "Modify jump height",
                 "Weed and tree cheating",
                 "Modify the magnification to cheat",
                 "Use acceleration and deceleration tools",
                 "Penalties for offline scanback cheating",
                 "Bypass device detection",
                 "Existence and cheating players teaming up",
                 "Use PC emulator plug-in",
                 "There are illegal violations in the game",
                 "Modify game code or data",
                 "Use modifier tools to modify game data",
                 "New registered high kill + team (tourist)",
                 "Use the emulator to play"
                 ]

    ban_rea = pd.DataFrame({'Reason1': Reason,
                            'ReasonEnglish': ReasonEng})

    df = pd.read_csv('coconut.txt', sep=',', index_col=None, error_bad_lines=False)
    df.columns = COLUMN_NAME

    df["OpenID"] = df["OpenID"].astype(DEFAULT_TYPE)
    df["RoleID"] = df["RoleID"].astype(DEFAULT_TYPE)

    df = df.join(ban_rea.set_index('Reason1'), on='Reason1')
    df = df.drop(columns=COLUMNS_TO_DROP)
    return df


def _find_id():
    global df
    with open('find_id(s).txt', 'r') as r:
        line = r.readlines()
        r.close()

    find_id = [i.replace('\n', '') for i in line]
    print(find_id)

    df["RoleID"] = df["RoleID"].astype("str")

    cond = df["RoleID"].isin(find_id)
    a = df[cond]
    print(a)
    banned_id = a["RoleID"].unique()
    a = df[df["RoleID"].isin(banned_id)].drop_duplicates(
        subset=['RoleID', 'Reason1'])

    a = a[["RoleID", "Date", "BanTime", "ReasonEnglish"]]

    a.to_csv(
        'result.txt',
        encoding='utf-8-sig',
        index=False)


def _update():
    # IMPORT DATA
    global COLUMN_NAME
    dir = 'Ban Account/'
    list_of_file = [
        fn for fn in os.listdir(dir) if fn.endswith('txt')
    ]
    df = pd.read_csv(dir + list_of_file[0], sep='|', error_bad_lines=False)
    df.columns = COLUMN_NAME
    df.dropna(how='all')

    df["RoleID"] = df["RoleID"].astype(DEFAULT_TYPE)
    df["RoleID"] = pd.to_numeric(df.RoleID, errors='coerce').fillna(0).astype(np.int64)
    df["OpenID"] = df["OpenID"].astype(DEFAULT_TYPE)
    df["OpenID"] = pd.to_numeric(df.OpenID, errors='coerce').fillna(0).astype(np.int64)
    df["BanTime"] = df["BanTime"].astype(DEFAULT_TYPE)
    df["BanTime"] = pd.to_numeric(df.BanTime, errors='coerce').fillna(0).astype(np.int64)


    progress_bar = tqdm(list_of_file[1:])
    for i in progress_bar:
        temp = pd.read_csv(dir + i, sep='|', error_bad_lines=False, index_col=None)
        temp.columns = COLUMN_NAME
        temp = temp.drop_duplicates()
        temp.dropna(how='all')
        temp["RoleID"] = temp["RoleID"].astype(DEFAULT_TYPE)
        temp["RoleID"] = pd.to_numeric(temp.RoleID, errors='coerce').fillna(0).astype(np.int64)
        temp["OpenID"] = temp["OpenID"].astype(DEFAULT_TYPE)
        temp["OpenID"] = pd.to_numeric(temp.OpenID, errors='coerce').fillna(0).astype(np.int64)
        temp["BanTime"] = temp["BanTime"].astype(DEFAULT_TYPE)
        temp["BanTime"] = pd.to_numeric(temp.BanTime, errors='coerce').fillna(0).astype(np.int64)
        df = df.append(temp, ignore_index=True)
        progress_bar.set_description('Extending...\"{}\"'.format(i))

    df["RoleID"] = df["RoleID"].astype(DEFAULT_TYPE)
    df.to_csv('coconut.txt', encoding='utf-8-sig', index=False)


if __name__ == '__main__':
    global df

    while True:
        os.system('cls')
        _load_logo()
        print("Select option: ")
        print("0.Quit ")
        print("1.Load database ")
        print("2.Find ID ")
        print("3.Update database ")
        c = int(input('Select: '))
        if c == 0:
            print("--- Pái pai! ---")
            time.sleep(2)
            break
        if c == 1:
            df = _load_dataframe()
            print(df.dtypes)
        if c == 2:
            _find_id()
        if c == 3:
            _update()
