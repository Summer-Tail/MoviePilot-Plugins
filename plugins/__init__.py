from app.plugins import _PluginBase
from app.core.event import eventmanager
from app.schemas.types import EventType
from app.utils.http import RequestUtils
from typing import Any, List, Dict, Tuple
from app.log import logger


class WebHook(_PluginBase):
    # 插件名称
    plugin_name = "autoDownloadDanmu"
    # 插件描述
    plugin_desc = "自动下载弹幕"
    # 插件图标
    plugin_icon = "https://raw.githubusercontent.com/Summer-Tail/MoviePilot-Plugins/main/icons/danmu.png"
    # 插件版本
    plugin_version = "1.0"
    # 插件作者
    plugin_author = "SummerTail"
    # 作者主页
    author_url = "https://github.com/Summer-Tail"
    # 插件配置项ID前缀
    plugin_config_prefix = "SummerTail_Danmu"
    # 加载顺序
    plugin_order = 14
    # 可使用的用户级别
    auth_level = 1

    # 私有属性
    _method = None
    _enabled = False
    _danmuUrl = None
    _time = None

    def init_plugin(self, config: dict = None):
        if config:
            self._enabled = config.get("enabled")
            self._danmuUrl = config.get("danmuUrl")
            self._method = config.get('request_method')
            self._time = config.get('time')

    def get_state(self) -> bool:
        return self._enabled

    @staticmethod
    def get_command() -> List[Dict[str, Any]]:
        pass

    def get_api(self) -> List[Dict[str, Any]]:
        pass

    def get_form(self) -> Tuple[List[dict], Dict[str, Any]]:
        """
        拼装插件配置页面，需要返回两块数据：1、页面配置；2、数据结构
        """
        return [
            {
                "component": "VForm",
                "content": [
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 6
                                },
                                "content": [
                                    {
                                        "component": "VSwitch",
                                        "props": {
                                            "model": "enabled",
                                            "label": "启用插件"
                                        }
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "component": "VRow",
                        "content": [
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 4
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "danmuku",
                                            "label": "需要刷新弹幕的库id"
                                        }
                                    }
                                ]
                            },
                            {
                                "component": "VCol",
                                "props": {
                                    "cols": 12,
                                    "md": 4
                                },
                                "content": [
                                    {
                                        "component": "VTextField",
                                        "props": {
                                            "model": "time",
                                            "label": "媒体库更新周期"
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        ], {
            "enabled": False,
            "danmuUrl": ""
        }

    def get_page(self) -> List[dict]:
        pass

    def get_service(self):
        """
        获取插件服务
        """
        return [{
            "id": "danmuDownload",
            "name": "弹幕下载",
            "trigger": "cron",
            "func": self.downloaddanmu,
            "kwargs": {self.time}
        }]

    def downloaddanmu(self):
        logger.info(self._time)
        pass

    def stop_service(self):
        """
        退出插件
        """
        pass
