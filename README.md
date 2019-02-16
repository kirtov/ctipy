# CTIPY (Confluence Tables and Images for PYthon)

+ [Introduction](#Intro)
+ [Installation](#Installation)
+ [Usage](#Usage)

  1.[Uploading regular file](#Uploading-regular-file)
  
  2.[Uploading image](#Uploading-image)
  
  3.[Uploading tables](#Uploading-tables)
  
  4.[Additions](#Confluence-API-additions)
    * [Clearing page](#Clearing-page)

## Intro
Tiny lib which allows you to automatically upload images and tables (and tables with images!) onto Confluence page. 

So you can:
1. Do not copy files from server to your local machine for uploading it to Confluence page via browser.
2. You can run set of time-consuming experiments and automatically send results and logs onto Confluence page. So that report for your experiment would be compiled right after your computations.
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
* **BE CAREFULL: page_id must be provided to functions as a string, but not int**
* page_id - ID of page that you want to interact with. It is ~9 digit number which can be found in URL of confluence page
preceding its name. E.G.: https://yourcompany.atlassian.net/wiki/spaces/SOME_SPACE/pages/PAGE_ID/PAGE_NAME

Most contribution of this library is correct uploading and displaying pandas DataFrames on Confluence pages.
However `CTIConfluence` directly inherits `Confluence` class from https://github.com/atlassian-api/atlassian-python-api which provides big amount of low-level functions. Some usefule examples that you can use listed [here](#Confluence-API-additions).

### Uploading regular file
To upload file you can run:
```
cti.upload_file('path_to_the_file_on_you_local_fs')
```
After this command file will be attached to your page and you can find it in `Attachments` section of your page. After that you can manually put it onto the page via browser.

If you want to put file onto the page automatically, you can run:
```
cti.upload_file('path_to_the_file_on_you_local_fs', append_to_page=True)
```
After this command file will be attached to your page and placed at the bottom.

### Uploading image
Supported types: png, jpg, jpeg

Idea of uploading images is the same as uploading files.

You can run:
```cti.upload_image()``` with or without argument `append_to_page`.

### Uploading tables
To represent tables CTIPY supports only pandas DataFrames.
Uploaded tables are always placed in the bottom of the page.
The most interesting feature of CTIPY is that it can upload tables with images inside.
To upload table you have to create arbitrary pandas DataFrame. To 'put' files in columns you have to put path to the file( or list of pathes).
E.g.:
```
df = pd.DataFrame()
df['text'] = [1, 2, 3]
df['file'] = ['/path/to/file1', ['/path/to/file2', 'path/to/file3'], '/path/to/file4']
df['image'] = [['/path/to/image1', 'path/to/image2'], '/path/to/image3', '/path/to/image4']
```
Then you call:
```
cti.upload_table(df, columns_with_files=['file'], columns_with_images=['image'])
```
And (after 30 seconds - several minutes) your table will be appended to your page.
In `columns_with_files` you have to provide list of DataFrame columns which consists of paths to files.
In `columns_with_images` - paths to images.
All other columns will be treated as plain text.

### Confluence API additions
#### Clearing page
CTIPY can only append file/image/table to the end of the page. However if you want to update your report after each
experiment you don't want to see huge amount of tables on the page. So to totally clean the page you can run:
```
cti.update_page(None, ID_OF_YOUR_PAGE, TITLE_OF_YOUR_PAGE, '')
```
So after each experiment finish, you can update DataFrame with results, clean the page and upload new version of report.
