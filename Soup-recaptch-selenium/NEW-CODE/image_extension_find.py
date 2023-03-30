import requests
import mimetypes

response = requests.get('https://assets.southwire.com/ImConvServlet/imconv/df15d8d573c43b05b277dee8ae8af54d790ba411/01200Wx1200H?use=productpictures&assetDescr=1-C%20CU%202.4kv%20EPR%20SIMpull%20PVC%20MV-90')
content_type = response.headers['content-type']
extension = mimetypes.guess_extension(content_type)
print(extension)