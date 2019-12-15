# pip install xmltodict
import xmltodict
import pprint
import json
my_xml = """
    <students>
      <student id="1">
      <name>Naveen</name>
      </student>
      <student id="2">
       <name>Praveen</name>
      </student>
    </students>
"""

pp = pprint.PrettyPrinter(indent=4)
# Converts JSON representation to String
json_str = json.dumps(xmltodict.parse(my_xml))

# Converts JSON String to Python object
json_obj = json.loads(json_str)
print(json_obj["students"]["student"][0]["@id"])


