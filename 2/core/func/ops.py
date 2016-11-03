import zpl
import pprint
import zpl.core.data as data
import pandas as pd
import random
import string
from zpl.core.func.files import import_file
import os


Frames = data.Frames


def prepare_for_import(fresh=True):
    zpl.data.Generate.gen_imports()
    files = zpl.data.Frames.imports
    return files


def prepare_import(df):
    items = data.Frames.items
    def process(file):
        # file['checksum'] = sha1_checksum(file.path)
        file['ufid']      = new_ufid()
        file['status']    = True
        file['origin']    = os.path.split(file.path)[1]
        file['extension'] = os.path.splitext(file.path)[1]
        file['size']      = os.path.getsize(file.path)
        return file

    df = df.apply(process, axis=1)
    return df


def do_import(df):
    df = df.apply(import_file,axis=1)
    df_dict = df.to_dict('records')
    # print df_dict
    # zpl.db.session.bulk_insert_mappings(zpl.Items, df_dict)
    # zpl.db.session.commit()
    df.drop(['fl_origin','fl_lib'], inplace=True, axis=1)
    df.to_sql(name='items', con=zpl.db.session.bind, if_exists='append', index=False)
    return df


def new_ufid(chars=string.ascii_uppercase + string.digits):
    UFID = ''.join(random.choice(chars) for _ in range(10))
    return UFID


def gen_imports():
    try:
        files = imp.get_imports(Dir='/mnt/library/data/import/')
        imports = pd.DataFrame({'path': files})
    except:
        return False
    else:
        Frames.imports = imports
        return True
