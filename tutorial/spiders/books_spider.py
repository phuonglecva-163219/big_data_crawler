import scrapy
import json
import sys
import math
# print(sys.argv)
# number = sys.argv
data = []
# indexes = ["Original Title", "ISBN", "Edition Language", "Series", "Characters", "Setting", "Literary Awards" ]
# i = 0
class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        # print("--------------------------------------------")
        # print("page: {}".format(self.page))
        # print("--------------------------------------------")
        # my_file = open("test/{}.txt".format(self.page), "r")
        my_file = open("result/input3.txt", "r")
        content_list = my_file. readlines()
        urls = [
        ]
        for t in content_list:
            urls.append(t.rstrip("\n"))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        characters = ''
        # title =''
        # isbn = ''
        # lang = ''
        img = ''
        description = ''
        awards = ''
        details = response.css("div#bookDataBox")
        boxes = details.css("div.clearFloats")
        # title = boxes[0].css("div.infoBoxRowItem::text").get().strip()
        # isbn = boxes[1].css("div.infoBoxRowItem::text").get().strip()
        # lang = boxes[2].css("div.infoBoxRowItem::text").get().strip()
        img = response.css("img#coverImage::attr(src)").get()
        description = " ".join(response.css("div#descriptionContainer span::text").extract())
        # print(description)
        item = {}
        for box in boxes:
            boxTitle = box.css("div.infoBoxRowTitle::text").get()
            # print(boxTitle)
            if (boxTitle.strip() == 'Characters'):
                characters = box.css("div.infoBoxRowItem a::text").extract()
                item['Characters'] = characters
            elif (boxTitle.strip() == 'Literary Awards'):
                awards = box.css("div.infoBoxRowItem a::text").extract()
                item['Literary Awards'] = awards
            else:
                item[box.css("div.infoBoxRowTitle::text").get().strip()] = box.css("div.infoBoxRowItem::text").get().strip()
        item['img'] = img
        item['description'] = description
        # print(item)
        # print(title, isbn, lang, characters) 
        data.append(item)
        print(len(data))
        # print(len(self.urls))
        # data.append({
        #     "title":title, 
        #     "isbn":isbn, 
        #     "lang":lang, 
        #     "characters":characters,
        #     "description": description,
        #     "awards":awards,
        #     "img":img
        # })
        with open('result/result3.json', 'w', encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

class mySpider2(scrapy.Spider):
    name = "spiders2"
    # my_file = open("test.txt", "r")
    # content_list = my_file. readlines()
    # print(content_list)
    def start_requests(self):
        my_file = open("input.txt", "r")
        content_list = my_file.readlines()
        # print(content_list)
        list_base_urls = [
        ]
        list_len_urls = [
        ]
        for row in content_list:
            list_base_urls.append(row.strip().split(" ")[0])
            list_len_urls.append(int(float(row.strip().split(" ")[1].replace(",", "."))/100) + 1)
        # print(list_len_urls)
        urls = []
        for i in range(len(list_base_urls)):
            for j in range(1, list_len_urls[i]):
                urls.append("{}?page={}".format(list_base_urls[i], j))
        # base_url = "https://www.goodreads.com/list/show/8166.Books_You_Wish_More_People_Knew_About?page="
        # urls = [
        #     "https://www.goodreads.com/list/show/8166.Books_You_Wish_More_People_Knew_About?page=1"
        # ]
        # for i in range(2, 168):
        #     urls.append("{}{}".format(base_url, i))
        print(len(urls))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        root = "https://www.goodreads.com"  
        bookTitles = response.css("a.bookTitle::attr(href)")
        data.append(1)
        print(len(data))
        # print(data)
        # print(i)
        # i += 1
        for bookTitle in bookTitles:
            with open("urls/test8.txt", "a") as f:
                f.write("{}{}".format(root, bookTitle.get()))
                f.write("\n")
    
class mySpider3(scrapy.Spider):
    name = "spider3"

    def start_requests(self):
        urls = [
            # "https://www.goodreads.com/list/popular_lists?page=9"
        ]
        for i in range(2100, 2300):
            urls.append("https://www.goodreads.com/list/popular_lists?page={}".format(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, response):
        # print(response.body)
        root = "https://www.goodreads.com" 
        lists = response.css("div.cell")
        # data = []
        # print(len(lists))
        for l in lists:
            name = l.css("a.listTitle::attr(href)").get()
            noBook = l.css("div.listFullDetails::text").get().strip().split(" ")[0]
            data.append({
                "name": root+name,
                "no": noBook
            })
        print(len(data))
        with open("input.txt", "w") as f:
            for d in data:
                f.write("{} {}".format(d['name'], d['no']))
                f.write("\n")
        

