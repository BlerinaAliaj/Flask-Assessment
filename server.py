from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
import jinja2


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# List of jobs available.

job_list = ["Software Engineer", "QA Engineer", "Product Manager"]


# YOUR ROUTES GO HERE
@app.route("/")
def index():
    """Return homepage."""

    return render_template("index.html")
    # return redirect("/application-form")

@app.route("/application-form")
def application_form():
    """Returns application form."""

    jobs = job_list
    return render_template("application-form.html", jobs=jobs)

@app.route("/application-success")
def application_success():
    """Passes information inputed from the form and returns response."""

    first_name = request.args.get("firstname")
    last_name = request.args.get("lastname")
    raw_salary = int(request.args.get("salary"))
    salary = "{:,}".format(raw_salary)
    job_title = request.args.get("job")


    return render_template("application-response.html", firstname=first_name,
        lastname=last_name, salary=salary, jobtitle=job_title)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
