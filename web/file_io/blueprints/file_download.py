from flask import Blueprint, request, send_file
from web.extensions import login_check, make_json_response
from werkzeug.utils import secure_filename
import jwt
import os

file_download_bp = Blueprint('file_download', __name__, url_prefix='/file')


@file_download_bp.route('/download', methods=["GET"])
def download():
    token = request.args.get('token', None)
    filename = request.args.get("filename", None)
    if True:
        login_msg = jwt.decode(token, key="priority_queue", algorithms="HS256")
        login_status = bool(login_msg.get('login_status', None))  # 传入bool值
        login_user_id = int(login_msg.get('login_user_id', None))  # 登录用户id 必须是全部由数字组成
        if login_status is True and login_user_id is not None:
            if filename is not None:
                # filename = secure_filename(filename)
                if '..' in filename:
                    raise
                dir_path = os.getcwd() + os.sep + 'file_upload' + os.sep + str(login_user_id)
                if os.path.exists(dir_path + os.sep + filename):
                    return send_file(filename_or_fp=dir_path + os.sep + filename, attachment_filename=filename,
                                     as_attachment=True)
        return make_json_response(status=0, message='FileUnExist', data=None)
    else:
        return "<script>window.alert('你没有登录哦 白嫖怪~');window.location.href='javascript:history.go(-1)';</script>"
