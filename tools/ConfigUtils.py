import os

runConfigFile = "RunOption.txt"

class ConfigUtils(object):
    def read_run_config(self):
        # pathRoot = os.getcwd().replace("tools","")
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        with open(pathRoot + "/configs/" + runConfigFile, "r") as f:
            configType = f.readline()
            print "Config Selected: {}" .format(configType)
            return configType
        return "dev"

    def read_config_file(self):
        # pathRoot = os.getcwd().replace("tools", "")
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        configFileName = self.read_run_config().replace("\n","");
        fullPath = pathRoot + "/configs/" + configFileName + ".ini"
        print fullPath

        sep = "="
        comment_char = "#"

        props = {}
        with open(fullPath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip('" \t')
                    props[key] = value
        return props

if __name__ == "__main__":
    # fineName = DriverUtils().read_run_config()
    # print fineName
    print ConfigUtils().read_config_file()
    # print os.getcwd().replace("tools")