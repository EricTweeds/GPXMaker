from xml.dom import minidom

input = minidom.parse('./Wetha.xml')

INPUT = 'C:\\Users\\etweedle\\repos\\GPXCreator\\Wetha.xml'
OUTPUT = 'output.xml'

inputfile = open(INPUT)

xml = minidom.parse(inputfile)

times = xml.getElementsByTagName("time")
locations = xml.getElementsByTagName("loc")

doc = minidom.Document()
gpx = doc.createElement("gpx")
name = doc.createElement("name")
name.appendChild(doc.createTextNode("Wilderness Traverse"))

trk = doc.createElement("trk")

trk.appendChild(name)

trkseg = doc.createElement("trkseg")

gpx.appendChild(name)

for idx, time in enumerate(times):
    trkpt = doc.createElement("trkpt")

    timestamp = time.firstChild.nodeValue
    locationData = locations[idx].firstChild.nodeValue.split(",")

    trkpt.attributes["lat"] = locationData[1]
    trkpt.attributes["lon"] = locationData[0]

    ele = doc.createElement("ele")
    ele.appendChild(doc.createTextNode(locationData[2]))

    time = doc.createElement("time")
    time.appendChild(doc.createTextNode(timestamp))

    trkpt.appendChild(ele)
    trkpt.appendChild(time)

    trkseg.appendChild(trkpt)

trk.appendChild(trkseg)
gpx.appendChild(trk)

doc.appendChild(gpx)

stringdoc = doc.toprettyxml()

newdoc = minidom.parseString(stringdoc)

with open(OUTPUT, "w") as xml_file:
    newdoc.writexml(xml_file)