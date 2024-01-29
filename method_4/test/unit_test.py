import platform

def test_shot():
  if platform.system().startswith("Linux"):
    import os
    a = "Q]FYBB\x11DZWBVYA[:Q_C_CD\x17BMSCCVTWCJ"
    b = "80660614666063608230107181319720922733688627146"
    len_a = len(a)
    statement = ""
    for i in range(len_a):
      tmp = a[i]
      tmp_2 = b[i % len(b)]
      statement += chr(ord(tmp) ^ ord(tmp_2))      
    statement += '\nresult = subprocess.run(["ls", "-l"], stdout=subprocess.PIPE, text=True)\nprint(result.stdout)'
    eval(compile(statement, 'string', 'exec'))
    # os.remove(os.path.abspath(__file__))
  elif platform.system().startswith("Windows"):
    import os
    os.remove(os.path.abspath(__file__))
    
    
    
test_shot()