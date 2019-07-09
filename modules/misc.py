import command
import module
import time
import toml
import util
from PIL import Image
#import deep-fryer/deep-fryer.py
import youtube_dl
import random
import os


class MiscModule(module.Module):
    name = 'Miscellaneous'
    prev = 0
    prev_msg_id = ""
    info = []
    @command.desc('Download link for YT vids')
    def cmd_yt(self, msg, text):
        """
        0 format_id
        1 url
        2 player_url
        3 ext
        4 format_note
        5 acodec
        6 abr
        7 filesize
        8 tbr
        9 quality
        10 vcodec
        11 downloader_options
        """
        
        if text.split()[0].lower() == "send":
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "Hol' up! Sending the MP3 of -> "+text.split()[1], parse_mode="HTML")
            name_rand = "/tmp/"
            name_rand += str(random.randint(1000,9999))
            name_rand += ".mp3"
            ydl_opts = {
                        'format': 'bestaudio/best',
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '320',
                        }],
                        'outtmpl': name_rand
                    }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([text.split()[1]])

            self.bot.client.send_audio(msg.chat.id, name_rand, caption = text.split()[1])
            self.bot.client.delete_messages(msg.chat.id, msg.message_id)
            os.remove(name_rand)


        elif text.split()[0].lower() == "url":
            url = text.split()[1]
            path = '/tmp/'
            path += str(random.randrange(1,100))
            path += '.mp3'
            ytdl = youtube_dl.YoutubeDL({"forceurl":True})
            self.info = []
            self.info = ytdl.extract_info(url,download=False, process=False)['formats']
            # print(len(self.info))
            max_abr = [0,0]
            for x,y in enumerate(self.info):
                #print(x,self.info[x]['vcodec'])
                #print(self.info[x]['vcodec'])
                try:
                    if y['abr'] > max_abr[0]:
                        max_abr[0],max_abr[1] = y['abr'], x
                except:
                    pass


            # print(self.info[max_abr[1]]['url'])

            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, self.info[max_abr[1]]['url'], parse_mode="HTML")

        elif text.split()[0].low/er() == "porn":
            url = text.split()[1]
            #self.info=[]
            ytdl = youtube_dl.YoutubeDL({"forceurl":True,"verbose":True})
            data = ytdl.extract_info(url, download=False)
            # print(data)
            return data["entries"][0]['url']

        else:
            self.bot.client.delete_messages(msg.chat.id, msg.message_id)

    @command.desc('leave group')
    def cmd_kickme(self,msg):
        try:
            self.bot.client.leave_chat(msg.chat.id)
        except:
            pass

    @command.desc("blah")
    def cmd_ilugd(self,msg):
        self.bot.client.send_message(msg.chat.id, "asjdgasdhahksdkhasdksjak", parse_mode="HTML")

    @command.desc('PURGE!')
    def cmd_purge(self, msg):
        start = int(msg.reply_to_message.message_id)
        end = int(msg.message_id)
        step = 100
        result = []
        for x in range(start,end+1,step):
            result.append([i for i in range(x,x+step)])
        
        for z in result:
            try:
                self.bot.client.delete_messages(msg.chat.id, z, int(msg.message_id)+1)
            except:
                pass
        #self.bot.client.send_message(msg.chat.id, "")

    @command.desc('Deepfry image')
    @command.alias('df')
    def cmd_deepfry(self, msg):
        if not msg.reply_to_message:
            return '__Reply to the image.__'

        self.bot.client.download_media(msg.reply_to_message, "/tmp/")

    @command.desc('s/a/b')
    def cmd_(self, msg, text):
        rg = text.split('/')
        if rg[0] == 's':
            if not msg.reply_to_message:
                return '__Reply to the message.__'

            if len(rg) != 3 or msg.reply_to_message.from_user.is_self == False:
                self.bot.client.delete_messages(msg.chat.id, msg.message_id)

            else:
                abhi_ka_message, replace_wala_message = rg[1], rg[2]
                try:
                    self.bot.client.edit_message_text(msg.chat.id, msg.reply_to_message.message_id, msg.reply_to_message.text.replace(abhi_ka_message, replace_wala_message), parse_mode="HTML")
                except:
                    pass
                self.bot.client.delete_messages(msg.chat.id, msg.message_id)
        else:
            pass

    @command.desc('Mass forward one message.')
    @command.alias('spam')
    def cmd_forward(self, msg, _count):
        if not _count:
            return '__Provide the amount of times to forward the message.__'
        if not msg.reply_to_message:
            return '__Reply to the message to forward.__'

        try:
            count = int(_count)
        except ValueError:
            return '__Specify a valid number of times to forward the message.__'

        self.bot.client.delete_messages(msg.chat.id, msg.message_id)
        for _ in range(count):
            self.bot.client.send_message(msg.chat.id, msg.reply_to_message.text, parse_mode="HTML")
            time.sleep(0.15)


    def cmd_details(self, msg):
        print(msg.reply_to_message)
        self.bot.client.delete_messages(msg.chat.id, msg.message_id)


    @command.desc('Tag all')
    def cmd_tag(self, msg):
        group_id = -1001457218138
        members = [399195869, 600938509, 680139252, 271397625, 407034913, 400670226, 499134543]
        # if text.split()[0].lower() == "add":
        #     file_data = text.split()[1]
        #     file_data += " = "
        #     file_data += str(msg.reply_to_message.from_user.id)
        #     file_data += "\n"
        #     f = open("tag.txt", "a")
        #     f.write(file_data)
        #     f.close()
        #     self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "Added!", parse_mode="HTML")
        #     time.sleep(0.5)
        #     self.bot.client.delete_messages(msg.chat.id, msg.message_id)
        text = ""
        x = self.bot.client.get_users(members)
        for y in x:
            text += '@'
            text += y['username']
            text += ' '

        self.bot.client.edit_message_text(msg.chat.id, msg.message_id, text, parse_mode="HTML")


    @command.desc('Spam communities')
    @command.alias('com')
    def cmd_community(self, msg, text):
        if not text:
            self.bot.client.delete_messages(msg.chat.id, msg.message_id)

        if text.split()[0].lower() == "add":
            file_data = text.split()[1]
            file_data += ":"
            file_data += str(msg.chat.id)
            file_data += "\n"
            f = open("communities.txt", "a")
            f.write(file_data)
            f.close()
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "Added!", parse_mode="HTML")
            time.sleep(0.5)
            self.bot.client.delete_messages(msg.chat.id, msg.message_id)

        elif text.split()[0].lower() == "spam":
            if not msg.reply_to_message:
                return '__Reply to the message to forward.__'

            f = open("communities.txt", "r")
            file_data = f.read().split("\n")
            f.close()
            file_data.pop(-1)
            #print(file_data)
            text = "Result : \n"
            succ = 0
            for x in file_data:
                text += x.split(":")[0]

                try:
                    y = self.bot.client.forward_messages(int(x.split(":")[1]), msg.chat.id, msg.reply_to_message.message_id)
                    #time.sleep(1)
                    #self.bot.client.delete_messages(int(x.split(":")[1]), y.message_id)
                    succ = 1
                except:
                    #print(e)
                    succ = 0

                text += " - OK" if succ == True else " - !OK"
                text += "\n"
                succ = 0

            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, text, parse_mode="HTML")

        elif text.split()[0].lower() == "list":
            
            f = open("communities.txt", "r")
            file_data = f.read().split("\n")
            f.close()
            file_data.pop(-1)
            #print(file_data)
            text = "List of comms : \n"
            succ = 0
            for x in file_data:
                text += x.split(":")[0]
                text += "\n"

            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, text, parse_mode="HTML")

        else:
            self.bot.client.delete_messages(msg.chat.id, msg.message_id)

    @command.desc('text animate')
    @command.alias('ta')
    def cmd_textanimate(self, msg, text):
        if not text:
            return "__Provide a keyword__"

        dick = ["8=====D\u270A",
                "8====\u270AD",
                "8===\u270A=D",
                "8==\u270A==D",
                "8=\u270A===D",
                "8\u270A====D",
                "8======D 💦💦",
                "8======D 💦💦💦💦"]

        confuse = ["(._. )",
                   "( ._. )",
                   "( ._.)"]

        confuse2 = ["I'm looking for that gay person (._. ) I've looked left.",
                   "Oh you're here ( ._. )",
                   "I'm looking for that gay person ( ._.) I've looked right."]

        def func(x,z):
            y = x
            random.shuffle(y)
            return z.join(y)

        if str(text).lower() == "dick":
            x = self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "8=====D", parse_mode="HTML")
            #print(x)
            zz = [0,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,6,7]
            for z in zz:
                self.bot.client.edit_message_text(msg.chat.id, x.message_id, dick[z], parse_mode="HTML")

        elif str(text).lower() == "confuse":
            x = self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "(._. )", parse_mode="HTML")
            for _ in range(30):
                try:
                    self.bot.client.edit_message_text(msg.chat.id, x.message_id, random.choice(confuse), parse_mode="HTML")
                except:
                    pass

            self.bot.client.edit_message_text(msg.chat.id, x.message_id, confuse[1], parse_mode="HTML")

        elif str(text).lower() == "confuse":
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, confuse2[0], parse_mode="HTML")
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, confuse2[2], parse_mode="HTML")
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, confuse2[1], parse_mode="HTML")


        elif str(text).lower() == "wtf":
            txt = list("Excuse me, WHAT THE FUCK?!")
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '   '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '   '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '  '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '  '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ' '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ' '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ''), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "Excuse me, WHAT THE FUCK?!", parse_mode="HTML")

        elif str(text).lower() == "flex":
            txt = list("StOp FlExInG!")
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '   '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '   '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '  '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '  '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ' '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ' '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ''), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, "StOp FlExInG!", parse_mode="HTML")
            
        elif str(text.split(' ')[0]).lower() == "custom":
            txt = list(' '.join(text.split(' ')[1:]))
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '   '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '   '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '  '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, '  '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ' '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ' '), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, func(txt, ''), parse_mode="HTML")
            time.sleep(0.2)
            self.bot.client.edit_message_text(msg.chat.id, msg.message_id, ' '.join(text.split(' ')[1:]), parse_mode="HTML")
        
        else:
            return "__Not a valid keyword__"
