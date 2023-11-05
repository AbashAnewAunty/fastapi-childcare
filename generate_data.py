# 学習データの書式に変換
input = "dataset/dataset_childcare.csv"
output = ""
with open(input, "r") as file:
    for line in file:
        strs = line.split(",")
        if len(strs) < 3:
            continue

        if strs[2][0] == '"':
            strs[2] = strs[2][1:]

        strs[2] = strs[2].replace("\n", "")
        # output += '{"messages": [{"role": "system", "content": "あなたは市役所に勤める勤勉な２０代女性です。"}, {"role": "user", "content": "'+strs[1]+'"}, {"role": "assistant", "content": "'+strs[2]+'"}]}\n'
        output += f'質問: {strs[1]}\n'
        output += f'回答: {strs[2]}\n'
        output += '------------------------------\n'

# 学習データの保存
with open("data/output_childcare.txt", "w") as file:
    file.write(output)