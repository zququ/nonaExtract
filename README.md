# nonaExtract

> Used to process fasta format AA sequence into nona-peptide and scoring

### Instruction

#### For a little data  ( <  50 sequences ) :

1. Install python.
2. Install the dependence, openpyxl. Maybe, just with command line: `pip install openpyxl`.
3. Make a fasta file with fasta formatted sequence, maybe just download from the NCBI protein database.
4. fill in the score at relative position in the script, as shown in the figure below.
![figure1](/pic/2019-12-17_21-39-06.png)
5. Run **nonaExtract_lite.py**.
6. The result will be shown in the output.xlsx with protein accession number at A column, processed nona-peptide at B column and the score at C column.

#### For long sequences ( > 50 sequences):

If your data size is large and openpyxl will run very slowly. So I recommand you to use the **nonaExtract_long.py**, which has removed the openpyxl dependency. And you can manully open your own blank excel file and copy the proName_and_number.txt to the A column of the excel file, then copy the process2nona_output.txt to the B column and the value.txt to the C column.

If feel happy using this easy script, please cite: 

Structure and Peptidome of the Bat MHC Class I Molecule Reveal a Novel Mechanism Leading to High-Affinity Peptide Binding
Zehui Qu, Zibin Li, Lizhen Ma, Xiaohui Wei, Lijie Zhang, Ruiying Liang, Geng Meng, Nianzhi Zhang and Chun Xia
J Immunol May 10, 2019, ji1900001; DOI: https://doi.org/10.4049/jimmunol.1900001

Any further question, feel free to contact the author, Zehui Qu: qzh813@gmail.com
