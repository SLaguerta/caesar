#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

from caesar import encrypt
page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar Cipher</title>
        <style>
            form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 500px;
                    font: 16px serif;
            }
            textarea {
                    margin: 10px 0;
                    width: 450px;
                    height: 300px;
            }

        </style>
    </head>
<body>
"""

form="""
<form method= "post">
    Encrypt
    <br>
    <div>
    <label for="rotate_value"> Rotate by:
    <input type="text" name="rotate_value" value="{}">
    </label>
    </div>
    <br>
    <label>Text to Encrypt
    <textarea type="text" name="text">{}</textarea></label>
    <br>
    <input type ="submit">
</form>
"""

class MainHandler(webapp2.RequestHandler):


    def get(self):
        response = page_header + form.format(0, "")

        self.response.out.write(response)

    def post(self):
        rot = self.request.get("rotate_value")
        rot =int(rot)
        user_text = self.request.get("text")

        answer = encrypt(user_text, rot)

        response = page_header + form.format(rot, cgi.escape(answer))
        self.response.out.write(response)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
