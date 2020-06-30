from nameko.extensions import DependencyProvider
import tempfile
import boto3


class ObjectStorage(DependencyProvider):

    def __init__(self, bucket, region='cn-north-1', **kwargs):
        self.bucket = bucket
        super(ObjectStorage, self).__init__(**kwargs)

    def setup(self):
        self.FileClient = FileClient(self.bucket)

    def get_dependency(self, worker_ctx):
        return self.FileClient


class FileClient(object):

    def __init__(self, bucket, region='cn-north-1', **kwargs):
        self.bucket = bucket
        self.client = boto3.client('s3')
        super(FileClient, self).__init__(**kwargs)

    def write(self, key, data):
        resp = self.client.upload_fileobj(data, self.bucket, key)
        print(resp)
        return resp

    def read(self, key):
        with tempfile.TemporaryFile() as tf:
            resp = self.client.download_fileobj(self.bucket, key, tf)
            tf.seek(0)
            content = tf.read()
        return content.decode()
