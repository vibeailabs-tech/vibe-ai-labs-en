import numpy as np
from scipy import ndimage as ndi
from skimage.measure import find_contours

def _resample(c, step=1.0):
    d=np.r_[0,np.cumsum(np.hypot(*np.diff(c,axis=0).T))]
    n=max(int(d[-1]/step),8)
    t=np.linspace(0,d[-1],n,endpoint=False)
    return np.c_[np.interp(t,d,c[:,0]),np.interp(t,d,c[:,1])]

def _cr(points, closed):
    P=np.asarray(points)
    n=len(P)
    segs=[]
    rng=range(n) if closed else range(n-1)
    for i in rng:
        p0=P[(i-1)%n] if (closed or i>0) else P[i]
        p1=P[i]; p2=P[(i+1)%n]
        p3=P[(i+2)%n] if (closed or i+2<n) else P[(i+1)%n]
        c1=p1+(p2-p0)/6.0; c2=p2-(p3-p1)/6.0
        segs.append((c1,c2,p2))
    return segs

def smooth_path(mask, dx=0, dy=0, fsig=2.0, sm=7.0, step=10, corner_deg=48, k=7, minlen=60):
    f=ndi.gaussian_filter(np.pad(mask.astype(float),2),fsig)
    out=""
    fmt=lambda p:"%.2f %.2f"%(p[1]-2-dx,p[0]-2-dy)
    for cnt in find_contours(f,0.5):
        if len(cnt)<minlen: continue
        c=_resample(cnt[:-1] if np.allclose(cnt[0],cnt[-1]) else cnt,1.0)
        n=len(c)
        # corners
        c1=np.c_[ndi.gaussian_filter1d(c[:,0],1.5,mode="wrap"),ndi.gaussian_filter1d(c[:,1],1.5,mode="wrap")]
        a=c1-np.roll(c1,k,axis=0); b=np.roll(c1,-k,axis=0)-c1
        ang=np.degrees(np.arccos(np.clip((a*b).sum(1)/(np.hypot(*a.T)*np.hypot(*b.T)+1e-9),-1,1)))
        cand=[i for i in range(n) if ang[i]>corner_deg and ang[i]==ang[np.arange(i-10,i+11)%n].max()]
        if not cand:
            s=np.c_[ndi.gaussian_filter1d(c[:,0],sm,mode="wrap"),ndi.gaussian_filter1d(c[:,1],sm,mode="wrap")]
            pts=s[::step]
            segs=_cr(pts,True)
            d="M"+fmt(pts[0])+"".join("C"+fmt(a_)+" "+fmt(b_)+" "+fmt(e) for a_,b_,e in segs)+"Z"
        else:
            cand=sorted(cand)
            d=None
            for j,i0 in enumerate(cand):
                i1=cand[(j+1)%len(cand)]
                idx=np.arange(i0,i1+1) if i1>i0 else np.r_[np.arange(i0,n),np.arange(0,i1+1)]
                seg=c[idx]
                if len(seg)<4: continue
                # smooth keeping ends: pad by reflection about endpoints
                pad=int(3*sm)
                lo=2*seg[0]-seg[1:pad+1][::-1]; hi=2*seg[-1]-seg[-pad-1:-1][::-1]
                ext=np.vstack([lo,seg,hi]) if len(seg)>pad+1 else seg
                if len(seg)>pad+1:
                    sx=ndi.gaussian_filter1d(ext[:,0],sm,mode="nearest")[pad:-pad]; sy=ndi.gaussian_filter1d(ext[:,1],sm,mode="nearest")[pad:-pad]
                    s=np.c_[sx,sy]
                else: s=seg
                s[0]=seg[0]; s[-1]=seg[-1]
                m=max(int(len(s)/step),1)
                pts=s[np.linspace(0,len(s)-1,m+1).astype(int)]
                segs=_cr(pts,False)
                if d is None: d="M"+fmt(pts[0])
                d+="".join("C"+fmt(a_)+" "+fmt(b_)+" "+fmt(e) for a_,b_,e in segs)
            d+="Z"
        out+=d
    return out
