import numpy as np

def Corr_curve(tc, triplet, dimension, *params):

	if triplet == "triplet":
		if dimension == "2D":
			return Corr_curve_2d_triplet(tc, *params)

		if dimension == "3D":
			return Corr_curve_3d_triplet(tc, *params)

	if triplet == "non triplet":
		if dimension == "2D":
			return Corr_curve_2d(tc, *params)

		if dimension == "3D":
			return Corr_curve_3d(tc, *params)






def Corr_curve_3d_triplet(tc, offset, GN0, A1, txy1, alpha1, AR1, B1, tauT1 ):

	txy1 = txy1 / 1000

	tauT1 = tauT1 / 1000

	G_Diff =  (A1*(((1+((tc/txy1)**alpha1))**-1)*(((1+(tc/((AR1**2)*txy1)))**-0.5))))

	G_T = 1 + (B1*np.exp(tc/(-tauT1)))

	return offset + GN0 * G_Diff * G_T

def Corr_curve_2d_triplet(tc, offset, GN0, A1, txy1, alpha1, B1, tauT1):

	txy1 = txy1 / 1000

	tauT1 = tauT1 / 1000

	G_Diff =  A1*(((1+((tc/txy1)**alpha1))**-1))

	G_T = 1 + (B1*np.exp(tc/(-tauT1)))

	return offset + GN0 * G_Diff * G_T


def Corr_curve_3d(tc, offset, GN0, A1, txy1, alpha1, AR1):

	txy1 = txy1 / 1000

	tauT1 = tauT1 / 1000

	G_Diff =  (A1*(((1+((tc/txy1)**alpha1))**-1)*(((1+(tc/((AR1**2)*txy1)))**-0.5))))

	return offset + GN0 * G_Diff


def Corr_curve_2d(tc, offset, GN0, A1, txy1, alpha1):

	txy1 = txy1 / 1000

	tauT1 = tauT1 / 1000

	G_Diff =  A1*(((1+((tc/txy1)**alpha1))**-1))

	return offset + GN0 * G_Diff