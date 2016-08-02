import os

propertySeparator = "="
commentSeparator = "#"
runConfigFile = "RunOption.txt"

class ConfigUtils(object):
    def read_run_config(self):
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(pathRoot,"configs", runConfigFile), "r") as f:
            configType = f.readline()
            print "Config Selected: {}" .format(configType)
            return configType
        return "dev"

    def read_config_file(self):
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        configFileName = self.read_run_config().replace("\n","");
        fullPath = os.path.join(pathRoot, "configs", configFileName + ".ini")
        print fullPath


        props = {}
        with open(fullPath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(commentSeparator):
                    key_value = l.split(propertySeparator)
                    key = key_value[0].strip()
                    value = propertySeparator.join(key_value[1:]).strip('" \t')
                    props[key] = value
        return props

if __name__ == "__main__":
    print ConfigUtils().read_config_file()