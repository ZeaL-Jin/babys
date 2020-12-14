# pip install pycryptodome
# pip install python-alipay-sdk

from alipay import AliPay
import time

alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAhfAWzMnl0cUWgvp4tV1YcJPAenOhNzopiAHGI/9NmokTo7AZ5ZAq3Tf+x1XUthVNtRimuhb2Ev+tZplFnYvGiY2XgfVsRWxCZQkQWrjCGB+GMYMz8wLxaR0EK6/XaAMVKhjY5U45Z9cx+4jSjXBW4NXVIObP0BnGMR/mTe09D5zP+XORmEM7YMMgBEyLmWma4DXQuYJa836GDn/jx/aTJvgPhsbA5St3PQfCNazQ3xI9OMhTgzqEI1vKYBhXfhtk+LF6cwYeS8DaitHSmFW5xB3bGXAw0kEemSt60xLdrzQRbVbWoljEmBYy3JG8nizdUaSnzV+5it3ajf42aUMO1QIDAQAB
-----END PUBLIC KEY-----"""
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAhfAWzMnl0cUWgvp4tV1YcJPAenOhNzopiAHGI/9NmokTo7AZ5ZAq3Tf+x1XUthVNtRimuhb2Ev+tZplFnYvGiY2XgfVsRWxCZQkQWrjCGB+GMYMz8wLxaR0EK6/XaAMVKhjY5U45Z9cx+4jSjXBW4NXVIObP0BnGMR/mTe09D5zP+XORmEM7YMMgBEyLmWma4DXQuYJa836GDn/jx/aTJvgPhsbA5St3PQfCNazQ3xI9OMhTgzqEI1vKYBhXfhtk+LF6cwYeS8DaitHSmFW5xB3bGXAw0kEemSt60xLdrzQRbVbWoljEmBYy3JG8nizdUaSnzV+5it3ajf42aUMO1QIDAQABAoIBAB66HNDwhJviRi7YPXcGKjLxgpfVDSg5XKvKFGXPvUL1rZ7A2MAUmfDUVsvuQfVf38rrE9zfRabIJ0TBZvokxfBqnlZ/Mk6e7oB1Wt4lQsn7+XJEcleO1klSEdHf7l/7TRCyUJgSoRLUiK/3DK7MFfJQvCtnKEfKkfBVLCW2hmqdLXtHs/Gjj6dTsAVlN/MNMluFBAzkyRPDULSxqZOtfDB0BE8MWb6zYF0z+6hRCrBl0oHe9Ddr+CBt3gAF1ZNfkMjoyemtwzLW8GkH3Z20dxPucgBgaKzmQzueQY4RRdZh+FBEXk33si0xtwgVinT/LyMFC0ZlMgHdW+u/0ga88qUCgYEA4N+B3U8qvWISIQwOWJS6CanvqN9FNv6UXlz3dUD5POGkS+QZJv/fA3iBkh0S+/CLcocrscseJ7Fsqr78H1+fle2zDd5i15n0AEVwKNXaD0MdnoTn0NYSOy+n3fUDW/cfxclBIMaRRo5ScgNOaHgcd7YiVIfofTmyTwwzuhpp7qsCgYEAmHo+0L+uAC9MKBJBjDfDnjVZJeVcNxGQd1hoXYuwH0IA4ZFVXv+nfoB2KvugTUmlX69Jz6siEqS+GH82YSIotvEWCyT/aTcEQQdzJ+KyV92M6hIZcY04O95/dIrI5crP66OYsFpkPWff2Ar0c2JLYD2Rgh87dtZvBr8B2A6A+H8CgYEAxSUuRUfSwJXqLu7S5PX+49oIMpULqVsn2FLI4BNGbwmjcKVZJ8fLTM+pSOAUdKw+lPnMZOMeXM4/5rHpd9ftoRPzloURQtPGBzbZTfOuaRL+NKtwULZc5WayVPUpLMdLI6t9Xa64TpMX1LzxUMV8r7cOAe3k9WRP3t1jvBTMKmECgYB1sCU7yjbrPZZyd2TQbVo3isW8UkPS3WO8OiiTy3WtKqyzbhGOuZT2NwD+PCmGfgl+yTUXbOdnrHBtSAMZBdyXF44EHBJni2dlKfLgHkG5P++72yx4UJ/O1fVaZqSZeOjy39rCg4JLQxmrDwmO5Zd4OQ1OefzTxL79XgB2WvuA0QKBgB/dwdKSJeXS7/KRWuoTKdL8Q1NOowwAOF1E+3tjbHyCCDxZzVZQSXpgxktBJr1+0D1fWfnd9K6nUJJB6uLCFKtvckAMtNmZTIg0aolYT/npgVj7KIHOwsRdY6oXAf3OaiCLj6JnC51RKkfEIqSFJo8yXIH9HD1yt+/5WivRe6c5
-----END RSA PRIVATE KEY-----"""


def get_pay(out_trade_no, total_amount, return_url):
    # 实例化支付应用
    alipay = AliPay(
        appid="2021000116669345",
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2"
    )
    # 发起支付请求
    order_string = alipay.api_alipay_trade_page_pay(
        # 订单号，每次发送请求都不能一样
        out_trade_no=out_trade_no,
        # 支付金额
        total_amount=str(total_amount),
        # 交易信息
        subject="测试",
        return_url=return_url + '?t=' + out_trade_no,
        notify_url=return_url + '?t=' + out_trade_no
    )
    return 'https://openapi.alipaydev.com/gateway.do?' + order_string
