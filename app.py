#download required packages
!pip install ghostscript
!apt install ghostscript python3-tk
!pip install camelot-py

from camelot import read_pdf
pdf_path = "/content/Fractal Analytics_FY22.pdf"
# Get all the tables within the file
all_tables = read_pdf(pdf_path, pages = 'all')
my_list = []
for i in range(0,len(all_tables)):
  v=all_tables[i].df[0].apply(str).str.contains("Revenue from operations")
  for j in range(0,len(v)):
    if v[j]:
      my_list.append(i)
  v1=all_tables[i].df[0].apply(str).str.contains("Current Tax")
  for j1 in range(0,len(v1)):
    if v[j1]:
      my_list.append(i)
my_list_without_duplicates = list(set(my_list))
for item in my_list_without_duplicates:
  filename = f'table_{item}.csv'
  all_tables[item].to_csv(filename, index=False)
