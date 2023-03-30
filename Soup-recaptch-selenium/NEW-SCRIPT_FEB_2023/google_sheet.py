import pygsheets

gc = pygsheets.authorize(service_file='C:/Users/hp/Downloads/raptorsupplies-375206-fb9368933801.json')
lst = gc.drive.list(q="mimeType='application/vnd.google-apps.spreadsheet'", fields="files(name, parents), nextPageToken, incompleteSearch")

# Create empty dataframe
# df = pd.DataFrame()
#
# # Create a column
# df['name'] = ['John', 'Steve', 'Sarah']
#
# #open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('rahul')
wks = sh[0]
wks_data = wks.get_all_values()
wks_data = [list(filter(None, lst)) for lst in wks_data]
wks_data = [ele for ele in wks_data if ele != []]
print(wks_data)
num_rows = len(wks_data)
wks.insert_rows(num_rows, values=['1','rahul'], inherit=False)
#
# #update the first sheet with df, starting at cell B2.
# wks.set_dataframe(df,(1,1))