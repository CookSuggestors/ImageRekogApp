import boto3
from googletrans import Translator
from dotenv import dotenv_values

class amazon_api:

    def call_api(self, img):
        env_info = dotenv_values(".env")
        AWS_ACCESS_KEY_ID = env_info['AWS_ACCESS_KEY_ID'] # AWSのアクセスキーID
        AWS_SECRET_ACCESS_KEY = env_info['AWS_SECRET_ACCESS_KEY'] # AWSのシークレットアクセスキー


        # Source = '/Users/Minami-Yuta/就活用/サマーインターンシップ/Optim/img/yasai.jpg'   # 検索対象となる画像を定義
        # imageSource = open(img,'rb').read()
        imageSource = img

        # Amazon Rekognitionインスタンスを作成
        rekognition = boto3.client('rekognition',
                aws_access_key_id=AWS_ACCESS_KEY_ID,
                aws_secret_access_key=AWS_SECRET_ACCESS_KEY ,
                region_name='ap-northeast-1'
        )

        response = rekognition.detect_labels(Image={'Bytes': imageSource}) # 画像認識を実行
        response_label_list = response['Labels'] # 出力ラベルを保持

        return response_label_list
    
    def output_label(self, response_label_list):
        response_label_list_len = len(response_label_list)


        translator = Translator() # 翻訳のためのインスタンス

        label_name_ja_list = [] # 画像処理後の食材ラベルのリスト

        for i in range(response_label_list_len):
            
            label_name_en = response_label_list[i]['Name'] # ラベル名（英語）
            label_name_ja = translator.translate(text=label_name_en, dest='ja', src='en').text # 英語->日本語に翻訳
            label_name_ja_list.append(label_name_ja) # リストに追加

        return label_name_ja_list

