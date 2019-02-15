from atlassian import Confluence
from .tables import upload_table
from .attachments import upload_file, upload_image


class CTIConfluence(Confluence):
    def __init__(self, url, username, password, page_id, **kwargs):
        super().__init__(url, username, password, **kwargs)

        self.page_id = page_id

    def upload_file(self, path, append_to_page=False):
        return upload_file(self, self.page_id, path, append_to_page)

    def upload_image(self, path, append_to_page=False):
        return upload_image(self, self.page_id, path, append_to_page)

    def upload_table(self, dataframe, columns_with_files=None,
                     columns_with_images=None):
        upload_table(self, self.page_id, dataframe,
                     columns_with_files, columns_with_images)
