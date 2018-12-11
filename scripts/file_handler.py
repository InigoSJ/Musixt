from google.cloud import storage
import midi

def create_midi(name,pattern):
  path='files/{}'.format(name)
  midi.write_midifile(path, pattern)

def to_bucket(name,pattern,bucket_name):
  midi.write_midifile(name, pattern)
  storage_client = storage.Client()
  bucket = storage_client.get_bucket(bucket_name)
  blob = bucket.blob(name)
  blob.upload_from_filename(name)
  print('File {} uploaded to {}.'.format(
        name,
        bucket_name))
