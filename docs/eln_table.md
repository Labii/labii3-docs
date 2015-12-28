# Table

Labii ELN supports Excel-like table functionality. A table can be edited in both Experiment-Templates and Experiment documents. Labii ELN tables also support formulas for simple calculations, see list of available formulas below.

# Overview

![labii-eln-table-overview](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-overview.png)

Labii ELN supports two types of table views: edit view (picture above), and read-only view.

For edit view, one additional column (header) and row are included. All other cells work exactly like in Excel. Each cell also supports a right-click menu consisting of:

* Black font color: editable cell
* Gray font folor: read only cell
* Yellow background: formula

![labii-eln-table-overview-readonly](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-overview-readonly.png)

A read-only table does not contain headers and cell content cannot been changed like in the picture above. 

# Insert a table

A table is inserted within the editor. Quickly insert a table by highlighting required columns and rows after clicking the table icon, or from the advanced table property by clicking the table icon and then “More”.

## Insert a table by selection of cells

![labii-eln-table-insert](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-insert.png)

* Click table icon from editor
* Select number of columns and rows
* A new table will be inserted into your document.

## Insert a table from advanced table properties

![labii-eln-table-insert-advanced](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-insert-advanced.png)

* Click table icon from editor
* Click "More"
* Fill in the expected number of rows, columns, and other information
* Click "OK"
* A new table will be inserted into your document

# Edit a table

Editing a table is just like in Excel; select a cell, type in any value, and the table will be automatically updated.”

### Right click menu
* Insert row above
* Insert row bellow
* Insert column on the left
* Insert column on the rihgt
* Remove row
* Remove column
* Undo
* Redo
* Read only
* Alignment
	* Left
	* Center
	* Right
	* Justify
	* Top
	* Middle
	* Botttom
* Merge cells

### Added formula
Labii ELN table uses the same formula functions from Excel. For example, to calculate 2 + 1, just type in "=2+1". See the next section for more details.

# Table formula
### Numeric calculation
Type "=" and follow with a formula, for example "=10/5".
### Caculation with other cells
Type "=" and use a cell’s column id and row id to represent a number or text. For example, the cell in row 1 and column A, can be referred to as "A1". To multiple a number in A1 by 5, type "=A1*5".
### [List of supported formulas](http://handsontable.github.io/ruleJS/)
| | |
|:------|:------|:------|
| ABS| CONFIDENCET| FALSE|
| ACCRINT| CONVERT| FDIST|
| ACOS| CORREL| FINV|
| ACOSH| COS| FISHER|
| ACOTH| COSH| FISHERINV|
| AND| COT| IF|
| ARABIC| COTH| INT|
| ASIN| COUNT| ISEVEN|
| ASINH| COUNTA| ISODD|
| ATAN| COUNTBLANK| LN|
| ATAN2| COUNTIF| LOG|
| ATANH| COUNTIFS| LOG10|
| AVEDEV| COUNTIN| MAX|
| AVERAGE| COUNTUNIQUE| MAXA|
| AVERAGEA| COVARIANCEP| MEDIAN|
| AVERAGEIF| COVARIANCES| MIN|
| BASE| CSC| MINA|
| BESSELI| CSCH| MOD|
| BESSELJ| CUMIPMT| NOT|
| BESSELK| CUMPRINC| ODD|
| BESSELY| DATE| OR|
| BETADIST| DATEVALUE| PI|
| BETAINV| DAY| POWER|
| BIN2DEC| DAYS| ROUND|
| BIN2HEX| DAYS360| ROUNDDOWN|
| BIN2OCT| DB| ROUNDUP|
| BINOMDIST| DDB| SIN|
| BINOMDISTRANGE| DEC2BIN| SINH|
| BINOMINV| DEC2HEX| SPLIT|
| BITAND| DEC2OCT| SQRT|
| BITLSHIFT| DECIMAL| SQRTPI|
| BITOR| DEGREES| SUM|
| BITRSHIFT| DELTA| SUMIF|
| BITXOR| DEVSQ| SUMIFS|
| CEILING| DOLLAR| SUMPRODUCT|
| CEILINGMATH| DOLLARDE| SUMSQ|
| CEILINGPRECISE| DOLLARFR| SUMX2MY2|
| CHAR| E| SUMX2PY2|
| CHISQDIST| EDATE| SUMXMY2|
| CHISQINV| EFFECT| TAN|
| CODE| EOMONTH| TANH|
| COMBIN| ERF| TRUE|
| COMBINA| ERFC| TRUNC|
| COMPLEX| EVEN| XOR|
| CONCATENATE| EXACT||
| CONFIDENCENORM| EXPONDIST||
* ABS
* ACCRINT
* ACOS
* ACOSH
* ACOTH
* AND
* ARABIC
* ASIN
* ASINH
* ATAN
* ATAN2
* ATANH
* AVEDEV
* AVERAGE
* AVERAGEA
* AVERAGEIF
* BASE
* BESSELI
* BESSELJ
* BESSELK
* BESSELY
* BETADIST
* BETAINV
* BIN2DEC
* BIN2HEX
* BIN2OCT
* BINOMDIST
* BINOMDISTRANGE
* BINOMINV
* BITAND
* BITLSHIFT
* BITOR
* BITRSHIFT
* BITXOR
* CEILING
* CEILINGMATH
* CEILINGPRECISE
* CHAR
* CHISQDIST
* CHISQINV
* CODE
* COMBIN
* COMBINA
* COMPLEX
* CONCATENATE
* CONFIDENCENORM
* CONFIDENCET
* CONVERT
* CORREL
* COS
* COSH
* COT
* COTH
* COUNT
* COUNTA
* COUNTBLANK
* COUNTIF
* COUNTIFS
* COUNTIN
* COUNTUNIQUE
* COVARIANCEP
* COVARIANCES
* CSC
* CSCH
* CUMIPMT
* CUMPRINC
* DATE
* DATEVALUE
* DAY
* DAYS
* DAYS360
* DB
* DDB
* DEC2BIN
* DEC2HEX
* DEC2OCT
* DECIMAL
* DEGREES
* DELTA
* DEVSQ
* DOLLAR
* DOLLARDE
* DOLLARFR
* E
* EDATE
* EFFECT
* EOMONTH
* ERF
* ERFC
* EVEN
* EXACT
* EXPONDIST
* FALSE
* FDIST
* FINV
* FISHER
* FISHERINV
* IF
* INT
* ISEVEN
* ISODD
* LN
* LOG
* LOG10
* MAX
* MAXA
* MEDIAN
* MIN
* MINA
* MOD
* NOT
* ODD
* OR
* PI
* POWER
* ROUND
* ROUNDDOWN
* ROUNDUP
* SIN
* SINH
* SPLIT
* SQRT
* SQRTPI
* SUM
* SUMIF
* SUMIFS
* SUMPRODUCT
* SUMSQ
* SUMX2MY2
* SUMX2PY2
* SUMXMY2
* TAN
* TANH
* TRUE
* TRUNC
* XOR

# Table permissions

There are two cases in which a table will be locked for editing:

* If you do not have permission to edit a document (either the Experiment-Template or Experiment), the table will be display as read-only
* If the document is on print view, the table will be display as read only
