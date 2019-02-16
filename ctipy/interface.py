from atlassian import Confluence
from .tables import upload_table
from .attachments import upload_file, upload_image


class CTIConfluence(Confluence):
    def __init__(self, url, username, password, page_id, **kwargs):
        """
            Arguments:
                url (str): URL of Confluence server.
                    e.g.: 'https://yourcompany.atlassian.net/wiki'
                username (str): Username/email of your user.
                password (str): Password.
                page_id (str): Id of the page you want to modify.
                    It can be found in URL of the page.
                    It is ~9-digit number.
                    BE CAREFULL: THIS ARGUMENT ACCEPTS STRING.
                **kwargs:
        """

        super().__init__(url, username, password, **kwargs)

        self.page_id = page_id

    def upload_file(self, path, append_to_page=False):
        """
            Uploads regular file (not image) to the page.

            Arguments:
                path (str): Path to the file on your local filesystem.
                append_to_page (bool): Whether to append this file to the
                    bottom of the page.
                    If False, then file can be found in `Attachments` section
                    of the page.

            Returns (str):
                Name of created attachment.
        """

        return upload_file(self, self.page_id, path, append_to_page)

    def upload_image(self, path, append_to_page=False):
         """
            Uploads image to the page.
            Supported types: PNG, JPEG, JPG.

            Arguments:
                path (str): Path to the image on your local filesystem.
                append_to_page (bool): Whether to append this image to the
                    bottom of the page.
                    If False, then it can be found in `Attachments` section
                    of the page.

            Returns (str):
                Name of created attachment.
        """

        return upload_image(self, self.page_id, path, append_to_page)

    def upload_table(self, dataframe, columns_with_files=None,
                     columns_with_images=None):
        """
            Uploads table to the page and appends it to the bottom of the page.

            See README on github for more explanation and examples.

            Arguments:
                dataframe (pd.DataFrame): Table itself.
                columns_with_files (list): Columns with files.
                columns_with_images (list): Columns with images.

            Returns: None
        """

        upload_table(self, self.page_id, dataframe,
                     columns_with_files, columns_with_images)
