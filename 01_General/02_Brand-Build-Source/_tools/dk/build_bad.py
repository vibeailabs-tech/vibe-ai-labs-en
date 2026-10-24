import sys; sys.path.insert(0,"/tmp/dk"); sys.path.insert(0,"/tmp/brandbuild")
from recipes import *
import render, os
OUTD="/tmp/dk/bad"; os.makedirs(OUTD,exist_ok=True)
W=H=1080
# A: too much text, 3 CTAs, small type
d,b=gfx.ribbon(W,H,True,cx=0.78,cy=0.97,wr=1.3,uid="ba")
lg=logo.horizontal_parts("reversed","la",False); ld,lb,lw,lh=logo.place(lg,60,50,width=280)
txt=["Marketing × AI × Creative: Giải pháp tích hợp cho bài toán","tăng trưởng và vận hành. Doanh nghiệp có thể đầu tư vào","Marketing, sử dụng nhiều công cụ AI và liên tục sản xuất nội","dung sáng tạo. Nhưng nếu các hoạt động này vận hành rời rạc,","hiệu quả tổng thể vẫn có thể chưa như kỳ vọng. Marketing tạo","ra kế hoạch, nhưng quy trình triển khai còn thủ công. AI được","đưa vào công việc, nhưng chưa kết nối với dữ liệu. Creative tạo","ra nhiều nội dung, nhưng thông điệp chưa nhất quán trên các","điểm chạm. Vibe AI Labs kết nối Marketing × AI × Creative để","cùng doanh nghiệp tìm ra hướng giải quyết phù hợp."]
body=b+lb+T(60,190,"🔥 Ba năng lực, một hệ thống!!!",44,800,"#FFFFFF",HF)
for i,l in enumerate(txt): body+=T(60,250+i*34,l,22,400,"#D9E2F2",BF)
for i,l in enumerate(("Nhắn tin ngay","Gọi hotline","Xem website")):
    body+='<rect x="%d" y="880" width="270" height="64" rx="32" fill="%s"/>'%(60+i*300,["#2563FF","#14D8C4","#F97316"][i])+T(60+i*300+135,921,l,22,700,"#FFFFFF",BF,"middle")
body+=T(60,1010,"vibe-ai-labs.vibeailabs.workers.dev · vibeailabs@gmail.com · facebook.com/vibe.ai.labs",18,400,"#D9E2F2",BF)
open(OUTD+"/bad_1.svg","w").write(wrap_svg(W,H,d+ld,body))
# B: low contrast, wrong colours, many gradients
d,b=gfx.ribbon(W,H,False,cx=0.78,cy=0.5,wr=1.5,opacity=0.5,uid="bb")
lg=logo.horizontal_parts("color","lb",False); ld,lb,lw,lh=logo.place(lg,86,86,width=360)
defs=grad_def("bg1",86,0,900,0,"#14D8C4","#8B5CF6")+grad_def("bg2",86,0,900,0,"#F97316","#14D8C4")
body=b+lb+T(86,420,"Ba năng lực.",120,800,"#14D8C4",HF)+T(86,550,"Một hệ thống.",120,800,"url(#bg1)",HF)+T(86,640,"Marketing × AI × Creative cùng vận hành.",34,500,"#B9C6E0",BF)
body+='<rect x="86" y="720" width="520" height="90" rx="45" fill="url(#bg2)"/>'+T(346,778,"Nhắn tin cho chúng tôi",30,700,"#14D8C4",BF,"middle")
open(OUTD+"/bad_2.svg","w").write(wrap_svg(W,H,d+ld+defs,body))
# C: stretched logo, shadow, off-grid, no hierarchy
d,b=gfx.waves(W,H,True,uid="bc")
lg=logo.stacked_parts("reversed","lc",False); ld,lb,lw,lh=logo.place(lg,30,40,width=760)
body=b+'<g transform="translate(0,0) scale(1,.65)" style="filter:drop-shadow(8px 8px 6px rgba(0,0,0,.8))">%s</g>'%lb
for i,l in enumerate(("Ba năng lực.","Một hệ thống.","Marketing","AI","Creative")): body+=T(60+i*20,620+i*70,l,[70,50,64,38,56][i],[800,400,800,300,700][i],["#FFFFFF","#FFC400","#14D8C4","#FF4D4D","#FFFFFF"][i],["Georgia",BF,HF,BF,"Comic Sans MS"][i])
open(OUTD+"/bad_3.svg","w").write(wrap_svg(W,H,d+ld,body))
jobs=[]
for n in ("bad_1","bad_2","bad_3"): jobs.append((open(OUTD+"/%s.svg"%n).read(),OUTD+"/%s.png"%n,1080,1080,False))
print(sum(render.batch(jobs,3)))
