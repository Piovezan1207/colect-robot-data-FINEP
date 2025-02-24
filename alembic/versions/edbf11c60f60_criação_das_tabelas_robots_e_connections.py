"""Criação das tabelas robots e connections

Revision ID: edbf11c60f60
Revises: 
Create Date: 2025-02-17 10:58:15.288516

"""
from typing import Sequence, Union

from sqlalchemy.orm import sessionmaker

from alembic import op
import sqlalchemy as sa
from models import Robot, Connection


# revision identifiers, used by Alembic.
revision: str = 'edbf11c60f60'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

#Comando para rodar : alembic upgrade head

def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('robots',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=128), nullable=False),
    sa.Column('axis', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('connections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('robot_id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(length=128), nullable=False),
    sa.Column('ip', sa.String(length=15), nullable=False),
    sa.Column('port', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=256), nullable=True),
    # sa.Column('number', sa.String(length=64), nullable=True),
    sa.Column('token', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['robot_id'], ['robots.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    
     # Agora insira os dados iniciais na tabela
    # Conecte ao banco de dados para inserir dados na tabela 'robots'
    bind = op.get_bind()
    session = sessionmaker(bind=bind)()

    # Dados a serem inseridos
    robots_data = [
        {'type': 'HC10', 'axis': 6, 'brand': 'YASKAWA'},
        {'type': 'GP8', 'axis': 6, 'brand': 'YASKAWA'},
        {'type': 'MIR100', 'axis': 3, 'brand': 'MIR'}
    ]

    # Inserir os dados
    for data in robots_data:
        robot = Robot(**data)  # Criar o objeto Robot
        session.add(robot)

    session.commit()  # Commit das inserções
    
    bind = op.get_bind()
    session = sessionmaker(bind=bind)()

    # Dados a serem inseridos
    conn_data = [
        {'robot_id': '1', 'topic': '/teste/2', 'ip': '0.0.0.0', 'port': 502, 'description': 'teste descrição', 'token': '1234'},
        {'robot_id': '2', 'topic': '/teste/3', 'ip': '1.0.2.0', 'port': 503, 'description': 'Main control testeteste', 'token': '123467'},
        

    ]

    # Inserir os dados
    for data in conn_data:
        conn = Connection(**data)  # Criar o objeto Robot
        session.add(conn)

    session.commit()  # Commit das inserções


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('connections')
    op.drop_table('robots')
    # ### end Alembic commands ###
