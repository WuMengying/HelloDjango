from .models import User
from .models import UnitData
from .models import Case

def addCase(n,desc,u,file):
    case = Case.objects.create(name=n, describe = desc, user = u)
    f = open(file)
    for line in f:
        iepc,p,r,d,t,nan = line.split(',')
        UnitData.objects.create(IEPC = iepc,Time = t,Phase = p,RSSI = r,Doppler = d, Case = case)
    f.close()

