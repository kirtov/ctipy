import ntpath
import os


def _wrap_file(filename):
    xhtml = f"""
                <ac:structured-macro ac:name="view-file" ac:schema-version="1">
                   <ac:parameter ac:name="name">
                       <ri:attachment ri:filename="{filename}"/>
                   </ac:parameter>
                   <ac:parameter ac:name="height">250</ac:parameter>
                </ac:structured-macro>
            """
    return xhtml.replace('\n', ' ')


def _wrap_image(filename):
    xhtml = f"""
               <ac:image ac:thumbnail="true" ac:height="150">
                   <ri:attachment ri:filename="{filename}" ri:version-at-save="1" />
               </ac:image>
             """
    return xhtml.replace('\n', ' ')


def upload_file(confluence, page_id, path, append_to_page=False,
                 wrap_func=_wrap_file):
    if not os.path.isfile(path):
        return path

    confluence.attach_file(path, page_id)
    filename = ntpath.basename(path)

    if append_to_page:
        page = confluence.get_page_by_id(page_id,
                                         expand='body.storage')
        page_body = page['body']['storage']['value']
        page_body += wrap_func(filename)
        confluence.update_page(None, page_id, page['title'],
                               page_body)
    return filename


def upload_image(confluence, page_id, path, append_to_page=False):
    return upload_file(confluence, page_id, path, append_to_page,
                       wrap_func=_wrap_image)


def _wrap_set_of_files(confluence, page_id, paths, _wrap_func=_wrap_file):
    if type(paths) == str:
        paths = [paths]
    uploaded_files = map(lambda x: upload_file(confluence, page_id, x),
                         paths)
    return ''.join(map(_wrap_func, uploaded_files))
