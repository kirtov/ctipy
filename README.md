# CTIPY (Confluence Tables and Images for PYthon)

+ [Intro](#Intro)
  1. a
  2. b
+ c

## Intro
Tiny lib which allows you to automatically upload images and tables (and tables with images!) onto Confluence page. 

So you can:
1. Do not copy files from server to your local machine before uploading it to Confluence page via browser.
2. You can run set of time-consuming experiments and automatically send results and logs onto Confluence page. So that report for your experiment would be finished right after your computations.
3. You can analyze results (right on Clonfluence page) of experiments that were already finished.

## Installation

Library distributed via PyPi, so you can run:
```
pip install ctipy
```

Also you can install it manually from github repos with:
```
python setup.py install
```

## Usage

Firstly you have to create `CTIConfluence` object with:
```
from ctipy import CTIConfluence

cti = CTIConfluence(url='https://yourcompany.atlassian.net/wiki',
                    username='youremail@yourcompany.com',
                    password='yourpassword',
                    page_id=pageid)
```

Notes:
* Format of URL of your company's Confluence can be different from 'https://yourcompany.atlassian.net/wiki'
* page_id - ID of page that you want to interact with. It is ~9 digit number which can be found in URL of confluence page
preceding its name. E.G.: https://yourcompany.atlassian.net/wiki/spaces/SOME_SPACE/pages/PAGE_ID/PAGE_NAME

After it you can interact with page:

### Uploading regular file
To upload file you can run:
```
cti.upload_file('path_to_the_file_on_you_local_fs')
```
After this command file will be attached to your page and you can find it in `Attachments` section of your page. After that you can manually put it onto the page via browser.

If you want to put file onto the page automatically, you can run:
```
cti.upload_file('/home/yvolkov/tmp/ckpt.meta', append_to_page=True)
```
After this command file will be attached to you page and placed at the bottom of your page.

### Uploading image
Supported types: png, jpg, jpe
Idea of uploading images is the same of uploading files:
You can run:
```cti.upload_image()``` with or without argument `append_to_page`.

### Uploading tables (pd.DataFrame)
Uploaded tables are always placed in the bottom of the page.
The most interesting feature of CTIPY is that it can upload tables with images inside.
To upload table you have to create arbitrar pandas DataFrame. To 'put' files in columns you have to put path to the file
of list of path to the files (same with images).
E.g.:
```df = pd.DataFrame()
df['text'] = [1, 2, 3]
df['file'] = ['/path/to/file1', ['/path/to/file2', 'path/to/file3'], '/path/to/file4']
df['image'] = [['/path/to/image1', 'path/to/image2'], '/path/to/image3', '/path/to/image4']
```
Then you call:
```
cti.upload_table(df, columns_with_files=['file'], columns_with_images=['image'])
```
And after (30 seconds - several minutes) you table will be appended to your page.
In `columns_with_files` you have provide list of DataFrame columns which consists paths to files.
In `columns_with_images` - paths to images. All other columns will be treated as plain text.


