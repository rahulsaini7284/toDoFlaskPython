from flask import render_template, request
from model import Person


def register_routes(app, db):

    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "GET":
            people = Person.query.all()
            total = len(Person.query.all())
            return render_template("index.html", people=people, total=total)
        elif request.method == "POST":
            name = request.form.get("name")
            age = int(request.form.get("age"))
            city = request.form.get("city")
            isAdult = request.form.get("isAdult")
            if isAdult == "on":
                isAdult = True
            else:
                isAdult = False
            person = Person(name=name, age=age, city=city, isAdult=isAdult)
            total = len(Person.query.all())
            db.session.add(person)
            db.session.commit()

            people = Person.query.all()
            return render_template("index.html", people=people, total=total)
        else:
            people = Person.query.all()
            total = len(Person.query.all())
            return render_template("index.html", people=people, total=total)

    @app.route("/delete/<pid>", methods=["DELETE"])
    def delete(pid):
        Person.query.filter(Person.pid == pid).delete()
        db.session.commit()
        total = len(Person.query.all())
        people = Person.query.all()
        return render_template("index.html", people=people, total=total)

    @app.route("/detail/<pid>", methods=["GET"])
    def detail(pid):
        person = Person.query.filter(Person.pid == pid).first()
        return render_template("detail.html", person=person)

    @app.route("/update/<pid>", methods=["POST", "GET"])
    def updatePerson(pid):
        if request.method == "POST":
            if request.form["method"] == "PUT":
                person = Person.query.filter(Person.pid == pid)
                print(person, pid)
                name = request.form.get("name") or person.name
                age = int(request.form.get("age")) or person.age
                city = request.form.get("city") or person.city
                isAdult = request.form.get("isAdult")
                if isAdult == "on":
                    isAdult = True
                else:
                    isAdult = False
                person.update(
                    {"name": name, "age": age, "city": city, "isAdult": isAdult}
                )
                db.session.commit()
                person = Person.query.filter(Person.pid == pid).first()
                return render_template("detail.html", person=person)
        elif request.method == "GET":
            print("This is the get request", request.method, pid)
            person = Person.query.filter(Person.pid == pid)
            return render_template("detail.html", person=person)
