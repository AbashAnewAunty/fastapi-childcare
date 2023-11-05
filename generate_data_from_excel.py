import pandas as pd

def extract_and_write_to_txt():
    try:
        # 使用例
        excel_file_path = 'dataset/dataset_childcare.xlsx'  # 実際のファイルパスに置き換えてください
        output_txt_file_path = 'data/output.txt'  # 書き込むtxtファイルのパス

        output = ""

        # Excelファイルからデータを読み込む
        df = pd.read_excel(excel_file_path)
        

        for i in range(600):
            data_1st_col = df.iloc[i - 1, 1]
            data_2nd_col = df.iloc[i - 1, 2]
            output += f"質問:{data_1st_col}\n"  
            output += f"回答:{data_2nd_col}\n"
            output += "--------------------------------------\n"
        
        # txtファイルに書き込む
        with open(output_txt_file_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(output)

    except Exception as e:
        print(f"エラー: {e}")



# n行目のデータを取得してtxtファイルに書き込む
print("start")
extract_and_write_to_txt()
print("complete")
