from xml.dom import minidom



if __name__ == '__main__':
        
    document = minidom.parse("input.xml")
    
    name = document.getElementsByTagName("name")[0]
    print(name.firstChild.data)
