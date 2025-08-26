from flask import Flask, request, render_template
from caesar_cipher import caesar_cipher, caesar_cipher_decypted, KEY

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    message = ""
    use_polish = False
    key = KEY

    if request.method == "POST":
        message = request.form.get("message", "")
        action = request.form.get("action")
        use_polish = request.form.get("use_polish") == "on"

        try:
            key = int(request.form.get("key", KEY))
        except ValueError:
            key = KEY

        if action == "encrypt":
            result = caesar_cipher(message, key=KEY, use_polish=use_polish)
        elif action == "decrypt":
            result = caesar_cipher_decypted(message, key=KEY, use_polish=use_polish)

    return render_template("index.html", result=result, message=message, use_polish=use_polish, key=key)


if __name__=="__main__":
    app.run(debug=True)