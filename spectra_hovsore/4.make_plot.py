#Carga de paquetes
import numpy as np
import matplotlib.pyplot as plt
import glob
from matplotlib.backends.backend_pdf import PdfPages
pdf_pages = PdfPages('plots/spectra.pdf')

def prom_movil(a,n):
	c = np.copy(a[1:len(a)])
	b = np.copy(c)
	if (n==0):
		pass
	else:
		for i in range(len(c[:,0])):
			if (i-n<0):
				aux    = c[0:i+n+1,1]
				b[i,1] = sum(aux)/len(aux)
			elif (i+n>len(c[:,0])-1):
				aux    = c[i-n:len(a[:,0]),1]
				b[i,1] = sum(aux)/len(aux)
			else:
				if (20<i<1090):
					cc = 12
					aux    = c[i-n-cc:i+n+cc,1]
					b[i,1] = sum(aux)/len(aux)
				else:
					aux    = c[i-n:i+n,1]
					b[i,1] = sum(aux)/len(aux)
	return b;

#Recta -5/3
x1=0.002
x2=0.03
y1=0.00001*x1**(-5.0/3.0)
y2=0.00001*x2**(-5.0/3.0)
x=[x1,x2]
y=[y1,y2]
#Obtención de datos para V
mm = 3
eta1 		= np.loadtxt("data/mean/eta01/V.txt")
modif_eta1 	= prom_movil(eta1,mm)
eta2 		= np.loadtxt("data/mean/eta02/V.txt")
modif_eta2 	= prom_movil(eta2,mm)
eta3 		= np.loadtxt("data/mean/eta03/V.txt")
modif_eta3	= prom_movil(eta3,mm)
eta4 		= np.loadtxt("data/mean/eta04/V.txt")
modif_eta4 	= prom_movil(eta4,mm)
eta5 		= np.loadtxt("data/mean/eta05/V.txt")
modif_eta5 	= prom_movil(eta5,mm)
# Gráfico del espectro para el número de onda
colors = plt.cm.viridis(np.linspace(1,0,5))
lww = 1.5
opa = 0.8
plot = plt.figure(figsize=(8,4))
plt.loglog(modif_eta1[:,0], modif_eta1[:,0]**2.0*modif_eta1[:,1]**2.0,lw=lww,label=r"$\eta_1\approx$ 5.25 [m]",color=colors[4],alpha=opa)
plt.loglog(modif_eta2[:,0], modif_eta2[:,0]**2.0*modif_eta2[:,1]**2.0,lw=lww,label=r"$\eta_2\approx$ 15.75 [m]",color=colors[3],alpha=opa)
plt.loglog(modif_eta3[:,0], modif_eta3[:,0]**2.0*modif_eta3[:,1]**2.0,lw=lww,label=r"$\eta_3\approx$ 26.26 [m]",color=colors[2],alpha=opa)
plt.loglog(modif_eta4[:,0], modif_eta4[:,0]**2.0*modif_eta4[:,1]**2.0,lw=lww,label=r"$\eta_4\approx$ 36.78 [m]",color=colors[1],alpha=opa)
plt.loglog(modif_eta5[:,0], modif_eta5[:,0]**2.0*modif_eta5[:,1]**2.0,lw=lww,label=r"$\eta_5\approx$ 49.57 [m]",color=colors[0],alpha=opa)
plt.loglog(x,y,ls="--",color="k")
plt.xlabel(r'k $[1/m]$')
plt.ylabel(r'$k^{2}|\hat{V}(k)|^2$ $[m^2/s^2]$')
plt.tight_layout()
plt.grid(b=True,which='both',axis='y')
plt.grid(b=True,which='both',axis='x')
plt.legend()
pdf_pages.savefig(plot)
pdf_pages.close()