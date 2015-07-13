from django.contrib import admin

from models import *

# Logger
admin.site.register(OperationSwitchControl)
admin.site.register(OperationLogger)
admin.site.register(DeepwellPump1Logger)
admin.site.register(DeepwellPump2Logger)
admin.site.register(DeepwellPump3Logger)
admin.site.register(DeepwellPump4Logger)
admin.site.register(CirculatingPumpLogger)
admin.site.register(DWPFlowmeterLogger) 
admin.site.register(CPFlowmeterLogger) 
admin.site.register(TemperatureLogger)
admin.site.register(TempHEIn1Logger)
admin.site.register(TempHEIn2Logger)
admin.site.register(TempHPIn1Logger)
admin.site.register(TempHPIn2Logger)
admin.site.register(TempHPIn3Logger)
admin.site.register(TempHPIn4Logger)
admin.site.register(TempHPIn5Logger)
admin.site.register(TempHPIn6Logger)
admin.site.register(TempHEOut1Logger)
admin.site.register(TempHEOut2Logger)
admin.site.register(TempHPOut1Logger)
admin.site.register(TempHPOut2Logger)
admin.site.register(TempHPOut3Logger)
admin.site.register(TempHPOut4Logger)
admin.site.register(TempHPOut5Logger)
admin.site.register(TempHPOut6Logger)
admin.site.register(HeatPump1Logger)
admin.site.register(HeatPump2Logger)
admin.site.register(HeatPump3Logger)
admin.site.register(HeatPump4Logger)
admin.site.register(HeatPump5Logger)
admin.site.register(HeatPump6Logger)
admin.site.register(PowerConsumptionLogger)
admin.site.register(RefrigerationTonLogger)
admin.site.register(TubeWellLogger)
# Ceiling Type Indoor Unit
admin.site.register(Floor1CIUs)
admin.site.register(Floor2CIUs)
admin.site.register(Floor3CIUs)
admin.site.register(Floor1CIU1)
admin.site.register(Floor1CIU2)
admin.site.register(Floor1CIU3)
admin.site.register(Floor1CIU4)
admin.site.register(Floor1CIU5)
admin.site.register(Floor1CIU6)
admin.site.register(Floor1CIU7)
admin.site.register(Floor1CIU8)
admin.site.register(Floor1CIU9)
admin.site.register(Floor1CIU10)
admin.site.register(Floor1CIU11)
admin.site.register(Floor1CIU12)
admin.site.register(Floor1CIU13)
admin.site.register(Floor1CIU14)
admin.site.register(Floor2CIU1)
admin.site.register(Floor2CIU2)
admin.site.register(Floor2CIU3)
admin.site.register(Floor2CIU4)
admin.site.register(Floor2CIU5)
admin.site.register(Floor2CIU6)
admin.site.register(Floor2CIU7)
admin.site.register(Floor2CIU8)
admin.site.register(Floor2CIU9)
admin.site.register(Floor2CIU10)
admin.site.register(Floor2CIU11)
admin.site.register(Floor2CIU12)
admin.site.register(Floor3CIU1)
admin.site.register(Floor3CIU2)
admin.site.register(Floor3CIU3)
admin.site.register(Floor3CIU4)
admin.site.register(Floor3CIU5)
admin.site.register(Floor3CIU6)
admin.site.register(Floor3CIU7)
admin.site.register(Floor3CIU8)
admin.site.register(Floor3CIU9)
admin.site.register(Floor3CIU10)
admin.site.register(Floor3CIU11)
admin.site.register(Floor3CIU12)

# Device Info
admin.site.register(FlowmeterInfo)
admin.site.register(InverterInfo)
admin.site.register(WattHourMeterInfo)
admin.site.register(HeatExchangerInfo)
admin.site.register(HeatPumpInfo)
admin.site.register(CirculatingPumpInfo)
admin.site.register(DeepwellPumpInfo)


