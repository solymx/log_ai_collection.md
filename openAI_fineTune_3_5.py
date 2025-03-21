## pip install openai

"""
###### merge data

import os
import json

# 設定要合併的檔案列表
jsonl_files = [
    "100_sqli_finetune_dataset.jsonl",
    "100_normal_sql_finetune_dataset.jsonl",
    "50_xss_finetune_dataset.jsonl",
    "100_xss_normal_finetune_dataset.jsonl",
    "100_command_injection_finetune_dataset.jsonl",
    "100_normal_command_injection_dataset.jsonl",
    "100_ssrf_finetune_dataset.jsonl",
    "100_normal_ssrf_finetune_dataset.jsonl"
]

output_file = "merged_finetune_dataset.jsonl"

# 開啟輸出檔案，將所有內容合併
with open(output_file, 'w', encoding='utf-8') as outfile:
    for fname in jsonl_files:
        try:
            with open(fname, 'r', encoding='utf-8') as infile:
                for line in infile:
                    outfile.write(line)  # 直接寫入新檔案
        except Exception as e:
            print(f"❌ 無法讀取 {fname}: {e}")

print(f"✅ 合併完成，已儲存為 {output_file}")
"""

## upload jsonl
```
import openai

openai.api_key = "你的_OPENAI_API_KEY"

# 直接使用新版 API 來上傳檔案
upload_response = openai.files.create(
    file=open("merged_finetune_dataset.jsonl", "rb"),
    purpose="fine-tune"
)

file_id = upload_response.id  # 取得 file_id
print(f"✅ 檔案上傳成功，file_id: {file_id}")
```

## fine tune GPT-3.5
```
fine_tune_response = openai.fine_tuning.jobs.create(
    training_file=file_id,  # 你的上傳檔案 ID
    model="gpt-3.5-turbo",  # 目前只支援 GPT-3.5 Turbo
    suffix="web-log-detector"  # 可選：自訂模型名稱
)

print(f"🚀 Fine-tune 啟動成功！Job ID: {fine_tune_response.id}")
```

看進度： https://platform.openai.com/finetune
