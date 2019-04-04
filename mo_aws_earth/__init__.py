from collections import OrderedDict
import hashlib
import json

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


def generate_key(metadata):
    predictable_metadata = OrderedDict()
    for key in sorted(metadata.keys()):
        if key not in ['time', 'created_time', 'object_size', 'ttl', 'bucket', 'key']:
            predictable_metadata[key] = metadata[key]
    hashedmetadata = hashlib.sha1(json.dumps(predictable_metadata).encode('UTF-8')).hexdigest()
    key = "{hashedmetadata}.nc".format(hashedmetadata=hashedmetadata)
    return key


def generate_object_uri(metadata):
    return f"/s3/aws-earth-{metadata['model']}/{generate_key(metadata)}"  # TODO: Make not Pangeo specific
