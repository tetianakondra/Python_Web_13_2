import json
from datetime import datetime

from mongoengine import disconnect

from models import Author, Quote

if __name__ == "__main__":

    with open ("authors.json", "r", encoding='utf-8') as fd:
        authors = json.load(fd)
        for el in authors:
            born_date_data = el["born_date"].split(",")
            born_date_data_str = born_date_data[0] + born_date_data[1]
            #born_date_m_d = born_date_data[0].split(" ")
            author = Author(fullname=el["fullname"])
            author.born_date = datetime.strptime(born_date_data_str, "%B %d %Y")
            author.born_location = el["born_location"]
            author.description = el["description"]
            author.save()
            
            with open ("quotes.json", "r", encoding='utf-8') as fh:
                quotes = json.load(fh)
                for el_q in quotes:
                    if el_q["author"][0] == el["fullname"]:

                        quote = Quote(tags=el_q["tags"], author=author.id)
                        quote.quote = el_q["quote"]
                        quote.save()

    disconnect()
