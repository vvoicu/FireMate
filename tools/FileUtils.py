import os

propertySeparator = "="
commentSeparator = "#"
listSeparator = ","

class FileUtils(object):

    def read_property(self, fileName, propertyName):
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(pathRoot,"data", fileName), "rt") as f:
            propertyValue = ""
            for line in f:
                l = line.strip()
                if l and not l.startswith(commentSeparator):
                    key_value = l.split(propertySeparator)
                    key = key_value[0].strip()
                    if propertyName == key:
                        propertyValue = propertySeparator.join(key_value[1:]).strip('" \t')
                        break
            return propertyValue


    def read_properties_as_list(self, fileName, propertyName):
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(pathRoot, "data", fileName), "rt") as f:
            propertyValues = []
            for line in f:
                l = line.strip()
                if l and not l.startswith(commentSeparator):
                    key_value = l.split(propertySeparator)
                    key = key_value[0].strip()
                    if propertyName == key:
                        propertyValues = propertySeparator.join(key_value[1:]).strip('" \t').strip('" \n').split(listSeparator)
                        break
            return propertyValues

if __name__ == "__main__":
    print FileUtils().read_property("TestData.ini","myList")
    print FileUtils().read_property("TestData.ini","myVar")
    print FileUtils().read_properties_as_list("TestData.ini", "myList")
    print FileUtils().read_properties_as_list("TestData.ini", "myVar")