![Blddata](68k_blddata/sample.png "Blddata")
       
|Command Summary|Command Syntax|[Calculator Compatibility](68k:cross-compatibility.html)|[Token Size](6k:tokenization.html)|
|--- |--- |--- |--- |
|Creates data variable dataVar based on the information used to plot the current graph.|BldData [*dataVar*]|This command works on all calculators.|? byte(s)|
       
### Menu Location
This command is only available from the CATALOG
# Blddata

Creates data variable *dataVar* based on the information used to plot the current graph. If dataVar is omitted, the data is stored in the
system variable sysData.

the increment for the independent value (ex. x for function or θ for polar graphs) is calculated based off the window settings. 

for 3D graphs, x remains constant until y increments through its range, this continues until x increments through its range.

When the Data/Matrix editor is started for the first time after BldData is run, *dataVar* or *sysData* will be the active variable.

## Related Commands

- Command 1
- Command 2
- Command 3 

## See Also

- Design Concept 1
- Design Concept 2
- Technique 1
