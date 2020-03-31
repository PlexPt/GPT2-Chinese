import json
import numpy as np
import gpt_gen
import sys
from datetime import datetime
import time
import logging
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "7"
batchGenerating=True
path_HFW = '../data/words_highFreq.txt'
path_configs = ['config/config_godText_large1.json','config/config_poem.json','config/config_dabaigou.json']
num0 = [20,4,4]
tags = ['(文)','(诗)','(大白狗)','(句联想)']
rmHFW = [False,False,True,False]
maxNext = 3
path_next = 'model/nnlm/D_next.json'
path_simi = 'model/nnlm/D_simi.json'
quick = False
HFW = [[],[],[],[]]
with open(path_HFW,'r') as f:
    HFW[2] = f.read().strip().split('\n')

def main(path_data,mode,path_config,path_target,topk):
    ii = int(mode)
    model, tokenizer, config, device = gpt_gen.getModel(path_config=path_config)
    config['topk'] = topk
    with open(path_data,'r') as f:
        s = f.read().strip().split('\n')
    D = []
    t0 = time.time()
    for data in s:
        result = []
        for _ in range(3):
            if ii==1:
                r0 = gpt_gen.generating_poem('a',data, model, config, tokenizer,device,quick,num0[ii],batchGenerating=batchGenerating)
            else:
                r0 = gpt_gen.generating('a',data, model, config, tokenizer,device,quick,num0[ii],removeHighFreqWords=rmHFW[ii],HighFreqWords=HFW[ii],batchGenerating=batchGenerating)
            r0 = [rr + tags[ii] for rr in r0]
            result.extend(r0)
        d = {'input':data,'outputs':result,'num':len(result)}
        D.append(d)
        with open(path_target,'w') as f:
            json.dump(D,f,ensure_ascii=False,indent=4)
    t1 = time.time()
    print('predict time is {} for parameter topk={}'.format(t1-t0,topk))
if __name__=='__main__':
    mode,path_config,data,path_target = sys.argv[1:5]
    if len(sys.argv)>5:
        topk = int(sys.argv[5])
    else:
        topk = 8
    main(data,mode,path_config,path_target,topk)