# EasyBioPlot
A tool for drawing pictures of biology.
## Functions of EasyBioPlot-Windows
You can unzip the compressed package (easybioplot.zip) to use EasyBioPlot in Windows.

![avatar](/imgs/EasyBioPlot.gif)

## Functions of EasyBioPlot-Linux
You can use EasyBioPlot by installing EasyBioPlot in Linux.

![avatar](/imgs/EasyBioPlot2.gif)

### Command
```
$ easybioplot weblogo [-d] FASTA_file [-f] folder_name [-o] out_name [-tp] type [-l] labels

optional arguments:
  -d   FASTA file name with sequences of equal length, and it can not use with -f.
  -f   folder name of FASTA files with sequences of equal length, and it can not use with -d.
  -o   out file name, and is should be end with '.svg'.
  -tp  type of data, and it defaults to 'p' ('p':Protein, 'n':Nucler, 'd':Disease).
  -l   labels of different FASTA files, and it should use with -f.
 ```
### example
```
$ easybioplot weblogo -d t1.txt -o t1.svg -tp p
$ easybioplot weblogo -f t3 -o t3.svg -tp p -l 1,2,3,4,5,6
```
### Command
```
$ easybioplot reduce [-d] FASTA_file [-sq] sequence [-o] out_name [-r] raacode

optional arguments:
  -d   FASTA file with single sequence, and it can not use with -sq.
  -sq  sequence, and it can not use with -d.
  -o   out file name, and is should be end with '.svg'.
  -r   reduce amino acid code, and it should be split by '-', such as 'LVIMCAGSTPFYW-EDNQKRH'.
 ```
### example
```
$ easybioplot reduce -d t2.txt -o t2 -r LVIMCAGSTPFYW-EDNQKRH
$ easybioplot reduce -sq KVFGRCELAAAMKRHGLDNYRGYSLGNWVCAAKFESNFNTQA -o t2 -r LVIMCAGSTPFYW-EDNQKRH
```
## Functions of EasyBioPlot-Python
You can use EasyBioPlot by installing EasyBioPlot in Linux.

![avatar](/imgs/EasyBioPlot3.gif)
