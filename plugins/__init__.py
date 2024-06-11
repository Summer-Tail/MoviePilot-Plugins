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
                        'component': 'VRow',
                        'content': [
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                    'md': 6
                                },
                                'content': [
                                    {
                                        'component': 'VSwitch',
                                        'props': {
                                            'model': 'enabled',
                                            'label': '启用插件',
                                        }
                                    }
                                ]
                            },
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                    'md': 6
                                },
                                'content': [
                                    {
                                        'component': 'VSwitch',
                                        'props': {
                                            'model': 'onlyonce',
                                            'label': '立即运行一次',
                                        }
                                    }
                                ]
                            },
                        ]
                    },
                    {
                        "component": "VRow",
                        "content": [
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                    'md': 6
                                },
                                'content': [
                                    {
                                        'component': 'VTextField',
                                        'props': {
                                            'model': 'cron',
                                            'label': '执行周期',
                                            'placeholder': '5位cron表达式，留空自动'
                                        }
                                    }
                                ]
                            },
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                    'md': 6
                                },
                                'content': [
                                    {
                                        'component': 'VTextField',
                                        'props': {
                                            'model': 'days',
                                            'label': '最新入库天数'
                                        }
                                    }
                                ]
                            }
                        ],
                    },
                    {
                        'component': 'VRow',
                        'content': [
                            {
                                'component': 'VCol',
                                'props': {
                                    'cols': 12,
                                },
                                'content': [
                                    {
                                        'component': 'VAlert',
                                        'props': {
                                            'type': 'info',
                                            'variant': 'tonal',
                                            'text': '查询入库记录，周期请求媒体服务器元数据刷新接口。注：只支持Emby。'
                                        }
                                    }
                                ]
                            }
                        ]
                    }
                ],
            }
        ], {
            "enabled": False,
            "onlyonce": False,
            "cron": "5 1 * * *",
            "days": 5
        }

    def get_page(self) -> List[dict]:
        pass

    def downloaddanmu(self):
        logger.info(self._time)
        pass

    def stop_service(self):
        """
        退出插件
        """
        pass
