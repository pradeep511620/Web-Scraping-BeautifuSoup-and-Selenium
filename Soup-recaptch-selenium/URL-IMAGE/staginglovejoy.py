import http.client

def exists(site, path):
    conn = http.client.HTTPConnection(site)
    conn.request('HEAD', path)
    response = conn.getresponse()
    conn.close()
    return response.status == 200
exists('//staging.raptorsupplies.com/pd/lovejoy/68514428875', 'https://cdn.raptorsupplies.com/pub/media/catalog/product/LOVEJOY-68514428875-GR0095623.JPG')