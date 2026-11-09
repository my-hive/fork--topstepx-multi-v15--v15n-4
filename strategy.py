"""Causal GC short-horizon reversal, sampled every 30 completed minutes to limit churn."""
import numpy as np
PARAMS={"lookback":5,"interval":30,"start_sec":34200,"end_sec":50400,"risk":250}
def entry_risk(panel): return {s:np.full(len(d),PARAMS['risk'],dtype=float) for s,d in panel.items()}
def signals(panel):
 out={s:np.zeros(len(d),dtype=np.int64) for s,d in panel.items()}
 if 'GC' not in panel:return out
 d=panel['GC'];c=d.close.to_numpy();sec=d.ct_sec.to_numpy();x=np.zeros(len(d),dtype=np.int64)
 for ix in d.groupby('session',sort=False).indices.values():
  side=0
  for j,i in enumerate(ix):
   if PARAMS['start_sec']<=sec[i]<PARAMS['end_sec'] and j>=PARAMS['lookback'] and j%PARAMS['interval']==0: side=-int(np.sign(c[i]-c[ix[j-PARAMS['lookback']]]))
   if PARAMS['start_sec']<=sec[i]<PARAMS['end_sec']:x[i]=side
 out['GC']=x;return out
