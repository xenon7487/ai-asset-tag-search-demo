import sys

ASSETS = [
    {'id': 'face-001', 'name': '清透少女脸', 'category': '脸', 'tags': ['少女', '清透', '圆脸']},
    {'id': 'pose-001', 'name': '自然站姿', 'category': '姿势', 'tags': ['站姿', '自然', '全身']},
    {'id': 'cloth-001', 'name': 'oversize 卫衣', 'category': '服装', 'tags': ['卫衣', '宽松', '休闲']},
    {'id': 'face-002', 'name': '港风成熟脸', 'category': '脸', 'tags': ['港风', '成熟', '方脸']},
]

def search(keyword):
    keyword = keyword.lower()
    results = []
    for asset in ASSETS:
        text = asset['name'] + ' ' + asset['category'] + ' ' + ' '.join(asset['tags'])
        if keyword in text.lower():
            results.append(asset)
    return results

def format_asset(asset):
    return asset['id'] + ' | ' + asset['name'] + ' | ' + asset['category'] + ' | ' + ', '.join(asset['tags'])

def main():
    args = sys.argv[1:]
    if not args:
        print('用法: python demo.py <关键词>')
        print('示例: python demo.py 圆脸')
        return
    keyword = args[0]
    results = search(keyword)
    if not results:
        print('未找到与 ' + keyword + ' 相关的素材')
        return
    print('找到 ' + str(len(results)) + ' 个与 ' + keyword + ' 相关的素材:')
    for asset in results:
        print(format_asset(asset))

if __name__ == '__main__':
    main()