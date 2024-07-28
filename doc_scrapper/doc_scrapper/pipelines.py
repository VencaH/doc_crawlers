# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import os


class TextValidationPipeline:
    def __init__(self):
        print("Pipeline initialized")

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter.get("text") and adapter.get("text") != "":
            return item
        else:
            print("got nothing back")
            raise DropItem(f"Missing or empty text field, no need for further processing")

class SaveToFolderPipeline:

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        if not (adapter.get("route")) or adapter.get("route") == "":
            raise DropItem(f"Missing or empty route field, can't save the file")
        if not (adapter.get("page")) or adapter.get("page") == "":
            raise DropItem(f"Missing or empty page field, can't save the file")
        
        folders = item.get("route")
        path = "/".join(folders)
        filename = item.get("page")
        text = item.get("text")
        print(path)
        self.ensure_path_exists(folders)
        self.save_to_file(path, filename, text)

        return item
        
    def ensure_path_exists(self, folders):
        print("folders:")
        print(folders)
        for i in range(len(folders)):
            path = "/".join(folders[:i+1])
            if not os.path.exists(path):
                os.makedirs(path) 

    def save_to_file(self, path, filename, text):
        full_path = f"{path}/{filename}.txt"
        with open(full_path, "w") as outfile:
            outfile.write(text)
        
