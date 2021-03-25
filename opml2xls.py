import opml 
import xlsxwriter

workbook = xlsxwriter.Workbook('rss.xlsx')
worksheet = workbook.add_worksheet()

outline = opml.parse('rss.opml')

arr = [[]]

for item in outline:
    title = item.title.replace(' on Medium', '').replace(' - Medium', '').replace('Stories by ', '')
    url = item.htmlUrl.split('?')[0]
    arr.append([title, url])

col = 0

for row, data in enumerate(arr):
    worksheet.write_row(row, col, data)

workbook.close()