import requests
import pdfkit
import unicodedata
import re
headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'http://172.31.1.204/jaf_list/',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6',
    #'Cookie': 'csrftoken=De0QEz4hmuMURXrmgc00xsBmRbSlAqRLcAGyGhpjYFyOsHWnaFvnaakvhae7RmZy; sessionid=9luz11iogbcyaziw9lxzkgg0g994yr5wftoken=XtykxtUxRjIHM6BLyfjmMZRUteQefT2EZK5WgEwa7u57GQx8oUSY0hZSDBXy8mHI; sessionid=d0poan0jpn9zr9rmekwh2cz6hsr9pb0q'
    'Cookie': 'csrftoken=1ONdRKoIez1rT7Y4L27sGWR3t8FpT8WyGZ6A328PfsNununW3R92M7hecnxAGfPo; sessionid=yxkim0yp5qvcmv1wg4qbydd4z59donif'
}

for i in range(1,800):
    url = 'http://172.31.1.202/jaf_view/'+str(i)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        #print(response.status_code)
        temp = response.text
        c1 = '<table class="table table-centered table-reponsive table-striped table-bordered table-hover">'
        c2 = '</table>\n</div>'
        com = '<td> Company :</td>'
        i1 = temp.find(c1)
        i2 = temp.find(c2)
        com_index = temp.find(com)
        temp_com = temp[com_index+19:]
        end = '</td>'
        start = '<td>'
        end_index = temp_com.find(end)
        start_index = temp_com.find(start)
        Company = temp_com[start_index+5:end_index]
        if start_index == -1:
            continue
        desg = '<td> Designation : </td>'
        desg_index = temp.find(desg)
        temp_des = temp[desg_index+24:]
        end = '</td>'
        start = '<td>'
        end_index = temp_des.find(end)
        start_index = temp_des.find(start)
        if start_index == -1:
            continue
        Designation = temp_des[start_index+5:end_index]
        temp = temp[i1:i2+16]
        Company = unicodedata.normalize('NFKD', Company).encode('ascii', 'ignore')
        Company = unicode(re.sub('[^\w\s-]', '', Company).strip().lower())
        Company = unicode(re.sub('[-\s]+', '-', Company))
        Designation = unicodedata.normalize('NFKD', Designation).encode('ascii', 'ignore')
        Designation = unicode(re.sub('[^\w\s-]', '', Designation).strip().lower())
        Designation = unicode(re.sub('[-\s]+', '-', Designation))
        filename = Company+"_"+Designation+".html"
        outfile = Company+"_"+Designation+".pdf"
        temp = temp.encode('utf8')
        with open(filename, "w+") as f:
            f.write(temp)
        pdfkit.from_file(filename, outfile) 
