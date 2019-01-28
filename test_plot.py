import base64
import gzip
import io
import os
import sys

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import notebook
import xlrd



def main():
	
	print("Verze Pythonu je {}.{}.".format(sys.version_info[0], sys.version_info[1]))

	if sys.version_info[0] < 3:
		print("Je potřeba nainstalovat Python 3. :-(")
		sys.exit(1)

	print("Verze Jupyter Notebooku je {}.".format(notebook.__version__))
	print("Verze XLRD je {}".format(xlrd.__version__))

	# Přečteme data, která jsou na konci tohoto skriptu.
	data_file = io.BytesIO(gzip.decompress(base64.b85decode(POINTS)))
	
	data = pd.read_csv(data_file)
	sns.set()
	plt.scatter(x='x', y='y', data=data, alpha=0.7)
	
	print("Jestli vidíte kódové slovo v grafu, nainstalovali jste všechno úspěšně. :)")
	plt.show(block=True)
	
	sys.exit(0)


# Následují body se zakódovaným slovem
POINTS = b'ABzY8qVrB%0{@MhTaFw%4n+TRE!l!3>baoV!_4j{)c(0voQo<LFyL;LBnBf$MrQeW|NH*$$?s2z)S~CQR;#_WmdjgOT5Z=>TW-6|{uC{%Y1X-G&7(x0`_Hn{s{S=<%qUO&U6pHIrPr0qERpN$`#+(DB}Ivub<WzWt+UWhc$yaGH1Zf{w>kGJd%u3j)8C(+*4|BjVvJJ8c>RcHoMmO#So(C=eTt5?1D^T*tkjnF*XNs7_xWDi&u6_qGtIfmY<)-WRUzD)Kl?1ov*e+LWsTm(e($}XqBM*YBlajc&e|RCz4=p=g`P$qOPimY=)>=|`+5}7PfPmkY_pA}&#rjy&7Tryl`=e99%~j|d+zt%{V7U7q#nIT?5vyA+1`8irwIL;R#k#$spl7Ezt`^jDdVgv;!DjTM)a*K&G+8^DMG)b_77&|{odO@Meye|{|bJ-zW<}ElvGNtRXk}!SsDNN(OvE%o|>8DJ@r09I#>t4Eqc_#M88#2EA#x8O)$${H?<MXT{g87&s{Zj0MS7<bpqExH+2!+O*wS~-Ay`?f$k=qC_s0UPE?}1X(s~cZrX_kbT{clN4lGMVgTJuJTZyxrX3+vlbF!j5C?15o%jBwy9p@vdvCZ%KP@xaN2*fASvBj<<7tJ-?(%7s`F_i%1+o1SPisVVmrm<Mb?7*QsP58flc)~b5voph&`#Sxcau)fKzEZ)FGP3KPOm_B(@qbdyGf@vq`Qfycc8n8rw^jLX{Vo`DZOjgyjRb8#4p)RK79e%O+9^IU7_S0uAGsX=_Bo#^}*Rzo3lKlFwbx0j7rB^{+<!<H~n+`%g{8_m~)KX>mDQKGjL|IAjbPm6&v&YGy$9l79F`#oU?}FRt`0!ZIbkT{h8m-MR=C?^Y}6=owrj~&C(KaD~7fTDj@gWwg2Y^GP^Mpu8zHVr+Ems*9;9b+6p_f-F^9iR=l3M-_L{N%5Y%KsppZE7**SRuJ^2h_3^&{s_*CSt)G3Kdsm|aYe|1|R|`87WQt(CpU02oB@XUSEkHLr+0kICy1wc@CsGT52zGuyb&B!q@_wGNb~PY9Mtu;jRnsXFW$ZooI2n9)gWd#T?oQo_;vDZcom2J5g0RN97aj^xY-oxQg^D!vMTnwg$OKFj+T7!SfkK<S-wfj=lX<I=Ld{2QX718;BN?tt{tckf&9KQMI_TmE9WZig#30B5lfpF*%Erm+0o*<i7TIZs+Xuo@>if+=SV}NB0Qj-h4h{f*oHc<1fd5+B(}{#n?3Q!wnuR)IE{lEb+C@@=Ts9kK6D#B85XNJ-MpP<vZEK?1$GfNv0Hs#%YBs-=8s1@S1k+uBT5es6oVAn7o|eg1JGG3cbpo+~sCE5IW`QtuV`hObvez{10$XIUiPyju*=*0QaYZiMvujL=2H7>HM2GAeQvzDKGbNyxJ5ylxK&Hfo>>5)V=z((3KoOLIMw+k;G}44+pphml12Wd%nEBG^fvnm2(&qc!GvxBy<v+QE(){@oq+YiA8>d!etiOB4q07JDJR&ST-j7e#PqC1{{_F;X!~5CEs0#rmme_N^7dEo=^?u`qOW*G|&ykAk^>>e9%YY6}MR7m}r;;dxZ5Wdn<**H9665HAv*qkqV8Ge3HYVb1d6UWZX}u>wyjoM!oXY<`IBzd^wI$_iigQg#+U2a1(RP$u%EDM!4k1&=8ER&^QPy8L{>X4U&XBhmfHUN6HpiLrHnCJu=B7VGdh1Gm)#-!v^hY6YovDlPqqU)kdTgnDQcgx%Gv_|_)4bNo;=-hyj3fr{p0{Y9Yn*k9asoMC1(**xUX&5Y@d`u`aw0npY^AKok6R0j^U9`<y<*l=FtloT1B{$n);=mN=WOA;Cgg3WagNsowBK2@?xeMo+`V;KU2+YrJ;_~QH;4oq3<r^5Q@H{X?21AH8k_+IKn5wvn?v!X#L1mI&?PC+EBA7K+J339K_Z?ucvc8$+a!-WZJV^=X{$M7s9uNaX)E4o0KOv|54NVRSoII>yUIB^oLB%|%`jLQbX7U0+qo+BTNscy;t4m5R6`$7T%zGT(Ly>PTF3`QTcB2Xv<16|QKc5DR2NlLVh|87d{s{T8bJ}^0=Ca_D`5K^w*s~gaq~xUgxmHW>8QzedxyMHlk2A94ib~|rn=*`Q4@~i>wT)$W}`8ttHOLs*j1Qt9lMGXE}(}KuH%OTF5wqA;u3zsi<s=)rABq6y}4-O1f;#Sh}kf5WA0?Z0Ubv>2EpTK$3$>$w2v7DWC-o;$N<!`;*Jae-3lTDSU0yfh;<9IONexXVs*oE?6^e%pd336Q4lT@q99xrL_w&yi9}S6C%?=MqH;X>WtOmZ^lIh{Ykj9|04}{j9Ds{FxyJ#x$d!8>gv*3D2$u!chLNFXPKb@XxzCI^X~>&<rJkt?t-jmQtQzL1P^L$k0#r>?ol+2KRY1T1;Aj{yKsY)E3?QD@-w-f>ILN~?hzp`#N#;u6$T;O0XTOcj>4xyU28UxIlu08YhB7N2y>#ikQ~-vObG~IZ(SCR+6TM*U)OBI~X-6;fKr=h`2tOHnNy|w<XANFj5K+%UY$kX#z5RJxNx5jqiV(}n!S^}u4WaYE;d1G;u%xLCa~31dH&(RHzDkSdE`NTArv_Da3i){SyRtjh^5<3$J;(CrRt=4;%bzoX-sR7&5NcH(YJlRj2EACPur7bJ{YFoJe;Y<YQB{bR)Cn~-DetA_rFDgBf`<IvG|2QOW%Z_HZL-Z^297&*VY(gI^iCFs+TEd?z@Q~(?y81C3+seW6j(!Xrob_XdS~S9jIZgR{(6b=0bfOT`2;?JCk35*8{u6+ksC1H^>YlWbN<#(<N>6=^%Hpl=`Z~#5@7tTpWk=Mz<5`XZiAe^H58>F=Wh)~smS?TL+S*``CCI#8Z!RYP?V00cMZk)CaiPbG!%tqQrA$Fg_OTE6z8p;jfSKlWdbN4sYEDg<KVRwM!h{qGXeb)zJddB0aciINj?=OUXV|PftTb{Vc>Q7R2X+%J{5;u6HvuT*CiA<=aPh?AmvR$QIYZ{Av7f*p=d~XlaSmw5#A&e0|^fj`eWB_%DaTlGhFAqODM>8x`d8BhbkY^ijtC>B2}Wbt^nmtKxEBZOI@7R_*>fS@}J@rS#vlO8b<3$=~@bJivt?>PYlp7@KhM4wBHsq;=6X2S=1_+rts7S>qgSvSts_TvaNJAf9D8i9#d|sW|9_*Xeo+FqlYAaO!?oc^)tIaCj#ko;vq<<dussU96N3|TPZKqBP~?<?7vqVR8TNfdz1?GNoM?JzE`Kd0S>E8^56sq)Fydw2gKkV)yf8dJ8a}5^AX2`-(W!LA06PZ(mw{^VbK10v}<_W;En}gIJg_Y0BDcx_TuJs2A>^atDf|z7@GC8@dA4_ydI@|X}WNTAz^bM$d<B+bCcJRiE|TGuZg1*RZZD#!rH3!Du}e@ZdFGbObWcwgtRSpYM8f$qpS+l6rAHclhD!9<HA7}3fba}Kp|V46RX;bGh#X3oDazHE>K(`!yEbqr3BwZLQ>d!_mWgyrtqq#%sj!yyXT}*GS;e1FqSy~r4F697K(i;IFggf$XSQZyX|!S*Fd)3P6jsKPKK7bY&jWP=E8N8q2bF*7gIYU;$42B47QAxuh%47apKKlNb6dMI=NHVGRnkLC)yI!mOAx9g!)dM<^_oNE=5fS+}e#}R|>`&DXVg5o?B8;Q7%fwU=6zx80(E)X>d7LWjnq58nY-=&O|7#T*RE2i{{gOuE(kHa4{7SF4ijxw_>>hs#NSBPL)~#7q5Oz_WPc<5NFwMiWd;99V0db<-jRqLr@;v>a*i#-`PR%>;*d%$QBt2y=hF|n`+Np9-F+k1AMou22YPMUEw3HBNi~=8e#$SEkG7H-~wnc;R0wd;W}h319!cjoUf%Dvd~Rh1#GRCw18O~GSwOaa>FaPZFm5@%^#ZpxNQO;25wt`hl9HT4F^|Vo8SO=yZc0dx7!<7z_vp%ax{+Bwg?OjS#1iy@Q~N`>jNIs?@wSXGl>L-zt99Uj@LFfgjHd{8$hh$1F~R<jDQ#%k<lOsfMj$G!$28>f^bwOSQkcR+0@OTY?$L=h>-1u3qr*B1RElr6)tE2%X8E9AmHh<F9r-x_32#4;7>uk&;37+17lmwNdN!'

if __name__ == "__main__":
	main()
