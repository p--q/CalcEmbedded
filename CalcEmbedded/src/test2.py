#!/opt/libreoffice5.2/program/python
# -*- coding: utf-8 -*-
def main():
    doc = XSCRIPTCONTEXT.getDocument()
    if doc.supportsService("com.sun.star.sheet.SpreadsheetDocument"):
        sheets = doc.getSheets()
        sheet = sheets.getByIndex(0)
        cellrange = sheet.getCellRangeByPosition(0, 0, 2, 5)
        cellrange.getCellByPosition(0, 0).setString(u'みかん')
        cellrange.getCellByPosition(1, 0).setString(u'りんご')
        subrange = cellrange.getCellRangeByPosition(0, 1, 2, 5)
        rangeAddress = subrange.RangeAddress
        for i in range(rangeAddress.EndRow - rangeAddress.StartRow):
            for j in range(rangeAddress.EndColumn - rangeAddress.StartColumn):
                subrange.getCellByPosition(j, i).setValue((i + 1) * (j + 2))
if __name__ == "__main__":
    import sys
    import unopy
    XSCRIPTCONTEXT = unopy.connect()
    if not XSCRIPTCONTEXT:
        print("Failed to connect.")
        sys.exit(0)
    sys.exit(main())