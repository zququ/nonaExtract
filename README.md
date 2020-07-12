# nonaExtract

<!-- TOC GFM -->

* [中文 README](#中文-readme)
	- [说明](#说明)
		+ [对于要处理数据量较少的情况（序列数少于50条）](#对于要处理数据量较少的情况序列数少于50条)
		+ [对于要处理数据量较大的情况](#对于要处理数据量较大的情况)
	- [版权与引用](#版权与引用)
	- [联系方式](#联系方式)
* [English README](#english-readme)
	- [Instruction](#instruction)
		+ [For a little data  ( <  50 sequences ) :](#for-a-little-data-----50-sequences--)
		+ [For long sequences ( > 50 sequences):](#for-long-sequences---50-sequences)
	- [Copyright and citation](#copyright-and-citation)
	- [Contact information](#contact-information)

<!-- /TOC -->

## 中文 README

> 用于将 `fasta` 格式氨基酸序列处理为九肽，并进行自定义打分的简单脚本。

### 说明

#### 对于要处理数据量较少的情况（序列数少于50条）

1. 安装 python
2. 安装 openpyxl 包。可以使用这个命令安装：`pip install openpyxl`。
3. 使用 fasta 格式，制作一个fasta文件，也许只需从NCBI蛋白质数据库下载即可。
4. 在填写脚本中对应位置改写分数，如下图所示。

![figure1](/pic/2019-12-17_21-39-06.png)

5. 运行 **nonaExtract_lite.py** 
6. 结果将显示在 output.xlsx 中，A 栏为蛋白质登录号以及九肽第一个氨基酸在蛋白序列中的位置，B 栏为处理后的九肽序列，C栏为得分。

#### 对于要处理数据量较大的情况

如果数据量很大，openpyxl 将运行非常缓慢。因此，我建议使用** nonaExtract_long.py **，它已删除了 openpyxl 依赖。 之后可以手动打开自己的空白 excel 文件，并将 proName_and_number.txt 复制到 excel 文件的 A 列，然后将 process2nona_output.txt 复制到 B 列，并将value.txt复制到 C 列。

### 版权与引用

如果使用此简单脚本感到满意，请引用：

Structure and Peptidome of the Bat MHC Class I Molecule Reveal a Novel Mechanism Leading to High-Affinity Peptide Binding
Zehui Qu, Zibin Li, Lizhen Ma, Xiaohui Wei, Lijie Zhang, Ruiying Liang, Geng Meng, Nianzhi Zhang and Chun Xia
J Immunol May 10, 2019, ji1900001; DOI: https://doi.org/10.4049/jimmunol.1900001

### 联系方式

如有任何其他疑问，请随时与作者(@曲泽慧)联系：qzh813@gmail.com。

## English README

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

### Copyright and citation

If feel happy using this easy script, please cite: 

Structure and Peptidome of the Bat MHC Class I Molecule Reveal a Novel Mechanism Leading to High-Affinity Peptide Binding
Zehui Qu, Zibin Li, Lizhen Ma, Xiaohui Wei, Lijie Zhang, Ruiying Liang, Geng Meng, Nianzhi Zhang and Chun Xia
J Immunol May 10, 2019, ji1900001; DOI: https://doi.org/10.4049/jimmunol.1900001

### Contact information

Any further question, feel free to contact the author, Zehui Qu: qzh813@gmail.com
