import os
import openai
import csv

# 请在这里设置调用 OpenAI API 的凭证
openai.api_key = ''
openai.api_base = ''
openai.api_type = ''
openai.api_version = '' 

# 打开输入CSV文件
input_csv_file = "input.csv"
output_csv_file = "output.csv"

# 打开输出CSV文件以写入结果
output_csv = open(output_csv_file, 'w', newline='', encoding='utf-8-sig')
output_csv_writer = csv.writer(output_csv)
output_csv_writer.writerow(['note_id', '景观名称', '对景观的具体描述'])

if api_key:
    # 在这里使用你的 API 密钥进行 OpenAI API 请求
    # 例如，设置 OpenAI API 密钥
    import openai
    openai.api_key = api_key

    # 执行 OpenAI 相关的操作
    # ...
else:
    print("没有找到 API 密钥，请确保环境变量已设置")

# 读取CSV文件
with open(input_csv_file, 'r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        note_id = row['note_id']
        text = row['text']

        # 使用OpenAI API创建对话
        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"请识别文本中的以下信息：(1)原文中的景观、景物或风景名称；(2)原文中的相应描述。将结果并以表格的形式返回。原文如下：\n"}]
        )
#解析+整理回答
def main():
    with open(result_file, "a", encoding="utf-8-sig") as f:
        writer = csv.writer(f)
        title = ["note_id", "text"]
        title = title + columns
        writer.writerow(title)
    with open(csv_file, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        next(reader)
        for line in reader:
            id = line[0]
            text = line[1]
            response = get_response(key, question, text, answer)
            response_text = response["choices"][0].message.content
            response_text = bytes(response_text, encoding="utf-8-sig").decode()
            response_text = response_text.replace(" | ", ",")
            response_text = response_text.replace("|", "")
            response_lists = response_text.split("\n")
            for i in response_lists:
                i = i.strip()
                i = i.split(",")
                i.insert(0, id)
                i.insert(1, text)
                print(id)
                print(i)
                with open(result_file, "a", encoding="utf-8-sig", newline="") as r:
                    writer = csv.writer(r)
                    writer.writerow(i)

print("处理完成并结果已保存到output.csv文件。")
