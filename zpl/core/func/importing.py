from zpl.core.frames import Frames, FrameLoad
from zpl.core.func.file import sha1_checksum
from zpl import db, md


FL = FrameLoad()

class Metadata(object):
    def __init__(self):
        FL.items()
        FL.metadata()

    def get_metadata(self):
        items = Frames.items
        metadata = Frames.metadata
        gen = items[['ufid','path']].merge(metadata, on='ufid', how='outer')
        # gen.drop(['uid'], inplace=True, axis=1)
        return gen


# def get_metadata(all=False):
#     FL.items()
#     FL.metadata()
#     items = Frames.items
#     metadata = Frames.metadata
#
#     gen = items[['ufid','path']].merge(metadata, on='ufid', how='outer')
#     gen.drop(['uid'], inplace=True, axis=1)
#     print gen
#     # gen = gen[gen['checksum'].isfalse()]
#     print gen
#     return gen
    # gen['checksum'] = gen.apply(sha1_checksum, axis=1)

    # return gen

    def update_metadata(self):
        data = get_metadata()
        metadata_columns = list(Frames.metadata.columns)[1:]
        metadata = data[metadata_columns]
        print metadata
        metadata.to_sql(name='metadata', con=db.session.bind, if_exists='append', index=False)


    def build_checksums(self, all=False):
        """Builds SHA1 checksums of files, all=True updates ALL checksums"""
        if all:
            metadata = self.get_metadata()
            # print metadata
            metadata = metadata.loc[metadata['checksum'].isnull()]
            # print metadata
        else:
            metadata = self.get_metadata()
        metadata['checksum'] = metadata.apply(sha1_checksum, axis=1)
        metadata_columns = list(Frames.metadata.columns)
        metadata = metadata[metadata_columns]
        # metadata.to_sql(name='metadata', con=db.session.bind, if_exists='append', index=False)
        # print metadata.head()
        update = metadata.to_dict('records')
        print update
        db.session.bulk_update_mappings(md.Metadata, update)
        db.session.commit()
        print metadata