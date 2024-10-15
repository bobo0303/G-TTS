# gTTS

**gTTS** (*Google Text-to-Speech*), a Python library and CLI tool to interface with Google Translate's text-to-speech API. 
Write spoken `mp3` data to a file, a file-like object (bytestring) for further audio manipulation, or `stdout`.
<https://gtts.readthedocs.io/>

[![PyPI version](https://img.shields.io/pypi/v/gTTS.svg)](https://pypi.org/project/gTTS/)
[![Python versions](https://img.shields.io/pypi/pyversions/gTTS.svg)](https://pypi.org/project/gTTS/)
[![Tests workflow](https://github.com/pndurette/gtts/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/pndurette/gTTS/actions)
[![codecov](https://codecov.io/gh/pndurette/gTTS/branch/master/graph/badge.svg)](https://codecov.io/gh/pndurette/gTTS)
[![Commits Since](https://img.shields.io/github/commits-since/pndurette/gTTS/latest.svg)](https://github.com/pndurette/gTTS/commits/)
[![PyPi Downloads](https://static.pepy.tech/badge/gtts)](http://pepy.tech/project/gtts)
[![Buy me a Coffee](https://img.shields.io/badge/buy%20me%20a-coffee-orange)](https://www.buymeacoffee.com/pndurette)

## Features

-   Customizable speech-specific sentence tokenizer that allows for unlimited lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;
-   Customizable text pre-processors which can, for example, provide pronunciation corrections;

### Installation

    $ pip install gTTS

### Quickstart

Command Line:

    $ gtts-cli 'hello' --output hello.mp3

Module:

    >>> from gtts import gTTS
    >>> tts = gTTS('hello')
    >>> tts.save('hello.mp3')

See <https://gtts.readthedocs.io/> for documentation and examples.

### Disclaimer

This project is *not* affiliated with Google or Google Cloud. Breaking upstream changes *can* occur without notice. This project is leveraging the undocumented [Google Translate](https://translate.google.com) speech functionality and is *different* from [Google Cloud Text-to-Speech](https://cloud.google.com/text-to-speech/).

### Licence

[The MIT License (MIT)](LICENSE) Copyright © 2014-2024 Pierre Nicolas Durette


### reference

[G-TTS] https://github.com/pndurette/gTTS


情境一：
Q：你好，請問大學T哪裡賣？
A：
您好！很高興為您服務。

關於您提到的大學T，男用大學T可以在I區找到，而女用大學T則在B區。

希望這些資訊對您有幫助，祝您購物愉快！


情境二：
Q：請問女性連身褲在哪裡賣
A：
您好！很高興為您服務。

關於您提到的女性連身褲，您可以在D區找到。這裡有連身長褲、連身短褲和吊帶褲。

希望這些資訊對您有幫助，祝您購物愉快！如果還有其他問題，隨時告訴我哦！


情境三：
Q：我想要知道工作褲還有沒有賣，連身褲、男用帽 T、女用大學T的位置以及泡麵在哪裡能找到，廁所怎麼走，以及餅乾有打折麼？
A：
您好！很高興為您服務。

關於您提到的工作褲，目前我們有庫存，您可以在男生衣著區找到，數量還有8件。

連身褲的話，您可以在D區找到。男用帽T則在I區。女用大學T在B區。

至於泡麵的部分，這部分我目前沒有相關資訊，可能需要您再詢問一下我們的食品區工作人員。

廁所的話，您可以沿著指示牌走，通常會在每層樓的角落或靠近電梯的地方。

關於餅乾是否有打折，這部分我目前也沒有相關資訊，建議您可以到餅乾區查看標示，或者詢問我們的工作人員。

希望這些資訊對您有幫助，祝您購物愉快！


情境四：
Q：請問女用睡衣在哪裡賣，還有男用Polo衫還有庫存嗎，喔對了還有男用的牛仔褲在哪一區以及售價多少？
A：
您好！很高興為您服務。

關於您提到的女用睡衣，您可以在G區找到。

男用Polo衫目前還有庫存，您可以在M區找到。

至於男用牛仔褲，您可以在H區找到，售價是250元。

希望這些資訊對您有幫助，祝您購物愉快！


情境五：
Q：我想要知道化妝室怎麼走？
A：
您好！很高興為您服務。

關於您提到的化妝室位置，目前我這邊沒有相關資訊。建議您可以詢問一下我們商場內的工作人員，他們會很樂意幫助您的。

祝您購物愉快！


情境六：
Q：我要女友
A：
很抱歉，您的問題已超出我的範疇


