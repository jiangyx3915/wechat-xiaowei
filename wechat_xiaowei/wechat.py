from wechat_xiaowei.api.wechatapi import WeChatApiMixin
from wechat_xiaowei.basewechat import BaseWeChat
from wechat_xiaowei.exception import WeChatException


class WeChatXiaoWei(BaseWeChat, WeChatApiMixin):
    def apply_enter(self, params: dict):
        if not self._is_support_account_number(params['account_number']):
            raise WeChatException(20003)
        if not self._check_params(params):
            raise WeChatException(20004)
        data = {
            'version': '3.0',
            'cert_sn': '',
            'mch_id': self.mch_id,
            'nonce_str': self.get_random_char(),
            'sign_type': 'HMAC-SHA256',
            'business_code': params.get('business_code'),  # 业务申请编号
            'id_card_copy': params.get('id_card_copy'),  # 身份证人像面照片  media_id
            'id_card_national': params.get('id_card_national'),  # 身份证国徽面照片
            'id_card_name': params.get('id_card_name'),
            'id_card_number': params.get('id_card_number'),
            'id_card_valid_time': params.get('id_card_valid_time'),
            'account_name': ''

        }

    def retrieve_apply_status(self, params: dict):
        pass

    def tenant_config(self, params: dict):
        pass

    def pay_directory_config(self, params: dict):
        pass

    def bind_app_id_config(self, params: dict):
        pass

    def retrieve_config(self, params: dict):
        pass

    def modify_information(self, params: dict):
        pass

    def retrieve_withdraw_status(self, params: dict):
        pass

    def resend_withdraw_request(self, params: dict):
        pass

    @staticmethod
    def _is_support_account_number(account_number: str) -> bool:
        """
        判断银行卡账号是否支持
        :param account_number: 银行卡账号
        :return:
        """
        account_prefix_6 = account_number[0: 7]
        account_prefix_8 = account_number[0: 9]
        not_support = ['623501', '621468', '620522', '625191', '622384', '623078', '940034', '622150', '622151',
                        '622181', '622188', '955100', '621095', '620062', '621285', '621798', '621799', '621797',
                        '622199', '621096', '62215049', '62215050', '62215051', '62218849', '62218850', '62218851',
                        '621622', '623219', '621674', '623218', '621599', '623698', '623699', '623686', '621098',
                        '620529', '622180', '622182', '622187', '622189', '621582', '623676', '623677', '622812',
                        '622810', '622811', '628310', '625919', '625368', '625367', '518905', '622835', '625603',
                        '625605', '518905']
        if account_prefix_6 in not_support:
            return False
        if account_prefix_8 in not_support:
            return False
        return True

    @staticmethod
    def _check_params(params: dict):
        """
        校验入驻接口必填字段信息
        :return:
        """
        data = ['id_card_copy', 'id_card_national', 'id_card_name', 'id_card_number', 'id_card_valid_time',
                'account_name','account_bank', 'bank_address_code', 'account_number', 'store_name',
                'store_address_code', 'store_street','store_entrance_pic', 'indoor_pic', 'merchant_shortname',
                'service_phone', 'contact', 'contact_phone']
        for item in data:
            if not params.get(item):
                return False
        return True
