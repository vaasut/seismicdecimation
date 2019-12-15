# Seismic Decimation Description

Decimation.py reads in an mseed file, decimates the sampling rate by the given decimation_factor and outputs the original data and the decimated data to a new output file. It may also plot a spectrogram of the waveform.

Decimation.py uses the [ObsPy framework](https://github.com/obspy/obspy/)

# Instructions
You can run Decimation.py from the command line

`python decimation.py <input_file> [-o output_filename] [-d decimation_factor] [-s]`

```
input file (required)
-o output filename (not required)
-d decimation_factor (not required)
-s spectrogram (not required)
```

The input file must be an mseed file.

If no output filename is specified the data will be written to decimated.txt.If the output filename is the same as an already existing file, 'new' will be prepended to the filename.

The decimation factor should be an integer value from 2 to 10. If none is given, the decimation factor will be 10.

Decimation.py only plots a spectrogram is you use the -s flag
