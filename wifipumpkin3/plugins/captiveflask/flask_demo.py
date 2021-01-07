from wifipumpkin3.plugins.captiveflask.plugin import CaptiveTemplatePlugin
import wifipumpkin3.core.utility.constants as C

# This file is part of the wifipumpkin3 Open Source Project.
# wifipumpkin3 is licensed under the Apache 2.0.

# Copyright 2020 P0cL4bs Team - Marcos Bomfim (mh4x0f)

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

# http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class FlaskDemo(CaptiveTemplatePlugin):
    meta = {
        "Name": "FlaskDemo",
        "Version": "1.0",
        "Description": "Example is a simple portal default page",
        "Author": "Pumpkin-Dev",
        "TemplatePath": C.TEMPLATES_FLASK + "templates/Flask",
        "StaticPath": C.TEMPLATES_FLASK + "templates/Flask/static",
        "Preview": "plugins/captivePortal/templates/Flask/preview.png",
    }

    def __init__(self):
        for key, value in self.meta.items():
            self.__dict__[key] = value
        self.dict_domain = {}
        self.ConfigParser = True

    def init_language(self, lang):
        if lang.lower() != "default":
            self.TemplatePath = (
                C.TEMPLATES_FLASK + "templates/Flask/language/{}".format(lang)
            )
            return
        for key, value in self.meta.items():
            self.__dict__[key] = value
