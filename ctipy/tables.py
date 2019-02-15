import pandas as pd
from .attachments import upload_file, upload_image, _wrap_file, \
                         _wrap_image, _wrap_set_of_files


def upload_table(confluence, page_id, dataframe, columns_with_files=None,
                 columns_with_images=None):
    dataframe = dataframe.copy()

    if columns_with_files is None:
        columns_with_files = []
    if columns_with_images is None:
        columns_with_images = []

    df_html = _wrap_dataframe(confluence, page_id, dataframe,
                              columns_with_files, columns_with_images)

    page = confluence.get_page_by_id(page_id,
                                     expand='body.storage')
    page_body = page['body']['storage']['value']
    with pd.option_context('display.max_colwidth', -1):
        page_body += df_html.to_html(escape=False)

    confluence.update_page(None, page_id, page['title'],
                           page_body, minor_edit=True)


def _wrap_dataframe(confluence, page_id, dataframe,
                    columns_with_files, columns_with_images):
    for col in columns_with_files:
        _wrap_func = lambda x: _wrap_set_of_files(confluence, page_id,
                                                  x, _wrap_file)
        dataframe[col] = (dataframe[col].apply(_wrap_func))

    for col in columns_with_images:
        _wrap_func = lambda x: _wrap_set_of_files(confluence, page_id,
                                                  x, _wrap_image)
        dataframe[col] = (dataframe[col].apply(_wrap_func))

    return dataframe
