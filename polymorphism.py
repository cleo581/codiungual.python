class india():
    def capcital(self):
        print("dehili is the capital of india")
    def language(self):
        print("hindi is the most widely spoken language in india")
    def type(self):
        print("india is a devolping country")

class usa():
    def capcital(self):
        print("washington is the capital of usa")
    def language(self):
        print("english is the most widely spoken language in usa")
    def type(self):
        print("usa is a developed country")
obj1=india()
obj2=usa()
for country in (obj1,obj2):
    country.capcital()
    country.language()
    country.type()

