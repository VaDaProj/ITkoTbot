# Functions for make actions (requests) on api.telegram.org
import requests  # For making requests


class Telekot:
    def __init__(self, token):
        """Here you write token of your Telegram bot"""
        self.token = token
        self.api_url = 'https://api.telegram.org/bot{}/'.format(token)  # Adress for requests

    def get_updates(self, offset=None, timeout=30):
        """For get updates in correspondence"""
        method = 'getUpdates'  # Method for get updates
        params = {'timeout': timeout,
                  'offset': offset}   # Extra options for get updates
        resp = requests.get(self.api_url + method, data=params)  # Request for get updates
        result = resp.json()['result']  # Return only with key 'result'

        return result

    def get_last_update(self):
        """For get last update in correspondence"""
        get_result = self.get_updates()  # Get all updates

        if len(get_result) > 0:  # If here were some updates
            last_update = get_result[-1]  # Return last update in 'get_result'
        else:
            last_update = get_result[len(get_result)]  # Return ...

        return last_update

    def get_last_message_id(self):
        """Return last message id of companion"""
        get_update = self.get_last_update()  # Get lust update
        result = get_update['message']['message_id']  # Get message id

        return result

    def get_last_message_text(self):
        """Return a last message text of companion"""
        get_update = self.get_last_update()  # Get lust update
        result = get_update['message']['text']  # Get message text

        return result

    def get_chat_id(self):
        """Return a chat id"""
        get_update = self.get_last_update()  # Get updates
        result = get_update['message']['chat']['id']  # Get chat id

        return result

    def get_user_name(self, only_first_name=False):
        """Return a user name"""
        get_update = self.get_last_update()  # Get updates
        if only_first_name:
            result = get_update['message']['from']['first_name']  # Get only first user name
        elif not only_first_name:
            result = get_update['message']['from']['first_name'] + \
                     ' ' + \
                     get_update['message']['from']['last_name']   # Get full user name

        return result

    def send_message(self, chat_id, text):
        """Send message to companion"""
        params = {'chat_id': chat_id,
                  'text': text}  # Options for send message
        method = 'sendMessage'  # Method for send message
        resp = requests.post(self.api_url + method, data=params)  # Request for send message

        return resp

    def forward_message(self, chat_id, from_chat_id, message_id):
        """Forward message what companion did send"""
        params = {'chat_id': chat_id,
                  'from_chat_id': from_chat_id,
                  'message_id': message_id}  # Options for forward message
        method = 'forwardMessage'  # Method for forward message
        resp = requests.post(self.api_url + method, data=params)  # Request for forward message

        return resp

    def send_photo(self, chat_id, photo):
        """Send photo to companion"""
        params = {'chat_id': chat_id,
                  'photo': photo}  # Options for send photo
        method = 'sendPhoto'  # Method for send photo
        resp = requests.post(self.api_url + method, data=params)  # Request for send photo

        return resp

    def send_audio(self, chat_id, audio):
        """Send audio to companion"""
        params = {'chat_id': chat_id,
                  'audio': audio}  # Options for send audio
        method = 'sendAudio'  # Method for send audio
        resp = requests.post(self.api_url + method, data=params)  # Request for send audio

        return resp

    def send_document(self, chat_id, document):
        """Send document to companion"""
        params = {'chat_id': chat_id,
                  'photo': document}  # Options for send document
        method = 'sendDocument'  # Method for send document
        resp = requests.post(self.api_url + method, data=params)  # Request for send document

        return resp

    def send_video(self, chat_id, video):
        """Send video to companion"""
        params = {'chat_id': chat_id,
                  'video': video}  # Options for send video
        method = 'sendVideo'  # Method for send video
        resp = requests.post(self.api_url + method, data=params)  # Request for send video

        return resp

    def send_voice(self, chat_id, voice):
        """Send voice to companion"""
        params = {'chat_id': chat_id,
                  'voice': voice}  # Options for send voice
        method = 'sendVoice'  # Method for send voice
        resp = requests.post(self.api_url + method, data=params)  # Request for send voice

        return resp

    def send_location(self, chat_id, latitude, longitude):
        """Send location to companion"""
        params = {'chat_id': chat_id,
                  'latitude': latitude,
                  'longitude': longitude}  # Options for send location
        method = 'sendLocation'  # Method for send location
        resp = requests.post(self.api_url + method, data=params)  # Request for send location

        return resp

    def send_contact(self, chat_id, phone_number, first_name, last_name=''):
        """Send contact to companion"""
        params = {'chat_id': chat_id,
                  'phone_number': phone_number,
                  'first_name': first_name,
                  'last_name': last_name}  # Options for send contact
        method = 'sendContact'  # Method for send contact
        resp = requests.post(self.api_url + method, data=params)  # Request for send contact

        return resp

    def send_chat_action(self, chat_id, action):
        """Send chat action to companion
        Example:
             Bot needs some time to process a request and upload the image.
             Instead of sending a text message along the lines of “Retrieving image, please wait…”,
             the bot may use sendChatAction with action = upload_photo.
             The user will see a “sending photo” status for the bot.
        All actions:
            typing for text messages, upload_photo for photos, record_video or upload_video for videos,
            record_audio or upload_audio for audio files, upload_document for general files,
            find_location for location data,
            record_video_note or upload_video_note for video notes.
        """
        params = {'chat_id': chat_id,
                  'action': action}  # Options for send chat action
        method = 'sendChatAction'  # Method for send chat action
        resp = requests.post(self.api_url + method, data=params)  # Request for send chat action

        return resp

    def get_user_profile_photo(self, user_id):
        """Return photo of user profile"""
        params = {'user_id': user_id}  # Options for get photo of user profile
        method = 'getUserProfilePhotos'  # Method for get photo of user profile
        resp = requests.post(self.api_url + method, data=params)  # Request for get photo of user profile
        result = resp.json()['result']['photos'][0][0]['file_id']  # Get file_id of user profile photo

        return result

    def send_sticker(self, chat_id, sticker):
        """Send sticker to companion"""
        params = {'chat_id': chat_id,
                  'sticker': sticker}  # Options for send sticker
        method = 'sendSticker'  # Method for send sticker
        resp = requests.post(self.api_url + method, data=params)  # Request for send sticker

        return resp

    def set_chat_photo(self, chat_id, photo):
        """Set the chat photo"""
        params = {'chat_id': chat_id,
                  'photo': photo}  # Options for set chat photo
        method = 'setChatPhoto'  # Method for set chat photo
        resp = requests.post(self.api_url + method, data=params)  # Request for set chat photo

        return resp

    def delete_chat_photo(self, chat_id):
        """Delete the chat photo"""
        params = {'chat_id': chat_id}  # Options for delete chat photo
        method = 'deleteChatPhoto'  # Method for delete chat photo
        resp = requests.post(self.api_url + method, data=params)  # Request for delete chat photo

        return resp

    def set_chat_title(self, chat_id, title):
        """Set the chat title"""
        params = {'chat_id': chat_id,
                  'title': title}  # Options for set chat title
        method = 'setChatTitle'  # Method for set chat title
        resp = requests.post(self.api_url + method, data=params)  # Request for set chat title

        return resp

    def set_chat_description(self, chat_id, description):
        """Set the chat description (max 255 simbols)"""
        params = {'chat_id': chat_id,
                  'description': description}  # Options for set chat description
        method = 'setChatDescription'  # Method for set chat description
        resp = requests.post(self.api_url + method, data=params)  # Request for set chat description

        return resp

    def pin_chat_message(self, chat_id, message_id):
        """Pin the chat message in supergroup"""
        params = {'chat_id': chat_id,
                  'message_id': message_id}  # Options for pin chat message
        method = 'pinChatMessage'  # Method for pin chat message
        resp = requests.post(self.api_url + method, data=params)  # Request for pin chat message

        return resp

    def unpin_chat_message(self, chat_id):
        """Unpin the chat in supergroup"""
        params = {'chat_id': chat_id}  # Options for unpin chat in supergroup
        method = 'unpinChatMessage'  # Method for unpin chat in supergroup
        resp = requests.post(self.api_url + method, data=params)  # Request for unpin chat in supergroup

        return resp

    def leave_chat(self, chat_id):
        """Leave a companion from a chat with bot"""
        params = {'chat_id': chat_id}  # Options for leave chat
        method = 'leaveChat'  # Method for leave chat
        resp = requests.post(self.api_url + method, data=params)  # Request for leave chat

        return resp

    def get_chat(self, chat_id):
        """Return a chat object of chat"""
        params = {'chat_id': chat_id}  # Options for get chat
        method = 'getChat'  # Method for get chat
        resp = requests.post(self.api_url + method, data=params)  # Request for get chat

        return resp

    def get_chat_administrations(self, chat_id):
        """Return an array of administrations the chat"""
        params = {'chat_id': chat_id}  # Options for get chat administrations
        method = 'getChatAdministrations'  # Method for get chat administrations
        resp = requests.post(self.api_url + method, data=params)  # Request for get chat administrations

        return resp

    def get_chat_members_count(self, chat_id):
        """Return a number of members in chat"""
        params = {'chat_id': chat_id}  # Options for get chat members count
        method = 'getChatMembersCount'  # Method for get chat members count
        resp = requests.post(self.api_url + method, data=params)  # Request for get chat members count

        return resp

    def get_chat_member(self, chat_id, user_id):
        """Return chatmember object about a member in chat"""
        params = {'chat_id': chat_id,
                  'user_id': user_id}  # Options for get chat member
        method = 'getChatMember'  # Method for get chat member
        resp = requests.post(self.api_url + method, data=params)  # Request for get chat member

        return resp

    def answer_callback_query(self, callback_query_id, text=''):
        """Send answers to callback queries"""
        params = {'callback_query_id': callback_query_id,
                  'text': text}  # Options for answer callback query
        method = 'answerCallbackQuery'  # Method for answer callback query
        resp = requests.post(self.api_url + method, data=params)  # Request for answer callback query

        return resp

    def send_video_note(self, chat_id, video_note):
        """Send video messages"""
        params = {'chat_id': chat_id,
                  'video_note': video_note}  # Options for send video note
        method = 'sendVideoNote'  # Method for send video note
        resp = requests.post(self.api_url + method, data=params)  # Request for send video note

        return resp

    def send_venue(self, chat_id, latitude, longitude, title, address):
        """Send information about venue"""
        params = {'chat_id': chat_id,
                  'latitude': latitude,
                  'longitude': longitude,
                  'title': title,
                  'address': address}  # Options for send venue
        method = 'sendVenue'  # Method for send venue
        resp = requests.post(self.api_url + method, data=params)  # Request for send venue

        return resp

    def get_file(self, file_id):
        """Get basic information about file"""
        params = {'file_id': file_id}  # Options for get file
        method = 'getFile'  # Method for get file
        resp = requests.post(self.api_url + method, data=params)  # Request for get file

        return resp

    def kick_chat_member(self, chat_id, user_id):
        """Kick a user from a group"""
        params = {'chat_id': chat_id,
                  'user_id': user_id}  # Options for kick chat member
        method = 'kickChatMember'  # Method for kick chat member
        resp = requests.post(self.api_url + method, data=params)  # Request for kick chat member

        return resp

    def unban_chat_member(self, chat_id, user_id):
        """Unban a user from a group"""
        params = {'chat_id': chat_id,
                  'user_id': user_id}  # Options for unban chat member
        method = 'unbanChatMember'  # Method for unban chat member
        resp = requests.post(self.api_url + method, data=params)  # Request for unban chat member

        return resp

    def restrict_chat_member(self, chat_id, user_id):
        """Restrict a user in supergroup"""
        params = {'chat_id': chat_id,
                  'user_id': user_id}  # Options for restrict chat member
        method = 'restrictChatMember'  # Method for restrict chat member
        resp = requests.post(self.api_url + method, data=params)  # Request for restrict chat member

        return resp

    def promote_chat_member(self, chat_id, user_id):
        """Promote or demote chat member in supergroup"""
        params = {'chat_id': chat_id,
                  'user_id': user_id}  # Options for promote chat member
        method = 'promoteChatMember'  # Method for promote chat member
        resp = requests.post(self.api_url + method, data=params)  # Request for promote chat member

        return resp

    def export_chat_invite_link(self, chat_id):
        """Export a link for invite in chat"""
        params = {'chat_id': chat_id}  # Options for export chat invite link
        method = 'exportChatInviteLink'  # Method for export chat invite link
        resp = requests.post(self.api_url + method, data=params)  # Request for export chat invite link

        return resp

    def edit_message_text(self, chat_id, text, message_id=None):  # @#$%(
        """Edit text in messages sent by bot"""
        params = {'chat_id': chat_id,
                  'message_id': message_id,
                  'text': text}  # Options for edit message text
        method = 'editMessageText'  # Method for edit message text
        resp = requests.post(self.api_url + method, data=params)  # Request for edit message text

        return resp

    def edit_message_caption(self, chat_id, message_id):  # (*)(&(*^*&%
        pass

    def edit_message_reply_markup(self, chat_id, message_id):  # *8(^&$*^$&#
        pass

    def delete_message(self, chat_id, message_id):
        """Delete a message"""
        params = {'chat_id': chat_id,
                  'message_id': message_id}  # Options for delete message
        method = 'deleteMessage'  # Method for delete message
        resp = requests.post(self.api_url + method, data=params)  # Request for delete message

        return resp

    def get_sticker_set(self, name):
        """Return a StickerObject"""
        params = {'name': name}  # Options for get sticker set
        method = 'getStickerSet'  # Method for get sticker set
        resp = requests.post(self.api_url + method, data=params)  # Request for get sticker set

        return resp

    def upload_sticker_file(self, user_id, png_sticker):
        """Upload .png file with a sticker"""
        params = {'user_id': user_id,
                  'png_sticker': png_sticker}  # Options for upload sticker file
        method = 'uploadStickerFile'  # Method for upload sticker file
        resp = requests.post(self.api_url + method, data=params)  # Request for upload sticker file

        return resp

    def create_new_sticker_set(self, user_id, name, title, png_sticker, emojis):
        """Create a new sticker set owned by user"""
        params = {'user_id': user_id,
                  'name': name,
                  'title': title,
                  'png_sticker': png_sticker,
                  'emojis': emojis}  # Options for create new sticker set
        method = 'createNewStickerSet'  # Method for create new sticker set
        resp = requests.post(self.api_url + method, data=params)  # Request for create new sticker set

        return resp

    def add_sticker_to_set(self, user_id, name, png_sticker, emojis):
        """Add a new sticker to a set"""
        params = {'user_id': user_id,
                  'name': name,
                  'png_sticker': png_sticker,
                  'emojis': emojis}  # Options for add sticker to set
        method = 'addStickerToSet'  # Method for add sticker to set
        resp = requests.post(self.api_url + method, data=params)  # Request for add sticker to set

        return resp

    def set_sticker_position_in_set(self, sticker, position):
        """Move sticker in the set"""
        params = {'sticker': sticker,
                  'position': position}  # Options for set sticker position in set
        method = 'setStickerPositionInSet'  # Method for set sticker position in set
        resp = requests.post(self.api_url + method, data=params)  # Request for set sticker position in set

        return resp

    def delete_sticker_from_set(self, sticker):
        """Delete a sticker from a set"""
        params = {'sticker': sticker}  # Options for delete sticker from set
        method = 'deleteStickerFromSet'  # Method for delete sticker from set
        resp = requests.post(self.api_url + method, data=params)  # Request for delete sticker from set

        return resp
