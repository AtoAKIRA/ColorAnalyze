# -- coding: utf-8 --

import emd
import utils

def calc_one_hist(file):
	wcslab = utils.calc_wcslab_cie2000('wcslab.csv')

	rgb = {}
	f_r = open(file, 'r')
	for line in f_r:
		data = line.split(',')
		tmp = tuple((data[0], data[1], data[2]))
		if rgb.has_key(tmp):
			rgb[tmp] = rgb[tmp] + 1
		else:
			rgb[tmp] = 1

	ret_fname = file.split("/")[-1].split('_rgb.csv')[0] + "_wcslab.csv"
	f_w = open(ret_fname, 'w')

	hist = wcslab.create_chart(rgb)
	for k, v in hist.items():
		print k[0], ' -> ', k[1]
		d1 = str(k[0])
		d2 = str(k[1])
		d3 = str(v)
		f_w.write(d1 + "," + d2 + "," + d3 + "\n") 


import os

def calc(path):
	for _,_,fs in os.walk(path):
		print fs
		for f in fs:
			calc_one_hist(path + f)
			#calc_one_hist("./keydata/AbM_rgb.csv")

calc('./keydata/')