from core.utilities.functions import delete_message
from core.utilities.message import message

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

    if msg.document is not None:
        if msg.document.mime_type == apk:
            print("NO APK ALLOWED")
        if msg.document.mime_type == doc or msg.document.mime_type == docx:
            print("NO DOC/DOCX ALLOWED")
        if msg.document.mime_type == exe:
            delete_message(update,context)
            message(update, context, "#Automatic Filter Handler: <b>No EXE Allowed!</b>")
        if msg.document.mime_type == gif:
            print("NO GIF ALLOWED")
        if msg.document.mime_type == jpg:
            print("NO JPG ALLOWED")
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
        if msg.document.mime_type == targz:
            print("NO TARGZ ALLOWED")
        if msg.document.mime_type == wav:
            print("NO WAV ALLOWED")
        if msg.document.mime_type == xml:
            print("NO XML ALLOWED")
        if msg.document.mime_type == filezip:
            print("NO FILEZIP ALLOWED")