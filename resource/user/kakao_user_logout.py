import json

import requests


class KaKaoUserLogOut:
    """https://developers.kakao.com/docs/latest/ko/kakaologin/rest-api#logout"""

    endpoint = "https://kapi.kakao.com/v1/user/logout"

    @classmethod
    def user_logout(cls, access_token: str):
        resp = requests.get(
            cls.endpoint,
            headers={
                "Authorization": f"Bearer ${access_token}"
            }
        )
        if resp.status_code == 200:
            return resp.json()
