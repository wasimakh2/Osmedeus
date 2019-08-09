---
title: "Common Issues"
date: 2019-08-08T21:14:11+07:00
draft: true
---

Currently Osmedeus will not support Windows so any issue about this OS will not support.

---

### Flask API error 

```
[-] Fail to set config, Something went from with Flask API !!!
```

#### Solution
Make sure you're installed Flask stuff via **python 3.6+** by this command
```
pip3 install flask flask_restful flask_jwt flask_cors flask_jwt_extended ansi2html
```

then manually verify that by run the Flask API indepenently.
```
python3 core/app.py
```
test if it's worked by using this commnad `curl -k https://127.0.0.1:5000`

---

### For running Error

Osmedeus support Continuous scan so you just have to **Ctrl+C** and run exactly your previous command it's gonna resume the scan.

If try all method above but still have error just open new issue.