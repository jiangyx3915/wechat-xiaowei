class WeChatApiMixin:

    def apply_enter(self, params: dict):
        """
        申请入驻小微商户
        :param params:
        :return:
        """
        raise NotImplementedError()

    def retrieve_apply_status(self, params: dict):
        """
        入驻申请状态查询
        :param params:
        :return:
        """
        raise NotImplementedError()

    def tenant_config(self, params: dict):
        """
        关注配置 小微商户关注功能配置API
        :param params:
        :return:
        """
        raise NotImplementedError()

    def pay_directory_config(self, params: dict):
        """
        支付目录配置  小微商户开发配置新增支付目录API
        :param params:
        :return:
        """
        raise NotImplementedError()

    def bind_app_id_config(self, params: dict):
        """
        绑定appid配置  小微商户新增对应APPID关联API
        :param params:
        :return:
        """
        raise NotImplementedError()

    def retrieve_config(self, params: dict):
        """
        查询配置
        :param params:
        :return:
        """
        raise NotImplementedError()

    def modify_information(self, params: dict):
        """
        小微商户修改资料接口-修改结算银行卡
        :param params:
        :return:
        """
        raise NotImplementedError()

    def retrieve_withdraw_status(self, params: dict):
        """
        服务商帮小微商户查询自动提现 - 查询提现状态
        :param params:
        :return:
        """
        raise NotImplementedError()

    def resend_withdraw_request(self, params: dict):
        """
         重新发起提现 - 服务商帮小微商户重新发起自动提现
        :param params:
        :return:
        """
        raise NotImplementedError()