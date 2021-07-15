lis=[]
lis1=[]
with open('line.txt') as f:
    flag=True
    for text in f.readlines():
        text=text.lstrip().rstrip().lower()
        if flag:
            text=text.upper()
            lis1.append(text)
            flag=False
            continue
        words=[word for word in text.split(' ') if not word in ['an','a','the','new'] ]
        name='_'.join(words)
        name+=".go"
        lis.append(name)
        flag=True
for name in sorted(lis):
  print(name)
print("\n\n\n")
lis2=[]
for text in lis:
    arr=text.split('_')
    arr[-1]=arr[-1].split('.')[0]
    arr=[ word.capitalize() for word in arr]
    name=''.join(arr)
    lis2.append(name)
for name in sorted(lis2):
  print(name)

import os

directory_name="ldap_servers"
id="ldapserverId"
baseUrl="/ldapservers"


parameters_string=""
directory_path="P:/VS/go/thinklink/jumpcloud-sdk-go/"+directory_name
try:
    os.mkdir(directory_path)
except:
    print("folder already there!")

for method,filename,funcname in zip(lis1,lis,lis2):
    path=os.path.join(directory_path,filename)
    arguments=""
    requestURL=f"requestURL := fmt.Sprintf(\"{baseUrl}/%s\", {id})"
    if method != "POST":
        arguments+=id +" string"
    else:
        requestURL="requestURL := \""+baseUrl+"\""
    if method in ["POST","PUT","PATCH"]:
        if arguments!= "":
            arguments+=", "
        arguments+="parameters map[string]interface{}"
        parameters_string="""
            Parameters: parameters,"""
    with open(path,'w+') as f:
        f.write(f"""package {directory_name}
import (
	jumpcloudsdk "bitbucket.org/thinklinkio/jumpcloud-sdk-go"
	"fmt"
)

// {funcname} : 
func {funcname}({arguments}) (*jumpcloudsdk.ResponseData, error) {{
	// Execute http request
	{requestURL}
	response, err := jumpcloudsdk.ExecRequest(
		&jumpcloudsdk.RequestData{{
			Method:        \"{method}\",
			RelativeURL:   requestURL,{parameters_string}
        }},
	)
	if err != nil {{
		return nil, err
	}}

	return response, nil
}}""")   