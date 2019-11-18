#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler)
from linebot.exceptions import (
    InvalidSignatureError)
import json

secretFileContentJson=json.load(open("./line_secret_key",'r'))
server_url=secretFileContentJson.get("server_url")


app = Flask(__name__,static_url_path = "/images" , static_folder = "./images/")


line_bot_api = LineBotApi(secretFileContentJson.get("channel_access_token"))
handler = WebhookHandler(secretFileContentJson.get("secret_key"))


@app.route("/", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


# In[2]:


flexCarouselContainerJsonDict = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/t5Li1hW.png",
        "size": "full",
        "margin": "none",
        "position": "relative"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "做人太辛苦～當狗看看！",
            "style": "normal",
            "weight": "bold",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "你將會成為怎麼樣的狗呢？",
            "size": "sm",
            "margin": "lg"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "參加",
              "data": "joinstory",
              "displayText": "很棒嘛～"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "沒興趣！",
              "uri": "https://store.line.me/stickershop/product/1367634/zh-Hant"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "hero": {
        "type": "image",
        "url": "https://i.imgur.com/5cUYSW8.jpg",
        "size": "full",
        "position": "relative",
        "margin": "none"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "知道更多",
            "style": "normal",
            "weight": "bold",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "作者祕密大公開",
            "size": "sm",
            "margin": "lg"
          },
          {
            "type": "button",
            "action": {
              "type": "postback",
              "label": "我想瞭解",
              "data": "knowmore",
              "displayText": "ＧＯＧＯＧＯ！"
            }
          },
          {
            "type": "button",
            "action": {
              "type": "uri",
              "label": "懶得瞭解",
              "uri": "https://store.line.me/stickershop/product/1367634/zh-Hant"
            }
          }
        ],
        "margin": "none"
      }
    }
  ]
}
"""


# In[3]:


from linebot.models import(
    FlexSendMessage,CarouselContainer,TemplateSendMessage
)

import json

carouselContent = CarouselContainer.new_from_json_dict(json.loads(flexCarouselContainerJsonDict))
print(carouselContent)
TemplateSendMessage(alt_text="請用手機開啟哦~", contents=carouselContent)


# In[4]:


#建立圖庫
from linebot.models import ImageSendMessage, VideoSendMessage
image_message_story1 = ImageSendMessage(    
    original_content_url='https://i.imgur.com/MV5Hcql.png',
    preview_image_url='https://i.imgur.com/MV5Hcql.png')

rvideo1 = VideoSendMessage(original_content_url='https://i.imgur.com/SxbtMNb.mp4',
                           preview_image_url='https://example.com/preview.jpg')



image_message_ebd1_2 = ImageSendMessage(
    original_content_url='https://i.imgur.com/LK0iNIu.png',
    preview_image_url='https://i.imgur.com/LK0iNIu.png'
)

rvideo2 = VideoSendMessage(original_content_url='https://%s/images/Video/intrv.mp4' % server_url,
                           preview_image_url='https://example.com/preview.jpg')



image_message_intro = ImageSendMessage(
    original_content_url='https://%s/images/intro.png' % server_url,
    preview_image_url='https://%s/images/intro.png' % server_url
)
image_message2_Experience= ImageSendMessage(
    original_content_url='https://%s/images/Experience.png' % server_url,
    preview_image_url='https://%s/images/Experience.png' % server_url
)
image_message3_skill = ImageSendMessage(
    original_content_url='https://%s/images/skill.png' % server_url,
    preview_image_url='https://%s/images/skill.png' % server_url
)

image_message4_non = ImageSendMessage(
    original_content_url='https://%s/images/non.png' % server_url,
    preview_image_url='https://%s/images/non.png' % server_url
)
image_message_ebd1_2 = ImageSendMessage(
    original_content_url='https://i.imgur.com/LK0iNIu.png',
    preview_image_url='https://i.imgur.com/LK0iNIu.png'
)


# In[5]:


from linebot.models import ImagemapSendMessage

from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction,MessageImagemapAction,PostbackEvent
)

imagemap_message = ImagemapSendMessage(
    base_url='https://i.imgur.com/KDTdmyw.png',
    alt_text='This is an imagemap',
    base_size=BaseSize(height=500, width=1040),
    actions=[
        MessageImagemapAction(
            text='現代',
            area=ImagemapArea(
                x=19, y=113, width=307, height=379
            )
        ),
        MessageImagemapAction(
            text='古代',
            area=ImagemapArea(
                x=366, y=118, width=315, height=370
            )
        ),
        MessageImagemapAction(
            text='60年代',
            area=ImagemapArea(
                x=709, y=121, width=323, height=363
            ))]
            
        

)


# In[6]:


from linebot.models import ImagemapSendMessage

from linebot.models import (
    ImagemapArea, BaseSize, URIImagemapAction,MessageImagemapAction,PostbackEvent
)

imagemap_message_space = ImagemapSendMessage(
    base_url='https://i.imgur.com/VLU2Loc.png',
    alt_text='This is an imagemap',
    base_size=BaseSize(height=701, width=1040),
    actions=[
        MessageImagemapAction(
            text='(￣﹁￣)你是誰?',
            area=ImagemapArea(
                x=8, y=4, width=238, height=214
            )
        ),
        MessageImagemapAction(
            text='(￣﹁￣)作品G',
            area=ImagemapArea(
                x=347, y=206, width=346, height=326
            )
        ),
        MessageImagemapAction(
            text='(￣﹁￣)略懂略懂',
            area=ImagemapArea(
                x=0, y=451, width=266, height=250
            )
        ),MessageImagemapAction(
            text='(￣﹁￣)都25個年頭了~',
            area=ImagemapArea(
                x=790, y=449, width=250, height=252
            )
        ),MessageImagemapAction(
            text='(￣﹁￣)學海無涯',
            area=ImagemapArea(
                x=782, y=0, width=258, height=246
            )
        )
    ]
)
        
    


# In[7]:


from linebot.models import TemplateSendMessage, ConfirmTemplate, PostbackAction, MessageAction


# In[8]:


confirm_template_message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='在市集遇到一個阿婆阿春,要跟著他走嗎?',
        actions=[
            PostbackAction(
                label='跟著她',
                display_text='汪汪撒嬌~',
                data='mission1'
            ),
            PostbackAction(
                label='懶得鳥她',
                display_text='因為不跟阿春阿嬤走\在市集裡餓死了...',
                data='dead1'
            )
        ]
    )
)   


# In[9]:


from linebot.models import ButtonsTemplate
buttons_template_message_story1 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/5fvfwUC.jpg',
        title='任務來襲!!!',
        text='跟著阿春到XXXXXXXX',
        actions=[
            PostbackAction(
                label='接收任務',
                display_text='我會到指定地點~',
                data='golocation'
            ),
            PostbackAction(
                label='放棄任務',
                display_text='安捏母湯啦!',
                data='giveup'
            )
            
        ]
    )
)


# In[10]:


from linebot.models import ButtonsTemplate
buttons_template_message_story1_1 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/0M30KGE.png',
        title='讓我們在XXXXXX與阿春逍遙吃喝',
        text='真是之爽狗,要回家了嗎?',
        actions=[
            PostbackAction(
                label='走吧~阿春家很溫暖的感覺',
                display_text='歐耶~我不是流浪狗了~',
                data='gohome'
            ),
            PostbackAction(
                label='故事到這了,所以....',
                display_text='我要匯款至700XXXXXXXXXX',
                data='gotojail'
            )
            
        ]
    )
)


# In[11]:


from linebot.models import ButtonsTemplate
buttons_template_message_story1_2 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/ZDDm5go.jpg',
        title='一夜!!!月黑風高',
        text='咻咻咻,有小偷闖進阿春家!!!',
        actions=[
            PostbackAction(
                label='阿春是我恩人\n衝過去咬~',
                display_text='我盡力了...\n我被小偷幹掉了QQ"',
                data='gotoendone'
            ),
            PostbackAction(
                label='小偷看起來凶神惡煞...嗚嗚',
                display_text='我是膽小狗!!!',
                data='gotoend2'
            )
            
        ]
    )
)


# In[12]:


from linebot.models import ButtonsTemplate, URIAction
buttons_template_message_storyend2 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/vP0oGkP.png',
        title='英勇殉職~',
        text='成為60年代忠狗代表\n是人會記得你的!',
        actions=[
            URIAction(
                label='買個阿奇貼圖保平安',
                uri='https://store.line.me/stickershop/product/1367634/zh-Hant'
            ),
            PostbackAction(
                label='換個年代',
                display_text='老子復活啦~汪',
                data='joinstory'
            )
            
        ]
    )
)


# In[13]:


from linebot.models import ButtonsTemplate, URIAction
buttons_template_message_storyend2_2 = TemplateSendMessage(
    alt_text='Buttons template',
    template=ButtonsTemplate(
        thumbnail_image_url='https://i.imgur.com/wWsi2LF.png',
        title='阿春財產盡失...也沒抓到犯人...',
        text='阿春沒錢養你了,所以...',
        actions=[
             MessageAction(
                label='最後怎麼了?',
                text='再次流浪街頭...\n且遺臭萬年!!!'
            ),
            PostbackAction(
                label='換個年代',
                display_text='老子復活啦~汪',
                data='joinstory'
            )
            
        ]
    )
)


# In[14]:


from linebot.models import (
    MessageAction, URIAction,
    PostbackAction, DatetimePickerAction,
    CameraAction, CameraRollAction, LocationAction,
    QuickReply, QuickReplyButton)
    
## 點擊後，跳出地理位置
locationQRB = QuickReplyButton(
    action=LocationAction(label="請確認你已抵達")
)
cameraQuickReplyButton = QuickReplyButton(
    action=CameraAction(label="拍張照~")
)
cameraRollQRB = QuickReplyButton(
    action=CameraRollAction(label="選擇照片")
)


# In[15]:


confirm_template_message2 = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='體驗故事不是有拍照嗎?\n傳個照片給阿奇~',
        actions=[
            PostbackAction(
                label='點我後傳送',
                display_text='請傳送照片',
                data='getphoto'
            ),
            PostbackAction(
                label='時空跳躍',
                display_text='投胎當人~',
                data='newstory'
            )
        ]
    )
)
    


# In[16]:


# 設計QuickReplyButton的List
quickReplyList = QuickReply(
    items = [locationQRB]
)


# In[17]:


from linebot.models import (
    TextSendMessage, MessageEvent, TextMessage
)
quickReplyTextSendMessage = TextSendMessage(text='你確定到了嗎???\n(確定請輸入:Y , 還沒到請輸入N)', quick_reply=quickReplyList)


# In[18]:


quickReplyList1 =  QuickReply(
    items = [cameraQuickReplyButton, cameraRollQRB])


# In[19]:


from linebot.models import (
    TextSendMessage, MessageEvent, TextMessage
)
quickReplyTextSendMessage1 = TextSendMessage(text='若拍好照請輸入:OK\n沒有其他選擇!!!)', quick_reply=quickReplyList1)


# In[20]:


# 用戶發出文字消息時， 按條件內容, 回傳合適消息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        template_message_dict.get(event.message.text)
    )


# In[21]:


#用戶點擊button後，觸發postback event，對其回傳做相對應處理

@handler.add(PostbackEvent)
def handle_post_message(event):
    user_profile = line_bot_api.get_profile(event.source.user_id)
    if (event.postback.data.find('joinstory')== 0):
        print(imagemap_message)
        line_bot_api.reply_message(event.reply_token,
            imagemap_message
            )
    elif (event.postback.data.find('dead1')== 0):
        line_bot_api.reply_message(event.reply_token,image_message_story1)
        
        
    elif (event.postback.data.find('mission1')== 0):
        line_bot_api.reply_message(event.reply_token,buttons_template_message_story1)
        
    elif (event.postback.data.find('golocation')== 0):
        print(quickReplyTextSendMessage)
        line_bot_api.reply_message(event.reply_token, quickReplyTextSendMessage)
        print(quickReplyList)
    elif (event.postback.data.find('gotojail')== 0): 
        line_bot_api.reply_message(event.reply_token, rvideo1)
    elif (event.postback.data.find('storytalk')== 0): 
        line_bot_api.reply_message(event.reply_token, TextSendMessage(
            text="阿奇是吉娃娃，現在已經8歲囉！\n換算成人類年齡，是56歲...\n活到這把年紀，使阿奇逐漸厭世。\n這次，阿奇前往未知宇宙，展開時空之旅！！！\n讓我們跟著體驗牠的生活～"))
    elif (event.postback.data.find('gohome')== 0):
        line_bot_api.reply_message(event.reply_token,buttons_template_message_story1_2)
    elif(event.postback.data.find('quiz')== 0):
        line_bot_api.reply_message(event.reply_token,confirm_template_message2)
        
    elif(event.postback.data.find('getphoto')== 0):
        @handler.add(MessageEvent, message=ImageMessage)
        def handle_message(event):
            
            message_content = line_bot_api.get_message_content(event.message.id)
            with open('./images/newimg/'+event.message.id+'.jpg', 'wb') as fd:
                for chunk in message_content.iter_content():
                    fd.write(chunk)
            from PIL import Image
            import cv2
            #開啟照片
            imageA = Image.open('./images/newimg/'+event.message.id+'.jpg')
            
            w,h = imageA.size
            imageA = imageA.resize((int(w/2),int(h/2))) 
            imageA = imageA.convert('RGBA')
            widthA , heightA = imageA.size

            #開啟簽名檔
            imageB = Image.open('./images/mt.png')
            imageB = imageB.convert('RGBA')
            widthB , heightB = imageB.size

            #重設簽名檔的寬為照片的1/2
            newWidthB = int(widthA/2)
            #重設簽名檔的高依據新的寬度等比例縮放
            newHeightB = int(heightB/widthB*newWidthB)
            #重設簽名檔圖片
            imageB_resize = imageB.resize((newWidthB, newHeightB))

            #新建一個透明的底圖
            resultPicture = Image.new('RGBA', imageA.size, (0, 0, 0, 0))
            #把照片貼到底圖
            resultPicture.paste(imageA,(0,0))

            #設定簽名檔的位置參數
            right_bottom = (widthA - newWidthB, heightA - newHeightB)

            #為了背景保留透明度，將im參數與mask參數皆帶入重設過後的簽名檔圖片
            resultPicture.paste(imageB_resize, right_bottom, imageB_resize)
            
            #儲存新的照片  
            resultPicture.save('./images/newimg/'+'new'+event.message.id+'.png')
    

            image_message_re = ImageSendMessage(original_content_url='https://%s/images/newimg/new%s.png' % (server_url,(event.message.id)),
                                                                       preview_image_url='https://%s/images/newimg/new%s.png'% (server_url,(event.message.id)))
        
            line_bot_api.reply_message(event.reply_token, image_message_re)
            
    elif(event.postback.data.find('change')== 0):
        line_bot_api.reply_message(event.reply_token, imagemap_message_space)
    elif(event.postback.data.find('gotoendone')== 0):
        line_bot_api.reply_message(event.reply_token, buttons_template_message_storyend2)  
        
    elif(event.postback.data.find('gotoend2')== 0):
        line_bot_api.reply_message(event.reply_token,buttons_template_message_storyend2_2 ) 
        
    elif(event.postback.data.find('knowmore')== 0):
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="還沒開放~"))    
        
        
        
    else:
        pass
    
            


# In[22]:


from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage
)


#引入所需要的消息與模板消息
from linebot.models import (
    MessageEvent, TemplateSendMessage , PostbackEvent, CarouselTemplate, CarouselColumn
)

#引入按鍵模板
from linebot.models.template import(
    ButtonsTemplate
)

#引入模板消息的可用行為
from linebot.models import(PostbackTemplateAction,MessageTemplateAction,URITemplateAction,DatetimePickerTemplateAction
)


reply_message_list = [
TextSendMessage(text="您好，初次見面！\nHello, Nice to meet you!\n初はじめまして~\nXin chào!!!"),
    ImageSendMessage(original_content_url='https://i.imgur.com/JTdeJWq.png',
    preview_image_url='https://i.imgur.com/bQZNAyT.png'),
    TextSendMessage(text="阿奇狗旅行計畫 ☥\n跟著故事去玩耍~\nGO GO GO～💪"),
    FlexSendMessage(alt_text="請用手機開啟哦~", contents=carouselContent)
]



# In[23]:


# 載入Follow事件
from linebot.models.events import (
    FollowEvent
)

# 載入requests套件
import requests


# 告知handler，如果收到FollowEvent，則做下面的方法處理
@handler.add(FollowEvent)
def reply_text_and_get_user_profile(event):
    
    # 取出消息內User的資料
    user_profile = line_bot_api.get_profile(event.source.user_id)
        
     # 將用戶資訊存在檔案內
    with open("./users.txt", "a") as myfile:
        myfile.write(json.dumps(vars(user_profile),sort_keys=True))
        myfile.write('\r\n')
        
        
    # 將菜單綁定在用戶身上
    linkRichMenuId=secretFileContentJson.get("rich_menu_id")
    linkMenuEndpoint='https://api.line.me/v2/bot/user/%s/richmenu/%s' % (event.source.user_id, linkRichMenuId)
    linkMenuRequestHeader={'Content-Type':'image/jpeg','Authorization':'Bearer %s' % secretFileContentJson["channel_access_token"]}
    lineLinkMenuResponse=requests.post(linkMenuEndpoint,headers=linkMenuRequestHeader)
    
    # 回覆文字消息與圖片消息
    line_bot_api.reply_message(
        event.reply_token,
        reply_message_list
    )


# In[24]:


# 根據自定義菜單四張故事線的圖，設定相對應image
template_message_dict = {
    "(￣﹁￣)你是誰?":TextSendMessage(text="嗨～\n我是宗翰\n是這個ChatBot的作者\n很高興可以介紹自己\n厲害的人都深藏不露\n害我想多說些什麼,但...\n的確~我已經說完了!"),
    "(￣﹁￣)學海無涯":TextSendMessage(text="我是東吳社工系,!\n想不到吧?\n寫程式跟當社工...但...\n程式就像處遇般,用不同方式來得到成就!!!\n"),
    "(￣﹁￣)作品G":TextSendMessage(text="還在製作中~"),
    "(￣﹁￣)略懂略懂":TextSendMessage(text="這個ChatBot\n融合了我會的事物~哦!!!"),
    "(￣﹁￣)都25個年頭了~":TextSendMessage(text="當了社工快一年半\n想做點吸引人的~\n工程師!?\n走!!!")
    
}


# In[25]:


# 載入Follow事件
from linebot.models.events import (
    FollowEvent, ImageMessage
)

import requests


# 告知handler，如果收到FollowEvent，則做下面的方法處理
@handler.add(FollowEvent)
def reply_text_and_get_user_profile(event):
    
    # 取出消息內User的資料
    user_profile = line_bot_api.get_profile(event.source.user_id)
        
     # 將用戶資訊存在檔案內
    with open("./users.txt", "a") as myfile:
        myfile.write(json.dumps(vars(user_profile),sort_keys=True))
        myfile.write('\r\n')
        
        
    # 將菜單綁定在用戶身上
    linkRichMenuId=secretFileContentJson.get("rich_menu_id")
    linkMenuEndpoint='https://api.line.me/v2/bot/user/%s/richmenu/%s' % (event.source.user_id, linkRichMenuId)
    linkMenuRequestHeader={'Content-Type':'image/jpeg','Authorization':'Bearer %s' % secretFileContentJson["channel_access_token"]}
    lineLinkMenuResponse=requests.post(linkMenuEndpoint,headers=linkMenuRequestHeader)
    
    # 回覆文字消息與圖片消息
    line_bot_api.reply_message(
        event.reply_token,
        reply_message_list
    )


# In[26]:


# 用戶發出文字消息時， 按條件內容, 回傳文字消息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if(event.message.text.find('(￣﹁￣)')!= -1):
        line_bot_api.reply_message(
        event.reply_token,
        template_message_dict.get(event.message.text))
    elif(event.message.text.find('60年代')!= -1):
        print("confirm_template_message")
        line_bot_api.reply_message(event.reply_token,confirm_template_message)
    elif(event.message.text.find('Y')!= -1):
        print(quickReplyTextSendMessage1)
        line_bot_api.reply_message(event.reply_token, quickReplyTextSendMessage1)
        print(quickReplyList1)
    elif(event.message.text.find('OK')!= -1):
        line_bot_api.reply_message(event.reply_token, buttons_template_message_story1_1)  
    elif(event.message.text.find('再次流浪街頭...\n且遺臭萬年!!!')!= -1):
        line_bot_api.reply_message(event.reply_token, ImageSendMessage(
            original_content_url='https://i.imgur.com/gCrUCjh.png',
            preview_image_url='https://i.imgur.com/gCrUCjh.png'))
    elif(event.message.text.find('登愣')!= -1):
        line_bot_api.reply_message(event.reply_token, rvideo2) 
    
    elif(event.message.text.find('現代')!= -1):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="故事準備中...未開放") )
    elif(event.message.text.find('古代')!= -1):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="故事準備中...未開放") )   
        
    elif(event.message.text.find('ok')!= -1):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="要大寫!!!"))
    elif(event.message.text.find('Ok')!= -1):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="兩個都要大寫!!!") )
    elif(event.message.text.find('y')!= -1):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="要大寫!!!") )
    elif(event.message.text.find('n')!= -1):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="要大寫!!!") )
                
                
                
    
    
        


# In[ ]:


# if __name__ == "__main__":
#     app.run(host='0.0.0.0')


# In[ ]:


import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])







