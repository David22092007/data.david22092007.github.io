import random, requests, json, time
from flask import Flask, redirect, url_for, render_template, request

_name_ = '_main_'

app = Flask(_name_)


@app.route("/", methods=["POST", "GET"])
def main():
  if request.method == "POST":
    data = request.form["data"]
    if data.find(':') >= 1 or data.find('/') >= 1:
      http_link_answers = True
      data = data.replace(':', '(.)')
      data = data.replace('/', '.().')
    else:
      http_link_answers = False
    return redirect(
        url_for("write_to_file",
                data=data,
                http_link_answers=http_link_answers))
  else:
    return render_template('another_sever.html')


@app.route("/write_to_file&<data>&<http_link_answers>",
           methods=["POST", "GET"])
def write_to_file(data, http_link_answers):
  data = data.replace('(.)', ':')
  data = data.replace('.().', '/')
  c = open('templates/data.html', 'a')
  a = open('templates/data.html', 'r')
  string = ''
  for i in a:
    string = i + string
  if string.find(data) == -1:
    if http_link_answers == True:
      a = open('templates/data.html', 'a')
      a.write(f'''<a href="{data}" class="sub_text" title="sub">{data}</a>''')
    else:
      a = open('templates/data.html', 'a')
      a.write('<div>' + data + '</div>')

  return render_template('data.html')


@app.route("/show", methods=["GET"])
def new_bie():
  return render_template('data.html')


if _name_ == "_main_":
  app.run(debug=True, host="0.0.0.0", port=80)
