import scrapy
import re
HTML_SOURCE = "file:///C:\\Users\\Admin\\Documents\\Học tập\\5.Xác suất thống kê\\Group Project\\OUTPUT\\{}.html"
OUTPUT = "../../../OUTPUT/{}.txt"

class ExtractSpider(scrapy.Spider):
    name = 'extract'
    def start_requests(self):
        with open("..\\..\\..\\test.txt", 'r') as f:
            for i in f:
                yield scrapy.Request(url = HTML_SOURCE.format(i), callback = self.parse)
    def parse(self, response):
        data = []
        for row in response.css("CallbackContent tr"):
            day_data = {}
            if isinstance(row.css("td::text").get(), str):
                day_data["Ngay"] = row.css("td::text").get().strip()
            if isinstance(row.css("td:nth-child(6)::text").get(), str):
                day_data["Gia"] = row.css("td:nth-child(6)::text").get().strip()
            if day_data.get("Gia") != None:
                data.append(day_data)
        with open("../../../OUTPUT/{}.txt".format(self.getFileName(response.url)), 'a') as f:
            for i in data:
                f.write(i.get("Ngay") + "-" + i.get("Gia") + "\n")
    def getFileName(self, file_path):
        return re.search("(?<=OUTPUT%5C)(.*)(?=.html)",file_path).group()

        