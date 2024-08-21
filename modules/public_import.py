import os, sys, time, io


def verify_conf(CONF_PATH="sg_server.conf"):
    conf_dict = {}
    try:
        confHandler = open(CONF_PATH, "r")
    except Exception as ERR:
        return (f"PLZ check if {CONF_PATH} is exist in workspace.", {})

    for line in confHandler.readlines():
        if not line.lstrip().startswith("#") and "=" in line:
            tmp = line.replace(" ", "").replace("\n", "").split("=")
            if len(tmp) != 2 or tmp[0] == "" or tmp[-1] == "":
                return (f"some param in {CONF_PATH} is wrong, PLZ check it.", {})
            conf_dict[tmp[0]] = tmp[-1]

    return conf_dict


def log_handler(path: str):
    if os.name == "nt":
        pathList = path.replace("\\", "/").split("/")
        path = path.replace("/", r"\\")
    if os.name == "posix":
        pathList = path.split("/")

    fh = None
    while not fh:
        try:
            fh = open(path, "wb+")

        except FileNotFoundError:
            root = os.getcwd()
            for d in pathList[0:-1]:
                if d in root:
                    continue
                try:
                    os.mkdir(d)
                    os.chdir(d)
                except:
                    continue
            os.chdir(root)

        except Exception as ERR:
            print(ERR)
            print(pathList)

    return fh


if __name__ == "__main__":

    # log_deal(path="C:\\Users\\admin\\Desktop\\scriptGet\\log\\test\\adb\\loga").write(
    #     time.strftime(r"success when log test at %Y-%m-%d_%H:%M:%S").encode()
    # )

    verify_conf()
