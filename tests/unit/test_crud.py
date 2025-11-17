import pytest

from app import app
from model.database import db
from model.professor import Professor
from model.turma import Turma
from controller.professor_controller import ProfessorController


@pytest.fixture()
def app_ctx():
    app.config.update(
        TESTING=True,
        SQLALCHEMY_DATABASE_URI="sqlite:///:memory:",
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app_ctx):
    return app_ctx.test_client()


def test_listar_professores_responde_200(client):
    resp = client.get("/professor/")
    assert resp.status_code == 200


def test_professor_controller_delete_remove_sem_turmas(app_ctx):
    with app_ctx.app_context():
        prof = Professor(nome="Sem Turma", idade=30, materia="Bio", observacoes=None)
        db.session.add(prof)
        db.session.commit()
        prof_id = prof.id

        result = ProfessorController.delete(prof_id)

        assert result is True
        assert Professor.query.get(prof_id) is None


def test_editar_turma_post_atualiza_campos(client, app_ctx):
    with app_ctx.app_context():
        prof1 = Professor(nome="Prof Antigo", idade=40, materia="Hist", observacoes=None)
        prof2 = Professor(nome="Prof Novo", idade=42, materia="Geo", observacoes=None)
        db.session.add_all([prof1, prof2])
        db.session.flush()

        
        prof2_id = prof2.id 

        turma = Turma(descricao="Turma X", ativo=False, professor_id=prof1.id)
        db.session.add(turma)
        db.session.commit()

        turma_id = turma.id
        old_desc = turma.descricao

    resp = client.post(
        f"/turma/editar/{old_desc}",
        data={
            "descricao": "Turma Y",
            "professor": str(prof2_id),
            "ativo": "on",
        },
        follow_redirects=False,
    )

    assert resp.status_code == 302
    assert resp.headers["Location"].endswith("/turma/")

    with app_ctx.app_context():
        turma_atualizada = Turma.query.get(turma_id)
        assert turma_atualizada.descricao == "Turma Y"
        assert turma_atualizada.professor_id == prof2_id
        assert turma_atualizada.ativo is True