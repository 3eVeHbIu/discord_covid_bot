import xml.dom.minidom as minidom


def get_country_dict(xml):
    doc = minidom.parse(xml)
    node = doc.documentElement
    countries = doc.getElementsByTagName('country')

    records = []
    for country in countries:
        nameObj = country.getElementsByTagName('name')[0]
        englishNameObj = country.getElementsByTagName('english')[0]
        alpha2Obj = country.getElementsByTagName('alpha2')[0]
        alpha3Obj = country.getElementsByTagName('alpha3')[0]
        records.append([nameObj, englishNameObj, alpha2Obj, alpha3Obj])
    answer = []
    for record in records:
        collection = []
        for i in range(4):
            nodes = record[i].childNodes
            for node in nodes:
                if node.nodeType == node.TEXT_NODE:
                    collection.append(node.data)
        answer.append(collection)
    return answer


document = 'table.xml'
print(*get_country_dict(document), sep='\n')
