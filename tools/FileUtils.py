import os
import ast

propertySeparator = "="
commentSeparator = "#"
listSeparator = ","

class FileUtils(object):
    def read_property(self, fileName, propertyName):
        pathRoot = os.path.dirname(os.path.dirname(__file__))
        with open(os.path.join(pathRoot, "data", fileName), "rt") as f:
            propertyValue = ""
            for line in f:
                l = line.strip()
                if l and not l.startswith(commentSeparator):
                    key_value = l.split(propertySeparator)
                    key = key_value[0].strip()
                    if propertyName == key:
                        return propertySeparator.join(key_value[1:]).strip('" \t')
                        break
            return propertyValue

    def read_properties_as_list(self, fileName, propertyName):
        return self.read_property(fileName, propertyName).split(listSeparator)

    def read_properties_as_dictionary(self, fileName, propertyName):
        dictionaryList = ast.literal_eval(self.read_property(fileName, propertyName))
        return list(dictionaryList)


if __name__ == "__main__":
    print FileUtils().read_property("TestData.ini","myList")
    print FileUtils().read_property("TestData.ini","myVar")
    print FileUtils().read_properties_as_list("TestData.ini", "myList")
    print FileUtils().read_properties_as_list("TestData.ini", "myVar")

    dictionaryList = FileUtils().read_properties_as_dictionary("policies.ini", "Workspace11")
    print dictionaryList[1]["date"]
    print dictionaryList
