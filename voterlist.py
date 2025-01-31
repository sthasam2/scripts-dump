import requests

headers = {
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.7",
    "Connection": "keep-alive",
    "Referer": "https://election.gov.np/np/page/voter-list-db",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-GPC": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36",
    "access-control-allow-origin": "*",
}

params = {
    "lang": "en",
}

response = requests.get(
    "https://election.gov.np/admin/public/api/page/voter-list-db",
    params=params,
    headers=headers,
)

print("done")


"""
'{"success":true,"message":"","data":{"id":93,"parent_id":null,"author_id":1,"created_at":"2022-03-02T11:25:13.000000Z","updated_at":"2022-09-16T09:16:13.000000Z","slug":"voter-list-db","thumbnail":null,"branch_id":null,"status":"active","title":"Voter Roll","body":"<h3 style=\\"text-align: center;\\"><span style=\\"color: #236fa1;\\">\\u0905\\u0928\\u094d\\u0924\\u093f\\u092e \\u092e\\u0924\\u0926\\u093e\\u0924\\u093e \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940<\\/span><\\/h3>\\r\\n<h3 style=\\"text-align: center;\\"><span style=\\"color: #236fa1;\\">\\u0968\\u0966\\u096d\\u096f \\u092c\\u0948\\u0936\\u093e\\u0916 \\u0968\\u096f \\u0917\\u0924\\u0947 \\u0938\\u092e\\u094d\\u092e \\u0967\\u096e \\u0935\\u0930\\u094d\\u0937 \\u0909\\u092e\\u0947\\u0930 \\u092a\\u0941\\u0930\\u093e \\u092d\\u090f\\u0915\\u093e \\u092e\\u0924\\u0926\\u093e\\u0924\\u093e\\u0915\\u094b \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940&nbsp;<\\/span><\\/h3>\\r\\n<p style=\\"font-size: medium; font-weight: 400; text-align: start;\\"><iframe style=\\"width: 1512px; height: 810px;\\" src=\\"https:\\/\\/voterlist.election.gov.np\\/bbvrs1\\/index_2.php\\" name=\\"bbvrs\\" frameborder=\\"0\\">Browser does not support IFRAME<\\/iframe><\\/p>\\r\\n<!-- <p style=\\"font-size: medium; font-weight: 400; text-align: start;\\"><img title=\\"Free Counter\\" src=\\"https:\\/\\/hitwebcounter.com\\/counter\\/counter.php?page=7954791&amp;style=0007&amp;nbdigits=7&amp;type=ip&amp;initCount=0\\" alt=\\"web counter\\" border=\\"0\\" \\/><\\/p> !>-->","translations":[{"id":167,"title":"Voter Roll","body":"<h3 style=\\"text-align: center;\\"><span style=\\"color: #236fa1;\\">\\u0905\\u0928\\u094d\\u0924\\u093f\\u092e \\u092e\\u0924\\u0926\\u093e\\u0924\\u093e \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940<\\/span><\\/h3>\\r\\n<h3 style=\\"text-align: center;\\"><span style=\\"color: #236fa1;\\">\\u0968\\u0966\\u096d\\u096f \\u092c\\u0948\\u0936\\u093e\\u0916 \\u0968\\u096f \\u0917\\u0924\\u0947 \\u0938\\u092e\\u094d\\u092e \\u0967\\u096e \\u0935\\u0930\\u094d\\u0937 \\u0909\\u092e\\u0947\\u0930 \\u092a\\u0941\\u0930\\u093e \\u092d\\u090f\\u0915\\u093e \\u092e\\u0924\\u0926\\u093e\\u0924\\u093e\\u0915\\u094b \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940&nbsp;<\\/span><\\/h3>\\r\\n<p style=\\"font-size: medium; font-weight: 400; text-align: start;\\"><iframe style=\\"width: 1512px; height: 810px;\\" src=\\"https:\\/\\/voterlist.election.gov.np\\/bbvrs1\\/index_2.php\\" name=\\"bbvrs\\" frameborder=\\"0\\">Browser does not support IFRAME<\\/iframe><\\/p>\\r\\n<!-- <p style=\\"font-size: medium; font-weight: 400; text-align: start;\\"><img title=\\"Free Counter\\" src=\\"https:\\/\\/hitwebcounter.com\\/counter\\/counter.php?page=7954791&amp;style=0007&amp;nbdigits=7&amp;type=ip&amp;initCount=0\\" alt=\\"web counter\\" border=\\"0\\" \\/><\\/p> !>-->","page_id":93,"locale":"en"},{"id":166,"title":"\\u0905\\u0928\\u094d\\u0924\\u093f\\u092e  \\u092e\\u0924\\u0926\\u093e\\u0924\\u093e \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940","body":"<h2 style=\\"text-align: center;\\"><span style=\\"color: #ef0909;\\"><strong>\\u092e\\u0924\\u0926\\u093e\\u0924\\u093e \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940&nbsp;<\\/strong><\\/span><\\/h2>\\r\\n<h3 style=\\"text-align: center;\\"><span style=\\"color: #0a37ff;\\"><strong>\\u0968\\u0966\\u096d\\u096f \\u092e\\u0902\\u0938\\u093f\\u0930 \\u0969 \\u0917\\u0924\\u0947 \\u0938\\u092e\\u094d\\u092e \\u0967\\u096e \\u0935\\u0930\\u094d\\u0937 \\u0909\\u092e\\u0947\\u0930 \\u092a\\u0941\\u0930\\u093e \\u092d\\u090f\\u0915\\u093e \\u092e\\u0924\\u0926\\u093e\\u0924\\u093e\\u0915\\u094b \\u0928\\u093e\\u092e\\u093e\\u0935\\u0932\\u0940&nbsp;<\\/strong><\\/span><\\/h3>\\r\\n<p><iframe style=\\"width: 1512px; height: 810px;\\" src=\\"https:\\/\\/voterlist.election.gov.np\\/bbvrs1\\/index_2.php\\" name=\\"bbvrs\\" frameborder=\\"0\\">Browser does not support IFRAME<\\/iframe><\\/p>\\r\\n<p style=\\"font-size: medium; font-weight: 400;\\"><img title=\\"Free Counter\\" src=\\"https:\\/\\/hitwebcounter.com\\/counter\\/counter.php?page=7954791&amp;style=0007&amp;nbdigits=7&amp;type=ip&amp;initCount=0\\" alt=\\"web counter\\" border=\\"0\\" \\/><\\/p>","page_id":93,"locale":"np"}]}}'
"""
