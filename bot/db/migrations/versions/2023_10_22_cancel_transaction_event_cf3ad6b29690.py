"""Add CANCEL to TransactionEvent

Revision ID: cf3ad6b29690
Revises: f41465e9e613
Create Date: 2023-10-22 11:48:49.365022

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = "cf3ad6b29690"
down_revision = "f41465e9e613"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE transactionevent ADD VALUE 'CANCEL'")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
