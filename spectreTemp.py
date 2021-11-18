import seabreeze
seabreeze.use('pyseabreeze')
import seabreeze.spectrometers as sb
from datetime import datetime




spec = sb.Spectrometer.from_serial_number()
spec.integration_time_micros(20000)
wavelengths = spec.wavelengths()
intens = spec.intensities()
print(wavelengths)
print(intens)
filename = datetime.utcnow().strftime("./AllData/spectre_%Y%m%d_%H%M.csv")
with open(filename,"a") as file:
    range = wavelengths.size -1
    z = 0
    while z < range:
        z += 1
        file.write(str(wavelengths[z]) + ",\t" +str(intens[z]) + "\n")