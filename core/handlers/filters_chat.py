from core.utilities.functions import delete_message
from core.utilities.message import message
from core.database.repository.group import GroupRepository
"""
This function allows you to terminate the type
of file that contains a message on telegram and filter it
"""
def init(update, context):
    apk = 'application/vnd.android.package-archive'
    doc = 'application/msword'
    docx = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    exe = 'application/x-ms-dos-executable'
    gif = 'video/mp4'
    jpg = 'image/jpeg'
    mp3 = 'audio/mpeg'
    pdf = 'application/pdf'
    py = 'text/x-python'
    svg = 'image/svg+xml'
    txt = 'text/plain'
    targz = 'application/x-compressed-tar'
    wav = 'audio/x-wav'
    xml = 'application/xml'
    filezip = 'application/zip'

    msg = update.effective_message
    chat = update.effective_message.chat_id
    group = GroupRepository().getById(chat)

    if msg.document is not None:
        #No APK Allowed
        if msg.document.mime_type == apk and group['apk_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No APK Allowed!</b>")
        #No DOC/DOCX Allowed
        if msg.document.mime_type == doc or msg.document.mime_type == docx and group['docx_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No DOC/DOCX Allowed!</b>")
        #No EXE Allowed
        if msg.document.mime_type == exe and group['exe_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No EXE Allowed!</b>")
        #No GIF Allowed
        if msg.document.mime_type == gif and group['gif_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No GIF Allowed!</b>")
        #No JPG Allowed
        if msg.document.mime_type == jpg and group['jpg_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No JPG Allowed!</b>")
        #No TARGZ Allowed
        if msg.document.mime_type == targz and group['targz_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No TARGZ Allowed!</b>")
        #No ZIP Allowed
        if msg.document.mime_type == filezip and group['zip_filter'] == 1:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No ZIP Allowed!</b>")
        if msg.document.mime_type == wav:
            print("NO WAV ALLOWED")
        if msg.document.mime_type == xml:
            print("NO XML ALLOWED")
        if msg.document.mime_type == mp3:
            print("NO MP3 ALLOWED")
        if msg.document.mime_type == pdf:
            print("NO PDF ALLOWED")
        if msg.document.mime_type == py:
            print("NO PY ALLOWED")
        if msg.document.mime_type == svg:
            print("NO SVG ALLOWED")
        if msg.document.mime_type == txt:
            print("NO TXT ALLOWED")