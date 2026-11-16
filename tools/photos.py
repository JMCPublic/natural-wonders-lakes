"""Lakes photos (16 Nov 2026): rebuild the PH list in index.html from the photos in /photos and the credits in tools/photo_credits.json.
A lake only gets a photo (and a credit) once photos/<id>.jpg exists. Run: python3 tools/photos.py"""
import json,os,re
root=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cred=json.load(open(os.path.join(root,'tools','photo_credits.json'),encoding='utf-8'))
have={int(f[:-4]) for f in os.listdir(os.path.join(root,'photos')) if f.endswith('.jpg')}
PH={i:cred[str(i)] for i in sorted(have) if str(i) in cred}
p=os.path.join(root,'index.html');s=open(p,encoding='utf-8').read()
s=re.sub(r"const PH=\{.*?\};",'const PH='+json.dumps(PH,ensure_ascii=False).replace('\\','\\\\')+';',s,count=1,flags=re.S)
open(p,'w',encoding='utf-8').write(s);print(len(PH),'lakes with photos')
