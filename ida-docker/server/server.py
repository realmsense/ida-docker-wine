import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEUBG"] = True


@app.route("/ida/command", methods=["POST"])
def ida_command():

    params = {
        "command": None,
        "auth": None,
    }

    for param in params:
        params[param] = request.args.get(param)
        if not params[param]: 
            return jsonify(error=f"Missing parameter '{param}'")

    # TODO: don't hardcode this variable
    if params["auth"] != "xEhT6qjM":
        return jsonify(error=f"Incorrect auth parameter")

    command = params["command"].split(" ")

    try:
        output = subprocess.Popen(command)
        output.communicate()
        return jsonify(message=f"Command finished with exit code: {output.returncode}")
    except Exception as e:
        return jsonify(error=str(e))


if __name__ == "__main__":
    app.run(host="0.0.0.0")
