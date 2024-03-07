from flask import Flask, render_template
from data import db_session
from data.jobs import Job
import web

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer.db")
    # job = Job()
    # job.team_leader_id, job.job, job.work_size, job.collaborators, job.is_finished = \
    #     [1, "deployment of residential modules 1 and 2", 15, "2, 3", False]
    db_sess = db_session.create_session()
    # db_sess.add(job)
    db_sess.commit()
    # app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Job)
    return render_template("index.html", jobs=jobs)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
