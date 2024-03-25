import requests
import json

# 读取输入文件，按行分隔
with open('input.txt', 'r', encoding='utf-8') as input_file:
    input_lines = input_file.readlines()

output_lines = []

# 分行处理文本
for line in input_lines:
    payload = json.dumps([{"src": line}])
    headers = {'Content-Type': 'application/json'}
    url = "https://punct.gj.cool/punct/test"
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    processed_line = response.text.strip()  # 去除处理结果的空白字符
    output_lines.append(processed_line)

# 将处理后的文本按行写入输出文件，保留输入文件的格式
with open('output.txt', 'w', encoding='utf-8-sig') as output_file:
    output_file.writelines(output_lines)

print("Done")
