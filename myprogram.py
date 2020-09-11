import json
import os
from miner_text_generator import extract_text_by_page
def export_as_json(pdf_path, json_path):
    filename=os.path.splitext(os.path.basename(pdf_path))[0]
    data={}
    for line in extract_text_by_page(pdf_path):
            command,description=line.strip().split(None, 1)
            data[command]=description.strip()
    out_file = open(json_path,'w')
    json.dump(data, out_file)
if __name__ == '__main__':
    pdf_path = 'Interview_sample_data.pdf'
    json_path = 'sample_data.json'
    export_as_json(pdf_path, json_path)