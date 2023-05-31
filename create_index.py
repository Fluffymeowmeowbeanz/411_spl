#### Used to construct the HTML file ####

#### data[year][title],[has_digital/physical],[digital/physical],[url],[total]

import jinja2

data = {}

class title():

	def __init__(self, title, has_digital, has_physical, digital, physical, url, total):
		self.title = title
		self.has_digital = has_digital
		self.has_physical = has_physical
		self.digital = digital
		self.physical = physical 
		self.url = url
		self.total = total

hill_17 = title(title="Hillbilly Elegy", has_physical=True, has_digital=True, digital="50%", physical="50%", url="./static/Hillbilly Elegy.JPG", total="8,059")
underg = title(title="The Underground Railroad", has_physical=True, has_digital=True, digital="50%", physical="50%", url="./static/The Underground Railroad.JPG", total="7,633")
eco_17 = title(title="The Economist", has_physical=False, has_digital=True, digital="100%", physical="0%", url="./static/The Economist.JPG", total="4,711")
arrival = title(title="Arrival", has_physical=True, has_digital=False, digital="0%", physical="100%", url="./static/Arrival.JPG", total="4,048")
ny_er = title(title="The New Yorker", has_physical=False, has_digital=True, digital="100%", physical="0%", url="./static/The New Yorker.JPG", total="3,790")

data["2017"] = {hill_17, underg, eco_17, arrival, ny_er}

edu_18 = title(title="Educated", has_physical=True, has_digital=True, digital="62%", physical="38%", url="./static/Educated.JPG", total="9,004")
power = title(title="The Power", has_physical=True, has_digital=True, digital="40%", physical="60%", url="./static/The Power.JPG", total="7,292")
hateu = title(title="The Hate U Give", has_physical=True, has_digital=True, digital="28%", physical="72%", url="./static/The Hate U Give.JPG", total="7,110")
soyou_18 = title(title="So You Want to Talk About Race", has_physical=True, has_digital=True, digital="22%", physical="78%", url="./static/So You Want to Talk About Race.JPG", total="6,255")
ny_18 = title(title="The New Yorker", has_physical=False, has_digital=True, digital="100%", physical="0%", url="./static/The New Yorker.JPG", total="5,974")

data["2018"] = {edu_18, power, hateu, soyou_18, ny_18}

becom_19 = title(title="Becoming", has_physical=True, has_digital=True, digital="66%", physical="34%", url="./static/Becoming.JPG", total="21,535")
crawdads = title(title="Where the Crawdads Sing", has_physical=True, has_digital=True, digital="54%", physical="46%", url="./static/Where the Crawdads Sing.JPG", total="15,734")
edu_19 = title(title="Educated", has_physical=True, has_digital=True, digital="66%", physical="34%", url="./static/Educated.JPG", total="15,614")
cra = title(title="Crazy Rich Asians", has_physical=True, has_digital=True, digital="90%", physical="10%", url="./static/Crazy Rich Asians.JPG", total="8,344")
normal = title(title="Normal People", has_physical=True, has_digital=True, digital="31%", physical="69%", url="./static/Normal People.JPG", total="6,410")

data["2019"] = {becom_19, crawdads, edu_19, cra, normal}

soyou_20 = title(title="So You Want to Talk About Race", has_physical=True, has_digital=True, digital="98%", physical="2%", url="./static/So You Want to Talk About Race.JPG", total="13,553")
becom_20 = title(title="Becoming", has_physical=True, has_digital=True, digital="96%", physical="4%", url="./static/Becoming.JPG", total="12,683")
craw_20 = title(title="Where the Crawdads Sing", has_physical=True, has_digital=True, digital="85%", physical="15%", url="./static/Where the Crawdads Sing.JPG", total="11,666")
edu_20 = title(title="Educated", has_physical=True, has_digital=True, digital="92%", physical="8%", url="./static/Educated.JPG", total="10,387")
talkto = title(title="Talking to Strangers", has_physical=True, has_digital=True, digital="85%", physical="15%", url="./static/Talk to Strangers.JPG", total="9,090")

data["2020"] = {soyou_20, becom_20, craw_20, edu_20, talkto}

vanishing = title(title="The Vanishing Half", has_physical=True, has_digital=True, digital="77%", physical="23%", url="./static/The Vanishing Half.JPG", total="16,776")
promised = title(title="A Promised Land", has_physical=True, has_digital=True, digital="91%", physical="9%", url="./static/A Promised Land.JPG", total="11,341")
midnight = title(title="The Midnight Library", has_physical=False, has_digital=True, digital="100%", physical="0%", url="./static/The Midnight Library.JPG", total="8,766")
braiding_21 = title(title="Braiding Sweetgrass", has_physical=True, has_digital=True, digital="93%", physical="7%", url="./static/Braiding Sweetgrass.JPG", total="7,271")
nomad = title(title="Nomadland", has_physical=True, has_digital=True, digital="94%", physical="6%", url="./static/Nomadland.JPG", total="6,827")

data["2021"] = {vanishing, promised, midnight, braiding_21, nomad}

cuckoo = title(title="Cloud Cuckoo Land", has_physical=True, has_digital=True, digital="83%", physical="17%", url="./static/Cloud Cuckoo Land.JPG", total="10,317")
house = title(title="The House of Broken", has_physical=True, has_digital=True, digital="82%", physical="18%", url="./static/The House of Broken.JPG", total="8,460")
last_thing = title(title="The Last Thing He Told Me", has_physical=True, has_digital=True, digital="91%", physical="9%", url="./static/The Last Thing He Told Me.JPG", total="8,216")
braiding_22 = title(title="Braiding Sweetgrass", has_physical=True, has_digital=True, digital="93%", physical="7%", url="./static/Braiding Sweetgrass.JPG", total="7,739")
essays = title(title="101 Essays That Will Change the Way You Think", has_physical=True, has_digital=True, digital="99%", physical="1%", url="./static/101 Essays that will Change the way You Think.JPG", total="4,816")

data["2022"] = {cuckoo, house, last_thing, braiding_22, essays}

from jinja2 import Environment, FileSystemLoader
environment = Environment(loader = FileSystemLoader(""))
template = environment.get_template("index_template.html")
content = template.render(data=data)

with open("index.html", "w", encoding="utf-8") as f:
	f.write(content)