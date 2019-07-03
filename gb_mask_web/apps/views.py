from flask import request,render_template,send_file
from apps import app,gb
import cv2
import numpy as np
import io
from PIL import Image

@app.route('/',methods=["GET", "POST"])
def index():
  title = 'ときドルコラッター'
  if request.method == 'GET':
    return render_template('index.html',title=title)
  else:
    img = request.files.get('upload_img')
    if img is None:
      alert = "ファイルをアップロードして下さい"
      return render_template('index.html',alert=alert,title=title)
    else:
      #画像変換
      res_img = gb.maskGreenBack(img)

      #レスポンス
      buf = io.BytesIO()
      res_img.save(buf,"PNG")
      buf.seek(0)
      new_filename = img.filename.split(".")[0] + "_masked.png"

      #return render_template('index.html',alert="ok",title=title)
      return send_file(buf,attachment_filename=new_filename,as_attachment=True)