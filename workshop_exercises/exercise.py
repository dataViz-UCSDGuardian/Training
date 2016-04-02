#Lesson 5: Importing excel files

#Need the openpxl library
#openpyxl: library for handling .xlsx files only.
import openpyxl

wb = openpyxl.load_workbook('finance_and_giving.xlsx')

#Use the get_sheet_by_name command
sheet1 = wb.get_sheet_by_name("12.1.1") #UC_Total_03to15
sheet2 = wb.get_sheet_by_name("12.1.2") #UC_Ind_03to15

#Note-In excel, columns are letters A to Z, and rows are numbered
#Note-Value B4 refers to row 4 column 2
print( sheet1.cell(row=4,column=2).value ) #command 1
print( sheet1['B4'].value ) #command 2
