import requests
import json
import time

# 定义一个函数来处理文本
def process_text(text):
    payload = json.dumps([{"src": text}])
    headers = {'Content-Type': 'application/json'}
    url = "https://punct.gj.cool/punct/test"
    
    max_retries = 3  # 最大重试次数
    retries = 0
    
    while retries < max_retries:
        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            return response.text.strip('" \n')
        except Exception as e:
            print(f"Error processing text: {str(e)}")
            retries += 1
            time.sleep(5)  # 增加到5秒的重试间隔
    
    print(f"Failed to process text after {max_retries} retries")
    return text

with open('input.txt', 'r', encoding='utf-8-sig') as input_file:
    input_lines = input_file.readlines()

output_lines = []

for line in input_lines:
    columns = line.strip('\n').split('\t')
    
    if len(columns) < 4:
        continue
    
    text = columns[3]
    processed_text = process_text(text)
    output_line = '\t'.join(columns[:3] + [processed_text]) + '\n'
    output_lines.append(output_line)

with open('output.txt', 'w', encoding='utf-8-sig') as output_file:
    output_file.writelines(output_lines)

print("Done")
