# Table

Labii ELN supports Excel-like table functionality. A table can be edited in both Experiment-Templates and Experiment documents. Labii ELN tables also support formulas for simple calculations, see list of available formulas below.

# Overview

![labii-eln-table-overview](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-overview.png)

Labii ELN supports two types of table views: edit view (picture above), and read-only view.

For editable view, one additional column serves as header and one addtioanl row is included. All other cells works exactly like Excel. Each cell also support a right click menu.

* Black font color: editable cell
* Gray font folor: read only cell
* Yellow background: formula

![labii-eln-table-overview-readonly](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-overview-readonly.png)

A read only table does not have any headers and the cell content can not been changed. See the picture above.

# Insert a table

A table can only been inserted within the editor. A table can be quickly inserted by either selelction required columns and rows or from advanced table property.

## Insert a table by selection of cells

![labii-eln-table-insert](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-insert.png)

* Click table icon from editor
* Select number of columns and rows
* A new table will be inserted into your document.

## Insert a table from advanced table properties

![labii-eln-table-insert-advanced](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-insert-advanced.png)

* Click table icon from editor
* Click more
* Fill in number of rows and columns, as well as other information
* Click OK
* A new table will be inserted into your document.

# Edit a table

To edit a table is as simple as using Excel. Just select a cell and type in any value, the table will be automatically updated.

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
Labii ELN table use same formula function in Excel. For example, to calculate 2 + 1, just type in "=2+1". Please see next section for more details.

# Table formula
### Numeric calculation
Type "=" and follow with formula, for example "=10/5"
### Caculation with other cells
Type "=" and use cell column id and row id to represent a number or text. For example, the cell on the row 1 and column A can be referred as "A1". For example, to multiple a number in A1 with number 5, you can do "=A1*5"
### [List of supported formulas](http://handsontable.github.io/ruleJS/)
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

In many cases, a table will be locked for editing.

* If you do not have permission to edit a document (either the Experiment-template or Experiment), the table will be display as read only;
* If the document is on print view, the table will be display as read only;
