import sys, getopt, os
from obspy import read

def decimate_data(input_file,output_filename,decimate_factor,spectrogram):
	""" function reads in an mseed file, decimates the samplerate by decimate_factor and 
	writes the original data and the decimated data to a new file with the name output_filename.
	It plots a spectrogram of the waveform if the spectrogram variable is true."""

	try: #change decimate_factor to valid integer if possible
		decimate_factor = int(decimate_factor)
	except:
		print("decimate_factor should be an integer from 2 to 10")
		sys.exit()
	else:
		if (decimate_factor < 2 or decimate_factor > 10):
			print("decimate_factor should be an integer from 2 to 10")
			sys.exit()

	#read in the mseed file
	try:
		st = read(input_file,"MSEED")
	except:
		print("Invalid file format for input file")
		sys.exit()

	#get the original and decimated data
	original_data = st[0].data
	string_data = "" #make one big string to limit write calls
	decimated_string_data = ""
	count = 0
	for i in original_data:
		string_data += (str(i) + "\n")
		if (count % decimate_factor ==  0):
			decimated_string_data += (str(i) + "\n")
		count += 1

	#write start time, original sample rate, and original data to file
	start_time = "Original Data\n\n" + str(st[0].stats.starttime) + "\n"
	sampling_rate = str(st[0].stats.sampling_rate) + "\n\n"
	final_data = open(output_filename,'w')
	final_data.write(start_time)
	final_data.write(sampling_rate)
	final_data.write(string_data)

	#write start time again, decimated sample rate, and decimated data to file
	start_time = "\n\nDecimated Data\n\n" + str(st[0].stats.starttime) + "\n"
	sampling_rate = str(st[0].stats.sampling_rate/decimate_factor) + "\n\n"
	final_data.write(start_time)
	final_data.write(sampling_rate)
	final_data.write(decimated_string_data)
	final_data.close()
	
	#plot spectrogram
	if (spectrogram):
		st.spectrogram(log=False, title="Seismic Data " + str(st[0].stats.starttime))

def main(argv):
	input_file = ""
	output_filename = "decimated.txt" #if no output filename was specified
	spectrogram = False
	decimate_factor = 10

	if (len(argv) < 2): #input file required
		print("decimation.py <input_file> [-o output_filename] [-s]")
		sys.exit()
	else:
		input_file = argv[1]

	try: #optional arguments
		opts, args = getopt.getopt(argv[2:],"o:d:s")
	except getopt.GetoptError:
		print ("decimation.py <input_file> [-o output_filename] [-d decimate_factor] [-s]")
		sys.exit()
	for opt, arg in opts:
		if opt == "-o":
			output_filename = arg
		elif opt == "-d":
			decimate_factor = arg
		elif opt == "-s":
			spectrogram = True


	while (os.path.exists(output_filename)): #ensure that data is written to new file
		output_filename = "new" + output_filename
		
	if (not os.path.exists(input_file)):
		print ("Invalid path for input file\ndecimation.py <input_file> [-o output_filename] [-d decimate_factor] [-s]")
		sys.exit()
	else:
		decimate_data(input_file,output_filename,decimate_factor,spectrogram)



if __name__ == "__main__":
	main(sys.argv)





