from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import time
import logging

app = Flask(__name__)
CORS(app)

INDEX_FILE = 'pi_birthday_index.pkl'
INDEX = {}

# 初始化全局 logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# 加载索引
def load_index():
    global INDEX
    with open(INDEX_FILE, 'rb') as f:
        INDEX = pickle.load(f)
    logger.info(f"索引加载完成，包含 {len(INDEX)} 个生日")
    # 验证 "19821203"
    if "19821203" in INDEX:
        logger.info(f"加载后找到 19821203: {INDEX['19821203']}")
    else:
        logger.info("加载后未找到 19821203")

# 在模块加载时执行
logger.info("开始加载索引...")
load_index()

@app.route('/search_pi', methods=['POST'])
def search_pi():
    data = request.get_json()
    birthday = data.get('birthday')
    logger.info(f"接收到的 birthday: '{birthday}' (类型: {type(birthday)})")
    if not birthday or not birthday.isdigit() or len(birthday) != 8:
        return jsonify({'position': -1, 'before': '', 'after': '', 'error': '无效的生日格式'})
    start_time = time.time()
    result = INDEX.get(birthday, {"position": -1, "before": "", "after": ""})
    position = result["position"]
    before = result["before"]
    after = result["after"]
    search_time = time.time() - start_time
    logger.info(f"搜索 {birthday}，位置: {position}，耗时: {search_time} 秒")
    return jsonify({'position': position, 'before': before, 'after': after, 'search_time': search_time})

if __name__ == '__main__':
    app.run(host='192.168.11.10', port=5000, debug=False)