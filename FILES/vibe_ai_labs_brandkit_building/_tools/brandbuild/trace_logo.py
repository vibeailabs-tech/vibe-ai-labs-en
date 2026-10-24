import json, numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage import morphology, measure
import potrace
import sys; sys.path.insert(0,'/tmp/brandbuild')
from smoothpath import smooth_path

SRC="/Users/henryle/Desktop/vibe_ai_labs/brandkit/01_Logos/Official/PNG/vibe-ai-labs-official-primary-no-tagline.png"
im=np.array(Image.open(SRC).convert("RGB")).astype(float)
mask=np.load("/tmp/trace/mask.npy"); labels=np.load("/tmp/trace/labels.npy")
UP=4

def trace_mask(m, sigma=0.9, alphamax=1.0, opttol=0.25, turd=8, dx=0, dy=0):
    f=ndi.gaussian_filter(m.astype(float),sigma)
    big=ndi.zoom(f,UP,order=3)>0.5
    bm=potrace.Bitmap(~big)
    pl=bm.trace(turdsize=turd*UP*UP//4, turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY, alphamax=alphamax, opticurve=True, opttolerance=opttol)
    def P(p): return "%.2f %.2f"%((p.x)/UP-dx,(p.y)/UP-dy)
    out=[]
    for c in pl:
        d="M"+P(c.start_point)
        for s in c.segments:
            if s.is_corner: d+="L"+P(s.c)+"L"+P(s.end_point)
            else: d+="C"+P(s.c1)+" "+P(s.c2)+" "+P(s.end_point)
        out.append(d+"Z")
    return "".join(out)

def fit_gradient(region, ox, oy, nstops=7, erode=4):
    er=morphology.binary_erosion(region,morphology.disk(erode))
    if er.sum()<200: er=region
    ys,xs=np.nonzero(er)
    sm=np.stack([ndi.gaussian_filter(im[...,c],1.2) for c in range(3)],-1)
    cols=sm[ys,xs]
    L=cols@np.array([.2126,.7152,.0722])
    A=np.c_[xs,ys,np.ones(len(xs))]
    a,b,c=np.linalg.lstsq(A,L,rcond=None)[0]
    n=np.hypot(a,b)
    d=np.array([a,b])/n if n>1e-6 else np.array([1.,0.])
    t=xs*d[0]+ys*d[1]
    t0,t1=np.percentile(t,[0.5,99.5])
    cx,cy=xs.mean(),ys.mean()
    base=np.array([cx,cy])-d*(d@np.array([cx,cy]))
    p0=base+d*t0; p1=base+d*t1
    edges=np.linspace(t0,t1,nstops+1)
    stops=[]
    for i in range(nstops):
        sel=(t>=edges[i])&(t<=edges[i+1])
        if sel.sum()<20: continue
        col=cols[sel].mean(0)
        off=(i+0.5)/nstops
        stops.append((off,"#%02X%02X%02X"%tuple(int(round(v)) for v in col)))
    # extend ends
    stops[0]=(0.0,stops[0][1]); stops[-1]=(1.0,stops[-1][1])
    return dict(x1=round(p0[0]-ox,1),y1=round(p0[1]-oy,1),x2=round(p1[0]-ox,1),y2=round(p1[1]-oy,1),stops=stops)

OX,OY=153,302   # lockup origin (stacked, original coordinates)
res={"origin":[OX,OY],"regions":[]}
sil=mask.copy(); sil[770:]=False
order=[(1,"back"),(3,"front"),(4,"mid"),(5,"under"),(2,"dot")]
# which label is which (centroids): 1 center(red) ,2 circle,3 front-bottom?, 4 left-back, 5 right underside
# print for sanity
for r in measure.regionprops(labels): print(r.label, r.area, [int(v) for v in r.centroid])

# ---- mark regions
sil=morphology.binary_closing(sil,morphology.disk(4))
sil=ndi.binary_fill_holes(sil)
sil_s=ndi.gaussian_filter(sil.astype(float),4.5)>0.5
core=np.where(sil&(labels>0),labels,0)
idx=ndi.distance_transform_edt(core==0,return_distances=False,return_indices=True)
lab2=core[idx[0],idx[1]]*sil_s
names={4:"back",3:"front",1:"core",5:"under"}
for lab in (4,3,1,5):
    reg=morphology.binary_dilation(lab2==lab,morphology.disk(2))&sil_s
    g=fit_gradient(labels==lab,OX,OY)
    res["regions"].append(dict(name=names[lab],d=smooth_path(reg,dx=OX,dy=OY,corner_deg=62,k=9,sm=6.0,step=9),grad=g))
# dot: perfect circle
dot=(labels==2)
ys,xs=np.nonzero(dot)
cy,cx=ys.mean(),xs.mean(); r=np.sqrt(dot.sum()/np.pi)
res["dot"]=dict(cx=round(cx-OX,1),cy=round(cy-OY,1),r=round(r,1),grad=fit_gradient(dot,OX,OY,nstops=5,erode=6))
# ---- wordmark
x0,y0,x1,y1=140,788,1125,935
crop=Image.fromarray(im[y0:y1,x0:x1].astype(np.uint8)).resize(((x1-x0)*UP,(y1-y0)*UP),Image.LANCZOS)
c=np.array(crop).astype(float)
big=c.max(axis=2)>150
big=ndi.binary_opening(big,iterations=1)
Rc,Gc,Bc=c[...,0],c[...,1],c[...,2]
counter=(Bc<215)&(Gc<75)&(Bc>120)
xs_=(np.arange(big.shape[1])/UP+x0)
zone=(xs_>600)&(xs_<640)
cm=counter&zone[None,:]
cm=ndi.binary_opening(cm,iterations=3)
big=big&~ndi.binary_dilation(cm,iterations=2)
lab=measure.label(ndi.binary_dilation(big,iterations=2))
parts={"vibe":np.zeros_like(big),"ai":np.zeros_like(big),"labs":np.zeros_like(big)}
for r_ in measure.regionprops(lab):
    cxo=(r_.centroid[1]/UP)+x0
    key="vibe" if cxo<548 else ("ai" if cxo<740 else "labs")
    parts[key]|=(lab==r_.label)&big
def tb(b):
    pl=potrace.Bitmap(~b).trace(turdsize=40,turnpolicy=potrace.POTRACE_TURNPOLICY_MINORITY,alphamax=0.9,opticurve=True,opttolerance=0.25)
    def P(p): return "%.2f %.2f"%(p.x/UP+x0-OX,p.y/UP+y0-OY)
    out=[]
    for cc in pl:
        d="M"+P(cc.start_point)
        for s in cc.segments:
            if s.is_corner: d+="L"+P(s.c)+"L"+P(s.end_point)
            else: d+="C"+P(s.c1)+" "+P(s.c2)+" "+P(s.end_point)
        out.append(d+"Z")
    return "".join(out)
from skimage.measure import find_contours, approximate_polygon
def poly_path(b, tol):
    d=""
    for cnt in find_contours(np.pad(b.astype(float),1),0.5):
        cnt=approximate_polygon(cnt,tol)[:-1]
        pts=[((q[1]-1)/UP+x0-OX,(q[0]-1)/UP+y0-OY) for q in cnt]
        d+="M"+"L".join("%.2f %.2f"%p for p in pts)+"Z"
    return d
ai_solid=ndi.binary_fill_holes(parts["ai"]|ndi.binary_dilation(cm,iterations=0))
ai_solid=ndi.binary_fill_holes(parts["ai"]) if False else parts["ai"]
# outer = fill holes of (ai part + counter)
ai_full=parts["ai"]|ndi.binary_dilation(cm,iterations=3)
ai_full=ndi.binary_fill_holes(ai_full)
ai_d=poly_path(ai_full,5.0)
cm_s=ndi.binary_dilation(cm,iterations=2)
print("counter poly:",poly_path(cm_s,9.0))
ai_d+="M464.3 539.2L475.7 569.2L452.0 569.2Z"
res["word"]={k:tb(v) for k,v in parts.items()}
res["word"]["ai"]=ai_d
# AI gradient (horizontal fit on original-res mask)
aim=np.zeros(mask.shape,bool)
a=parts["ai"]; aa=ndi.zoom(a.astype(float),1/UP,order=1)>0.5
aim[y0:y0+aa.shape[0],x0:x0+aa.shape[1]]=aa[:aim.shape[0]-y0,:aim.shape[1]-x0]
res["ai_grad"]=fit_gradient(aim,OX,OY,nstops=6,erode=2)
res["bounds"]=dict(w=1109-153+2,h=925-302+2)
json.dump(res,open("/tmp/brandbuild/logo_paths.json","w"))
print({k:(len(v["d"]) if isinstance(v,dict) and "d" in v else "") for k,v in zip(range(4),res["regions"])},{k:len(v) for k,v in res["word"].items()})
print(res["ai_grad"])
for r in res["regions"]: print(r["name"],r["grad"])
print(res["dot"])
