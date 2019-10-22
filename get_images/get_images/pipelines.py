import scrapy
import os
from urllib.parse import urlparse
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class GetImagesPipeline(ImagesPipeline):

    def file_path(self, request, response=None, info=None):
        return './images/' + os.path.basename(urlparse(request.url).path)

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_urls'] = image_paths
        return item


