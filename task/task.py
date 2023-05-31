from flask import Blueprint, render_template
import os

taskBp = Blueprint("task", __name__)

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# task json
task_file = os.path.join(__location__, "../data/task.json")


# untuk penamaan url-nya GET & POST seperti ini gk usah di tulis url-nya
# soalnya url-nya dari __init__.py
@taskBp.route("", methods=['GET'], strict_slashes = False)
# tinggal mengubah fungsi dibawah
def home():

    return "ini url task"


# untuk penamaan url PUT atau delete tinggal tambahkan /<id>
