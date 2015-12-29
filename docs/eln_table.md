# Table

Labii ELN supports Excel-like table functionality. A table can be edited in both Experiment-Templates and Experiment documents. Labii ELN tables also support formulas for simple calculations, see list of available formulas below.

# Overview

![labii-eln-table-overview](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-overview.png)

Labii ELN supports two types of table views: edit view (picture above), and read-only view (picture bellow).

For edit view, one additional column (header) and row are included. All other cells work exactly like in Excel. Each cell also supports a right-click menu. 

The format of each indicating:

* Black font color: editable cell
* Gray font color: read only cell
* Yellow background: formula

![labii-eln-table-overview-readonly](https://labiiblog.files.wordpress.com/2015/12/labii-eln-table-overview-readonly.png)

A read-only table does not contain headers and cell content cannot been changed like in the picture above. 

# Insert a table

A table is inserted within the editor. Quickly insert a table by highlighting required columns and rows after clicking the table icon, or from the advanced table property by clicking the table icon and then "More".

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

Editing a table is just like in Excel; select a cell, type in any value, and the table will be automatically updated.

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

### Calculation with other cells

Type "=" and use a cell’s column id and row id to represent a number or text. For example, the cell in row 1 and column A, can be referred to as "A1". To multiple a number in A1 by 5, type "=A1*5".

### [List of supported formulas](http://handsontable.github.io/ruleJS/)

| | | | | |
|:------|:------|:------|:------|:------|
| ABS| BINOMINV| COUNTIF| EDATE| OR|
| ACCRINT| BITAND| COUNTIFS| EFFECT| PI|
| ACOS| BITLSHIFT| COUNTIN| EOMONTH| POWER|
| ACOSH| BITOR| COUNTUNIQUE| ERF| ROUND|
| ACOTH| BITRSHIFT| COVARIANCEP| ERFC| ROUNDDOWN|
| AND| BITXOR| COVARIANCES| EVEN| ROUNDUP|
| ARABIC| CEILING| CSC| EXACT| SIN|
| ASIN| CEILINGMATH| CSCH| EXPONDIST| SINH|
| ASINH| CEILINGPRECISE| CUMIPMT| FALSE| SPLIT|
| ATAN| CHAR| CUMPRINC| FDIST| SQRT|
| ATAN2| CHISQDIST| DATE| FINV| SQRTPI|
| ATANH| CHISQINV| DATEVALUE| FISHER| SUM|
| AVEDEV| CODE| DAY| FISHERINV| SUMIF|
| AVERAGE| COMBIN| DAYS| IF| SUMIFS|
| AVERAGEA| COMBINA| DAYS360| INT| SUMPRODUCT|
| AVERAGEIF| COMPLEX| DB| ISEVEN| SUMSQ|
| BASE| CONCATENATE| DDB| ISODD| SUMX2MY2|
| BESSELI| CONFIDENCENORM| DEC2BIN| LN| SUMX2PY2|
| BESSELJ| CONFIDENCET| DEC2HEX| LOG| SUMXMY2|
| BESSELK| CONVERT| DEC2OCT| LOG10| TAN|
| BESSELY| CORREL| DECIMAL| MAX| TANH|
| BETADIST| COS| DEGREES| MAXA| TRUE|
| BETAINV| COSH| DELTA| MEDIAN| TRUNC|
| BIN2DEC| COT| DEVSQ| MIN| XOR|
| BIN2HEX| COTH| DOLLAR| MINA||
| BIN2OCT| COUNT| DOLLARDE| MOD||
| BINOMDIST| COUNTA| DOLLARFR| NOT||
| BINOMDISTRANGE| COUNTBLANK| E| ODD||

# Table permissions

There are two cases in which a table will be locked for editing:

* If you do not have permission to edit a document (either the Experiment-Template or Experiment), the table will be display as read-only
* If the document is on print view, the table will be display as read only
