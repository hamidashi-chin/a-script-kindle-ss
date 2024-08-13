from PIL import Image
import os

def convert_pngs_to_pdf(input_dir, output_pdf_path):
    # ディレクトリ内の全てのPNGファイルを取得
    png_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]
    png_files.sort()  # ファイル名順にソート
    
    # 画像リストを作成
    images = []
    for file in png_files:
        img_path = os.path.join(input_dir, file)
        img = Image.open(img_path)
        # PNGは通常RGBAモード（透過ピクセルを含む）ですが、PDFではRGBが必要
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        images.append(img)

    # 最初の画像をベースにPDFとして保存し、他の画像を追加
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

# 実行部分
input_dir = '/Users/takafumitakehara/tmp/capture1'  # PNGファイルが格納されているディレクトリのパス
output_pdf_path = './file1.pdf'  # 出力PDFファイルのパス
#output_pdf_path = '/Users/takafumitakehara/tmp/pdf/file.pdf'  # 出力PDFファイルのパス

convert_pngs_to_pdf(input_dir, output_pdf_path)

print(f"PDFファイルが {output_pdf_path} に保存されました。")




# from PIL import Image
# import os

# # PNGファイルが格納されているディレクトリのパス
# input_dir = '~/tmp/capture'
# # 出力PDFファイルのパス
# output_pdf_path = '~/tmp/pdf/file.pdf'

# # ディレクトリ内の全てのPNGファイルを取得
# png_files = [f for f in os.listdir(input_dir) if f.endswith('.png')]
# png_files.sort()  # ファイル名順にソート

# # PNGファイルを開いて、リストに追加
# images = []
# for file in png_files:
#     img_path = os.path.join(input_dir, file)
#     img = Image.open(img_path)
#     # すべての画像をRGBモードに変換
#     if img.mode == 'RGBA':
#         img = img.convert('RGB')
#     images.append(img)

# # 画像を1つのPDFとして保存
# if images:
#     images[0].save(output_pdf_path, save_all=True, append_images=images[1:])

# print(f"PDFファイルが {output_pdf_path} に保存されました。")
