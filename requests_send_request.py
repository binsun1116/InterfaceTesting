import requests

httpbin_get = requests.get('http://httpbin.org/get', data={'key':'value'})
print('httpbin_get:', httpbin_get.text)

httpbin_post = requests.post('http://httpbin.org/post', data={'key':'value'})
print('httpbin_post:', httpbin_post.text)

httpbin_put = requests.put('http://httpbin.org/put', data={'key':'value'})
print('httpbin_put:', httpbin_put.text)

httpbin_delete = requests.delete('http://httpbin.org/delete', data={'key':'value'})
print('httpbin_delete:', httpbin_delete)

httpbin_patch = requests.patch('https://httpbin.org/patch', data={'key': 'value'})
print('httpbin_patch', httpbin_patch)