import boto3
from googletrans import Translator
from dotenv import dotenv_values

env_info = dotenv_values(".env")
AWS_ACCESS_KEY_ID = env_info['AWS_ACCESS_KEY_ID'] # AWSのアクセスキーID
AWS_SECRET_ACCESS_KEY = env_info['AWS_SECRET_ACCESS_KEY'] # AWSのシークレットアクセスキー


Source = '/Users/Minami-Yuta/就活用/サマーインターンシップ/Optim/img/yasai.jpg'   # 検索対象となる画像を定義
imageSource = open(Source,'rb').read()

rekognition = boto3.client('rekognition',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY ,
        region_name='ap-northeast-1'
)

response = rekognition.detect_labels(Image={'Bytes': imageSource})
response_label_list = response['Labels']
response_label_list_len = len(response_label_list)


translator = Translator() # 翻訳のためのインスタンス

label_name_ja_list = [] # 画像処理後の食材ラベルのリスト

for i in range(response_label_list_len):
    
    label_name_en = response['Labels'][i]['Name'] # ラベル名（英語）
    label_name_ja = translator.translate(text=label_name_en, dest='ja', src='en').text # 英語->日本語に翻訳
    label_name_ja_list.append(label_name_ja) # リストに追加

print(label_name_ja_list)

