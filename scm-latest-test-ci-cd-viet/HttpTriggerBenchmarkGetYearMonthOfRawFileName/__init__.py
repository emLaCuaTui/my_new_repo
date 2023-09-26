import logging

import azure.functions as func
#Sep 26 6:57

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    request_body = req.get_json()
    name = request_body.get('raw_file_name')
    


    if name[4:5]=='0':
        month = int(name[5:6])
    else:
        month=int(name[4:6])
    if month>=5:
        year_folder = 'FY'+name[0:4]
    else:
        year = int(name[0:4])-1
        year_folder = 'FY'+str(year)
    
    
    return func.HttpResponse(
            year_folder,
            status_code=200
    )
