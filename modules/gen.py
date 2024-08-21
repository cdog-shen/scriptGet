from public_import import *
from run import file_tree
from shutil import copyfile


def file_list(startpath) -> list:
    flist = []
    for root, dirs, files in os.walk(startpath):
        for file in files:
            flist.append(f"{root}/{file}")
    return flist


class generator:

    def __init__(self, conf_dict):
        if conf_dict is tuple:
            print("config err quiting...")

        self.scriptDir = conf_dict["script_dir"]  # type: ignore
        self.scriptFiles = file_list(conf_dict["script_dir"])  # type: ignore
        self.genTo = conf_dict["gen_dir"]  # type: ignore
        self.logHandler = log_handler(
            conf_dict["log_dir"]  # type: ignore
            + "/gen_"
            + time.strftime(r"%Y-%m-%d_%H:%M:%S")
            + ".log"
        )
        self.__say()

    def __say(self):
        """for test check self params"""
        print(self.__dict__)

    def __gc(self):
        self.logHandler.write(
            time.strftime(
                r"---%Y-%m-%d_%H:%M:%S generator quiting... Now closed log file handler---"
            ).encode()
        )
        self.logHandler.close()

    def __gen(self):
        # deal with index
        index = self.genTo + "/index.html"  # type: ignore
        os.system(
            f"echo 'welcome to scriptGet, request to '/ls' to check script file tree :)' > {index}"
        )
        # del with ls
        ls = self.genTo + "/ls.html"  # type: ignore
        context = file_tree(self.scriptDir).decode('utf-8')
        os.system(f"echo {context} > {ls}")
        # deal with script response
        for root, dirs, files in os.walk(self.scriptDir):  # type: ignore
            relative_path = os.path.relpath(root, self.scriptDir)  # type: ignore
            dest_path = os.path.join(self.genTo, relative_path)  # type: ignore
            os.makedirs(dest_path, exist_ok=True)

        for file in self.scriptFiles:
            copyfile(file, str(file).replace(self.scriptDir, self.genTo).replace(".sh", ".html"))  # type: ignore

    def test(self):
        self.__gen()

    def done(self):
        self.__gc()


if __name__ == "__main__":
    confDict = verify_conf()
    ag = generator(conf_dict=confDict)
    ag.test()
    ag.done()
