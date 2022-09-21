from flask import Flask, render_template, request
import db.db as db

app = Flask(__name__)


@app.route("/")
def hello_world():
    con = db.get_db()
    cur = con.cursor()

    cur.execute(
        'select * from challenges'
    )
    challenges = cur.fetchall()

    return render_template('hello.html', challenges=challenges)


@app.route("/add")
def add_challenge():
    return render_template('add.html')


@app.route("/savedetails", methods=["POST"])
def saveDetails():
    msg = "msg"
    try:
        name = request.form["name"]
        description = request.form["description"]
        start_date = request.form["start_date"]
        end_date = request.form["end_date"]
        done = request.form["done"]

        with db.get_db() as con:
            cur = con.cursor()
            cur.execute("INSERT into challenges (name, description, start_date, end_date, done) values (%s,%s,%s,%s,%s)",
                        (name, description, start_date, end_date, done))
            con.commit()
            msg = "challenge successfully Added"
            print("success")
            con.close()
    except:
        con.rollback()
        msg = "We can not add the employee to the list"
        print("fail")
        con.close()
    finally:
        return render_template("succes.html", msg=msg)


@app.route("/delete/<int:id>")
def delete(id):
    with db.get_db() as con:
        try:
            cur = con.cursor()
            cur.execute("delete from challenges where id=" + str(id))
            con.commit()
        except:
            con.rollback()
        finally:
            return hello_world()


if __name__ == "__main__":
    app.run()
