import os
import hashlib
import random
import hmac
from wechat_xiaowei.exception import WeChatException


class BaseWeChat:
    # 请求根地址
    WX_API_HOST = 'https://api.mch.weixin.qq.com/'

    # 根目录
    ROOT_DIR = os.path.dirname(__file__)

    def __init__(self, wechat_config: dict):
        # 服务商商户号
        self.mch_id = wechat_config.get('mch_id')
        # 商户证书序列号
        self.serial_no = wechat_config.get('serial_no')
        # 加密秘钥
        self.aes_key = wechat_config.get('aes_key')
        # 商户自定义key
        self.diy_key = wechat_config.get('diy_key')
        # app_id
        self.app_id = wechat_config.get('app_id')
        # secret_key
        self.secret_key = wechat_config.get('secret_key')
        # 私钥地址
        self.private_key_addr = f'{self.ROOT_DIR}/Certificate/apiclient_key.pem'
        # 公钥地址
        self.ssl_cert_addr = f'{self.ROOT_DIR}/Certificate/apiclient_cert.pem'
        # 最新的证书完整响应体存放位置
        self.new_response_data_addr = f'{self.ROOT_DIR}/Certificate/jiemi.json'
        # 解密后证书地址
        self.public_key_addr = f'{self.ROOT_DIR}/Certificate/jiemi.pem'

    def http_request(self, url: dict, data='', headers=None, use_cert=False, timeout=30):
        if not headers:
            headers = []

    @staticmethod
    def dict2xml(params: dict):
        """
        字典对象转为xml
        :param params:
        :return:
        """
        if not params:
            raise WeChatException(30001)

        xml = '<xml>'
        for k, v in params.items():
            if str(v).isdigit():
                xml += f'<{k}>{v}</{k}>'
            else:
                xml += f'<{k}><![CDATA[{v}]]></{k}>'
        xml += '</xml>'
        return xml

    def download_certificates(self):
        """
        下载证书
        :return:
        """
        data = {
            'mch_id': self.mch_id,
            'nonce_str': self.get_random_char(),
            'sign_type': 'HMAC-SHA256',
            'sign': ''
        }

    @staticmethod
    def get_random_char(length: int=32) -> str:
        """
        生成随机字符串
        :param length:
        :return:
        """
        result = ''
        str_pol = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz"
        for i in range(length):
            result += str_pol[random.randint(0, 31)]
        return result

    @staticmethod
    def to_url_params(data: dict) -> str:
        """
        将字典数据排序后生url参数
        :param data:
        :return:
        """
        sort_data = sorted(data.items(), key=lambda d: d[0])
        buff = ''
        for item in sort_data:
            k, v = item
            if k == 'sign' or not v:
                continue
            buff += f'{k}={v}&'
        return buff.rstrip('&')

    def make_sign(self, data: dict, sign_type: str='HMAC-SHA256'):
        """
        生成签名
        :param data:
        :param sign_type:
        :return:
        """
        sign_string = f'{self.to_url_params(data)}&key={self.diy_key}'
        if sign_type == 'md5':
            m = hashlib.md5()
            m.update(sign_string.encode(encoding='utf-8'))
            sign_string = m.hexdigest()
        else:
            sign_string = hmac.new(self.diy_key.encode('utf-8'), sign_string.encode(encoding='utf-8'),
                                                    digestmod=hashlib.sha256).hexdigest()
        return sign_string.upper()